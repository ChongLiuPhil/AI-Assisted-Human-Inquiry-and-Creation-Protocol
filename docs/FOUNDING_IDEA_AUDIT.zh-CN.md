# 创始思想整合审计

**审计日期：** 2026-09-17  
**范围：** 导致 HARC 建立的讨论中，由人类明确提出的思想。  
**状态：** 初始三遍覆盖审计已完成；后续修复流程见 `THREE_CYCLE_REPAIR_AUDIT.zh-CN.md` 与 `FINAL_POST_REPAIR_AUDIT.zh-CN.md`。

> **本中文文件是规范性基准；英文 `FOUNDING_IDEA_AUDIT.md` 是同步镜像。**  
> 本文件由 AI 维护，用于检查覆盖情况；它不取代 `core/PROTOCOL_CORE.zh-CN.md` 或人类 Decision Log。

---

## 审计方法

创始讨论从三个不同角度进行检查。

### 第 1 遍 — 语义覆盖

问题：**每一个独立的人类原创协作思想，是否都已经在 HARC 中得到表示，而没有被 AI 解释静默替换？**

### 第 2 遍 — 操作覆盖

问题：**每个思想只是被描述了，还是能够通过文件、状态、模板、更新路径与批准规则实际执行？**

### 第 3 遍 — 新 Agent 交接模拟

问题：**如果原始聊天消失，一个新的、能力合格的 AI Agent 只获得仓库，它是否能够重建并继续预期协作模型？**

> 后来人类进一步明确：所谓多轮审计必须是每轮都“审查—识别缺陷—修复—验证”，而不是三遍被动阅读。该修正规则已进入 Protocol Core；本文件保留为创始思想覆盖清单，而真正的三轮修复记录见后续审计文件。

---

# 第 1 遍 — 语义覆盖

## F01 — GitHub 作为持久协作研究记忆

**创始思想：** 项目连续性应明确存在于 GitHub 文本/版本状态中，而不是依赖某一个 AI 账号、平台记忆、模型或聊天上下文。

**实现位置：**

- `core/PROTOCOL_CORE.zh-CN.md` P1、P9、P10
- `protocol/PERSISTENT_MEMORY.zh-CN.md`
- `protocol/SPECIFICATION.zh-CN.md`
- 项目 `AGENTS.zh-CN.md`

**状态：** FULLY INTEGRATED。

---

## F02 — 把人类研究内容意图保存到基础文本

**创始思想：** 人类有关研究主题的陈述、纠正、确认、拒绝与修订，应沉淀到基础规范内容文档。

**实现位置：**

- Protocol Core P2
- HARC Content Core 模型
- `templates/research-project/core/CONTENT_CORE.zh-CN.md`
- Decision Log + upstream-first 规则

**状态：** FULLY INTEGRATED。

---

## F03 — AI 扩写必须服从人类内容基础

**创始思想：** AI 展开不得静默违背、替换或漂移离开人类作者的基础思想。

**实现位置：**

- Protocol Core P2、P5、P8
- Specification 中 upstream-first、provenance 与 framework fidelity 规则

**状态：** FULLY INTEGRATED。

---

## F04 — AI 维护第二层操作性文本

**创始思想：** AI 应维护文章/书籍实际论证的压缩表示，显式表示主张、关系、章节角色与未决问题。

**实现位置：**

- Protocol Core P4
- Working Argument Map 模型
- `templates/research-project/docs/argument-map.zh-CN.md`

**状态：** FULLY INTEGRATED。

---

## F05 — 操作性 framework 是主要人机讨论界面

**创始思想：** 对大型成果，人机结构讨论主要在压缩 framework 上进行，而不是每次重新通读完整扩写稿。

**实现位置：**

- Protocol Core P4
- Specification Working Argument Map 规则
- 白皮书与项目模板

**状态：** FULLY INTEGRATED。

---

## F06 — 人类修改先向上游传播

**创始思想：** 人类给出实质性反馈后，应先保存人类决定，再更新操作性 framework，最后更新最终成果。

**实现位置：**

- Protocol Core P5
- Specification upstream-first update
- CONTENT / FORM / PROTOCOL 路由

**状态：** FULLY INTEGRATED。

---

## F07 — 研究内容与形式/呈现分开

**创始思想：** 主张与论证不同于字体、版式、视觉设计、引用呈现、格式和成果类型；Agent 应先分类再持久化。

