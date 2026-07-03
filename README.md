# blockAds module variants

## Repository layout

This repository is organized by client type:

- `surge-modules/`: Surge modules, including the upstream-derived blockAds variant and converted Kelee modules.
- `loon-plugins/`: Loon plugins, including upstream-derived plugins and manually captured app-specific plugins.
- `scripts/`: Sync, merge, and conversion scripts.
- `docs/`: Notes for conversion workflows.

## Credits

Surge upstream:

```text
https://github.com/fmz200/wool_scripts
https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module
```

Loon upstream:

```text
https://rucu6.pages.dev/Plugins/myblockads.lpx
```

Thanks to the upstream maintainers. This repository keeps personal variants and captured app-specific plugins.

## Surge modules

### blockAds with Bilibili search preserved

```text
https://raw.githubusercontent.com/zwjtano/blockAds-module/master/surge-modules/blockAds-bilibili-search-preserved.module
```

This file is synced by GitHub Actions from fmz200/wool_scripts and merged with Kelee's Bilibili Surge module while preserving Bilibili hot search, search discovery, and default search words.

### Converted Kelee modules

Converted Surge modules live in:

```text
surge-modules/
```

The converter reads Loon plugins from `https://hub.kelee.one/` and writes Surge `.sgmodule` files into this directory.

## Loon plugins

### MyBlockAds with Bilibili search preserved

```text
https://raw.githubusercontent.com/zwjtano/blockAds-module/master/loon-plugins/myblockads-bilibili-search-preserved.lpx
```

This file is synced by GitHub Actions from RuCu6's MyBlockAds and preserves Bilibili hot search, search discovery, and default search words when those rules appear upstream.

### FotMob ad block

```text
https://raw.githubusercontent.com/zwjtano/blockAds-module/master/loon-plugins/FotMob_remove_ads.lpx
```

This plugin was built from Loon HAR captures. It clears FotMob house ads and blocks captured ad SDK, image, and bidding endpoints.

## Scripts

```text
scripts/update_bilibili_search_preserved.py
scripts/convert_kelee_loon_to_surge.py
```

More details:

```text
docs/loon-to-surge.md
```
