# blockAds module variants

## 来源与感谢

本仓库包含两个自动同步派生版本，分别来源于以下上游项目/插件：

Surge 原始模块来自 fmz200 / wool_scripts：

```text
https://github.com/fmz200/wool_scripts
```

Surge 原始模块地址：

```text
https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module
```

Loon 原始插件来自 RuCu6 的 MyBlockAds：

```text
https://rucu6.pages.dev/Plugins/myblockads.lpx
```

感谢原作者及相关脚本维护者长期整理和维护规则。本仓库仅做个人需求向的自动同步派生：保留哔哩哔哩热搜、搜索发现和默认搜索词，其余内容尽量保持上游原样。

## Surge 版

订阅这个模块：

```text
https://raw.githubusercontent.com/zwjtano/blockAds-module/master/blockAds-bilibili-search-preserved.module
```

这个文件由 GitHub Actions 自动同步上游：

```text
https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module
```

同步时只放行哔哩哔哩热搜、搜索发现和默认搜索词，其余规则保持上游原样。

说明：Surge 模块规则是合并生效的，单独写一个补丁模块通常不能删除另一个模块里的 `[Map Local]` 拦截规则。因此要保留这些内容，需要订阅这个自动同步后的派生模块，而不是同时订阅上游模块和补丁模块。

## Loon 版

订阅这个插件：

```text
https://raw.githubusercontent.com/zwjtano/blockAds-module/master/myblockads-bilibili-search-preserved.lpx
```

这个文件由 GitHub Actions 自动同步上游：

```text
https://rucu6.pages.dev/Plugins/myblockads.lpx
```

当前 Loon 上游插件本身没有包含哔哩哔哩 `v2/search/square` 或 `Search/DefaultWords` 拦截规则；工作流会保留现有规则，并在未来上游加入相关规则时自动放行哔哩哔哩热搜、搜索发现和默认搜索词。

## Kelee Loon 插件转 Surge 模块

`generated-surge-modules/` 目录包含从 `https://hub.kelee.one/` 插件中心批量转换得到的 Surge 模块。

转换脚本：

```text
scripts/convert_kelee_loon_to_surge.py
```

说明文档：

```text
docs/loon-to-surge.md
```

转换流程由 GitHub Actions 定时同步，源 `.lpx` 插件来自 Kelee 的 Loon 插件列表。
