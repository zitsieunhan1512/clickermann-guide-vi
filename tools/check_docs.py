"""Kiểm tra nội dung docs/ so với help. Chạy: python3 -I tools/check_docs.py <thư mục dự án> [--all]

Mặc định chỉ kiểm phần tra cứu lệnh; --all kiểm thêm các trang và sơ đồ bắt buộc.
"""
import glob
import os
import re
import sys

ROOT = sys.argv[1]
ALL = '--all' in sys.argv
DOCS = os.path.join(ROOT, 'docs')
HELP = os.path.join(ROOT, 'sources', 'help-text')
errors = []


def err(where, msg):
    errors.append(f'{where}: {msg}')


def norm(s):
    return re.sub(r'\s+', '', s).upper()


# Trang lệnh tương ứng với từng file help
GROUPS = {'var': 'so', 'str': 'chuoi-file', 'mouse': 'chuot', 'keyboard': 'ban-phim', 'constr': 'cau-truc',
          'screen': 'man-hinh', 'output': 'nhat-ky', 'script': 'kich-ban', 'winapi': 'winapi'}
HEAD = re.compile(r'^[A-Z_0-9, .…()]+$')
HIDDEN = {'NUM', 'STR', 'ADDR', 'FROMADDR', 'TOADDR', 'LOAD'}
# Từ khóa ngôn ngữ và các lệnh chỉ có trong keywords.txt nhưng không có tài liệu
NOT_DOCUMENTED = {'GOSUB', 'IF_KEYDOWN', 'IF_TIME', 'HTTPPOST', 'TRAYSAY'}


def help_entries(group):
    """Trả về [(tiêu đề, dòng cú pháp đầu)] của một file help."""
    lines = open(f'{HELP}/all_{group}.txt', encoding='utf-8').read().split('\n')
    out = []
    for i, line in enumerate(lines):
        if line.strip() in ('Синтаксис', 'Управление потоком'):
            j = i - 1
            while j >= 0 and not HEAD.match(lines[j].strip()):
                j -= 1
            syntax = re.sub(r' - .*', '', lines[i + 1].strip())
            out.append((lines[j].strip(), syntax))
    return out


known = {w.strip().upper() for w in open(f'{ROOT}/sources/keywords.txt', encoding='utf-8-sig')
         if w.strip() and not w.startswith('//')}
known -= NOT_DOCUMENTED | HIDDEN

total = 0
for group, page in GROUPS.items():
    path = f'{DOCS}/lenh/{page}.md'
    if not os.path.exists(path):
        err(f'lenh/{page}.md', 'chưa có trang')
        continue
    text = open(path, encoding='utf-8').read()
    sections = dict()
    for m in re.finditer(r'^## (.+?)\n(.*?)(?=^## |\Z)', text, re.M | re.S):
        sections[norm(m.group(1).replace('…', '...'))] = m.group(2)
    for title, syntax in help_entries(group):
        total += 1
        body = sections.get(norm(title.replace('…', '...')))
        if body is None:
            err(f'lenh/{page}.md', f'thiếu mục "{title}"')
            continue
        if '**Trạng thái:**' not in body:
            err(f'lenh/{page}.md', f'mục "{title}" thiếu nhãn trạng thái')
        if syntax.endswith(')') and norm(syntax) not in norm(body):
            err(f'lenh/{page}.md', f'mục "{title}" sai cú pháp, help ghi: {syntax}')

# Điểm mâu thuẫn đã biết phải được đánh dấu 🟠 trong mục của lệnh
CONFLICTS = {'so': ['GETVAR', 'SETVAR'], 'man-hinh': ['SCREENSHOTEX'], 'kich-ban': ['CALL'], 'winapi': ['WNDSETINFO'],
             'cau-truc': ['THREAD...END_THREAD', 'SETTHREAD']}
for page, names in CONFLICTS.items():
    path = f'{DOCS}/lenh/{page}.md'
    if not os.path.exists(path):
        continue
    text = open(path, encoding='utf-8').read()
    for m in re.finditer(r'^## (.+?)\n(.*?)(?=^## |\Z)', text, re.M | re.S):
        if norm(m.group(1)) in names and '🟠' not in m.group(2):
            err(f'lenh/{page}.md', f'mục {m.group(1)} phải có 🟠')

