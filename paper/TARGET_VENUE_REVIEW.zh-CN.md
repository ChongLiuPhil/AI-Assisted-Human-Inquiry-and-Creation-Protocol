# 方法论文章 — Target Venue Review

**状态：** `HUMAN-SELECTED — PRIMARY TARGET: ETHICS AND INFORMATION TECHNOLOGY`  
**核验日期：** 2026-09-21  
**当前英文稿长度：** 约 6,427 words（仓库当前 Markdown 粗略计数；最终投稿需按期刊定义重新计数）  
**Framework 基线：** `MA-FW-001`

## 1. 结论

当前稿件不应只按“主题相似度”选刊。由于论文真实开发过程包含实质性的 AI-assisted drafting / restructuring / evidence organization，**目标期刊对生成式 AI 写作的政策兼容性必须和学术 scope 同时审查**。

基于 2026-09-21 官方期刊页面，当前优先顺序建议为：

1. **Ethics and Information Technology** — 当前最平衡的 primary candidate；
2. **Science and Engineering Ethics** — 很强的 secondary candidate，尤其适合强化 research responsibility / scholarly governance 后；
3. **AI & Society** — 主题很契合，但当前 LLM policy 与本项目真实生成式 AI 使用存在明显张力；
4. **Journal of Documentation** — knowledge / memory 主题相关，但 Emerald 当前禁止用生成式 AI copywriting 新材料，因此不适合作为当前稿件的投稿目标。

该排序最初来自 AI-researched review；依据 AHICP-D032，人类现已选择 **Ethics and Information Technology** 为当前 primary target，并保留 **Science and Engineering Ethics** 为 secondary candidate。

---

## 2. Primary candidate — Ethics and Information Technology

官方 scope：
https://link.springer.com/journal/10676/aims-and-scope

官方 submission guidelines：
https://link.springer.com/journal/10676/submission-guidelines

### 适配点

- 期刊明确关注 moral philosophy 与 ICT 的对话；
- scope 接受 conceptual analysis，以及 technology assessment、cognitive science、legal/social studies 等交叉讨论；
- AHICP 的 governed Project Memory、human decision persistence、authority/provenance、responsibility 与 AI-assisted inquiry governance 均可自然落入该范围；
- Original Research Paper 约 5,000–8,000 words；当前英文稿约 6,427 words，长度层面目前适配；
- double-blind review；
- LLM 不可作为 author，但生成式 LLM 使用可以在 Methods 或适当部分披露；最终版本必须由人类承担 accountability。

### 投稿时需要调整

- 把文章定位从“协议介绍”进一步收紧为一个 **normative + information-governance architecture**；
- 更清楚解释 Project Memory 为什么是 information-technology governance 问题，而不是单纯 productivity workflow；
- 保留 T9 的规范性边界，避免泛化成 universal authorship theory；
- 增加明确的 **AI-use disclosure / methodology-of-manuscript-development**；
- 准备 double-blind manuscript，避免 GitHub/作者身份线索直接暴露在 blind version 中；
- 检查 public repository / preprint 是否可能破坏匿名性，并按期刊规则处理。

### 当前判断

**最适合当前 MA-FW-001 的默认 target。**

原因不是“最容易发表”，而是其 scope、篇幅、conceptual framework 形式与真实 AI-use disclosure policy 目前最一致。

---

## 3. Secondary candidate — Science and Engineering Ethics

官方 journal overview：
https://link.springer.com/journal/11948

官方 submission guidelines：
https://link.springer.com/journal/11948/submission-guidelines

### 适配点

- scope 明确包括 research ethics、ethics of new and emerging technologies、computer ethics、ethics in design、values in technology；
- 接受 Original Article：research / scholarly article / review article；
- 10,000 words（excluding references）；
- double-blind review；
- 2026 年仍有 ongoing **Ethics of AI** collection；
- LLM 不可作为 author，但允许使用，要求在 Methods 或适当位置 proper documentation；最终文本必须由人类承担 accountability。

### 投稿时需要调整

