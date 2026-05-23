---
name: Git Commit Format
description: Robbie 要求的 git commit message 格式和推送流程
type: feedback
originSessionId: 8e6e316d-6dab-4894-86f1-6bcab0f86270
---
Commit message 默认使用英文，格式如下：

```
type(scope): 简短描述（50字内）

问题：一句话说清用户看到的现象。

根因：定位到具体的代码位置和机制，说明为什么会发生。

修复：做了什么改动，为什么这样改能解决问题。

变更文件：
- file1: 改动说明
- file2: 改动说明
```

**Why:** Robbie 是非技术运营人员，需要清晰理解每次提交的业务影响和原因，方便 review。
**How to apply:** 每次 Robbie 要求推送时，先输出完整的 commit message（包含问题、根因、修复、变更文件），确认后再执行 commit。不要主动 commit/push，等 Robbie 确认。
