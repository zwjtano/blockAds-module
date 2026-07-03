# blockAds module variants

## Repository layout

This repository now focuses on Surge modules:

- `surge-modules/`: Surge modules, including the upstream-derived blockAds variant and converted Kelee modules.
- `scripts/`: Sync, merge, and conversion scripts.
- `docs/`: Notes for conversion workflows.

Loon plugins were moved to:

```text
https://github.com/zwjtano/loon-
```

## Credits

Surge upstream:

```text
https://github.com/fmz200/wool_scripts
https://raw.githubusercontent.com/fmz200/wool_scripts/refs/heads/main/Surge/module/blockAds.module
```

Thanks to the upstream maintainers. This repository keeps personal Surge variants and converted modules.

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

Use the dedicated Loon repository:

```text
https://github.com/zwjtano/loon-
```

Common plugin links:

```text
https://raw.githubusercontent.com/zwjtano/loon-/master/Plugins/FotMob_remove_ads.lpx
https://raw.githubusercontent.com/zwjtano/loon-/master/Plugins/myblockads-bilibili-search-preserved.lpx
```

## Scripts

```text
scripts/update_bilibili_search_preserved.py
scripts/convert_kelee_loon_to_surge.py
```

More details:

```text
docs/loon-to-surge.md
```
