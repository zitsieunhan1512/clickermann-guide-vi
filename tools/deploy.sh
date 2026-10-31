#!/bin/sh
# Build trang với base của GitHub Pages rồi đẩy bản build lên nhánh gh-pages.
set -eu

ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
REMOTE=$(git remote get-url origin)
SHA=$(git rev-parse --short HEAD)

VITEPRESS_BASE=/clickermann-guide-vi/ npm run build

OUT=$(mktemp -d)
trap 'rm -rf "$OUT"' EXIT
cp -R docs/.vitepress/dist/. "$OUT/"
touch "$OUT/.nojekyll"

cd "$OUT"
git init -q -b gh-pages
git config user.name "$(git -C "$ROOT" config user.name)"
git config user.email "$(git -C "$ROOT" config user.email)"
git add -A
git commit -q -m "Deploy $SHA"
git push -f "$REMOTE" gh-pages
