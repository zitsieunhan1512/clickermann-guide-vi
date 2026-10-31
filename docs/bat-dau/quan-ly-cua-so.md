# Quản lý cửa sổ

Trang này giới thiệu công cụ Quản lý cửa sổ (Window Manager) tích hợp trong Clickermann, giúp xem và cố định vị trí/kích thước cửa sổ ứng dụng cũng như xử lý các cửa sổ bị trong suốt.

::: info Ảnh sẽ bổ sung
Ảnh chụp: cửa sổ Quản lý cửa sổ (Window Manager) của Clickermann với các thông số cửa sổ và ô chọn độ trong suốt Alpha. Cần máy Windows.
:::

## Hai công dụng chính của Quản lý cửa sổ

Theo help, bài Quản lý cửa sổ, công cụ này mang lại hai khả năng rất hữu ích khi viết script tự động hóa:

### Xem và khôi phục thông số cửa sổ

Khi làm việc với một ứng dụng không chạy toàn màn hình, không có gì đảm bảo ở lần mở tiếp theo cửa sổ đó sẽ nằm ở đúng vị trí cũ (theo help, bài Quản lý cửa sổ).

Nhờ công cụ Quản lý cửa sổ (theo help, bài Quản lý cửa sổ và Lịch sử phiên bản), bạn có thể:

- Dễ dàng biết được các thông số của bất kỳ cửa sổ nào và khôi phục lại các thông số đó khi cần thiết (từ bản v4.5.000 theo help, Lịch sử phiên bản, có thể nhập tay `HWND` trong Quản lý cửa sổ).
- Kết hợp với các lệnh [`WNDPOS`](/lenh/winapi#wndpos), [`WNDSIZE`](/lenh/winapi#wndsize), [`WNDGETINFO`](/lenh/winapi#wndgetinfo) và [`WNDSETINFO`](/lenh/winapi#wndsetinfo) trong script để cố định vị trí và kích thước cửa sổ.

### Đặt độ trong suốt (Alpha) để Clickermann nhìn thấy cửa sổ

Clickermann không nhìn thấy các cửa sổ trong suốt (alpha) — thay vì thấy cửa sổ đó, chương trình chỉ nhìn thấy những gì nằm phía dưới nó, dù vẫn có thể bấm chuột lên cửa sổ đó (theo help, bài Quản lý cửa sổ).

Trong công cụ Quản lý cửa sổ, bạn có thể đặt mức **100% Alpha** (theo ảnh trong help của bản cũ: chọn **Alpha 100%** ở ô chọn thả xuống rồi bấm nút áp dụng bên cạnh). Khi đó, cờ cửa sổ phân lớp được gỡ bỏ (theo help, phần FAQ) và cửa sổ trước đó bị trong suốt sẽ hiển thị đầy đủ cho cả Clickermann lẫn bạn.
