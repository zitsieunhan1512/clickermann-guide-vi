# Màn hình chính

Trang này giới thiệu bố cục và chức năng của các nút điều khiển, bảng phím tắt toàn cục và khung thông tin trên cửa sổ chính của Clickermann.

::: info Hình minh họa sẽ bổ sung
Hình chụp cửa sổ chính của Clickermann v4.13 (với hàng nút chức năng phía trên, các nút điều khiển bên trái và khung thông tin chế độ khóa cửa sổ) sẽ được bổ sung sau khi chụp trực tiếp trên máy Windows.
:::

## Vai trò của cửa sổ chính

Cửa sổ chính là giao diện xuất hiện đầu tiên khi mở Clickermann, chủ yếu dùng để nạp nhanh và chạy các script đã viết sẵn, cũng như mở các cửa sổ phụ trợ.

Ở **hàng nút phía trên cùng** là các nút chức năng dùng để nạp tệp script (`.cms`) và mở các cửa sổ phụ trợ như cửa sổ cài đặt chương trình, cửa sổ nhật ký và [Quản lý cửa sổ](/bat-dau/quan-ly-cua-so).

::: tip Lưu ý về nhãn nút trên màn hình
Do chưa xác minh trực tiếp giao diện trên Windows (nhãn chữ hoặc biểu tượng thực tế trên từng nút có thể hiển thị bằng tiếng Nga hoặc tiếng Anh tùy bản), tài liệu mô tả các nút theo **vị trí** và khuyến khích bạn dùng **phím tắt toàn cục** (`Alt + A` để chạy/tạm dừng, `Alt + S` để dừng) vì phím tắt luôn hoạt động ổn định bất kể ngôn ngữ giao diện.
:::

## Các nút điều khiển script

Ở **cột phía bên trái** cửa sổ chính (theo bố cục trong help) gồm 4 nút điều khiển chính:

1. **Nút Chạy / Tạm dừng (phím tắt `Alt + A`):**
   - Bắt đầu chạy script hiện tại (script vừa mở từ tệp, vừa bấm nút **Áp dụng** từ trình soạn thảo, hoặc vừa ghi lại).
   - Nếu script đang chạy mà bấm lại nút này (hoặc nhấn `Alt + A`) một lần nữa, chương trình sẽ chuyển sang **tạm dừng**; bấm thêm lần nữa sẽ tiếp tục chạy từ đúng câu lệnh vừa dừng.
2. **Nút Ghi thao tác (phím tắt `Alt + R`):**
   - Bắt đầu ghi lại các thao tác chuột và bàn phím của bạn. Mọi hành động thực hiện sau khi bấm nút này sẽ được tự động chuyển thành câu lệnh trong script.
3. **Nút Dừng (phím tắt `Alt + S`):**
   - Ngắt hẳn quá trình đang chạy hoặc đang ghi script. Khi chạy thử các script điều khiển chuột, hãy luôn nhớ phím tắt **`Alt + S`** để dừng ngay khi cần.
4. **Nút mở Trình soạn thảo:**
   - Mở cửa sổ [Trình soạn thảo script](/bat-dau/trinh-soan-thao) để gõ và chỉnh sửa mã lệnh.

## Phím tắt toàn cục mặc định

Để tiện điều khiển ngay cả khi cửa sổ Clickermann không nằm ở phía trước (hoặc khi chuột đang bận chạy theo script), chương trình gắn sẵn tổ hợp phím tắt toàn cục cho các thao tác quan trọng nhất:

| Phím tắt mặc định | Tác dụng | Dùng ở đâu |
|---|---|---|
| `Alt + A` | **Chạy / Tạm dừng** script | Mọi lúc |
| `Alt + S` | **Dừng hẳn** script (hoặc dừng ghi thao tác) | Mọi lúc |
| `Alt + R` | **Bắt đầu ghi** thao tác chuột và bàn phím | Mọi lúc |
| `Alt + W` | **Bật khóa cửa sổ** vào phần tử đang nằm dưới con trỏ chuột | Mọi lúc (xem [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so)) |
| `Alt + Q` | **Chèn nhanh tọa độ và màu** tại mũi trỏ chuột vào script | Khi đang mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) |
| `Alt + G` | **Chụp nhanh ảnh mẫu `100×100`** vùng kính lúp thành tệp `.bmp` | Khi đang mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) |

Bạn có thể xem hoặc thay đổi các tổ hợp phím tắt này trong cửa sổ cài đặt của chương trình.

## Bảng thông tin và chế độ chạy

Ngoài các nút bấm, cửa sổ chính còn có:

- **Khung thông tin chế độ khóa cửa sổ:** Hiển thị trạng thái bật/tắt khóa cửa sổ, mã `HWND` của phần tử đang dưới trỏ chuột (hoặc phần tử đang khóa), mã tiến trình (`PID`) và tên tệp `.exe` của ứng dụng đó.
- 🟠 **Khung thiết lập chế độ chạy script:**
  - **Nên làm:** Nếu không thấy khung hẹn số vòng lặp ngay trên cửa sổ chính của bản v4.13, hãy tìm nút mở cửa sổ thiết lập chế độ chạy trên thanh công cụ hoặc dùng lệnh [`HALT`](/lenh/kich-ban#halt) / biến đếm trực tiếp trong script.
  ::: details Vì sao chưa chắc
  Trong help, bài Màn hình chính ghi trên cửa sổ chính có khung thiết lập chế độ thực thi script. Tuy nhiên, trong [Lịch sử phiên bản](/phu-luc/lich-su) của help, bản v4.7.000 ghi đã bỏ các chế độ chạy khỏi cửa sổ chính, và bản v4.7.000 SE ghi các chế độ thực thi đã trở lại dưới dạng một cửa sổ riêng. Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#vi-tri-khung-thiet-lap-che-do-chay-script).
  :::

---

*Nguồn: Tài liệu trợ giúp `help.chm` (bài Màn hình chính, Trình soạn thảo, Khóa cửa sổ và Lịch sử phiên bản).*
