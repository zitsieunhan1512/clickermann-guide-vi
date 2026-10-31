# Bảng thuật ngữ cố định

Trang này giải thích các thuật ngữ cố định được sử dụng thống nhất trong toàn bộ tài liệu Clickermann v4.13 tiếng Việt để người mới học dễ tra cứu.

## Danh sách thuật ngữ

| Thuật ngữ trong tài liệu | Tên tiếng Anh / Ký hiệu | Giải thích ý nghĩa |
|---|---|---|
| **Clickermann** | Clickermann | Tên chương trình tự động hóa (trong tài liệu này luôn gọi thống nhất là Clickermann, không gọi chung chung là "tool") |
| **script** | Script (`.cms`) | Tệp kịch bản chứa danh sách các câu lệnh điều khiển Clickermann |
| **tệp** | File | Tệp tin lưu trên ổ đĩa (như tệp kịch bản `.cms`, tệp văn bản `.txt`, tệp cấu hình `.ini`, tệp ảnh `.bmp`) |
| **thư mục dự án** | Project Folder | Thư mục chứa tệp script `.cms` đang nạp; từ bản v4.6.000, mọi đường dẫn tệp tương đối trong script đều được tính từ thư mục này |
| **`%Clickermann%`** | Program Directory | Ký hiệu chỉ thư mục chương trình Clickermann (nơi chứa tệp chạy `.exe` và thư mục `data/`) |
| **nhật ký** | Log | Cửa sổ Nhật ký hoặc tệp nhật ký dùng để hiển thị/lưu các dòng thông báo xuất ra từ lệnh [`PRINT`](/lenh/nhat-ky#logwrite-print) / `LOGWRITE` |
| **thanh tác vụ** | Taskbar | Thanh tác vụ của Windows (nằm ở cạnh màn hình, nơi hiển thị biểu tượng các cửa sổ đang mở hoặc đang thu nhỏ) |
| **điểm ảnh** | Pixel | Một chấm màu nhỏ nhất tạo nên hình ảnh trên lưới màn hình, được xác định bởi tọa độ `(x, y)` và mã màu riêng |
| **bộ đệm ảnh** | Analysis Buffer | Vùng bộ nhớ lưu bức ảnh chụp màn hình từ lệnh [`GETSCREEN`](/lenh/man-hinh#getscreen) để các lệnh đồ họa (`PXL`, `IF_PIXEL_IN`, `IF_PICTURE_IN`...) phân tích |
| **giảm màu** | Color Correction (`COLORMODE`) | Việc giảm bớt số lượng màu trong bộ đệm ảnh bằng lệnh [`COLORMODE`](/lenh/man-hinh#colormode) để gom các sắc độ gần nhau về một màu đồng nhất |
| **kính lúp** | Magnifier | Công cụ phóng to vùng điểm ảnh dưới trỏ chuột ở góc dưới trái của [Trình soạn thảo](/bat-dau/trinh-soan-thao) |
| **khóa cửa sổ, chế độ khóa cửa sổ** | Window Mode (`Alt + W`) | Chế độ gửi thông điệp thao tác riêng tới một cửa sổ/phần tử cụ thể mà không chiếm con trỏ chuột và bàn phím thật của người dùng |
| **phần tử đang khóa** | Target Element (`$_hwnd`) | Phần tử cửa sổ (xác định bởi mã `HWND`) đang được Clickermann khóa làm mục tiêu ở chế độ khóa cửa sổ |
| **phần tử con** | Child Window / Control | Các thành phần bên trong một cửa sổ ứng dụng (nút bấm, khung nhập, khung nội dung...), mỗi phần tử có mã `HWND` và hệ tọa độ tương đối riêng |
| **`HWND`** | Window Handle (`hwnd`) | Mã số định danh duy nhất mà hệ điều hành Windows cấp cho mỗi cửa sổ hoặc phần tử con đang mở |
| **`PID`** | Process ID (`pid`) | Mã số định danh tiến trình của một chương trình đang chạy trong Windows (xem được trên cửa sổ chính hoặc lấy qua [`HGETPID`](/lenh/winapi#hgetpid)) |
| **thông điệp** | Windows Message | Tín hiệu điều khiển mà hệ điều hành Windows gửi tới cửa sổ hoặc phần tử (như thông điệp bấm chuột, gõ phím ở chế độ khóa cửa sổ hoặc thông điệp qua [`SENDMESSAGE`](/lenh/winapi#sendmessage-postmessage)) |
| **thủ tục / hàm** | Procedure / Function | **Thủ tục** là câu lệnh thực hiện hành động (như `LCLICK`); **hàm** là câu lệnh tính toán và trả về một giá trị ngay tại nơi gọi (như `RND`, `PXL`) |
| **tham số** | Parameter / Argument | Giá trị, biến hoặc biểu thức truyền vào bên trong cặp ngoặc tròn `( )` khi gọi một thủ tục hoặc hàm (ví dụ `100` và `200` trong `LCLICK(100, 200)`) |
| **biến** | Variable (`$var`) | Ô nhớ dùng để lưu dữ liệu (số hoặc chuỗi) trong lúc chạy script, tên luôn bắt đầu bằng dấu `$` (ví dụ `$dem`, `$x`) |
| **chuỗi** | String (`"..."`) | Dãy ký tự văn bản đặt trong cặp dấu ngoặc kép `"..."` (giữ nguyên nguyên văn, không bị tính toán như biểu thức số) |
| **mảng** | Array (`$arr[i]`) | Tập hợp các biến có chung tên, truy cập từng phần tử qua chỉ số nguyên trong ngoặc vuông (bắt đầu từ `0`) |
| **hằng** | Constant (`#CONST`) | Giá trị cố định không thay đổi trong lúc chạy, tên bắt đầu bằng dấu `#` và được nạp từ tệp `data/const.txt` (ví dụ `#SPACE`, `#ENTER`, `#TRUE`) |
| **nhãn** | Label (`ten_nhan:`) | Điểm đánh dấu dòng trong script (viết tên kèm dấu hai chấm `:`, đứng riêng một dòng) để lệnh [`GOTO`](/lenh/kich-ban#goto) nhảy tới |
| **chương trình con (`SUB`)** | Subroutine (`SUB`) | Khối lệnh có tên riêng khai báo bằng [`SUB ... END_SUB`](/lenh/cau-truc#sub-end-sub) ở bất kỳ đâu trong script nhưng phải nằm trước lời gọi |
| **luồng** | Thread (`THREAD`) | Chuỗi lệnh chạy song song độc lập với script chính, khai báo bằng [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread) và điều khiển qua [`SETTHREAD`](/lenh/cau-truc#setthread) |
| **chỉ thị** | Preprocessor Directive | Các lệnh tiền xử lý bắt đầu bằng dấu `#` (như `#name`, `#include`, `#logfile`, `#autorun`, `#define`), chỉ xử lý lúc nạp script |
| **phím tắt** | Hotkey | Tổ hợp phím điều khiển nhanh (như `Alt + A` chạy/tạm dừng, `Alt + S` dừng, `Alt + R` ghi, `Alt + W` khóa cửa sổ, `Alt + Q` chèn tọa độ, `Alt + G` chụp kính lúp) |
| **`alt_winmode`** | Alternative Windowed Mode (`alt_winmode.cms`) | Thư viện cộng đồng gồm các chương trình con `SUB` (`A_LCLICK`, `A_KEYPRESS`, `A_GETSCREEN`...) dùng `POSTMESSAGE` và `WNDGETINFO` để điều khiển nhiều cửa sổ theo từng `hwnd` riêng (không phải tính năng chính thức trong help — xem [Thư viện alt_winmode](/nang-cao/alt-winmode)) |
