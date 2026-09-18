# HARC 架构

> **本中文文件是规范性基准；英文 `ARCHITECTURE.md` 是同步镜像。**

## 系统模型

```text
        Zero-context Bootstrap / Onboarding Handshake
      START_HERE + MANIFEST + CONTEXT_INTERFACE
                       |
               Repository Resolver
                       |
                 Working Memory
        stage / goals / tasks / blockers
      clarifications / TODO / handoff / status
              /           |           \
             v            v            v
     +-----------+   +-----------+   +-----------+
     |  Layer 1  |-->|  Layer 2  |-->|  Layer 3  |
     | Authorial |   |  Current  |   |  Derived  |
     |   Core    |   | Framework |   | Artifact  |
     +-----------+   +-----------+   +-----------+
          ^               ^               ^
          |               |               |
          +------ Promotion from ----------+
                 resolved Working Memory
```

三层都是长期研究记忆。Working Memory 与三层并行，负责当前工作的可续接状态。

采用双语配置时，上述所有人类可读规范状态同时具有中文 canonical 与英文 mirror。

## Repository-backed context

HARC 把 GitHub 定义为唯一权威项目状态源：

`GitHub Repository = authoritative external memory + working state`

`Model Context = transient retrieval cache + control plane`

Agent 会话只保留最小 Repository Resolver。Blocking Clarifications、Framework、Artifact、Core、Decision Log 等动态状态需要时从 GitHub 最新 canonical revision 按需读取。写入后，旧上下文缓存立即视为 stale。

## 权威性不等于时间先后

较晚出现的文本不会仅仅因为生成得更晚，就自动比早期规范状态更有权威。

一段成熟的正文不能仅因后生成，就覆盖 Content Core。

一个经人类批准的 framework 也不能覆盖之后明确的人类内容决定；相反，旧 framework 会变成不同步状态，需要修订并重新批准。

## 长期记忆、工作记忆与历史

HARC 区分：

- **长期记忆 Layer 1** — 人类作者核心基础；
- **长期记忆 Layer 2** — 当前论述框架；
- **长期记忆 Layer 3** — 派生成果；
- **Working Memory** — 当前阶段、目标、任务、阻塞、clarification、TODO 与 handoff；
- **历史** — 决策、旧 framework、证据、归档草稿与 Git 历史。

Working Memory 用于续接，不取代长期层。稳定结果通过 Promotion 进入相应长期层。

## 三个路由平面

### Content 平面

```text
人类内容反馈
  -> 如存在高影响歧义：Working Memory / Clarification
  -> 人类解决
  -> Promotion -> Decision Log
  -> Content Core
  -> Working Argument Map
  -> 如属实质变化则进行 Framework Approval
  -> Derived Artifact
```

### Form 平面

```text
人类形式反馈
  -> Decision Log
  -> Form Core
  -> Typesetting / Rendering
  -> Derived Artifact
```

### Protocol 平面

```text
人类工作流反馈
  -> Decision Log
  -> Protocol / AGENTS
  -> Agent 行为 / 模板
```

## 两个批准门

```text
Working intellectual structure
  -> FRAMEWORK_APPROVAL
  -> AI-assisted large-scale expansion
  -> FINAL_ARTIFACT_APPROVAL
  -> release/submission
```

第一个门治理思想架构；第二个门治理具体发布版本。

## 核心不变量

一个稳定 HARC 项目应先让新的、能力合格的 Agent 通过 START_HERE / HARC_MANIFEST / HARC_CONTEXT_INTERFACE 完成 Onboarding Handshake，激活 Repository Resolver，然后仅通过 GitHub 最新 canonical 状态回答：

1. 人类当前究竟想论证什么？
2. 人类当前希望成果怎样呈现？
3. 哪个论证 framework 实际已经得到人类批准？
4. 哪些内容由 AI 提议但人类尚未接受？
5. 哪些证据约束当前主张？
6. Working Memory 中有哪些 blocker、pending human decision 与 clarification？
7. 哪些问题仍未解决？
8. 当前成果是否与已批准状态同步？
9. 中英文规范文件是否保持语义同步？

如果离开旧聊天就无法回答这些问题，项目存在持久化或双语同步缺陷。
