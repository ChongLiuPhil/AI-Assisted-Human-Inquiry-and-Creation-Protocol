# HARC → AHICP 语义迁移计划

**状态：** Working migration plan  
**目标版本：** v0.3.0-draft  
**规范性方向：** Human-led, AI-assisted, repository-grounded.

## 1. 迁移目的

本次迁移不是简单改名。

旧名称 **Human–AI Research Collaboration Protocol (HARC)** 主要围绕长期研究协作形成。新的正式名称：

> **AI-Assisted Human Inquiry and Creation Protocol (AHICP)**

副标题固定为：

> **A protocol for human-led inquiry, research, reasoning, writing, and creation with AI assistance.**

迁移的目的，是让协议名称、规范范围和既有治理结构一致，并避免把 AI 表述为与人对称的认知主体或知识劳动主体。

## 2. 保留的核心架构

下列成熟设计原则继续保留：

- repository-backed persistent project state；
- Chat 不是持久真值源；
- Content / Form / Protocol 三路由；
- Content Core / Form Core / Decision Log；
- Working Memory；
- Working / Approved Framework 区分；
- Framework Approval 与 Final Artifact Approval；
- AI proposal ≠ human commitment；
- evidence constraints；
- zero-context onboarding；
- cross-agent handoff；
- audit discipline；
- bilingual Chinese-canonical / English-mirror governance；
- 人类作为目的、判断、批准与最终责任的承担者。

## 3. 需要上位化的部分

旧协议中把通用机制限定为 `research` 的地方，应逐项判断并迁移为更准确的上位概念：

- `research project` → 在通用语境下改为 `inquiry or creation project` / `project`；
- `research state` → `project state`；
- `research memory` → `project memory` 或 `inquiry-and-creation memory`；
- `research content` → 视上下文改为 `substantive content`、`project content` 或保留 `research content`；
- `research collaboration` → 不再作为协议的总括性类别。

凡确实只讨论研究、证据、论文、学术政策或研究诚信的段落，继续保留 `research`，不得机械替换。

## 4. AI 的规范性地位

AHICP 的规范模型是：

```text
Human
  ├─ purpose
  ├─ inquiry
  ├─ reasoning
  ├─ judgment
  ├─ creation
  ├─ approval
  └─ responsibility
          ▲
          │
     AI assistance
          │
  ├─ retrieve
  ├─ compare
  ├─ structure
  ├─ propose
  ├─ draft
  ├─ verify
  ├─ transform
  └─ maintain project state
```

规范文本不得因为使用 `collaboration` 等日常词汇，而暗示 AI 是与人对称的认知主体、作者责任主体或最终知识责任承担者。

## 5. 三层模型的泛化

旧模型：

`Human Authorial Core -> Current Framework -> Derived Artifact`

保留其逻辑，但允许在不同项目类型中实例化：

- Layer 1 — **Human Intentional / Authorial Core**
- Layer 2 — **Operational Framework**
- Layer 3 — **Derived Artifact**

研究项目可以继续使用 Argument Map；创作项目可以使用适合该作品类型的结构表示。

## 6. 文件与标识迁移

迁移分阶段进行：

### Phase A — 语义入口
- README 中英文；
- Specification 中英文；
- AGENTS 中英文；
- protocol core / decision state；
- methodology article 的项目名称与范围声明。

### Phase B — 控制平面
- `HARC_MANIFEST.yaml` → `AHICP_MANIFEST.yaml`；
- `HARC_CONTEXT_INTERFACE.yaml` → `AHICP_CONTEXT_INTERFACE.yaml`；
- bootstrap / onboarding 文档内部引用；
- downstream template references。

旧文件名在过渡期可以保留兼容指针，但不得长期形成两个规范真值源。

### Phase C — 全仓语义审计
逐文件判断：
- 应泛化；
- 应继续保留 research-specific 语言；
- 应作为历史记录保持原文；
- 应更新 legacy identifiers。

### Phase D — 双语与接管验证
完成：
- bilingual parity audit；
- zero-context onboarding test；
- semantic migration audit；
- post-migration repair audit。

## 7. 版本策略

本迁移建议从 HARC v0.2.x 演进为：

> **AHICP v0.3.0-draft**

因为协议的核心治理架构被保留，但适用范围和规范性语言发生了实质扩展。

## 8. 与 PPF 的边界

AHICP 只规范 AI 如何辅助人的探究与创作，不定义出版基础设施。

**Personal Publishing Framework (PPF)** 负责作品的 source / build / publish / release / archive 生命周期。

项目可以采用：

```text
AHICP only
PPF only
AHICP + PPF
```

两者不得重复维护同一套规则。
