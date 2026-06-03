# blockAds module variants

## 来源与感谢

本仓库的模块来源于 fmz200 / wool_scripts：

```text
https://github.com/fmz200/wool_scripts
```

原始模块：

```text
https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module
```

感谢原作者及相关脚本维护者长期整理和维护规则。本仓库仅做个人需求向的自动同步派生：保留哔哩哔哩热搜、搜索发现和默认搜索词，其余内容尽量保持上游原样。

## 保留哔哩哔哩热搜和搜索发现

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