**实现位置：**

- Protocol Core P3
- `protocol/FORM_CONTENT_ROUTING.zh-CN.md`
- Content Core / Form Core 分离

**状态：** FULLY INTEGRATED。

---

## F08 — 形式偏好可跨项目复用

**创始思想：** 作者可以形成跨书籍、论文、文章复用的呈现习惯，不必每个项目从零建立。

**实现位置：**

- Protocol Core P3、P14
- `protocol/FORM_PROFILE_INHERITANCE.zh-CN.md`
- `templates/form-profiles/AUTHOR_PROFILE.zh-CN.md`

**状态：** FULLY INTEGRATED AFTER AUDIT FIX。

---

## F09 — 不同成果类型需要不同 Form Profile

**创始思想：** 书籍、学术论文、普通文章可以共享作者级偏好，但具有不同的成果类型结构。

**实现位置：**

- Protocol Core P14
- BOOK / ACADEMIC_PAPER / ARTICLE 双语模板

**状态：** FULLY INTEGRATED AFTER AUDIT FIX。

---

## F10 — AI 默认值不得伪装成人类偏好

**创始思想：** 临时实现选择必须与真正的人类形式决定区分。

**实现位置：**

- Form Core 模型
- `TEMPORARY-DEFAULT`
- Form-profile inheritance 规则

**状态：** FULLY INTEGRATED。

---

## F11 — Working Framework 与 Human-Approved Framework 必须区分

**创始思想：** AI 维护的操作性表示不自动得到人类认可；只有明确阅读/确认后，某个版本才成为权威基线。

**实现位置：**

- Protocol Core P6
- `protocol/FRAMEWORK_APPROVAL.zh-CN.md`
- Framework Status 模型
- 不可变 `FW-xxx` 快照约定

**状态：** FULLY INTEGRATED。

---

## F12 — Approved Framework 是主要实质性思想责任锚点

**创始思想：** 在长篇 AI 扩写成果中，人类最高强度的实质责任应集中在理解和确认核心命题、论证关系、区分与章节功能。

**实现位置：**

- Protocol Core P6、P13
- HARC-D011
- Framework Approval 责任模型

**状态：** FULLY INTEGRATED AFTER AUDIT CLARIFICATION。

---

## F13 — 区分 framework 缺陷与 AI 扩写缺陷

**创始思想：** 经人类确认的论证结构中存在的缺陷，与后续 AI 文字/实现中局部引入的缺陷不是同一种问题。

**实现位置：**

- Protocol Core P13
- Framework Approval 中专门的 defect 区分
- `DERIVED-PROVISIONAL`

**状态：** FULLY INTEGRATED AFTER AUDIT CLARIFICATION。

**限定：** HARC 还保留公开投稿/发布前独立 Final Artifact Approval，因为 framework approval 本身不能满足所有外部问责规则。

---

## F14 — Approved Framework 必须投影到面向读者的总览

**创始思想：** 被确认的思想架构应出现在论文摘要/引言、文章开篇/概览或书籍导论/章节路线图中。

**实现位置：**

- Protocol Core P7
- Specification Overview Projection
- Framework Approval 规则
- 成果类型 Form Profile

**状态：** FULLY INTEGRATED。

---

## F15 — 仓库记忆可持续增长，而 active state 保持紧凑

**创始思想：** 外部化项目记忆应超越单一聊天上下文长期积累，同时不要求新 Agent 每次加载全部历史。

**实现位置：**

- Protocol Core P9、P10
- Persistent Memory 规则
- active / historical state 分离

**状态：** FULLY INTEGRATED。

---

## F16 — 新 AI Agent 无需原始聊天即可接管

**创始思想：** 项目状态层面应与特定平台/Agent 解耦；替换 Agent 应能从 GitHub 重建当前项目。

**实现位置：**

- Protocol Core P1、P9
- Persistent-memory handoff target
- Specification Agent Handoff
- 项目 AGENTS 模板

**状态：** FULLY INTEGRATED。

---

## F17 — 工作流应成为未来研究项目的可复用模板

**创始思想：** 新项目可以把 HARC 交给新的 AI Agent，由它针对主题建立适当目录和文件，同时保留相同协作逻辑。

**实现位置：**

- Protocol Core P11
- `templates/research-project/`
- Form-profile 模板

**状态：** FULLY INTEGRATED。

---

