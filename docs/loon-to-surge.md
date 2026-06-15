# Loon 插件批量转换 Surge 模块

本仓库提供 `scripts/convert_kelee_loon_to_surge.py`，用于读取 `https://hub.kelee.one/list.json` 中的 Loon 插件列表，并将 `.lpx` 转换为 Surge `.sgmodule`。

## 基本用法

```bash
python scripts/convert_kelee_loon_to_surge.py --out-dir generated-surge-modules
```

脚本会生成：

- `generated-surge-modules/*.sgmodule`
- `generated-surge-modules/README.md`
- `generated-surge-modules/conversion-report.json`

## 使用本地 Loon 插件源

如果远程 `.lpx` 源地址无法直接下载，可以先把 `.lpx` 文件放进一个目录，文件名保持和列表 URL 一致，再运行：

```bash
python scripts/convert_kelee_loon_to_surge.py --source-dir downloaded-lpx --out-dir generated-surge-modules
```

例如列表中的 `https://kelee.one/Tool/Loon/Lpx/Block_HTTPDNS.lpx`，本地文件应为：

```text
downloaded-lpx/Block_HTTPDNS.lpx
```

## 当前限制

当前环境中 `https://kelee.one/Tool/Loon/Lpx/*.lpx` 返回 `403 Forbidden`，而 `https://hub.kelee.one/Tool/Loon/Lpx/*.lpx` 返回的是插件中心 HTML，不是插件本体。脚本会在报告中标记这些下载失败，避免生成错误模块。

转换器会自动处理常见段落：

- `[Rule]`
- `[Rewrite]` -> `[URL Rewrite]`
- `[Script]`
- `[MITM]`

其中 Loon 脚本行会转换为 Surge 模块格式，例如：

```text
http-response ^https:\/\/example\.com script-path=https://example.com/a.js, requires-body=true, tag=demo
```

会转换为：

```text
demo = type=http-response, pattern=^https:\/\/example\.com, script-path=https://example.com/a.js, requires-body=true
```

复杂插件仍建议查看 `conversion-report.json` 中的 `needs-review` 项并人工抽查。
