# Quản lý cửa sổ

Trang này giới thiệu công cụ Quản lý cửa sổ (Window Manager) tích hợp trong Clickermann, giúp xem và khôi phục vị trí, kích thước cửa sổ ứng dụng cũng như xử lý các cửa sổ bị trong suốt.

::: info Hình minh họa sẽ bổ sung
Hình chụp cửa sổ Quản lý cửa sổ (Window Manager) của Clickermann (với các thông số cửa sổ và ô chọn độ trong suốt Alpha) sẽ được bổ sung sau khi chụp trực tiếp trên máy Windows.
:::

## Hai công dụng chính của Quản lý cửa sổ

Công cụ Quản lý cửa sổ mang lại hai khả năng hữu ích khi viết script tự động hóa:

### Xem và khôi phục thông số cửa sổ

Khi làm việc với một ứng dụng không chạy toàn màn hình, không có gì đảm bảo ở lần mở tiếp theo cửa sổ đó sẽ nằm ở đúng vị trí cũ.

Nhờ công cụ Quản lý cửa sổ, bạn có thể dễ dàng xem được các thông số của bất kỳ cửa sổ nào và khôi phục lại các thông số đó khi cần thiết (từ bản v4.5.000, bạn có thể nhập tay mã `HWND` vào Quản lý cửa sổ).

**Suy luận:** Ngoài thao tác thủ công trên cửa sổ công cụ này, bạn có thể kết hợp các lệnh [`WNDPOS`](/lenh/winapi#wndpos), [`WNDSIZE`](/lenh/winapi#wndsize), [`WNDGETINFO`](/lenh/winapi#wndgetinfo) và [`WNDSETINFO`](/lenh/winapi#wndsetinfo) ngay trong script để tự động cố định vị trí và kích thước cửa sổ trước khi bấm chuột.

### Đặt độ trong suốt (Alpha) để Clickermann nhìn thấy cửa sổ

Clickermann không nhìn thấy các cửa sổ trong suốt (alpha) — thay vì thấy cửa sổ đó, chương trình chỉ nhìn thấy những gì nằm phía dưới nó, dù vẫn có thể bấm chuột lên cửa sổ đó.

Trong công cụ Quản lý cửa sổ, bạn có thể đặt mức **100% Alpha** (theo ảnh trong help của bản cũ: chọn **Alpha 100%** ở ô chọn thả xuống rồi bấm nút áp dụng bên cạnh). Khi đó, cờ cửa sổ phân lớp được gỡ bỏ và cửa sổ trước đó bị trong suốt sẽ hiển thị đầy đủ cho cả Clickermann lẫn bạn.

---

*Nguồn: Tài liệu trợ giúp `help.chm` (bài Quản lý cửa sổ, FAQ và Lịch sử phiên bản).*
