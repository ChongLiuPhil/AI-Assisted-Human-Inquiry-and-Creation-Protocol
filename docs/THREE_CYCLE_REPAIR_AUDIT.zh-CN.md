# 三轮“审查—修复”审计

**日期：** 2026-09-17  
**范围：** 整合发起人明确提出的 HARC 思想，以及 HARC 自身必须产出方法论文章的要求。  
**解释：** 每一轮都是 `审查 -> 识别缺陷 -> 修复/实现 -> 验证修复`。

> **本中文文件是规范性基准；英文 `THREE_CYCLE_REPAIR_AUDIT.md` 是同步镜像。**

本文件取代任何把早期“三遍审查”理解为三次被动阅读之后只进行一次修复的解释。

---

## 第 1 轮 — 语义 / 真值源修复

### 审查问题

所有人类原创设计承诺是否已经显式进入创始人层规范状态，还是仍有重要思想只存在于说明性文字中？

### 发现的缺陷

1. 审计程序本身定义不足：“三遍审查”此前仍过于接近重复检查，而不是三轮完整修复循环。
2. 新明确的“双重产出”要求尚未进入创始人层状态：HARC 必须同时是可执行开放项目与方法论文章项目。
3. 人类认知责任，以及“认知劳动委托”与“认识责任委托”的区分，需要成为明确项目承诺，而不是只从 framework approval 中间接推出。

### 已实施修复

- 在 `core/PROTOCOL_CORE` 加入 P15：多轮审计必须是审查—修复循环，并在要求时完成独立修复后审计。
- 加入 P16：HARC 有两个互相支撑的产出——可执行开放协议与方法论文章。
- 加入 P17：认知劳动可以大量委托，但高杠杆认识责任保持在人类治理之下。
- 在 `core/DECISION_LOG` 加入 HARC-D013 与 HARC-D014。

### 验证

创始人层规范状态现在已经明确保存这些承诺；它们不再依赖当前聊天，也不依赖 AI 从白皮书反向推断。

**第 1 轮状态：** `REPAIRED AND VERIFIED`。

---

## 第 2 轮 — 操作 / 成果修复

### 审查问题

创始人层承诺是否能够通过具体文件和状态实际执行，尤其是“产出真正方法论文章”的要求？

### 发现的缺陷

1. HARC 已有概念性白皮书，但方法论文章尚未作为独立、受治理的学术成果存在。
2. 缺少文章级 Working Framework 来区分人类确认思想与 AI 提议术语/结构。
3. 文章需要显式状态，防止 AI 生成的第一版草稿被误称为人类已批准的学术立场。

### 已实施修复

建立：

- `paper/METHODOLOGY_ARTICLE_ARGUMENT_MAP`
  - 状态：`WORKING-FRAMEWORK`；
  - 记录当前命题集合、论证结构、证据锚点、等待人类决定的问题和 AI 提议术语。
- `paper/METHODOLOGY_ARTICLE.zh-CN.md`
  - 第一份完整中文方法论文章草稿；
  - 状态：`DERIVED-PROVISIONAL`；
  - 把 HARC 展开为关于持久研究状态、语义版本控制、认知劳动委托、认识责任、framework approval 与可审计作者性的研究方法论。

草稿还引入并区分：

- 认知劳动委托 vs 认识责任委托；
- framework defect vs derived-expansion defect；
- Framework Approval vs Final Artifact Approval；
- 持久外部状态 vs 单次运行上下文；
- contribution transparency vs authorship/accountability。

### 加入文章的证据

草稿连接了相关文献/政策，包括：

- Clark & Chalmers：extended mind；
- Hutchins：distributed cognition；
- Hardwig：epistemic dependence；
- Parasuraman & Riley：automation reliance；
- ICMJE authorship/accountability 要求；
- Nature/Springer Nature AI 与 authorship 政策；
- CRediT contributor-role taxonomy；
- UNESCO 以人为中心的生成式 AI 治理指南。

### 验证

方法论文章已经作为独立学术成果存在，并且自身受到它所描述的协议治理。Working Framework 没有被错误标成已获人类批准，正文也没有被错误标成 final。

**第 2 轮状态：** `REPAIRED AND VERIFIED`。

---

## 第 3 轮 — 可发现性 / 交接修复

### 审查问题

如果原始对话消失，新 AI Agent 只收到仓库，它是否无需依赖搜索运气就能发现审计纪律、方法论文章、文章状态与相关协议扩展？

### 发现的缺陷

1. 根 `AGENTS.md` 没有明确要求把多轮审计解释为审查—修复循环。
2. 根 `AGENTS.md` 没有明确把方法论文章标识为受 HARC 治理的成果。
3. 根 `README.md` 没有醒目呈现协议与方法论文章两个同等重要的项目产出。
4. 新文章文件与审计文件需要出现在常规的人类/Agent onboarding 路径中。

### 已实施修复

更新 `AGENTS.md`：

- 定义多轮审计为修复循环；
- 标识方法论文章及其 Working Framework；
- 在人类批准前维持 `DERIVED-PROVISIONAL`；
- 把 form-profile inheritance 加入 Agent 读取顺序。

更新 `README.md`：

- 把 HARC 表述为双重产出项目；
- 链接方法论文章与 argument map；
- 解释认知劳动委托 vs 认识责任；
- 暴露审计纪律；
- 链接 repair audit 与 final audit；
- 提供明确的人类与 AI onboarding 路径。

### 验证

一个从 `README.md` 或 `AGENTS.md` 开始的新 Agent 现在可以发现：

- 可执行协议；
- 创始人层真值源；
- 方法论文章；
- 文章批准状态；
- 审查—修复要求；
- 可复用模板与 form-profile inheritance。

**第 3 轮状态：** `REPAIRED AND VERIFIED`。

---

# 三轮修复后的状态

要求的三轮循环均已完成。

每一轮都包含：

1. 审查；
2. 识别缺陷；
3. 仓库修复/实现；
4. 验证修复。

下一步是独立的**修复后审计**，在这些修复全部结束之后执行，而不是被包含在三轮之一中。