- 强化“human responsibility / approval / accountability”与 research integrity / engineering governance 的联系；
- Project Memory Architecture 的技术细节应服务于伦理与责任论证，而不是让文章看起来像软件设计 specification；
- 可以把 Agent substitution、decision persistence、auditability 作为“责任可持续性”的 operational mechanism；
- 仍需提供 AI-use disclosure；
- 由于期刊自 2025 年起 fully Open Access，投稿前需核实 APC / institutional funding / waiver 情况。

### 当前判断

**非常有竞争力的第二选择。**

如果最终文章更强调“责任、作者性、研究诚信与 AI-assisted scientific practice”，它可能比 Ethics and Information Technology 更自然。

---

## 4. Conditional candidate — AI & Society

官方 aims and scope：
https://link.springer.com/journal/146/aims-and-scope

官方 submission guidelines：
https://link.springer.com/journal/146/submission-guidelines

### 学术适配

主题上高度相关：
- human-centered AI；
- responsibility；
- authorship；
- AI-mediated workflows；
- methodology / societal implications；
- Open Forum / Review 等栏目允许概念与方法论反思。

Research 正常长度约 10k；Open Forum 约 8k。

### 关键政策张力

该刊 2026 年官方 guideline 明确写明：

> LLM use for tasks other than grammar and translation ... are strongly discouraged.

同时其 submission guidelines 又要求非 copy-editing 的 LLM 使用被 proper documented。

AHICP 方法论文章的真实开发过程包含：
- AI-assisted structural rewriting；
- generative drafting；
- literature organization；
- bilingual synchronized rewriting；
- validator / governance implementation。

因此，把本稿投给 AI & Society 会产生真实 policy-fit 风险。不能通过把这些工作描述成“仅 copy editing”来规避，因为那会与项目 provenance 不符。

### 当前判断

**主题强匹配，但当前不作为 primary target。**

除非编辑部对透明披露后的这类 AI-assisted methodology manuscript 明确表示可接受，否则不建议优先投入格式化成本。

---

## 5. Excluded for current manuscript — Journal of Documentation

官方 journal / author guidelines：
https://www.emeraldgrouppublishing.com/journal/jd

该刊在 knowledge / documentation / information practices 方面主题相关，且篇幅 4,000–10,000 words。

但 Emerald 当前 AI policy 明确：
- 允许 AI-assisted copy editing；
- **不允许使用 generative AI copywriting 生成 submission 的新材料**。

本论文已有实质生成式 AI drafting / restructuring provenance，因此当前稿件与该政策不兼容。

**结论：不应把真实 AI-assisted generation 隐瞒或重新标记为 copy editing。当前排除。**

---

## 6. 推荐的 venue-facing article positioning

若以 **Ethics and Information Technology** 为默认 target，建议文章的外部定位从：

> protocol for AI-assisted research

进一步精炼为：

> **a governed project-memory architecture for preserving authoritative state, human decision semantics, and accountability across replaceable AI agents**

重点顺序建议：

1. persistent authoritative Project Memory；
2. Agent memory vs Project Memory；
3. Human Decision Persistence / provenance；
4. Agent-model substitution as continuity stress test；
5. structured human-review gates and responsibility；
6. memory curation / stale/conflict / authorization/publication boundaries；
7. proposed empirical evaluation。

不要把 GitHub 文件树作为主贡献；GitHub 只作为 reference implementation。

---

## 7. 必须加入最终投稿稿的 AI-use disclosure

无论选择当前两个 Springer candidate 中的哪一个，本项目都不应把 AI 使用缩减描述为 copy editing。

最终 disclosure 至少应准确说明：

- AI tools were used for iterative drafting, restructuring, literature organization, bilingual synchronization, consistency checking, and repository-oriented implementation support;
- the human author supplied and approved the core project direction, substantive framework, boundary decisions, and final claims;
- AI outputs were treated as proposals and were subject to human governance / review;
- all citations, claims, and final manuscript content remain the human author's responsibility;
- no AI system is listed as an author.

具体模型名称、版本、使用日期及 venue 要求，应在 Final Artifact 阶段按真实记录填写，不应现在猜测。

---

## 8. 当前人类决定项

`WAITING-HUMAN — TARGET VENUE SELECTION`

当前建议默认：

`Ethics and Information Technology`

备选：

`Science and Engineering Ethics`

选择 venue 后，再进入 venue-specific manuscript transformation；在选择前，不应把 canonical article 过早改成某一刊的专用格式。