## F18 — 初始范围以 GitHub 为中心，其他平台后置

**创始思想：** 本地/其他系统以后可以考虑，但当前协议先聚焦 GitHub + human + AI Agent(s)。

**实现位置：**

- Protocol Core P1 与范围
- Specification
- HARC-D002

**状态：** FULLY INTEGRATED。

---

## F19 — HARC 应成为独立项目，不依赖具体研究主题

**创始思想：** 把协作方法论从客观概率论文中分离，成为独立可复用项目。

**实现位置：**

- 独立 HARC repository
- HARC-D001
- Protocol Core P11

**状态：** FULLY INTEGRATED。

---

## F20 — 独立项目同时包含说明性文章与可执行协议/模板

**创始思想：** HARC 既要像文章一样解释协作模式，也必须在实践中可直接使用。

**实现位置：**

- Whitepaper 中英双语
- Methodology Article
- Specification
- Templates
- Architecture / contribution docs

**状态：** FULLY INTEGRATED。

---

## F21 — HARC 全项目中英双语，中文为规范基准

**创始思想（2026-09-18 新增）：** 项目所有实质性内容必须做成中英双语；人类编辑与审阅以中文为基准；任何中文编辑都必须同步英语；冲突时中文优先。

**实现位置：**

- Protocol Core P18
- HARC-D015
- `protocol/BILINGUAL_SYNC.zh-CN.md`
- Specification bilingual synchronization
- AGENTS bilingual contract
- 全仓库双语迁移

**状态：** FULLY INTEGRATED AFTER BILINGUAL PARITY AUDIT。

---

# 第 2 遍 — 操作覆盖

第二遍检查上述原则是否真正可执行。

## 已确认的操作元素

- Content Core 模板存在；
- Form Core 模板存在；
- Decision Log 模板存在；
- Working Argument Map 模板存在；
- Framework Status 模板存在；
- immutable Approved Framework 约定存在；
- feedback routing 存在；
- upstream-first propagation 存在；
- persistent-memory promotion test 存在；
- evidence-conflict procedure 存在；
- `DERIVED-PROVISIONAL` 与 final-approval 状态存在；
- 新 Agent AGENTS contract 存在；
- artifact-type form profiles 存在；
- reusable author form profile 存在；
- 双语 canonical/mirror 规则与模板正在完整迁移。

## 审计中发现并修复的缺口

### Gap A — 形式复用已有规范，但操作模板不完整

**修复：** 加入 Form Profile Inheritance，以及 author、book、academic paper、article 模板。

### Gap B — 责任区分存在，但没有充分进入 founder state

**修复：** 加入 Protocol Core P13、HARC-D011，并在 Framework Approval 中独立说明 framework-level 与 expansion-level defect。

### Gap C — 新项目没有明确 pin 所采用的 HARC 版本

**修复：** Project AGENTS 与 bootstrap README 增加 protocol source/version/commit。该项是 AI 审计加入的实现保护，不宣称为原始创始思想。

### Gap D — 项目后来要求双语，但历史文件为单语

**修复：** 建立中文 canonical / 英文 synchronized mirror 规范，并执行仓库范围迁移。最终状态由独立 bilingual parity audit 验证。

---

# 第 3 遍 — 新 Agent 交接模拟

假设：原始聊天不可用，新 Agent 只获得 HARC 仓库与目标项目/主题。

## Agent 是否能知道怎么工作？

**是。** 它可以从 README / AGENTS、Specification、Persistent Memory、Routing、Framework Approval、Form Inheritance、Bilingual Sync 及 Templates 重建工作流。

## 能否在不发明人类观点的情况下初始化新项目？

**是。** 模板要求未知项保持 `UNRESOLVED`，不得静默用 AI 猜测填入人类规范状态。

## 能否区分人类内容、人类形式、AI 结构与派生正文？

**是。** 状态模型与路由规则明确这些角色。

## 能否知道哪个 framework 真正得到人类批准？

**是，前提是项目遵守 snapshot rule。**

## 能否恢复长期历史而不一次加载全部？

**原则上可以。** Persistent Memory 定义 active state、historical state、index/archive 与 selective retrieval。

## 能否知道当前正文是否只是 provisional？

**可以。** 成果状态区分 `DERIVED-PROVISIONAL`、`FINAL-REVIEW`、`FINAL-APPROVED`。

## 能否知道哪种语言具有规范权威？

