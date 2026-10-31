"""Chuyển trang help (cp1251) sang text UTF-8, giữ dấu < trong code."""
import glob, html, os, re, sys
root, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
TAG = r'</?[a-zA-Z][a-zA-Z0-9]*(\s[^<>]*)?/?>|<!--.*?-->|<![^>]*>'
for f in sorted(glob.glob(root + '/*.htm') + glob.glob(root + '/help/*.html')):
    b = open(f, 'rb').read()
    try:
        t = b.decode('utf-8')
    except UnicodeDecodeError:
        t = b.decode('cp1251', 'replace')
    t = re.sub(r'(?is)<(script|style)\b.*?</\1>', '', t)
    t = re.sub(r'(?i)<br\s*/?>|</(p|div|tr|h\d|li|table)>', '\n', t)
    t = re.sub(TAG, '', t, flags=re.S)
    t = html.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t).strip()
    open(os.path.join(out, os.path.basename(f).rsplit('.', 1)[0] + '.txt'), 'w', encoding='utf-8').write(t)
