---
name: claude-code-backup-sync
description: Claude Code 配置/记忆/技能自动同步到 GitHub 备份仓库的机制
metadata:
  type: reference
---

## 同步架构

三个关键路径已通过 **symlink** 指向备份仓库 `~/Github/Claude-Code-Backup/`：

| 路径 | → Symlink 目标 |
|------|---------------|
| `~/.claude/CLAUDE.md` | `~/Github/Claude-Code-Backup/CLAUDE.md` |
| `~/.claude/settings.json` | `~/Github/Claude-Code-Backup/settings.json` |
| `~/.claude/projects/-Users-robbieli/memory/` | `~/Github/Claude-Code-Backup/memory/` |

备份仓库 remote：`https://github.com/robbieli2025/Claude-Code-Backup.git`

## 工作原理

因为 symlink 的存在，Claude Code 对 memory/CLAUDE.md/settings.json 的任何读写都直接发生在 git 仓库内。每次会话结束后，只需要 `git commit + push` 即可完成同步。

**Why:** Robbie 需要在多台电脑之间无缝切换工作。备份仓库克隆到任何机器后，创建相同的 symlink，Claude Code 就能读取到最新的记忆和配置。

**How to apply:** 每次修改 memory、CLAUDE.md 或 settings.json 后，自动 commit 并 push 到 GitHub。不需要用户提醒。

## 新机器初始化步骤

```bash
# 1. 克隆备份仓库
git clone https://github.com/robbieli2025/Claude-Code-Backup.git ~/Github/Claude-Code-Backup

# 2. 创建 symlink（先备份原有文件）
mv ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.orig 2>/dev/null
mv ~/.claude/settings.json ~/.claude/settings.json.orig 2>/dev/null
rm -rf ~/.claude/projects/-Users-robbieli/memory 2>/dev/null

ln -s ~/Github/Claude-Code-Backup/CLAUDE.md ~/.claude/CLAUDE.md
ln -s ~/Github/Claude-Code-Backup/settings.json ~/.claude/settings.json
ln -s ~/Github/Claude-Code-Backup/memory ~/.claude/projects/-Users-robbieli/memory
```

## 当前已同步内容

- `CLAUDE.md` — 全局 CLAUDE.md 规则
- `settings.json` — Claude Code 设置
- `memory/` — 所有记忆文件（用户偏好、项目事实、reference 等）
- `skills/` — 用户技能目录（备份仓库中有副本，未 symlink）
- `plans/` — 历史 plan 文件
