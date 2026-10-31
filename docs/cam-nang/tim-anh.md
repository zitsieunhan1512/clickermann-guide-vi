# Cẩm nang: Tìm hình ảnh mẫu trên màn hình

Trang này hướng dẫn từng bước cách chuẩn bị tệp ảnh mẫu `.bmp` và dùng cấu trúc `IF_PICTURE_IN` (hoặc `SCANPICTURE`) để tìm biểu tượng/nút bấm trên màn hình rồi thao tác chuột.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Bước 1: Chuẩn bị tệp ảnh mẫu `.bmp`

Theo help, mục Màn hình và bài [Trình soạn thảo](/bat-dau/trinh-soan-thao), tệp hình ảnh mẫu dùng để tìm kiếm phải tuân thủ đúng các yêu cầu kỹ thuật sau:

1. **Định dạng tệp:** Phải là ảnh **BMP chuẩn 24-bit** (`*.bmp`) và đặt trong thư mục dự án (theo help, mục Màn hình).
2. **Cách chụp ảnh mẫu nhanh nhất (theo help, bài Trình soạn thảo):**
   - Mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) và bật **Kính lúp**.
   - Đưa con trỏ chuột tới biểu tượng hoặc nút bấm cần tìm trên màn hình rồi nhấn tổ hợp phím **`Alt + G`**.
   - Clickermann sẽ chụp nhanh một ảnh `.bmp` kích thước `100×100` pixel của vùng kính lúp đang nhìn thấy (tự động áp dụng mức giảm màu hiện tại). Help không nói rõ nơi lưu ảnh chụp từ `Alt + G` (xem mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#noi-luu-anh-chup-nhanh-100x100-cua-phim-tat-alt-g)).
   - Mở tệp `.bmp` vừa chụp trong trình chỉnh ảnh **Paint**, cắt gọn phần cần dùng rồi lưu lại thành tệp `.bmp` **vào trong thư mục dự án** (cùng thư mục với tệp script `.cms`).

---

## Bước 2: Tìm ảnh và di chuyển / bấm vào tâm ảnh

Khi [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if) tìm thấy ảnh mẫu trên bộ đệm ảnh, nó sẽ ghi tọa độ **góc trái trên cùng** của bức ảnh khớp vào hai biến hệ thống `$_return1` (X) và `$_return2` (Y).

Để bấm trúng vào giữa nút bấm thay vì mép góc trái trên, bạn cộng thêm một khoảng lệch nhỏ (ví dụ `+4` pixel cho cả X và Y nếu ảnh mẫu rộng khoảng `8×8` pixel). Dưới đây là mẫu kịch bản dựa theo script mẫu đi kèm tool (lưu ý: số `2366701` trong ví dụ là mã màu nền cần bỏ qua của bức ảnh mẫu trong tệp ví dụ đó; khi áp dụng thực tế, bạn phải thay bằng mã màu nền của ảnh mẫu do bạn chụp, hoặc bỏ qua tham số này nếu không dùng màu trong suốt):

```cms
// Chụp màn hình hiện tại vào bộ đệm ảnh
GETSCREEN

// Tìm ảnh "nut_bam.bmp" trên toàn màn hình, bỏ qua màu nền 2366701
IF_PICTURE_IN(0, 0, $_xmax, $_ymax, "nut_bam.bmp", 2366701)
   PRINT("Tim thay anh tai X=", $_return1, ", Y=", $_return2)
   // Dịch vào tâm ảnh (+4 pixel mỗi chiều)
   MOVE($_return1 + 4, $_return2 + 4)
ELSE
   PRINT("Khong tim thay anh mau")
END_IF

HALT
```

---

## Bước 3: Kết hợp độ chính xác (`currency`) và giảm màu (`COLORMODE`)

Trong thực tế, đôi khi hình ảnh nút bấm trên màn hình có hiệu ứng sáng tối nhẹ làm một vài điểm ảnh không khớp tuyệt đối 100% với tệp `.bmp`. Bạn có hai cách xử lý theo help, mục Màn hình:

### Cách A: Giảm thông số độ chính xác `currency`

Tham số thứ 7 của `IF_PICTURE_IN` là `currency` (`1..100`, mặc định là `100`). Nếu bạn không cần bỏ qua màu nền nhưng muốn đặt độ chính xác `90%`, hãy truyền tham số màu nền `bgcolor` là `-1` (trong ví dụ dưới, `+5` là khoảng dịch từ góc trái trên vào tâm của ảnh mẫu rộng khoảng `10×10` pixel):

```cms
GETSCREEN

// Tìm ảnh "bieu_tuong.bmp" trong vùng (0, 0) -> (800, 600)
// Không bỏ qua màu nền (-1), chấp nhận độ khớp từ 90% trở lên
IF_PICTURE_IN(0, 0, 800, 600, "bieu_tuong.bmp", -1, 90)
   LCLICK($_return1 + 5, $_return2 + 5)
END_IF

HALT
```

### Cách B: Dùng `COLORMODE` để làm phẳng màu sắc

Nếu dùng [`COLORMODE`](/lenh/man-hinh#colormode), bạn hãy nhớ tệp ảnh mẫu `.bmp` cũng phải được chụp sau khi đã qua cùng mức `COLORMODE` đó:

```cms
// Chụp và lọc giảm màu mức 6 cho vùng (50, 50) -> (600, 500)
GETSCREEN(50, 50, 600, 500)
COLORMODE(6, 50, 50, 600, 500)

// Tìm tệp mẫu đã được tạo ở mức COLORMODE(6)
IF_PICTURE_IN(50, 50, 600, 500, "mau_mode6.bmp")
   LCLICK($_return1 + 5, $_return2 + 5)
END_IF

HALT
```
