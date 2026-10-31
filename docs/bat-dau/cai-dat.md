# Cài đặt và chạy lần đầu

Trang này hướng dẫn cách tải bản Clickermann v4.13 chính thức, mở cửa sổ chính lần đầu và làm quen với các thư mục quan trọng nhất.

## Các bước mở cửa sổ chính lần đầu

Clickermann là phần mềm miễn phí (**FREEWARE**) chạy trên Windows, được phân phối nguyên trạng và không đi kèm mã nguồn. Bản chính thức duy nhất được tải từ trang chủ của tác giả:

1. **Tải chương trình:** Truy cập trang chủ chính thức [http://crapware.aidf.org](http://crapware.aidf.org) để tải bản Clickermann v4.13 (tài liệu này **không đính kèm tệp `.exe`**, và bạn không nên mua bán chương trình dưới mọi hình thức).
2. **Giải nén:** Trang chủ có hai tệp nén là `cm413_32.zip` (32-bit) và `cm413_64.zip` (64-bit). Giải nén một tệp ra thư mục riêng trên máy. Help không hướng dẫn nên chọn bản nào.
3. **Mở chương trình:** Trong thư mục vừa giải nén, chạy tệp `Clickermann.exe`.
4. **Kiểm tra:** Cửa sổ chính của Clickermann xuất hiện. Bước này chưa được chạy thử trên Windows.

Tên tệp ở các bước trên lấy từ hai tệp nén tải về trang chủ ngày 31/10/2026, không phải từ help.

::: info Hình minh họa sẽ bổ sung
Hình chụp thư mục chương trình Clickermann v4.13 trên Windows (gồm bản 32-bit, 64-bit và các thư mục con) sẽ được bổ sung sau khi chụp trực tiếp trên máy Windows.
:::

## Ba thành phần cần biết khi mới dùng

Khi làm việc hằng ngày với Clickermann, bạn chỉ cần quan tâm tới 3 nơi sau:

- **Tệp chạy chính (`.exe`):** Nằm trong thư mục chương trình (`%Clickermann%`), dùng để khởi động Clickermann.
- **Thư mục `data/` (và tệp `data/const.txt`):** Chứa các tệp dữ liệu của chương trình, quan trọng nhất là tệp `data/const.txt` định nghĩa các hằng số nạp lúc khởi động (như mã phím `#SPACE`, `#ENTER`, `#TRUE`, `#FALSE`...). Bạn có thể chỉnh sửa `data/const.txt`, nhưng hãy nhớ sao lưu lại khi tải phiên bản mới.
- **Thư mục dự án:** Là thư mục chứa tệp script `.cms` mà bạn đang mở. Từ bản v4.6.000, mọi đường dẫn tương đối trong script (như tệp ảnh `.bmp`, tệp `.txt`, `.ini`) đều được tính từ thư mục chứa tệp script đang nạp. Vì vậy, bạn nên tạo một thư mục riêng cho mỗi bài thực hành và lưu tệp `.cms` vào đó.

## Lưu ý khi khởi chạy lần đầu

### Kiểm tra cập nhật qua mạng khi khởi động

Mỗi khi khởi động, Clickermann sẽ **tự động kết nối mạng để kiểm tra phiên bản mới** trên máy chủ của tác giả. Nếu tường lửa (Firewall) có hỏi hoặc báo hoạt động mạng lúc vừa mở chương trình thì đây là hành vi bình thường.

Nếu không muốn chương trình tự kết nối mạng khi mở, bạn có thể **tắt tính năng tự động kiểm tra cập nhật trong phần cài đặt** của chương trình.

### Cảnh báo từ phần mềm diệt virus

Một số phần mềm diệt virus (thường là các trình diệt virus ít tên tuổi, không phổ biến) có thể cảnh báo vì chương trình có khả năng theo dõi, mô phỏng chuột và bàn phím. Help khuyên thêm Clickermann vào danh sách loại trừ (exclusion) của trình diệt virus. Trước khi làm vậy, bạn nên biết tệp `.exe` tải về không có chữ ký số và trang chủ chỉ dùng HTTP, nên khó tự xác minh tệp còn nguyên vẹn. Nếu lo ngại, hãy chạy trong máy ảo và không tắt bảo vệ trên máy chính.

## Chi tiết thêm về các tệp khác trong thư mục chương trình

Các tệp và thư mục dưới đây ít khi cần chạm tới khi mới bắt đầu:

- **`data/default.txt`:** Tệp đặt kịch bản mặc định (hỗ trợ từ v4.13.014; Suy luận: dùng làm mẫu khi tạo script mới).
- **`data/lang/...`:** Chứa thư mục mẫu code (`data/lang/ru/templates/`) và tệp cấu hình menu chèn lệnh nhanh (`data/lang/ru/qinsert_menu.txt`, có thể thay `ru` bằng ngôn ngữ khác).
- **`plugins/` (🟠 Chưa thống nhất):**
  - **Nên làm:** Khi dùng plugin mở rộng (`.dll`), hãy ưu tiên đặt tệp `.dll` trong thư mục `%Clickermann%/plugins/` hoặc đặt ngay cùng thư mục với tệp script `.cms`.
  ::: details Vì sao chưa chắc
  Trang lệnh [`CALL`](/lenh/kich-ban#call) trong help nhắc tới thư mục `%Clickermann%/plugins`, trong khi bài viết [Plugin](/khai-niem/plugin) trong help lại ghi tệp DLL đặt trong thư mục dự án (cạnh script đang chạy hoặc trong thư mục con). Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#thu-muc-nap-plugin-dll-cua-call).
  :::
- **`config.ini`:** Tệp cấu hình của chương trình. Lịch sử phiên bản (v4.11.000) ghi cài đặt phím tắt mới không tương thích với `config.ini` cũ, và phần mô tả lệnh [`GETMESSAGE`](/lenh/winapi#getmessage) có nhắc tới việc bật tham số `msg_hook` trong `config.ini`.

---

**Bước tiếp theo:** Sau khi mở được chương trình, hãy chuyển sang bài [Màn hình chính](/bat-dau/man-hinh-chinh) để làm quen với các nút điều khiển và phím tắt.

*Nguồn: Tài liệu trợ giúp `help.chm` (phần Thông tin chương trình, Giới thiệu ngôn ngữ, Trình soạn thảo, FAQ và Lịch sử phiên bản).*
