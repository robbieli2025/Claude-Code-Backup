#!/usr/bin/env python3
"""
Write an expense record to Feishu Bitable (飞书多维表格).

Usage:
    python3 write_record.py --amount 29.00 --date 2026-05-15 --vendor Shopify --description "Shopify Basic Plan 月费"

Requirements:
    Python 3.6+ (stdlib only, no extra dependencies)
    Environment variables: FEISHU_APP_ID, FEISHU_APP_SECRET, FEISHU_BITABLE_APP_TOKEN, FEISHU_TABLE_ID

Note: Uses batch_create endpoint because the single-record endpoint returns 403
in some Feishu workspace configurations.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta
import urllib.request
import urllib.error

# Beijing timezone for date conversion
BJT = timezone(timedelta(hours=8))


def get_token(app_id: str, app_secret: str) -> str:
    """Get tenant access token from Feishu API."""
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    data = json.dumps({"app_id": app_id, "app_secret": app_secret}).encode()
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"获取 token 失败: HTTP {e.code}", file=sys.stderr)
        print(e.read().decode(), file=sys.stderr)
        sys.exit(1)

    if body.get("code") != 0:
        print(f"获取 token 失败: {body.get('msg', 'unknown error')}", file=sys.stderr)
        sys.exit(1)

    return body["tenant_access_token"]


def date_to_timestamp(date_str: str) -> int:
    """Convert YYYY-MM-DD date string to Feishu unix timestamp (ms, UTC+8)."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    dt_bj = dt.replace(tzinfo=BJT)
    return int(dt_bj.timestamp() * 1000)


def create_records(token: str, app_token: str, table_id: str,
                   records: list[dict]) -> list[str]:
    """Create records in Feishu Bitable via batch_create endpoint."""
    url = (
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}"
        f"/tables/{table_id}/records/batch_create"
    )
    data = json.dumps({"records": records}).encode()
    req = urllib.request.Request(
        url, data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"写入失败: HTTP {e.code}", file=sys.stderr)
        print(error_body, file=sys.stderr)
        sys.exit(1)

    if body.get("code") != 0:
        print(f"写入失败: {body.get('msg', 'unknown error')}", file=sys.stderr)
        if "DatetimeFieldConvFail" in str(body.get("msg", "")):
            print("日期格式错误，需要使用 Unix 毫秒时间戳", file=sys.stderr)
        sys.exit(1)

    return [r["record_id"] for r in body["data"]["records"]]


def main():
    parser = argparse.ArgumentParser(
        description="Write expense record to Feishu Bitable"
    )
    parser.add_argument("--amount", required=True, help="金额 (如 29.00)")
    parser.add_argument("--date", required=True, help="日期 (YYYY-MM-DD)")
    parser.add_argument("--vendor", required=True, help="服务商名称")
    parser.add_argument("--description", required=True, help="费用名称/描述")
    parser.add_argument("--category", default="办公",
                        help="报销科目 (默认: 办公)")
    parser.add_argument("--status", default="未报销",
                        help="报销进度 (默认: 未报销)")
    args = parser.parse_args()

    # Load credentials from environment
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    app_token = os.environ.get("FEISHU_BITABLE_APP_TOKEN")
    table_id = os.environ.get("FEISHU_TABLE_ID")

    missing = []
    if not app_id:
        missing.append("FEISHU_APP_ID")
    if not app_secret:
        missing.append("FEISHU_APP_SECRET")
    if not app_token:
        missing.append("FEISHU_BITABLE_APP_TOKEN")
    if not table_id:
        missing.append("FEISHU_TABLE_ID")

    if missing:
        print(f"缺少环境变量: {', '.join(missing)}", file=sys.stderr)
        print("请参考 references/feishu-api.md 配置环境变量", file=sys.stderr)
        sys.exit(1)

    # Get token
    token = get_token(app_id, app_secret)

    # Build fields matching the actual Feishu table schema
    summary = f"{args.vendor} - {args.description}"
    fields = {
        "报销摘要": summary,
        "费用金额": float(args.amount),
        "报销日期": date_to_timestamp(args.date),
        "报销科目": args.category,
        "报销进度": args.status,
        "备注": f"服务商: {args.vendor}",
    }

    # Write via batch_create
    record = {"fields": fields}
    record_ids = create_records(token, app_token, table_id, [record])

    print(f"写入成功。记录 ID: {record_ids[0]}")
    print(f"  {args.date} | {args.vendor} | ¥{args.amount} | {args.description}")


if __name__ == "__main__":
    main()
