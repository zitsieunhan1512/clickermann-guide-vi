# Cẩm nang: Tìm hình ảnh mẫu trên màn hình

Trang này hướng dẫn từng bước cách chuẩn bị tệp ảnh mẫu `.bmp` và dùng cấu trúc `IF_PICTURE_IN` (hoặc [`SCANPICTURE`](/lenh/man-hinh#scanpicture)) để tìm biểu tượng/nút bấm trên màn hình rồi thao tác chuột.

::: important Chuẩn bị thư mục dự án trước khi bắt đầu
Hãy **tạo một thư mục riêng (thư mục dự án) và lưu tệp script `.cms` vào đó trước khi chạy**. Mọi tệp ảnh mẫu `.bmp` đều được Clickermann tìm trong thư mục dự án này.
:::

## Bước 1: Chuẩn bị tệp ảnh mẫu `.bmp`

Tệp hình ảnh mẫu dùng để tìm kiếm phải là ảnh **BMP chuẩn 24-bit** (`*.bmp`) và đặt trong thư mục dự án (cùng chỗ với tệp `.cms`). Bạn có thể tạo tệp ảnh mẫu theo một trong hai cách sau:

### Cách 1: Cắt trực tiếp vùng ảnh bằng lệnh `SCREENSHOTFIX` trong script

Nếu bạn đã biết tọa độ góc trái trên `(x1, y1)` và góc phải dưới `(x2, y2)` của nút bấm (xem tọa độ trong [Trình soạn thảo](/bat-dau/trinh-soan-thao)), bạn có thể chạy một script ngắn dùng lệnh [`SCREENSHOTFIX`](/lenh/man-hinh#screenshotfix) để cắt đúng vùng đó thành tệp `"nut_bam.bmp"` ngay trong thư mục dự án:

```cms
// Chụp màn hình và cắt vùng từ (100, 200) đến (120, 210) lưu thành "nut_bam.bmp"
GETSCREEN
SCREENSHOTFIX(100, 200, 120, 210, "nut_bam.bmp")
PRINT("Da luu anh mau nut_bam.bmp")
HALT
```

### Cách 2: Chụp nhanh qua kính lúp (`Alt + G`) rồi cắt bằng Paint

1. Mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) và bật **Kính lúp**.
2. Đưa con trỏ chuột tới biểu tượng hoặc nút bấm cần tìm trên màn hình rồi nhấn tổ hợp phím **`Alt + G`**.
3. Clickermann sẽ chụp nhanh một ảnh `.bmp` kích thước `100×100` điểm ảnh của vùng kính lúp đang nhìn thấy (tự động áp dụng mức giảm màu hiện tại; xem mục kiểm tra nơi lưu ảnh tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#noi-luu-anh-chup-nhanh-100x100-cua-phim-tat-alt-g)). *(Nhớ **tắt kính lúp** sau khi chụp xong nếu thấy con trỏ chuột di chuyển chậm).*
4. Mở tệp `.bmp` vừa chụp trong chương trình **Paint**, cắt gọn phần nút bấm cần dùng (nên cắt nhỏ gọn bên trong nút), rồi chọn *Save As* với kiểu tệp **"24-bit Bitmap (`*.bmp`)"** và lưu vào **thư mục dự án**.

---

## Bước 2: Tìm ảnh và bấm vào tâm ảnh

Khi [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if) tìm thấy ảnh mẫu trên bộ đệm ảnh, nó sẽ ghi tọa độ **góc trái trên cùng** của bức ảnh khớp vào hai biến hệ thống `$_return1` (X) và `$_return2` (Y).

Để bấm trúng vào chính giữa nút bấm thay vì mép góc trái trên, bạn áp dụng quy tắc: **cộng một nửa chiều rộng vào `$_return1` và cộng một nửa chiều cao của bức ảnh bạn đã cắt vào `$_return2`**.

Ví dụ: nếu bức ảnh `nut_bam.bmp` của bạn có chiều rộng `20` điểm ảnh và chiều cao `10` điểm ảnh, một nửa chiều rộng là `10` và một nửa chiều cao là `5`:

```cms
// Chụp màn hình hiện tại vào bộ đệm ảnh
GETSCREEN

// Tìm ảnh "nut_bam.bmp" trên toàn màn hình
IF_PICTURE_IN(0, 0, $_xmax, $_ymax, "nut_bam.bmp")
   PRINT("Tim thay anh tai X=", $_return1, ", Y=", $_return2)
   // Bấm vào tâm ảnh: cộng nửa chiều rộng (+10) vào X và nửa chiều cao (+5) vào Y
   LCLICK($_return1 + 10, $_return2 + 5)
ELSE
   PRINT("Khong tim thay anh mau")
END_IF

HALT
```

*(Nếu trên màn hình có nhiều biểu tượng giống hệt nhau và bạn muốn lấy danh sách tọa độ của tất cả các biểu tượng đó vào mảng, hãy xem thủ tục [`SCANPICTURE`](/lenh/man-hinh#scanpicture)).*

---

## Bước 3: Tùy chọn nâng cao (màu nền trong suốt, độ chính xác và giảm màu)

Trong thực tế, đôi khi biểu tượng cần tìm nằm đè lên nền thay đổi hoặc có hiệu ứng sáng tối nhẹ. Bạn có thể kết hợp thêm các kỹ thuật sau:

### Cách A: Bỏ qua màu nền (`bgcolor`) và đặt độ chính xác (`currency`)

Cú pháp đầy đủ của lệnh là `IF_PICTURE_IN(x1, y1, x2, y2, "file", [bgcolor], [currency])`:

- **`bgcolor` (màu nền trong suốt):** Nếu biểu tượng có phần viền nền xung quanh mà bạn muốn chương trình bỏ qua không so sánh khi tìm, hãy truyền mã màu của nền đó vào tham số thứ 6 (ví dụ `2366701`; khi dùng thực tế, bạn phải thay bằng mã màu nền trên ảnh mẫu của bạn). Nếu không cần bỏ qua màu nền, hãy truyền **`-1`**.
- **`currency` (độ chính xác):** Là tỷ lệ phần trăm điểm ảnh khớp từ `1` đến `100` (mặc định là `100`, tức phải khớp tuyệt đối 100%). Bạn có thể hạ xuống `90` (tức khớp 90%) nếu ảnh trên màn hình hơi lệch màu nhẹ:

```cms
GETSCREEN

// Tìm ảnh "bieu_tuong.bmp" trong vùng (0, 0) -> (800, 600)
// Không bỏ qua màu nền (-1), chấp nhận độ chính xác từ 90% trở lên
IF_PICTURE_IN(0, 0, 800, 600, "bieu_tuong.bmp", -1, 90)
   LCLICK($_return1 + 5, $_return2 + 5)
END_IF

HALT
```

Ví dụ khi dùng tham số màu nền trong suốt `bgcolor` (thay `2366701` bằng mã màu nền thực tế trên ảnh mẫu `.bmp` của bạn):

```cms
GETSCREEN

// Tìm ảnh "nut_bam.bmp" và bỏ qua các điểm ảnh có màu nền 2366701
IF_PICTURE_IN(0, 0, $_xmax, $_ymax, "nut_bam.bmp", 2366701)
   LCLICK($_return1 + 4, $_return2 + 4)
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

---

*Nguồn: Tài liệu trợ giúp `help.chm` (mục Màn hình, bài Trình soạn thảo và bài Giảm màu).*
