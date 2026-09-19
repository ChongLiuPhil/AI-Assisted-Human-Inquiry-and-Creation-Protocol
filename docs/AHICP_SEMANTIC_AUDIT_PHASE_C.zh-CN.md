# AHICP v0.3 Phase C 语义审计

**状态：** IN PROGRESS  
**日期：** 2026-09-19  
**依据：** AHICP-D026、AHICP Semantic Migration Plan

## 审计目标

本审计逐类区分旧 HARC 仓库内容在 AHICP v0.3 中应如何处理，避免把“扩大适用范围”误解为机械删除所有 research 语言。

## 四类处理规则

### 1. GENERALIZE

适用于原本承担通用协议功能、但因旧 HARC 默认研究场景而被写成 research-specific 的内容。

已识别并开始迁移：
- Protocol Core 的项目总范围；
- README / Specification 的总定义；
- Agent contract / onboarding 控制链；
- persistent project state / project memory；
- 通用 Content / Form / Protocol routing；
- 通用 Working Memory / handoff / approval 机制。

### 2. RETAIN RESEARCH-SPECIFIC

下列内容继续允许明确使用 research / scholarly 语言：
- 方法论文章本身；
- evidence / source verification；
- research integrity、academic authorship、venue policy；
- 研究论文、学术书籍等 artifact-specific profiles；
- `templates/research-project/` 作为研究特化模板。

迁移不得为了名称统一而把这些内容错误泛化。

### 3. PRESERVE HISTORICAL

历史事实与审计标识保持原样：
- `HARC-D001`–`HARC-D025`；
- 旧项目名称出现在历史决策、审计记录或当时语境中的事实性陈述；
- 已完成的历史 audit snapshot。

新决定从 `AHICP-D026` 开始采用 AHICP 前缀。

### 4. MIGRATE LEGACY IDENTIFIER

当前控制面、启动链、模板和 live navigation 中的旧标识必须迁移：
- `HARC_MANIFEST.yaml` → `AHICP_MANIFEST.yaml`；
- `HARC_CONTEXT_INTERFACE.yaml` → `AHICP_CONTEXT_INTERFACE.yaml`；
- 当前 README / Specification / AGENTS / START_HERE 等；
- template control files；
- old repository URL。

旧控制文件可以短期保留 compatibility pointer，但不得继续作为规范真值源。

## 当前审计结论

AHICP 的稳定核心不是“research collaboration”，而是：

> **human-led inquiry and creation with AI assistance**

其中：
- 人保持 purpose、direction、substantive judgment、approval、responsibility；
- AI 可以大量执行/辅助工作，但不成为对称认知主体或最终责任主体；
- repository-backed state 使 AI Agent 可替换；
- Content / Form / Protocol、Working Memory、Framework Approval、Final Artifact Approval 等成熟结构继续保留。

## 与 PPF 的边界

AHICP 不承担出版基础设施规范。

**Personal Publishing Framework (PPF)** 负责：
`SOURCE -> BUILD -> PUBLISH -> RELEASE -> ARCHIVE`

项目可以采用 AHICP only、PPF only 或 AHICP + PPF。

## 尚待完成

- live Architecture / Roadmap / template navigation 全面迁移；
- repository-wide legacy-path scan；
- bilingual parity audit；
- zero-context onboarding test；
- post-migration repair audit；
- 方法论文章中“项目名称变化”与“文章本身仍为 research-specific”的精确处理。

## 合并条件

Phase C 不以“找不到 HARC 字样”为目标。

合并条件是：
1. 所有 live control paths 使用 AHICP；
2. 历史 HARC 标识保留可解释性；
3. research-specific 内容未被误泛化；
4. 双语同步；
5. onboarding 可从零上下文恢复；
6. post-migration audit 无阻塞缺陷。
