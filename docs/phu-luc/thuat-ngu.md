# Bảng thuật ngữ cố định

Trang này giải thích các thuật ngữ cố định được sử dụng thống nhất trong toàn bộ tài liệu Clickermann v4.13 tiếng Việt để người mới học dễ tra cứu.

## Danh sách thuật ngữ

| Thuật ngữ trong tài liệu | Tên tiếng Anh / Ký hiệu | Giải thích ý nghĩa |
|---|---|---|
| **script** | Script (`.cms`) | Tệp kịch bản chứa danh sách các câu lệnh điều khiển Clickermann |
| **bộ đệm ảnh** | Analysis Buffer | Vùng bộ nhớ lưu bức ảnh chụp màn hình từ lệnh [`GETSCREEN`](/lenh/man-hinh#getscreen) để các lệnh đồ họa (`PXL`, `IF_PIXEL_IN`, `IF_PICTURE_IN`...) phân tích |
| **khóa cửa sổ, chế độ khóa cửa sổ** | Window Mode (`Alt + W`) | Chế độ gửi thông điệp thao tác riêng tới một cửa sổ/phần tử cụ thể mà không chiếm con trỏ chuột và bàn phím thật của người dùng |
| **phần tử đang khóa** | Target Element (`$_hwnd`) | Phần tử cửa sổ (xác định bởi mã `HWND`) đang được Clickermann khóa làm mục tiêu ở chế độ khóa cửa sổ |
| **phần tử con** | Child Window / Control | Các thành phần bên trong một cửa sổ ứng dụng (nút bấm, khung nhập, khung nội dung...), mỗi phần tử có mã `HWND` và hệ tọa độ tương đối riêng |
| **luồng** | Thread (`THREAD`) | Chuỗi lệnh chạy song song độc lập với script chính, khai báo bằng [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread) và điều khiển qua [`SETTHREAD`](/lenh/cau-truc#setthread) |
| **thủ tục / hàm** | Procedure / Function | **Thủ tục** là câu lệnh thực hiện hành động (như `LCLICK`); **hàm** là câu lệnh tính toán và trả về một giá trị ngay tại nơi gọi (như `RND`, `PXL`) |
| **chương trình con (`SUB`)** | Subroutine (`SUB`) | Khối lệnh có tên riêng khai báo bằng [`SUB ... END_SUB`](/lenh/cau-truc#sub-end-sub) ở bất kỳ đâu trong script nhưng phải nằm trước lời gọi (theo help, mục Cấu trúc lệnh) |
| **mảng** | Array (`$arr[i]`) | Tập hợp các biến có chung tên, truy cập từng phần tử qua chỉ số nguyên trong ngoặc vuông (bắt đầu từ `0`) |
| **chỉ thị** | Preprocessor Directive | Các lệnh tiền xử lý bắt đầu bằng dấu `#` (như `#name`, `#include`, `#logfile`, `#autorun`, `#define`), chỉ xử lý lúc nạp script |
| **giảm màu** | Color Correction (`COLORMODE`) | Việc giảm bớt số lượng màu trong bộ đệm ảnh bằng lệnh [`COLORMODE`](/lenh/man-hinh#colormode) để gom các sắc độ gần nhau về một màu đồng nhất |
| **kính lúp** | Magnifier | Công cụ phóng to vùng điểm ảnh dưới trỏ chuột ở góc dưới trái của [Trình soạn thảo](/bat-dau/trinh-soan-thao) |
| **phím tắt** | Hotkey | Tổ hợp phím điều khiển nhanh (như `Alt + A` chạy/tạm dừng, `Alt + S` dừng, `Alt + R` ghi, `Alt + W` khóa cửa sổ, `Alt + Q` chèn tọa độ, `Alt + G` chụp kính lúp) |
