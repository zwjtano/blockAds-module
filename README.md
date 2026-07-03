# blockAds 模块仓库

这个仓库现在主要整理 Surge 模块。

## 目录结构

- `surge-modules/`：Surge 模块，包括自动同步的 blockAds 派生版和从 Kelee Loon 插件转换得到的 Surge 模块。
- `scripts/`：同步、合并和转换脚本。
- `docs/`：转换流程说明文档。

Loon 插件已经迁移到独立仓库：

```text
https://github.com/zwjtano/loon-
```

## 来源与感谢

Surge 上游：

```text
https://github.com/fmz200/wool_scripts
https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module
```

感谢上游作者和相关维护者。本仓库只保存个人使用的 Surge 派生版本和转换模块。

## Surge 模块

### blockAds - 保留哔哩哔哩热搜和搜索发现

```text
https://raw.githubusercontent.com/zwjtano/blockAds-module/master/surge-modules/blockAds-bilibili-search-preserved.module
```

这个文件由 GitHub Actions 自动同步 fmz200/wool_scripts，并合并 Kelee 的哔哩哔哩 Surge 模块，同时保留哔哩哔哩热搜、搜索发现和默认搜索词。

### Kelee 转换模块

从 Kelee Loon 插件批量转换得到的 Surge 模块放在：

```text
surge-modules/
```

转换脚本会读取 `https://hub.kelee.one/` 的 Loon 插件列表，并输出 `.sgmodule` 文件。

## Loon 插件

请使用独立的 Loon 仓库：

```text
https://github.com/zwjtano/loon-
```

常用插件链接：

```text
https://raw.githubusercontent.com/zwjtano/loon-/master/Plugins/FotMob_remove_ads.lpx
https://raw.githubusercontent.com/zwjtano/loon-/master/Plugins/myblockads-bilibili-search-preserved.lpx
```

## 脚本

```text
scripts/update_bilibili_search_preserved.py
scripts/convert_kelee_loon_to_surge.py
```

更多说明：

```text
docs/loon-to-surge.md
```
