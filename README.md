# Victor Frankenstein — Academic Website Showcase

This repository contains a fictional academic website created by OxCommunicate to demonstrate free-hosted static academic websites using HugoBlox and GitHub Pages. It presents Dr Victor Heinrich Frankenstein as a fictional early career researcher: a 2023 PhD graduate and current Postdoctoral Research Fellow at the Geneva Institute for Experimental Science.

All academic records, publication venues, courses, projects and events are fictional showcase content. The homepage includes a prominent notice explaining the site's purpose. The existing HugoBlox structure and GitHub Pages deployment configuration are retained.

The authoritative website copy is supplied in `victor-frankenstein-site-content-ecr.md`. Changes should be checked against that specification, built with the repository's existing pinned toolchain, and reviewed before deployment.

## Development

Use Hugo Extended 0.160.0 (the pin in `hugoblox.yaml`), Go for Hugo modules, Node.js 22 and pnpm 10.14.0.

```sh
pnpm install --frozen-lockfile
pnpm dev
```

The development server uses port 1313. Build for the GitHub Pages project path and index search:

```sh
hugo --minify --baseURL "https://oxcommunicate.github.io/victor-heinrich-frankenstein.github.io/"
pnpm run pagefind
```

GitHub Actions uses its Pages-provided base URL and deploys on pushes to `main`. Review content changes on a working branch before merging. Generated `public/` files are not source content.
