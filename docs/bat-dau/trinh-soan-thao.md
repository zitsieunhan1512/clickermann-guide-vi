# Trình soạn thảo và kính lúp

Trang này hướng dẫn cách sử dụng cửa sổ trình soạn thảo script tích hợp của Clickermann, phím tắt chèn nhanh tọa độ/màu sắc và công cụ kính lúp màn hình.

::: info Hình minh họa sẽ bổ sung
Hình chụp cửa sổ trình soạn thảo script (với 4 nhóm nút trên thanh công cụ, khung thông tin tọa độ/màu sắc/HWND theo thời gian thực và ô kính lúp ở góc dưới bên trái) sẽ được bổ sung sau khi chụp trực tiếp trên máy Windows.
:::

## Bố cục thanh công cụ

Trình soạn thảo là nơi bạn dành phần lớn thời gian để viết và chỉnh sửa mã lệnh `.cms`. Cửa sổ được trang bị tô màu cú pháp, tự động căn lề và nhiều công cụ lấy thông số màn hình.

Các cụm nút chức năng trên trình soạn thảo được chia thành 4 nhóm chính:

1. **Nhóm quản lý tệp script (hàng trên):** Tạo mới, mở tệp, mở lịch sử các tệp gần đây, lưu (`Ctrl + S`) và lưu thành tệp mới.
2. **Nhóm công cụ hỗ trợ (hàng trên):** Tìm kiếm và thay thế văn bản, bật/tắt **kính lúp màn hình**, tự động căn lề mã nguồn, v.v.
3. **Nhóm chèn nhanh mẫu lệnh (ở cột bên trái):** Mở menu mẫu code và menu phân cấp để chèn nhanh lệnh vào trình soạn thảo.
   - Các tệp mẫu nằm tại thư mục `%Clickermann%/data/lang/ru/templates/` (thay cho `ru` có thể là ngôn ngữ khác), bạn có thể tự sửa hoặc tạo mẫu mới.
   - Tệp menu phân cấp chèn lệnh nhanh nằm tại `%Clickermann%/data/lang/ru/qinsert_menu.txt`, bạn cũng có thể chỉnh sửa bằng trình soạn thảo văn bản thông thường (như Notepad) miễn là giữ đúng định dạng.
4. **Nhóm điều khiển chạy script (ở cột bên trái, ngay bên dưới nhóm 3):** Gồm các nút **Áp dụng**, **Chạy**, **Dừng** và **Nhật ký**. Ba nút cuối lặp lại chức năng của các nút tương ứng trên màn hình chính; riêng nút **Áp dụng** dùng để cập nhật nội dung đang hiển thị trong trình soạn thảo thành script làm việc hiện tại của chương trình.

## Khung thông tin thời gian thực và phím tắt `Alt + Q`

Ở cột bên trái (phía dưới các nút điều khiển), chương trình hiển thị liên tục theo thời gian thực các thông số tại vị trí con trỏ chuột hiện tại:

- Tọa độ con trỏ chuột `X`, `Y`.
- Mã màu của điểm ảnh ngay dưới mũi trỏ chuột.
- Mã định danh `HWND` của phần tử cửa sổ dưới trỏ chuột.

- **Mẹo thao tác nhanh với `Alt + Q`:** Nhấn tổ hợp phím `Alt + Q` (mặc định) để chèn nhanh tọa độ và màu sắc hiện tại vào script dưới dạng câu lệnh `LCLICK` để không phải gõ lại từng con số bằng tay; hoặc chỉ chép tọa độ hiện tại vào bộ nhớ tạm (Clipboard) khi bật chế độ tương ứng bằng nút có biểu tượng Clipboard.

## Kính lúp màn hình và chụp nhanh mẫu ảnh `Alt + G`

Ở góc dưới cùng bên trái của trình soạn thảo là **kính lúp** giúp phóng to vùng điểm ảnh quanh con trỏ chuột.

- **Hiển thị đúng như Clickermann nhìn thấy:** Kính lúp hiển thị hình ảnh màn hình sau khi đã áp dụng chế độ giảm màu (`COLORMODE`) và chế độ khóa cửa sổ, giúp bạn kiểm tra chính xác những gì chương trình đang nhận diện.
- **Bật / tắt kính lúp:** Mặc định kính lúp được tắt để đỡ tốn tài nguyên CPU. Bạn bật kính lúp bằng nút có hình kính lúp trên thanh công cụ phía trên.
- **Các nút dưới khung kính lúp (từ trái sang phải):** Phóng to, thu nhỏ, đổi màu tâm ngắm và nút chuyển mức giảm màu (`0..7`). Lưu ý nút đổi mức giảm màu dưới kính lúp chỉ để xem thử bằng mắt, không tự thêm lệnh `COLORMODE` vào script.
- **Giảm tốc độ chuột khi bật kính lúp:** Khi kính lúp đang bật, tốc độ di chuyển chuột sẽ được làm chậm lại để bạn dễ căn chỉnh vào từng điểm ảnh. **Hãy nhớ tắt kính lúp khi không dùng nữa hoặc trước khi đóng chương trình** để tốc độ chuột trở lại bình thường.
- **Chụp nhanh ảnh mẫu `100×100` bằng `Alt + G`:** Nhấn `Alt + G` để chụp nhanh vùng ảnh `100×100` điểm ảnh mà kính lúp đang nhìn thấy; ảnh chụp tự động được áp dụng mức giảm màu hiện tại và lưu ở định dạng `.bmp`, bạn chỉ cần mở trong Paint để cắt gọn phần cần dùng.

## Khung soạn thảo văn bản

Toàn bộ phần bên phải là khung soạn thảo văn bản chuẩn. Bạn có thể dùng các phím tắt quen thuộc như:

- `Ctrl + S`: Lưu nhanh tệp script.
- `Tab` / `Shift + Tab`: Thụt lề vào hoặc lùi lề ra cho cả khối dòng đang bôi đen.

---

*Nguồn: Tài liệu trợ giúp `help.chm` (bài Trình soạn thảo).*
