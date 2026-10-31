# Cài đặt và chạy lần đầu

Trang này hướng dẫn cách tải bản Clickermann v4.13 chính thức, làm quen với cấu trúc thư mục và những lưu ý quan trọng khi khởi chạy chương trình lần đầu.

## Tải chương trình từ trang chính thức

Clickermann là phần mềm miễn phí (**FREEWARE**), được phân phối nguyên trạng và không đi kèm mã nguồn. Theo thông tin từ tác giả (help, phần Thông tin chương trình), bản cài đặt chính thức duy nhất là bản được tải từ trang chủ:

- **Trang chủ chính thức:** [http://crapware.aidf.org](http://crapware.aidf.org)

Tài liệu này **không đính kèm file `.exe`**. Bạn chỉ nên tải chương trình trực tiếp từ trang chủ chính thức ở trên và không mua bán chương trình dưới mọi hình thức.

::: info Ảnh sẽ bổ sung
Ảnh chụp: thư mục giải nén của Clickermann v4.13 gồm bản 32-bit, 64-bit và các thư mục con. Cần máy Windows.
:::

## Cấu trúc thư mục của chương trình

Help không nói rõ chương trình được đóng gói dạng tệp nén chạy trực tiếp hay qua bộ cài đặt. Các tệp và thư mục được nhắc tới trong tài liệu help gồm:

- **Tệp chạy chính (`.exe`):** Từ phiên bản v4.13.014 (theo help, Lịch sử phiên bản), chương trình có cả bản 32-bit và bản 64-bit.
- **`data/`:** Chứa các tệp dữ liệu của chương trình:
  - File hằng trong thư mục `data` của tool: Tệp định nghĩa các hằng số nạp lúc khởi động (như mã phím `#SPACE`, `#ENTER`, `#TRUE`, `#FALSE`...). Bạn có thể chỉnh sửa tệp này, nhưng hãy nhớ sao lưu lại khi tải phiên bản mới (theo help, phần Giới thiệu ngôn ngữ).
  - `data/default.txt`: Tệp đặt kịch bản mặc định (hỗ trợ từ v4.13.014 theo help, Lịch sử phiên bản; Suy luận: dùng làm mẫu khi tạo script mới).
  - `data/lang/...`: Chứa thư mục mẫu code (`data/lang/ru/templates/`) và tệp cấu hình menu chèn lệnh nhanh (`data/lang/ru/qinsert_menu.txt`, có thể thay `ru` bằng ngôn ngữ khác theo help, bài Trình soạn thảo).
- **`plugins/` (🟠 Chưa thống nhất):** Trang lệnh [`CALL`](/lenh/kich-ban#call) (help, mục Script và plugin) nhắc tới thư mục `%Clickermann%/plugins`, trong khi bài viết [Plugin](/khai-niem/plugin) (help, bài Plugin) lại ghi tệp DLL đặt trong thư mục dự án (cạnh script đang chạy hoặc trong thư mục con).
- **Thư mục dự án (theo help, Lịch sử phiên bản):** Từ bản v4.6.000, mọi đường dẫn được tính tương đối theo thư mục chứa tệp script đang nạp.
- **`config.ini`:** Được nhắc ở help, Lịch sử phiên bản (bản v4.11.000: cài đặt phím tắt mới không tương thích với `config.ini` cũ); ngoài ra help không nói rõ chi tiết cấu trúc và vai trò của tệp này.

## Lưu ý khi khởi chạy lần đầu

### Kiểm tra cập nhật qua mạng khi khởi động

Theo help, phần FAQ, mỗi khi khởi động, Clickermann sẽ **tự động kết nối mạng để kiểm tra phiên bản mới** trên máy chủ của tác giả. Nếu tường lửa (Firewall) có hỏi hoặc báo hoạt động mạng lúc vừa mở chương trình thì đây là hành vi bình thường.

Nếu không muốn chương trình tự kết nối mạng khi mở, bạn có thể **tắt tính năng tự động kiểm tra cập nhật trong phần cài đặt** của chương trình.

### Cảnh báo từ phần mềm diệt virus

Theo help, phần FAQ, một số phần mềm diệt virus (thường là các trình diệt virus ít tên tuổi, không phổ biến) có thể không thích khả năng theo dõi chuột, bàn phím và các chức năng tương tự của chương trình. Nếu bạn tải đúng bản gốc từ trang chủ `http://crapware.aidf.org`, bạn có thể thêm Clickermann vào danh sách loại trừ (exclusion) của trình diệt virus.

::: info Chế độ PS/2
Clickermann có chỉ thị `#ps2_mouse`, `#ps2_keyboard` (chế độ PS/2). Tài liệu này không hướng dẫn phần đó.
:::
