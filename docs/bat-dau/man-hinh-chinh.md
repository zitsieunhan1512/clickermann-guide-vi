# Màn hình chính

Trang này giới thiệu bố cục và chức năng của các nút điều khiển, phím tắt toàn cục và bảng thông tin trên cửa sổ chính của Clickermann.

::: info Ảnh sẽ bổ sung
Ảnh chụp: cửa sổ chính của Clickermann v4.13 với hàng nút chức năng phía trên, các nút điều khiển bên trái và khung thông tin chế độ khóa cửa sổ. Cần máy Windows.
:::

## Vai trò của cửa sổ chính

Cửa sổ chính là giao diện xuất hiện đầu tiên khi mở Clickermann, chủ yếu dùng để nạp nhanh và chạy các script đã viết sẵn, cũng như mở các cửa sổ phụ trợ.

Ở **hàng nút phía trên cùng** là các nút chức năng dùng để nạp tệp script (`.cms`) và mở các cửa sổ phụ trợ như cửa sổ cài đặt chương trình, cửa sổ nhật ký (Log) và [Quản lý cửa sổ](/bat-dau/quan-ly-cua-so) (xem help, bài Quản lý cửa sổ). *(Lưu ý: các tên tiếng Anh như Settings, Run, Pause, Record, Stop, Editor dưới đây là tên minh họa do tài liệu đặt thêm để dễ hình dung, vì tài liệu help gốc viết bằng tiếng Nga).*

## Các nút điều khiển script

Ở **phía bên trái** cửa sổ chính gồm 4 nút điều khiển chính:

1. **Chạy / Tạm dừng (Run / Pause):**
   - Bắt đầu chạy script hiện tại (script vừa mở từ tệp, vừa bấm "Áp dụng" từ trình soạn thảo, hoặc vừa ghi lại).
   - Nếu script đang chạy mà bấm lại nút này một lần nữa, chương trình sẽ chuyển sang **tạm dừng (Pause)**; bấm thêm lần nữa sẽ tiếp tục chạy từ đúng câu lệnh vừa dừng.
2. **Ghi thao tác (Record):**
   - Bắt đầu ghi lại các thao tác chuột và bàn phím của bạn. Mọi hành động thực hiện sau khi bấm nút này sẽ được tự động chuyển thành câu lệnh trong script.
3. **Dừng (Stop):**
   - Ngắt hẳn quá trình đang chạy hoặc đang ghi script.
4. **Trình soạn thảo (Editor):**
   - Mở cửa sổ [Trình soạn thảo script](/bat-dau/trinh-soan-thao).

## Phím tắt điều khiển toàn cục

Để tiện điều khiển ngay cả khi cửa sổ Clickermann không nằm ở phía trước, chương trình gắn sẵn tổ hợp phím tắt toàn cục cho các thao tác chính:

| Phím tắt mặc định | Tác dụng |
|---|---|
| `Alt + A` | Chạy / Tạm dừng script |
| `Alt + S` | Dừng hẳn script (hoặc dừng ghi) |
| `Alt + R` | Bắt đầu ghi thao tác |

Bạn có thể thay đổi các tổ hợp phím tắt này trong cửa sổ cài đặt (Settings) của chương trình.

## Bảng thông tin và chế độ chạy

Ngoài các nút bấm, cửa sổ chính còn có:

- **Khung thông tin chế độ khóa cửa sổ:** Hiển thị trạng thái bật/tắt khóa cửa sổ, mã `HWND` của phần tử đang dưới trỏ chuột (hoặc phần tử đang khóa), mã tiến trình (`PID`) và tên tệp `.exe` của ứng dụng đó.
- 🟠 **Khung thiết lập chế độ chạy script:** Trong help, bài Màn hình chính ghi trên cửa sổ chính có khung thiết lập chế độ thực thi script. Tuy nhiên, trong [Lịch sử phiên bản](/phu-luc/lich-su) của help, bản v4.7.000 ghi đã bỏ các chế độ chạy khỏi cửa sổ chính, và bản v4.7.000 SE ghi các chế độ thực thi đã trở lại dưới dạng một cửa sổ riêng. Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#vi-tri-khung-thiet-lap-che-do-chay-script).
