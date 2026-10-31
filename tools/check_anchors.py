"""Kiểm tra link nội bộ có neo (#...) trong bản build trỏ tới id có thật."""
import glob, os, re, sys, html
dist = sys.argv[1]
ids = {}
pages = glob.glob(dist + '/**/*.html', recursive=True)
for f in pages:
    rel = '/' + os.path.relpath(f, dist)
    ids[rel] = set(re.findall(r'\sid="([^"]+)"', open(f, encoding='utf-8').read()))
bad = 0
for f in pages:
    rel = '/' + os.path.relpath(f, dist)
    t = open(f, encoding='utf-8').read()
    body = t.split('<main', 1)[-1]
    for href in sorted(set(re.findall(r'href="(/[^"#]*)#([^"]+)"', body))):
        target = href[0]
        if target.endswith('/'):
            target += 'index.html'
        if not target.endswith('.html'):
            target += '.html'
        if html.unescape(href[1]) not in ids.get(target, set()):
            print('HỎNG', rel, '->', href[0] + '#' + href[1])
            bad += 1
print('neo hỏng:', bad)
sys.exit(1 if bad else 0)
