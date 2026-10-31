# Clickermann v4.13 tiếng Việt

Tài liệu cộng đồng hướng dẫn Clickermann v4.13 cho người Việt, dựa trên help chính thức của tác giả J.Challenger. Đây không phải tài liệu chính thức. Tài liệu miễn phí, không bán và không đính kèm phần mềm; tải Clickermann tại site chính thức: <http://crapware.aidf.org>.

Nội dung chưa được chạy thử trên Windows. Mỗi lệnh có nhãn trạng thái, các điểm chưa thống nhất nằm ở trang "Cần kiểm tra trên Windows".

Nếu bạn là tác giả nội dung gốc và muốn thay đổi hoặc gỡ tài liệu, hãy mở issue trong repo này.

## Chạy trên máy

```
npm ci
npm run dev
```

## Phát hành

```
tools/deploy.sh
```

Script build trang rồi đẩy lên nhánh `gh-pages`.

`tools/check_docs.py` cần thư mục `sources/` (help gốc), thư mục này không nằm trong repo. `tools/check_anchors.py` chỉ cần bản build.
