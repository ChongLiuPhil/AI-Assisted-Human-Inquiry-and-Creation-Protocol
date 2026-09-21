# Ethics and Information Technology — 双盲匿名化审查说明

**状态：** `MASKED DERIVATIVE PREPARED — HUMAN / EDITORIAL CONFIRMATION PENDING`  
**依据：** AHICP-D033  
**对象：**
- `MANUSCRIPT_BLINDED.md` — 去除直接身份信息，但保留协议名称的基线版本；
- `MANUSCRIPT_BLINDED_MASKED.md` — 面向 double-anonymous review 的 masked derivative。

## 1. 风险来源

原 blinded manuscript 已移除：

- 作者姓名；
- affiliation / contact information；
- GitHub URL；
- 内部 Decision IDs；
- Framework IDs；
- Working Memory IDs；
- development-status metadata。

但该稿仍出现大量 `AHICP` / 协议全称。由于该协议已有公开项目，独特名称本身可能通过普通搜索直接指向作者或公开仓库，因此“删除作者姓名”不足以提供合理的 double-anonymous separation。

## 2. 当前缓解方案

`MANUSCRIPT_BLINDED_MASKED.md`：

- 保留同一标题、论证结构、引文、参考文献、AI-use disclosure 与 Data Availability Statement；
- 不改 `MA-FW-001`；
- 不改 canonical article；
- 将协议全称 / `AHICP` 替换为中性的：
  - `the protocol`
  - `the proposed Project Memory Architecture`
  - `the protocol's Project Memory`
- 保持 reference implementation 的描述为 provider-neutral / repository-neutral；
- 不加入虚构的机构、作者或项目来源信息。

机器检查结果：

- `AHICP`：0；
- 协议全称：0；
- direct GitHub URL：0；
- internal Decision / Framework / Working-Memory IDs：0。

latest-head CI 还要求：

- masked 稿与 traceable 稿之间只允许 deterministic identity-masking transform，避免出现第二套 substantive manuscript；
- 两稿 reference section 完全一致；
- 禁止常见机械 masking 语法错误；
- DOCX core metadata 不含项目 owner / author identity marker。

## 3. 推荐的投稿路径

当前建议：

> **如果期刊编辑部没有另行要求，double-anonymous reviewer manuscript 优先使用 masked derivative。**

unmasked blinded version 继续保留为：

- 项目可追溯基线；
- 编辑部如明确允许保留协议名时的替代稿；
- 审稿结束 / 去盲后恢复专名的来源。

## 4. residual risk

masked derivative 可以显著降低“搜索协议名即可找到作者”的直接风险，但不能保证数学意义上的完全匿名。

仍可能存在：

- 标题或独特短语与公开项目的文本相似性；
- 公开时间线；
- prior public repository / webpage；
- 特殊概念组合带来的可识别性。

因此不得声称“已经完全匿名”。

当前 EIT / Springer double-anonymous 指引把匿名化责任放在作者一侧，并明确提醒公开在线材料可能增加反向识别可能性；因此 masked derivative 是保守 reviewer-facing 路线，但公开项目带来的残余 discoverability 不能被技术检查消除。正式 submission 前仍需按 live guidelines / interface 再确认。

## 5. 提交前人类门

正式 submission 前必须完成以下之一：

1. 人类明确选择 masked derivative 作为 reviewer manuscript；或
2. 编辑部明确说明可以在 double-anonymous review 中保留公开协议名；或
3. 根据编辑部建议采用其他 masked-material / supplementary-material route。

同时仍需确认：

- reviewer 可访问的 supplementary / repository material 不直接泄露身份；
- submission-system 的 title-page / author metadata 不进入 reviewer manuscript；
- self-citation 措辞不泄露身份。

## 6. 治理边界

创建 masked derivative：

- 不等于 Final Artifact Approval；
- 不等于 submission authorization；
- 不等于修改 `MA-FW-001`；
- 不等于承诺期刊会认为该匿名化充分。

它只是一个为了满足 double-anonymous review 而准备的 venue-specific derivative。