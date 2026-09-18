# HARC 架构

> **本中文文件是规范性基准；英文 `ARCHITECTURE.md` 是同步镜像。**

## 系统模型

```text
                   人类作者
                      |
        +-------------+-------------+
        |             |             |
     CONTENT         FORM        PROTOCOL
        |             |             |
        v             v             v
  CONTENT_CORE    FORM_CORE     AGENTS / spec
        \             /             |
         \           /              |
          +--- DECISION_LOG <---------+
                    ^
                    |
             human resolution
                    |
          Critical Clarification
              Register (1.5)
                    ^
                    |
          AI detects ambiguity
                    |
                    v
           Working Argument Map
                    |
          人类 Framework Approval
                    |
                    v
             Approved FW-xxx
                    |
        +-----------+------------+
        |                        |
        v                        v
      Evidence               AI Expansion
        \                        /
         \                      /
          +----- Derived Artifact
                    |
              Final Review
                    |
                    v
             Final Approved
```

采用双语配置时，上述所有人类可读规范状态同时具有中文 canonical 与英文 mirror。

## 权威性不等于时间先后

较晚出现的文本不会仅仅因为生成得更晚，就自动比早期规范状态更有权威。

一段成熟的正文不能仅因后生成，就覆盖 Content Core。

一个经人类批准的 framework 也不能覆盖之后明确的人类内容决定；相反，旧 framework 会变成不同步状态，需要修订并重新批准。

## 当前状态与历史

HARC 区分：

- **当前状态** — 紧凑的规范文件，治理当前工作；
- **历史** — 决策、旧 framework、证据、归档草稿。

这样既可以保存长期记忆，又不用让每个 Agent 一次性加载所有历史细节。

## 三个路由平面

### Content 平面

```text
人类内容反馈
  -> 如存在高影响歧义：Clarification Register
  -> 人类解决
  -> Decision Log
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

一个稳定 HARC 项目应允许新的、能力合格的 Agent 仅通过仓库状态回答：

1. 人类当前究竟想论证什么？
2. 人类当前希望成果怎样呈现？
3. 哪个论证 framework 实际已经得到人类批准？
4. 哪些内容由 AI 提议但人类尚未接受？
5. 哪些证据约束当前主张？
6. 哪些高影响不确定性正在 Clarification Register 中等待人类决定？
7. 哪些问题仍未解决？
8. 当前成果是否与已批准状态同步？
9. 中英文规范文件是否保持语义同步？

如果离开旧聊天就无法回答这些问题，项目存在持久化或双语同步缺陷。