BLOCKS = [(r'IF|IF_PIXEL_IN|IF_PICTURE_IN', 'END_IF'), (r'FOR|WHILE', 'END_CYC'), (r'SUB', 'END_SUB'),
          (r'THREAD', 'END_THREAD'), (r'SWITCH', 'END_SWITCH')]
for path in glob.glob(f'{DOCS}/**/*.md', recursive=True):
    rel = os.path.relpath(path, DOCS)
    text = open(path, encoding='utf-8').read()
    if re.search(r'[А-Яа-яЁё]', text):
        err(rel, 'còn chữ Nga')
    for bad in ('gunny', 'gameguard', 'frost', 'zhyk', 'allcheats', '🟢'):
        if bad in text.lower():
            err(rel, f'chứa nội dung cấm: {bad}')
    # data/const.txt và data/keywords.txt là file có thật của tool nên được phép nêu tên
    internal = re.findall(r'(?<!data/)(?:all_\w+|wnd[123]|faq|history|plugin|colors|winmode|what|about|appendix|const|keywords)\.(?:txt|htm|bmp|png)'
                          r'|sources/|big_test|doi-chieu|help-text|help-html', text)
    if internal:
        err(rel, f'lộ tên file nội bộ {len(internal)} chỗ, ví dụ {internal[0]}')
    if re.search(r'^#+ \d', text, re.M):
        err(rel, 'tiêu đề bắt đầu bằng số làm hỏng link neo')
    for code in re.findall(r'```cms\n(.*?)```', text, re.S):
        lines = [re.sub(r'//.*', '', x).strip() for x in code.split('\n')]
        real = [x for x in lines if x]
        is_syntax = any(x == '...' or x.startswith('[') for x in lines) or (len(real) == 1 and '[' in real[0])
        subs = {m.group(1).upper() for x in lines for m in [re.match(r'(?i)sub\s*\(\s*(\w+)', x)] if m}
        threads = set()
        for x in lines:
            m = re.match(r'(\w+)\s*\(', x)
            if m and not is_syntax:
                name = m.group(1).upper()
                if name not in known and name not in subs:
                    err(rel, f'ví dụ gọi lệnh không có trong help: {m.group(1)}')
                if name in ('READMEM', 'WRITEMEM'):
                    err(rel, f'không được có ví dụ {name}')
        if not is_syntax:
            for opener, closer in BLOCKS:
                opens = sum(bool(re.match(rf'(?i)({opener})\s*\(', x)) for x in lines)
                closes = sum(bool(re.match(rf'(?i){closer}\b', x)) for x in lines)
                if opens != closes:
                    err(rel, f'ví dụ lệch khối {closer}: mở {opens}, đóng {closes}: {code[:60]!r}')

if ALL:
    REQUIRED = """index bat-dau/cai-dat bat-dau/script-dau-tien bat-dau/man-hinh-chinh bat-dau/trinh-soan-thao
    bat-dau/quan-ly-cua-so khai-niem/ngon-ngu khai-niem/bo-dem-anh khai-niem/toa-do khai-niem/mau-sac
    khai-niem/khoa-cua-so khai-niem/luong khai-niem/plugin lenh/index cam-nang/click-theo-lich cam-nang/tim-mau
    cam-nang/tim-anh cam-nang/doc-ghi-file cam-nang/tu-ve xu-ly-loi phu-luc/ma-phim phu-luc/lich-su
    phu-luc/thuat-ngu phu-luc/lenh-an phu-luc/can-kiem-tra-tren-windows phu-luc/nguon""".split()
    for page in REQUIRED:
        if not os.path.exists(f'{DOCS}/{page}.md'):
            err(page, 'chưa có trang')
    for svg in glob.glob(f'{DOCS}/public/so-do/*.svg'):
        name = os.path.basename(svg)
        text = open(svg, encoding='utf-8').read()
        if not text.lstrip().startswith(('<svg', '<?xml')):
            err(name, 'không phải SVG')
        if not re.search(r'<title>', text):
            err(name, 'thiếu <title>')
        if not re.search(r'<rect[^>]*fill="#(fff|ffffff)"', text, re.I):
            err(name, 'thiếu nền trắng')
        used = any(name in open(p, encoding='utf-8').read() for p in glob.glob(f'{DOCS}/**/*.md', recursive=True))
        if not used:
            err(name, 'sơ đồ chưa được trang nào dùng')

print(f'Đã so {total} mục lệnh với help.')
for e in errors:
    print('LỖI', e)
print(f'Tổng: {len(errors)} lỗi')
sys.exit(1 if errors else 0)