**可以。** 中文 canonical / 英文 mirror 规则现已进入 Protocol Core、Specification、AGENTS 与独立 Bilingual Sync Policy。

---

# 后续人类确认的发展

本节不把后来的设计演化追溯性地伪装成 2026-09-17 最初创始讨论的一部分，而是记录之后由人类项目发起人明确提出并确认的新协议承诺。

## E01 — GitHub 作为权威外部记忆与工作状态接口

**后续人类决定：** 不在聊天上下文中长期维护第二份项目状态，而把 GitHub 直接作为权威 external memory + working state；模型上下文只保留 Repository Resolver 与当前任务所需的临时检索缓存。

**实现位置：**

- Protocol Core P21–P22
- HARC-D020
- `protocol/REPOSITORY_CONTEXT_INTERFACE.zh-CN.md`
- `HARC_CONTEXT_INTERFACE.yaml`
- project template context interface
- methodology article C13 / T11

**状态：** IMPLEMENTED。

## E02 — 三层长期研究记忆 + 并行 Working Memory

**后续人类决定：** 原 “Layer 1.5” 模型被取消。三个内容层都属于 Long-Term Research Memory：

`Layer 1 Human Authorial Core -> Layer 2 Current Framework -> Layer 3 Derived Artifact`

另设与三层并行的 Working Memory，记录当前阶段、目标、active tasks、完成状态、next actions、TODO、blockers、pending human decisions、Clarifications、sync defects 与 handoff。

Clarification 是 Working Memory item。人类解决后的稳定内容必须 Promotion 到相应长期记忆；Working Memory 退出 active 状态后只保留状态、Decision ID 与目标指针。

**实现位置：**

- Protocol Core P19、P23
- HARC-D021
- `protocol/WORKING_MEMORY.zh-CN.md`
- `docs/working-memory.zh-CN.md`
- Manifest / Context Interface / Onboarding / AGENTS
- project templates
- methodology article C11、C14 / T9、T12 / draft

**状态：** IMPLEMENTED。

---

## E03 — Working Memory 模块化：Current Focus / Task Plan / Work Log

**后续人类决定：** Working Memory 是功能区，不应被固定成单一文档。项目可根据工程需求、AI 性能与工作流便利性采用单文件或多文件实现，但至少应有三个逻辑角色：

- Current Focus — 当前最近期最高优先级目标；
- Task Plan — 动态任务、计划、TODO、blockers、pending decisions / Clarifications；
- Work Log — 主要供人类作者以后回顾的大体进展、里程碑与思想/工作路径变化。

完成的任务应退出 active Task Plan，并以适当粒度进入 Work Log；稳定规范结果仍需 Promotion 到 Long-Term Memory。

Work Log 需要定期维护，但默认不进入 AI onboarding 上下文。它不保存 AI 隐藏 chain-of-thought / scratchpad。

**实现位置：**

- Protocol Core P24
- HARC-D022
- `protocol/WORKING_MEMORY.zh-CN.md`
- `docs/working-memory.zh-CN.md`（Index）
- `docs/working-memory/current-focus.zh-CN.md`
- `docs/working-memory/task-plan.zh-CN.md`
- `docs/working-memory/work-log.zh-CN.md`
- Manifest / Context Interface / Onboarding / AGENTS
- project templates
- methodology article C15 / T13 / draft

**状态：** IMPLEMENTED。

---

## E04 — 当前全讨论覆盖复核

**复核日期：** 2026-09-18  
**范围：** 基于当前可恢复的人类—AI 讨论与仓库状态，对迄今已明确讨论的 HARC 设计再次执行一轮“审查 -> 修复 -> 验证”。

### 覆盖结果

以下讨论内容均已找到规范承诺、执行机制与可发现入口：

