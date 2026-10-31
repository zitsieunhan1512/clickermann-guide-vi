# Cẩm nang: Tìm màu trên màn hình rồi bấm chuột

Trang này hướng dẫn từng bước cách dùng `GETSCREEN`, `IF_PIXEL_IN` và `SCANPXL` để tìm điểm ảnh có màu chỉ định trên màn hình rồi tự động bấm chuột vào vị trí tìm thấy.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Quy trình chuẩn khi tìm màu

Mọi kịch bản tìm màu trong Clickermann đều đi theo 3 bước cố định:

1. **Chụp màn hình vào bộ đệm ảnh:** Gọi [`GETSCREEN`](/lenh/man-hinh#getscreen) (hoặc `GETSCREEN(x1, y1, x2, y2)` nếu chỉ cần chụp vùng nhỏ). Nếu không có bước này, chương trình sẽ không nhìn thấy những gì mới xuất hiện trên màn hình.
2. **Tìm điểm màu trong bộ đệm ảnh:**
   - Dùng [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if) nếu chỉ cần tìm **điểm đầu tiên** khớp màu.
   - Dùng [`SCANPXL`](/lenh/man-hinh#scanpxl) nếu cần lấy danh sách **tất cả các điểm** khớp màu trong vùng.
3. **Thao tác với tọa độ tìm được:** Với `IF_PIXEL_IN`, tọa độ tìm thấy nằm trong hai biến hệ thống `$_return1` (X) và `$_return2` (Y).

---

## Kịch bản 1: Tìm một màu và bấm chuột ngay khi thấy

Giả sử bạn cần theo dõi vùng màn hình từ `(100, 100)` đến `(500, 400)`: nếu xuất hiện thông báo có điểm màu đỏ (`255`) thì bấm chuột trái vào đúng điểm đó; nếu chưa thấy thì chờ `100` mili-giây rồi quét lại.

### Giải thích từng bước

1. Gọi `GETSCREEN(100, 100, 500, 400)` để cập nhật vùng cần theo dõi vào bộ đệm ảnh.
2. Dùng `IF_PIXEL_IN(100, 100, 500, 400, 255)` để tìm mã màu `255`.
3. Nếu tìm thấy, gọi `LCLICK($_return1, $_return2)` để bấm vào tọa độ vừa tìm được.
4. Nếu không thấy (nhánh `ELSE`), gọi `WAITMS(100)` để nghỉ ngắn trước khi lặp lại vòng sau (vì script không có `HALT` nên sẽ lặp vô tận; nhấn phím tắt `Alt + S` khi muốn dừng theo help, bài Màn hình chính).

```cms
// Cập nhật vùng màn hình (100, 100) -> (500, 400) vào bộ đệm ảnh
GETSCREEN(100, 100, 500, 400)

// Tìm điểm ảnh màu đỏ (255) trong vùng đó
IF_PIXEL_IN(100, 100, 500, 400, 255)
   LOGWRITE("Tim thay mau tai X=", $_return1, " Y=", $_return2)
   LCLICK($_return1, $_return2)
   WAIT(1)
ELSE
   // Chưa thấy màu -> nghỉ 100ms để không làm nặng CPU
   WAITMS(100)
END_IF
```

---

## Kịch bản 2: Chờ cho tới khi màu xuất hiện rồi mới đi tiếp

Khi một công việc văn phòng có nhiều bước nối tiếp nhau (ví dụ: bấm nút "Xuất báo cáo", chờ thanh trạng thái đổi sang màu xanh lá `65280` báo hoàn tất rồi mới bấm nút "Đóng" ở tọa độ `300, 120`), bạn đặt `GETSCREEN` và `IF_PIXEL_IN` bên trong vòng lặp [`WHILE ... END_CYC`](/lenh/cau-truc#while-end-cyc).

*(Lưu ý: vòng lặp `WHILE` dưới đây có thể chờ mãi nếu màu `65280` không bao giờ xuất hiện trên vùng quét; khi đó bạn có thể dừng script bằng phím tắt `Alt + S` theo help, bài Màn hình chính).*

```cms
// Bước 1: Bấm nút bắt đầu công việc
LCLICK(150, 120)
LOGWRITE("Dang cho bieu tuong hoan tat mau xanh la (65280)...")

// Bước 2: Lặp kiểm tra cho tới khi thấy màu 65280 trong vùng (200, 200) -> (250, 250)
$thay_mau = 0
WHILE($thay_mau = 0)
   GETSCREEN(200, 200, 250, 250)
   IF_PIXEL_IN(200, 200, 250, 250, 65280)
      $thay_mau = 1
      LOGWRITE("Da thay mau hoan tat tai: ", $_return1, ", ", $_return2)
   ELSE
      WAITMS(100)
   END_IF
END_CYC

// Bước 3: Sau khi vòng lặp kết thúc, bấm vào nút Đóng tại (300, 120)
LCLICK(300, 120)
LOGWRITE("Da bam nut Dong va xong quy trinh.")
HALT
```

---

## Kịch bản 3: Quét toàn bộ các điểm cùng màu bằng `SCANPXL`

Khi trên màn hình có nhiều điểm cùng mang mã màu `255` và bạn muốn lấy tọa độ của tất cả các điểm đó, hãy dùng thủ tục [`SCANPXL`](/lenh/man-hinh#scanpxl).

### Giải thích từng bước

1. Gọi `GETSCREEN` để chụp màn hình vào bộ đệm ảnh.
2. Gọi `SCANPXL($var, 0, 0, 500, 500, 255)` để đưa toàn bộ các cặp tọa độ `(X, Y)` tìm thấy vào mảng `$var`.
3. Dùng vòng lặp `WHILE(ARRSIZE($var) > 0)` kết hợp [`ARRPOP`](/lenh/so#arrpop) để lấy tọa độ từ cuối mảng ra. Lưu ý vì mảng lưu theo thứ tự `[X1, Y1, X2, Y2, ...]`, khi rút từ cuối mảng bằng `ARRPOP`, bạn phải **rút `$y` trước rồi mới rút `$x`**.

```cms
GETSCREEN

// Tìm tất cả điểm ảnh màu đỏ (255) trong vùng 0,0 -> 500,500
SCANPXL($var, 0, 0, 500, 500, 255)
LOGWRITE("Tong so phan tu trong mang (2 * so diem): ", ARRSIZE($var))

// Rút lần lượt từng cặp tọa độ từ cuối mảng ra
WHILE(ARRSIZE($var) > 0)
   $y = ARRPOP($var)
   $x = ARRPOP($var)
   PRINT("Diem tim thay -> X: ", $x, " | Y: ", $y)
END_CYC

HALT
```
