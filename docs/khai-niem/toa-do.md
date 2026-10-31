# Hệ tọa độ màn hình và phần tử

Trang này giải thích cách xác định tọa độ điểm ảnh `(x, y)` trên màn hình, cách xem tọa độ thực tế trong Trình soạn thảo và sự thay đổi sang hệ tọa độ tương đối khi bật chế độ khóa cửa sổ.

## Tọa độ tuyệt đối trên màn hình

Màn hình máy tính là một lưới hình chữ nhật gồm các điểm ảnh:

- Điểm ảnh ở **góc trái trên cùng** của màn hình luôn có tọa độ là **`(0, 0)`**.
- Trục hoành **`X`** tăng dần từ trái sang phải.
- Trục tung **`Y`** tăng dần từ trên xuống dưới.
- Nếu màn hình của bạn có độ phân giải `800×600`, điểm ảnh ở góc phải dưới cùng sẽ có tọa độ là `(799, 599)`.
- Khi dùng nhiều màn hình ghép nối (Extended Desktop), Clickermann hỗ trợ đầy đủ cả tọa độ dương lẫn tọa độ âm.

**Cách lấy tọa độ của một điểm trên màn hình:** Bạn hãy mở cửa sổ [Trình soạn thảo](/bat-dau/trinh-soan-thao) và di chuyển con trỏ chuột tới vị trí cần lấy trên màn hình; tọa độ `X`, `Y` tại đầu mũi chuột sẽ hiện liên tục ở khung thông tin cột bên trái. Bạn có thể nhấn phím tắt **`Alt + Q`** để chèn nhanh tọa độ (kèm mã màu) tại vị trí chuột vào thẳng dòng lệnh trong trình soạn thảo.

![So sánh hệ tọa độ màn hình và hệ tọa độ tương đối của phần tử đang khóa](/so-do/toa-do.svg)

## Tọa độ tương đối của phần tử đang khóa

Khi bạn bật **chế độ khóa cửa sổ** (`Alt + W` hoặc lệnh [`HSET`](/lenh/winapi#hset)), hệ tọa độ trong cả trình soạn thảo lẫn khi chạy script sẽ tự động chuyển sang **hệ tọa độ tương đối của phần tử đang khóa**:

- Gốc tọa độ **`(0, 0)`** lúc này nằm tại **góc trái trên cùng của chính phần tử đang khóa** (không còn là góc trái trên của màn hình nền).
- Hệ tọa độ này được gọi là *tương đối* vì ngay cả khi bạn kéo cửa sổ ứng dụng đi chỗ khác trên màn hình, tọa độ nội bộ của các điểm bên trong phần tử đó vẫn giữ nguyên không đổi.

## Các biến hệ thống giới hạn tọa độ (`$_xmax`, `$_ymax`, `$_xmin`, `$_ymin`)

Trong bảng biến hệ thống, Clickermann cung cấp các biến `$_xmax`, `$_ymax`, `$_xmin` và `$_ymin`:

- 🟠 **Lưu ý khi dùng `$_xmax`, `$_ymax`, `$_xmin`, `$_ymin`:**
  - **Nên làm:** Ở chế độ thường toàn màn hình, bạn có thể dùng `0, 0, $_xmax, $_ymax` để quét toàn màn hình. Khi đang bật khóa cửa sổ vào một cửa sổ nhỏ, hãy in thử giá trị của chúng bằng `PRINT($_xmin, ", ", $_ymin, " -> ", $_xmax, ", ", $_ymax)` hoặc điền trực tiếp tọa độ vùng cần quét.
  ::: details Vì sao chưa chắc
  - **Theo help (phần Giới thiệu ngôn ngữ):** `$_xmax`, `$_ymax`, `$_xmin`, `$_ymin` là giá trị tọa độ X, Y lớn nhất và nhỏ nhất cho phép, được **tính từ cấu hình màn hình desktop**.
  - **Theo sách của Chô tô (tr. 26):** Ghi rằng `$_xmax`, `$_ymax` là **tọa độ lớn nhất của cửa sổ**, còn `$_xmin`, `$_ymin` là **tọa độ nhỏ nhất (ở góc trái trên) của cửa sổ**.
  - Suy luận: ở chế độ thường một màn hình thì hai cách nói cho kết quả gần giống nhau, nhưng khi đang bật chế độ khóa cửa sổ vào một cửa sổ nhỏ thì hai cách hiểu này sẽ khác nhau. Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#gia-tri-cua-xmax-va-ymax-khi-khoa-cua-so).
  :::

---

*Nguồn: Tài liệu trợ giúp `help.chm` (mục Màn hình, bài Khóa cửa sổ, phần Giới thiệu ngôn ngữ và FAQ); tham khảo đối chiếu sách của Chô tô (tr. 26).*
