# HARC Onboarding Report Template

> **本中文文件是规范性基准；英文 `ONBOARDING_REPORT_TEMPLATE.md` 是同步镜像。**

新的 AI Agent 在进行实质性工作前，应按照本模板向人类报告其从仓库重建出的当前状态。

## A. 协议状态

- HARC version：
- adopted commit/tag：
- canonical language：
- bootstrap / AGENTS / manifest 状态：
- 协议文件同步缺陷：

## B. 人类已确认的当前状态

### B1. 研究目的
- 

### B2. 当前主要人类承诺
- 

### B3. Form / presentation 状态
- 

### B4. 最近重要人类决定
- 

## C. Critical Clarification 状态

### C1. Blocking
- `CLR-...` — 

### C2. 与当前任务相关的 Non-blocking
- `CLR-...` — 

### C3. 当前必须向人类询问的问题
- 

## D. Framework 状态

- Working Framework：
- 最新 Approved Framework：
- Framework Approval：
- 是否被 Clarification Gate 阻塞：
- 已知 framework synchronization defect：

## E. Artifact 状态

- 当前主要 Artifact：
- Artifact status：
- Final Artifact Approval：
- 与 Framework 的同步状态：

## F. Evidence / conflict 状态

- 与当前任务直接相关的 evidence：
- 已知 evidence conflict：
- 是否需要重新核验时效性来源：

## G. 双语状态

- 中文 canonical：
- 英文 mirror：
- 当前 parity：
- 已知 translation/terminology clarification：

## H. 当前请求的允许下一步

### 可以安全执行
- 

### 当前被阻塞
- 

### 本次请求的 HARC propagation path
`...`

## I. Onboarding 结论

- `PASS` — 已能仅根据仓库重建足够状态，可以进入允许的实质工作；
- `FAIL` — 存在 onboarding/persistence defect，先修复；
- `PARTIAL` — 可进行有限工作，但某些部分被 clarification / missing state 阻塞。

**结论：**

## J. Repository Context Resolver

根据 `HARC_CONTEXT_INTERFACE.yaml` 与 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`，Agent 必须确认：

`HARC REPOSITORY CONTEXT — ACTIVE`

至少包括：

- source of truth = GitHub；
- manifest / context-interface 路径；
- canonical language；
- `repository-backed / selective retrieval / no authoritative session copy`；
- `read latest before high-impact action`；
- `read latest before write`；
- `invalidate touched cache after write`；
- 当前任务 CONTENT / FORM / PROTOCOL route；
- authoritative refs 只列路径，不复制动态状态。

**Repository context active：** `YES / NO`

如果为 `NO`，Onboarding 不得判定为 `PASS`。

> 注意：本报告中的 Blocking Clarifications、Framework、Artifact 等摘要仅用于人类检查 Agent 是否理解正确；后续工作必须从 GitHub 最新 canonical revision 重新按需读取，不能把本报告当成权威状态。
