# AHICP v0.3 迁移验证记录

**日期：** 2026-09-19  
**分支：** `ahicp-semantic-migration-v0.3`  
**状态：** STRUCTURAL CHECKS PASSED / SEMANTIC REVIEW CONTINUES

## 1. Manifest 路径一致性

对 `AHICP_MANIFEST.yaml` 中可解析为仓库文件路径的引用进行检查：

- 检查路径候选：33
- 缺失文件：0

结论：当前 manifest 没有指向不存在的 live control/state 文件。

## 2. 双语文件配对

对迁移分支中的 `*.zh-CN.md` 文件进行配对检查：

- 中文文件：62
- 缺失 English mirror：0

这证明物理文件配对完整，但**不自动证明语义逐段完全等价**。语义 parity 仍属于后续人工/AI 审计项。

## 3. Zero-context control-chain 检查

检查以下中文 canonical 入口：

- `START_HERE.zh-CN.md`
- `BOOTSTRAP_PROMPT.zh-CN.md`
- `SESSION_CONTEXT_BOOTSTRAP.zh-CN.md`
- `AGENTS.zh-CN.md`
- `protocol/ONBOARDING_HANDSHAKE.zh-CN.md`
- `AHICP_MANIFEST.yaml`
- `AHICP_CONTEXT_INTERFACE.yaml`

结果：

- 全部引用新的 `AHICP_MANIFEST.yaml` / `AHICP_CONTEXT_INTERFACE.yaml`；
- live onboarding/control chain 中未检测到 `HARC_MANIFEST.yaml` / `HARC_CONTEXT_INTERFACE.yaml` 旧引用；
- 旧 `HARC_*` 文件仅作为 compatibility pointer 保留。

## 4. 历史标识处理

迁移不重写历史 `HARC-D001`–`HARC-D025`。

新的命名与范围决定记录为：

- `AHICP-D026`

这保持了“历史发生过什么”和“当前规范叫什么”之间的可审计区分。

## 5. 研究特化模板

`templates/research-project/` 保留为 research-specific specialization，而不是被错误泛化为所有 inquiry / creation 项目的唯一结构。

该模板已经：
- 建立 `AHICP_MANIFEST.yaml`；
- 建立 `AHICP_CONTEXT_INTERFACE.yaml`；
- 把旧 `HARC_*` 控制文件降级为 compatibility pointer；
- 更新主要 onboarding / agent 文件到 AHICP 标识。

## 6. 仍未完成的语义检查

以下项目仍需在 PR 合并前处理：

1. 方法论文章中旧项目名称与当前 AHICP 名称之间的精确叙述；
2. evidence / methodology files 中哪些 HARC 表达是历史事实、哪些是 live project reference；
3. 中英文**语义 parity**，而不仅是文件配对；
4. 迁移后的独立 post-repair audit。

## 7. 当前结论

控制平面和项目入口已经可以按 AHICP v0.3 结构运行。

但本记录不把“结构检查通过”解释成“完整语义迁移已经完成”。PR 仍应保持开放，直到剩余语义审计完成。
