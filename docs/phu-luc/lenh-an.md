# Lệnh ẩn và lệnh không có tài liệu

Trang này liệt kê các từ khóa đặc biệt của Clickermann v4.13: 6 lệnh bị ẩn trong chú thích HTML của tệp `help.chm`, 5 từ khóa có trong file từ khóa trong thư mục `data` của tool nhưng không có mục hướng dẫn riêng trong help, và 2 từ khóa xuất hiện trong phần Lịch sử phiên bản của help.

## Sáu lệnh bị ẩn trong mã nguồn HTML của help

Khi kiểm tra mã nguồn các trang trong `help.chm` (mục Làm việc với số, mục Chuỗi và file, mục Script và plugin), có 6 mục lệnh đã bị đóng trong cặp thẻ chú thích `<!-- ... -->` nên người đọc help thông thường không nhìn thấy.

| Lệnh | Nơi xuất hiện trong nguồn | Ghi chú |
|---|---|---|
| `NUM` | help, mục Làm việc với số (ẩn trong chú thích HTML) | Bị ẩn trong help, chưa rõ còn chạy không. |
| `STR` | help, mục Chuỗi và file (ẩn trong chú thích HTML) | Bị ẩn trong help, chưa rõ còn chạy không. |
| `ADDR` | help, mục Làm việc với số (ẩn trong chú thích HTML) | Bị ẩn trong help, chưa rõ còn chạy không. |
| `FROMADDR` | help, mục Làm việc với số (ẩn trong chú thích HTML) | Bị ẩn trong help, chưa rõ còn chạy không. |
| `TOADDR` | help, mục Làm việc với số (ẩn trong chú thích HTML) | Bị ẩn trong help, chưa rõ còn chạy không. |
| `LOAD` | help, mục Script và plugin (ẩn trong chú thích HTML) và Lịch sử phiên bản | Bị ẩn trong help, chưa rõ còn chạy không (Lịch sử phiên bản mục v4.12.001 ghi đã gỡ bỏ lệnh `LOAD`). |

---

## Năm từ khóa có trong file từ khóa của tool nhưng không có mục tra cứu riêng

File từ khóa trong thư mục `data` của tool (danh sách từ khóa để trình soạn thảo tô màu) còn chứa 5 từ khóa dưới đây nhưng cả `help.chm` lẫn sách của Chô tô đều không có mục tra cứu riêng cho chúng:

| Từ khóa | Nơi xuất hiện trong nguồn | Ghi chú |
|---|---|---|
| `GOSUB` | File từ khóa của tool, help (Lịch sử phiên bản v4.1.000), script mẫu đi kèm tool | Không có mục tra cứu riêng trong help, chưa rõ còn chạy không. |
| `IF_KEYDOWN` | File từ khóa của tool, help (Lịch sử phiên bản v3.2 beta) | Không có mục tra cứu riêng trong help, chưa rõ còn chạy không. |
| `IF_TIME` | File từ khóa của tool, help (Lịch sử phiên bản v3.1 beta, v4.0.002) | Không có mục tra cứu riêng trong help, chưa rõ còn chạy không. |
| `HTTPPOST` | File từ khóa của tool | Không có tài liệu mô tả trong help, chưa rõ còn chạy không. |
| `TRAYSAY` | File từ khóa của tool | Không có tài liệu mô tả trong help, chưa rõ còn chạy không. |

---

## Hai từ khóa xuất hiện trong Lịch sử phiên bản

Ngoài hai nhóm trên, trong [Lịch sử phiên bản](/phu-luc/lich-su) còn nhắc tới:

| Từ khóa | Nơi xuất hiện trong nguồn | Ghi chú |
|---|---|---|
| `BREAK` | File từ khóa của tool, help (Lịch sử phiên bản v4.0.002) | Không có mục tra cứu riêng trong help (mục Cấu trúc lệnh), chưa rõ còn chạy không. |
| `$_line` | Help (Lịch sử phiên bản v3.2 beta), script mẫu đi kèm tool | Không có trong bảng biến hệ thống của help (phần Giới thiệu ngôn ngữ), chưa rõ còn chạy không. |
