# Self-hosted Academic fonts

Official Google Fonts distributions, pinned to google/fonts commit `9710da1eacb3be272583c3224dcb70f9da6eadbb`:

- [Lora.ttf](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/lora/Lora%5Bwght%5D.ttf) — SHA-256 `822a6621ccbe8d97d20ac88c1c41f5615c9c2c202eaa75f272cd452aac6475a7`
- [Lora-OFL.txt](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/lora/OFL.txt) — SHA-256 `1d9a970809ac804b582a6ce7f0ebc4e7fefcbfd7ff6299cad35ee656a21be716`
- [SourceSerif4.ttf](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/sourceserif4/SourceSerif4%5Bopsz%2Cwght%5D.ttf) — SHA-256 `97b2d4da6e3cb494b5a1e66ae176914d852ccabef49e0c02c0df25f3e39aca0b`
- [SourceSerif4-Italic.ttf](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/sourceserif4/SourceSerif4-Italic%5Bopsz%2Cwght%5D.ttf) — SHA-256 `15fbc7e4679489a501998c3669272637a6646388ef7e4bd77eebb5bf967a1f42`
- [SourceSerif4-OFL.txt](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/sourceserif4/OFL.txt) — SHA-256 `5f94c3fd3a23131a417ab5a0c8452de57e70c3cfb9f604d88241f7065ebf9fd9`
- [SourceCodePro.ttf](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/sourcecodepro/SourceCodePro%5Bwght%5D.ttf) — SHA-256 `b400fc584e10aff25d0e775ce181b4fc1c5ea1b5dc37b81aeb2084375b945790`
- [SourceCodePro-OFL.txt](https://raw.githubusercontent.com/google/fonts/9710da1eacb3be272583c3224dcb70f9da6eadbb/ofl/sourcecodepro/OFL.txt) — SHA-256 `cb30d3086a8b3ce0b9e3690bf48d6620402b61160bc658076f95180ccd9e9dae`

All three families use SIL Open Font License 1.1; the adjacent OFL files must be retained with redistributions. Lora originates from Cyreal; Source Serif 4 and Source Code Pro from Adobe.

WOFF2 subsets in `assets/fonts/academic/` were generated with fontTools 4.66.1 and Brotli 1.2.0. They contain printable ASCII and characters used in generated HTML text (105–109 supported Unicode characters), retaining shaping features. Lora: normal 500–700. Source Serif 4: normal 400–700, italic 400, with the original optical-size axis. Source Code Pro: normal 400–600. Higher CSS heading weights retain the original browser synthesis behavior; typography settings and sizes are unchanged.

Modified subsets have internal family names Academic Heading, Academic Body and Academic Code to respect reserved font names. The CSS aliases remain Lora, Source Serif 4 and Source Code Pro; these are subsets of those fonts, not replacement typefaces.

`data/academic_fonts.json` declares file, CSS family, weight and style. The small `layouts/_partials/functions/typography.html` override preserves the pinned HugoBlox typography variables while loading these faces. The installed loader supports only one file per family and cannot describe italic faces. There is no remote-font fallback or local() source: the browser loads these exact subsets.

To regenerate after adding text, download the pinned sources above into a temporary directory using the listed filenames. Build the site first. In an isolated Python environment install fonttools==4.66.1, brotli==1.2.0 and beautifulsoup4, then run `python scripts/subset-academic-fonts.py SOURCE_DIRECTORY` from the repository root. Review resulting font/data changes, rebuild, regenerate Pagefind and verify actual rendered fonts. No Python tooling is needed by the normal Hugo/GitHub Pages build. When upgrading HugoBlox separately, compare the typography-variable section with its upstream partial.
