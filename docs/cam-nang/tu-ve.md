# Cẩm nang: Tự động vẽ hình trong Paint

Trang này hướng dẫn từng bước cách dùng các lệnh điều khiển chuột (`LDOWN`, `MOVE`, `LUP`), hàm lượng giác (`SIN`, `COS`) và lệnh đọc tệp văn bản để tự động vẽ đoạn thẳng, hình vuông, đường tròn và hình theo danh sách tọa độ trong chương trình Paint của Windows.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Chuẩn bị trước khi chạy và nguyên tắc vẽ bằng chuột

Trước khi chạy các đoạn script bên dưới, bạn cần chuẩn bị cửa sổ **Paint** như sau:

1. Mở chương trình **Paint**, đặt vị trí và kích thước cửa sổ sao cho vùng giấy vẽ trắng bao phủ toàn bộ các tọa độ sẽ vẽ (ví dụ vùng từ `X = 150..500`, `Y = 100..420`).
2. Chọn sẵn công cụ **Cọ vẽ (Brushes)** hoặc **Bút chì (Pencil)** và chọn màu nét vẽ khác màu trắng.
3. Mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) của Clickermann và đưa trỏ chuột lên trang giấy trắng của Paint để kiểm tra xem các tọa độ trong script đã nằm gọn bên trong khung vẽ hay chưa.

**Nguyên tắc tạo nét kéo chuột:**

