# START HERE — HARC 项目零上下文接管入口

> **本中文文件是规范性基准；英文 `START_HERE.md` 是同步镜像。**

本文件用于任何从零开始接手本研究项目的 AI Agent。

## 强制第一步

在实质性工作前：

1. 读取 `HARC_MANIFEST.yaml`；
2. 读取 `HARC_CONTEXT_INTERFACE.yaml`；
3. 读取 `BOOTSTRAP_PROMPT.zh-CN.md`；
4. 读取 `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`；
5. 读取 `AGENTS.zh-CN.md`；
6. 按 manifest / context interface 的 task route 按需读取当前状态；
7. 使用 `ONBOARDING_REPORT_TEMPLATE.zh-CN.md` 向人类输出 HARC Onboarding Report，并确认 `HARC REPOSITORY CONTEXT — ACTIVE`；
8. 只有在报告通过、Repository Context 已激活后，才开始实质工作；后续动态状态一律从 GitHub 最新 canonical revision 按需读取。

## Onboarding Report 至少包含

- 协议版本 / adopted commit；
- canonical language；
- 当前人类内容承诺；
- 当前 Form 状态；
- 当前 `BLOCKING` clarifications；
- 与任务相关的 `NON-BLOCKING` clarifications；
- Working / Approved Framework 状态；
- 当前 Artifact 状态；
- 已知同步缺陷；
- 当前请求的允许传播路径。

## Clarification-first

如果对核心命题、概念、术语/翻译、范围、推论关系或结构存在高影响不确定性，不要猜测：

`ambiguity -> Clarification Register -> human resolution -> Decision Log -> Core -> Argument Map -> Artifact`

## 正常决定传播

`human decision -> Decision Log -> appropriate Core -> Argument Map -> Artifact -> bilingual parity`

## 双语

除非本项目明确另有决定，中文 canonical，英文 synchronized mirror。

---

## 可复制给 AI Agent 的启动提示词

> 完整可复制启动提示词见 `BOOTSTRAP_PROMPT.zh-CN.md`。
