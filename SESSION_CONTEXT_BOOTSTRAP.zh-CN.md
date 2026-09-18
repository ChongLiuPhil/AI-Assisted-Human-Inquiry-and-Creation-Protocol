# HARC Session Context Bootstrap
## 会话上下文启动契约

> **本中文文件是规范性基准；英文 `SESSION_CONTEXT_BOOTSTRAP.md` 是同步镜像。**

## 0. 作用

本文件用于形成 HARC 的第二层保险：

1. **GitHub repository** 保存持久、可审计的项目状态；
2. **当前 AI 会话上下文** 保存一份由仓库状态重新生成的压缩操作契约。

新的 AI Agent 在完成仓库 onboarding 后，应把本文件要求的 **HARC Active Session Contract** 明确写入自己的当前对话回复，使这些关键规则再次进入本轮会话上下文。

这不是平台级真正的 `system prompt`，也不得声称能够覆盖平台的 system / developer / safety instructions。

正确关系是：

`Platform system/developer rules > HARC Session Contract > ordinary task-level AI defaults`

HARC Session Contract 是**项目级会话操作契约**。

## 1. 何时加载

以下情况 MUST 加载或重新加载 Session Contract：

- 新 AI Agent 第一次接管项目；
- 新会话开始；
- Agent 无法访问前一会话上下文；
- Onboarding Handshake 完成后；
- 发生重大人类决定并改变 Core / Clarification / Framework 状态；
- Framework Approval 前；
- Final Artifact Review 前；
- Agent 怀疑自己已经丢失或压缩掉重要 HARC 状态时。

## 2. 加载动作

Agent 完成 required read order 后，必须在第一份 Onboarding Report 中加入一个明确区块：

`HARC ACTIVE SESSION CONTRACT — LOADED`

并把以下当前状态压缩写入它自己的回复。

### A. Authority

- repository state outranks prior chat memory;
- Chinese canonical outranks English mirror;
- human-confirmed Core outranks AI proposals;
- Approved Framework outranks Working Argument Map;
- platform system/developer instructions remain higher priority than HARC.

### B. Current project status

- 当前人类研究目的；
- 当前 Content / Form / Protocol 的关键人类承诺；
- 当前 Blocking Clarifications；
- 当前 Working Framework status；
- 最新 Approved Framework（如有）；
- 当前 Artifact status；
- 当前 Final Approval status。

### C. Required behavior

- high-impact uncertainty -> Clarification Register；
- explicit human decision -> Decision Log -> appropriate Core -> downstream propagation；
- no silent promotion of AI proposals；
- no Framework Approval while blocking clarification remains unresolved unless explicitly deferred by the human；
- Chinese substantive edits -> English mirror in the same work cycle；
- derived artifacts remain provisional until the required approval gate.

### D. Current task constraint

Agent 应说明本轮当前请求：

- 属于 CONTENT / FORM / PROTOCOL 哪一类；
- 是否触发 clarification；
- 哪些文件必须上游优先更新；
- 哪些动作当前被阻塞。

## 3. 推荐回显格式

Agent 应在自己的回复中生成类似：

```text
HARC ACTIVE SESSION CONTRACT — LOADED

Authority:
- Repository state > prior chat memory
- Chinese canonical > English mirror
- Human-confirmed Core > AI proposals
- Approved Framework > Working Argument Map
- Platform system/developer instructions > HARC project contract

Blocking Clarifications:
- CLR-...

Framework:
- Working: ...
- Approved: ...

Artifact:
- Status: ...

Current task:
- Classification: CONTENT / FORM / PROTOCOL
- Upstream files: ...
- Blocked actions: ...

Operational invariants:
- High-impact ambiguity -> Clarification Register
- Human decision -> Decision Log -> Core -> Argument Map -> Artifact
- Chinese edit -> English mirror
```

该区块应简洁，不要复制整个仓库。

## 4. 为什么必须“回显”

只读取文件并不能保证重要规则在一个长会话中始终保持高显著度。

把压缩后的 Session Contract 由 Agent 自己重新写入当前回复，有三个作用：

1. **进入当前会话上下文**：后续生成可以再次看到这些规则；
2. **让人类验证**：人类可以立即发现 Agent 是否误读仓库；
3. **形成显式承诺**：Agent 的后续动作可以与它刚刚回显的契约进行一致性检查。

## 5. Context Refresh

Session Contract 不应只在第一轮出现一次。

以下节点 SHOULD 触发一次简短 `HARC CONTEXT REFRESH`：

- 人类解决一个 Blocking Clarification；
- Content Core / Form Core / Protocol Core 发生实质变化；
- 创建新的 Approved Framework；
- 从 framework 阶段进入大规模 Artifact expansion；
- 从中文 canonical 进入正式英文发布准备；
- Final Artifact Review；
- 长对话中 Agent 无法确定先前 session contract 是否仍在有效上下文。

Refresh 只需要更新发生变化的字段，不必重复完整 Onboarding Report。

## 6. 不得伪造隐藏记忆

Agent 不得声称：

- 已经把 HARC 写入平台的真正 system prompt；
- 已经永久写入模型参数；
- 已经修改平台级 memory；
- 即使开启新会话也会自动记住。

如果平台本身提供用户可控制的 custom instruction / project instruction / pinned context 功能，可以额外使用，但这属于平台能力，不是 HARC 仓库能够保证的能力。

HARC 能保证的是：

> **仓库提供可恢复的持久状态；Agent 通过显式回显把关键状态重新注入当前可见会话上下文。**

## 7. 会话上下文失效时

如果 Agent 怀疑当前对话已经压缩、截断、迁移或丢失早期 HARC contract，应：

1. 停止依赖记忆猜测；
2. 重新读取 `HARC_MANIFEST.yaml`；
3. 重新读取相关 canonical state；
4. 输出 `HARC CONTEXT REFRESH`；
5. 再继续实质工作。

## 8. 原则

> **Repository memory provides persistence; Session Context Bootstrap restores salience.**

中文：

> **仓库记忆负责持久化；会话上下文启动负责让关键规则在当前 Agent 的活动上下文中重新变得显著。**