1. Đưa cọ tới điểm đầu tiên và **nhấn giữ chuột trái** bằng [`LDOWN(x, y)`](/lenh/chuot#ldown).
2. **Suy luận:** Trong khi chuột trái vẫn đang giữ, kéo con trỏ đi qua các điểm tiếp theo bằng một hoặc nhiều lệnh [`MOVE(x, y)`](/lenh/chuot#move) kèm khoảng chờ ngắn [`WAITMS`](/lenh/kich-ban#waitms) để Paint vẽ nối liền giữa các điểm (trong help, mục Chuột, ví dụ kéo thả chỉ gồm `LDOWN`, `WAITMS` rồi `LUP` ở tọa độ mới mà không có `MOVE` ở giữa — xem mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#keo-chuot-ve-net-lien-bang-ldown-move-lup-trong-paint)).
3. Tại điểm cuối cùng của nét, **nhả nút chuột trái** bằng [`LUP(x, y)`](/lenh/chuot#lup).

![Quy trình vẽ một nét liền trong Paint bằng LDOWN, các lệnh MOVE và LUP](/so-do/tu-ve.svg)

---

## Bước 1: Vẽ một đoạn thẳng

Để vẽ một đoạn thẳng từ điểm `(200, 200)` sang điểm `(450, 200)` trên khung vẽ của Paint:

```cms
// Chờ 2 giây để bạn chuyển sang cửa sổ Paint
WAIT(2)

// Nhấn giữ chuột trái tại điểm đầu (200, 200)
LDOWN(200, 200)
WAITMS(50)

// Kéo chuột tới điểm cuối (450, 200) và nhả chuột trái
MOVE(450, 200)
WAITMS(50)
LUP(450, 200)

HALT
```

---

## Bước 2: Vẽ hình vuông khép kín

Hình vuông là một đường gấp khúc khép kín đi qua 4 đỉnh rồi quay về đỉnh xuất phát. Giả sử đỉnh góc trái trên là `(200, 200)` và cạnh hình vuông dài `150` pixel:

```cms
// Chờ 2 giây để chuyển sang cửa sổ Paint
WAIT(2)

// Bắt đầu đặt bút tại đỉnh trái trên (200, 200)
LDOWN(200, 200)
WAITMS(50)

// Kéo sang đỉnh phải trên (350, 200)
MOVE(350, 200)
WAITMS(50)

// Kéo xuống đỉnh phải dưới (350, 350)
MOVE(350, 350)
WAITMS(50)

// Kéo sang đỉnh trái dưới (200, 350)
MOVE(200, 350)
WAITMS(50)

// Kéo về lại đỉnh trái trên (200, 200) và nhả bút
MOVE(200, 200)
WAITMS(50)
LUP(200, 200)

HALT
```

---

## Bước 3: Vẽ đường tròn bằng hàm `SIN` và `COS`

Theo help, mục Làm việc với số, hai hàm lượng giác [`SIN(arg)`](/lenh/so#sin) và [`COS(arg)`](/lenh/so#cos) nhận tham số góc `arg` tính bằng **độ** (degrees). Một đường tròn đầy đủ có góc quét từ `0` đến `360` độ.

Với tâm đường tròn tại `($tam_x, $tam_y)` và bán kính `$ban_kinh`, tọa độ mỗi điểm trên đường tròn ứng với góc `$goc` (độ) được tính bằng công thức:

- `$x = $tam_x + INT($ban_kinh * COS($goc))`
- `$y = $tam_y + INT($ban_kinh * SIN($goc))`

```cms
// Chờ 2 giây để chuyển sang cửa sổ Paint
WAIT(2)

$tam_x = 350
$tam_y = 300
$ban_kinh = 100

// Điểm bắt đầu tại góc 0 độ
$x0 = $tam_x + INT($ban_kinh * COS(0))
$y0 = $tam_y + INT($ban_kinh * SIN(0))
LDOWN($x0, $y0)
WAITMS(20)

// Quét góc từ 5 đến 360 độ, mỗi bước tăng 5 độ
FOR($goc=5, $goc <= 360, 5)
   $x = $tam_x + INT($ban_kinh * COS($goc))
   $y = $tam_y + INT($ban_kinh * SIN($goc))
   MOVE($x, $y)
   WAITMS(15)
END_CYC

// Nhả chuột tại điểm cuối để hoàn tất đường tròn
LUP($x0, $y0)
HALT
```

---

## Bước 4: Đọc danh sách tọa độ điểm từ tệp `.txt` để vẽ

Khi cần vẽ một hình phức tạp gồm nhiều điểm nối tiếp nhau, bạn có thể lưu danh sách các điểm tọa độ `X,Y` vào một tệp văn bản (ví dụ `diem_ve.txt`), mỗi điểm trên một dòng:

```text
200,200
300,120
400,200
360,320
240,320
200,200
```

Đoạn script dưới đây tạo tệp `diem_ve.txt` mẫu, sau đó đọc từng dòng bằng [`TFREAD`](/lenh/chuoi-file#tfread), tách tọa độ `X, Y` bằng [`STRSEPARATE`](/lenh/chuoi-file#strseparate) và tự động nối các điểm thành hình đa giác trong Paint:

```cms
// 1. Tạo tệp danh sách tọa độ mẫu "diem_ve.txt" (hình ngũ giác khép kín)
IF(TFCOUNT("diem_ve.txt") > 0)
   TFCLEAR("diem_ve.txt", 1)
END_IF
TFWRITE("diem_ve.txt", "200,200")
TFWRITE("diem_ve.txt", "300,120")
TFWRITE("diem_ve.txt", "400,200")
TFWRITE("diem_ve.txt", "360,320")
TFWRITE("diem_ve.txt", "240,320")
TFWRITE("diem_ve.txt", "200,200")

// Chờ 2 giây để bạn chuyển sang cửa sổ Paint
WAIT(2)

$so_diem = TFCOUNT("diem_ve.txt")

// 2. Đọc điểm đầu tiên (dòng 1) để nhấn giữ chuột trái (LDOWN)
UNDEFINE($toa_do)
STRSEPARATE(TFREAD("diem_ve.txt", 1), ",", $toa_do)
$x_dau = INT($toa_do[0])
$y_dau = INT($toa_do[1])
LDOWN($x_dau, $y_dau)
WAITMS(40)

// 3. Duyệt từ điểm thứ 2 đến điểm cuối để kéo nét vẽ (MOVE)
FOR($i=2, $i <= $so_diem)
   UNDEFINE($toa_do)
   STRSEPARATE(TFREAD("diem_ve.txt", $i), ",", $toa_do)
   $x = INT($toa_do[0])
   $y = INT($toa_do[1])
   MOVE($x, $y)
   WAITMS(40)
END_CYC

// 4. Nhả chuột tại điểm cuối cùng
LUP($x, $y)
HALT
```