- GitHub 作为持久共享研究记忆与权威工作状态；
- AI Agent 可替换、项目状态不可依赖单一聊天/模型；
- CONTENT / FORM / PROTOCOL 分流与上游优先传播；
- Layer 1 Human Authorial Core；
- Layer 2 Current Framework；
- Layer 3 Derived Artifact；
- 三层 Long-Term Research Memory 与并行 Working Memory 的区分；
- Working Memory 作为可单文件或多文件实现的功能区；
- Current Focus / Task Plan / Work Log 三类逻辑角色；
- Work Log 主要供人类历史回顾、定期维护、默认不进入 AI onboarding；
- 高影响不确定性进入 Task Plan / Clarification；
- 人类解决后 Promotion 到相应 Long-Term Memory；
- 零上下文 START_HERE / Bootstrap Prompt / Onboarding Handshake；
- GitHub 作为 Repository-Backed Context，模型上下文只保留 Resolver 与临时 cache；
- 中文 canonical / 英文 synchronized mirror；
- pre-cutover English-ahead 内容先回填中文，再完成 canonical cutover；
- Framework Approval 与 Final Artifact Approval 两个批准门；
- framework-level defect 与 derived-expansion defect；
- Approved Framework -> reader-facing overview projection；
- evidence 作为横向约束，不静默改写人类意图；
- author / artifact-type / project form-profile inheritance；
- HARC 同时产出可执行协议与受自身治理的方法论文章；
- 方法论文章中的人类认知/认识责任、可委托认知劳动与不可静默委托的责任边界；
- 三轮 review-repair-verify + 独立 post-repair audit；
- HARC 自托管、自举接管与模板继承。

### 本轮发现并修复的残留

1. 根 `START_HERE` 的英文 mirror 仍把旧 Clarification Register 当活跃入口；
2. 根 `AGENTS.md` 仍残留旧 Clarification Register、旧方法论文章读取顺序与缺失的 Repository-Backed Context 细节；
3. project-template `START_HERE` 出现步骤编号回归，并仍使用旧 Clarification Register 路由；
4. project-template `AGENTS` 仍把 legacy clarification-register 当 active read/write target；
5. English Onboarding Handshake 尚未完全镜像 Current Focus / Task Plan 模型；
6. Persistent Memory 与 Bootstrap Prompt 有少量旧单体 Working Memory / Clarification 表述；
7. 本审计自身的双语迁移状态说明已经过时。

上述项目均已在本轮修复并同步中英文。

### 当前显式人类待决边界

这些项目已经被正确持久化为“等待人类决定”，因此不是实现缺口：

- `CLR-001` — 方法论文章中心责任概念；
- `CLR-002` — Framework Responsibility Thesis 强度；
- `CLR-003` — semantic version control 是否正式作为 HARC working term；
- `CLR-004` — generation–verification asymmetry 的地位；
- `CLR-005` — responsibility concentration 是否保留或替换；
- `CLR-006` — extended / distributed cognition 的理论关系；
- `CLR-007` — 经验验证计划在文章中的地位；
- `CLR-008` — 学科 / intellectual positioning；
- `CLR-009` — 正式开放许可；
- `CLR-010` — 目标发布渠道与渠道特定形式约束；
- 方法论文章整体 Framework Approval（尚无 `MA-FW-001`）；
- Final Artifact Approval（尚未进行）。

其中 `CLR-001 / CLR-002 / CLR-005` 当前阻塞方法论文章 Framework Approval；`CLR-009` 阻塞 formal release；`CLR-010` 不阻塞思想 framework，但阻塞最终投稿/发布形式冻结。

### 结论边界

本节能确认的是：**当前可恢复讨论中已明确形成的人机协作设计要求，都已在仓库中找到实现或明确的人类待决状态。**

它不能证明任何已删除、不可访问或从未持久化的历史对话内容也被覆盖。

**状态：** `PASS AFTER REPAIR`。

---

---

# 仍未解决的项目

## Open-source licensing

发起人明确希望 HARC 成为开放项目。仓库已公开并有贡献基础设施，但公开 GitHub 仓库不自动构成 open-source/open-content 授权。

确切许可证尚未经人类确认。

见 `LICENSE-DECISION.zh-CN.md`。

**状态：** HUMAN DECISION STILL REQUIRED。

---

# 审计结论

在最初三遍覆盖检查及后续修复之后：

- 创始讨论中识别的实质性协作概念都已经进入 HARC；
- 原本部分操作化的 form-profile reuse 已补齐；
- framework vs expansion responsibility 已进入 founder-level state；
- protocol version pinning 强化了新 Agent 交接；
- HARC 不需要任何客观概率研究内容；
- 开放许可仍是一个需要人类决定的法律/治理问题；
- 2026-09-18 新增的双语治理已经完成初始仓库级 migration/parity audit；后续每次实质编辑仍必须把双语同步作为完成条件。

未来审计应把新的人类创始决定与本清单比较；出现真正的新设计承诺时，应先更新 Protocol Core / Decision Log。
