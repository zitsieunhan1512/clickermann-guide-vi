# Số, biến và mảng

Trang này mô tả các thủ tục và hàm dùng để khai báo biến, tính toán số học, lượng giác, sinh số ngẫu nhiên và thao tác với mảng trong Clickermann.

## DEFINE

Khai báo một biến mới và gán giá trị ban đầu cho biến đó.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
DEFINE ($var, [value])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | biến | có | | Tên biến cần khai báo |
| `value` | số / chuỗi | không | `0` | Giá trị ban đầu gán cho biến |

**Ví dụ**

```cms
DEFINE($myvar, 5)
DEFINE($myvar, 10)
LOGWRITE("Gia tri: ", $myvar)
HALT
```

**Lưu ý**

- Lệnh chỉ có tác dụng nếu biến `$var` chưa từng được khai báo trước đó; nếu biến đã tồn tại thì lệnh này sẽ bị bỏ qua (trong ví dụ trên, `$myvar` giữ nguyên giá trị `5`).
- Nếu bỏ qua tham số `value`, biến sẽ được khởi tạo bằng `0`.

---

## UNDEFINE

Xóa một biến hoặc toàn bộ mảng khỏi bộ nhớ.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
UNDEFINE ($var)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | biến / mảng | có | | Tên biến hoặc mảng cần xóa |

**Ví dụ**

```cms
$myvar = 123
UNDEFINE($myvar)
LOGWRITE("Sau khi xoa: ", $myvar)
HALT
```

**Lưu ý**

- Nếu đọc lại một biến đã bị xóa bằng `UNDEFINE`, giá trị của nó sẽ trở về `0`.
- Thủ tục này cũng dùng để xóa một mảng cùng toàn bộ các phần tử bên trong mảng đó.

---

## INC

Cộng thêm một lượng vào giá trị hiện tại của biến.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
INC ($var, [value])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | biến | có | | Biến cần thay đổi giá trị |
| `value` | số | không | `1` | Giá trị cộng thêm vào biến (dùng số âm nếu muốn trừ bớt) |

**Ví dụ**

```cms
INC($myvar, 5)  // tăng giá trị biến thêm 5
INC($myvar, -3) // giảm giá trị biến đi 3
LOGWRITE("Ket qua: ", $myvar)
HALT
```

**Lưu ý**

- Nếu không truyền tham số `value`, biến `$var` mặc định tăng thêm `1`.

---

## RND

Trả về một số nguyên ngẫu nhiên nằm trong khoảng cho trước.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
RND (from, to)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `from` | số | có | | Cận dưới của khoảng ngẫu nhiên |
| `to` | số | có | | Cận trên của khoảng ngẫu nhiên |

**Trả về:** Số nguyên ngẫu nhiên trong đoạn từ `from` đến `to`.

**Ví dụ**

```cms
// Bấm chuột trái vào một tọa độ ngẫu nhiên trong vùng 0..100
LCLICK(RND(0, 100), RND(0, 100))
HALT
```

**Lưu ý**

- Cả hai đầu mút `from` và `to` đều nằm trong tập giá trị mà hàm có thể trả về.

---

## RNDFROM

Chọn ngẫu nhiên một phần tử từ danh sách các đối số truyền vào.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
RNDFROM (a, b, ...)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `a, b, ...` | số / chuỗi | có | | Danh sách các phần tử để chọn ngẫu nhiên (số lượng tham số không giới hạn) |

**Trả về:** Một phần tử được chọn ngẫu nhiên từ các đối số đã truyền.

**Ví dụ**

```cms
$var = RNDFROM(1, "tao", 5)
PRINT($var)
HALT
```

---

## INT

Lấy phần nguyên của một số (cắt bỏ phần thập phân, không làm tròn) hoặc ép kiểu dữ liệu về số.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
INT (num)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `num` | số / chuỗi | có | | Giá trị cần lấy phần nguyên hoặc chuyển thành số |

**Trả về:** Phần nguyên của `num` dưới dạng số.

**Ví dụ**

```cms
$var = INT(25.73)
PRINT($var) // kết quả là 25
HALT
```

**Lưu ý**

- Hàm này có thể dùng để ép kiểu dữ liệu, cho phép chuyển một chuỗi thành số.
- Nếu bạn muốn làm tròn số đến độ chính xác nhất định thay vì cắt bỏ phần lẻ, hãy dùng hàm [`ROUND`](#round).

---

## DIST

Tính khoảng cách hình học giữa hai điểm tọa độ.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
DIST (x1, y1, x2, y2)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x1, y1` | số | có | | Tọa độ của điểm thứ nhất |
| `x2, y2` | số | có | | Tọa độ của điểm thứ hai |

**Trả về:** Khoảng cách giữa hai điểm dưới dạng số thực (số có dấu chấm động).

**Ví dụ**

```cms
$distance = DIST(0, 0, 3, 3)
PRINT($distance)
HALT
```

---

## SIN

Tính giá trị sin lượng giác của một góc tính bằng độ.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SIN (arg)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Góc đầu vào (đơn vị: độ) |

**Trả về:** Giá trị sin của góc `arg`.

**Ví dụ**

```cms
// Di chuyển con trỏ chuột theo đường hình sin
FOR($i, $i < 500)
   $y1 = SIN($i) * 180 / 3.1415
   MOVE($i * 2, INT($y1) + 300)
   WAITMS(100)
END_CYC
HALT
```

---

## COS

Tính giá trị cosin lượng giác của một góc tính bằng độ.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
COS (arg)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Góc đầu vào (đơn vị: độ) |

**Trả về:** Giá trị cosin của góc `arg`.

**Ví dụ**

```cms
$c = COS(60)
PRINT($c)
HALT
```

---

## ARCSIN

Tính góc (theo độ) từ giá trị sin đã biết (hàm ngược của hàm `SIN`).

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ARCSIN (arg)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Giá trị sin cần tìm lại góc ban đầu |

**Trả về:** Số đo góc tương ứng (đơn vị: độ).

**Ví dụ**

```cms
$var = 30
PRINT($var)
$var = SIN($var)    // sin(30) = 0.5
PRINT($var)
$var = ARCSIN($var) // arcsin(0.5) = 30
PRINT($var)
HALT
```

---

## ARCCOS

Tính góc (theo độ) từ giá trị cosin đã biết (hàm ngược của hàm `COS`).

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ARCCOS (arg)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Giá trị cosin cần tìm lại góc ban đầu |

**Trả về:** Số đo góc tương ứng (đơn vị: độ).

**Ví dụ**

```cms
$goc = ARCCOS(0.5)
PRINT($goc)
HALT
```

---

## SQRT

Tính căn bậc hai của một số.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SQRT (arg)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Số cần lấy căn bậc hai |

**Trả về:** Căn bậc hai của `arg`.

**Ví dụ**

```cms
$kq = SQRT(400)
PRINT($kq) // 20
HALT
```

---

## POW

Tính lũy thừa của một số.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
POW (arg, power)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Cơ số |
| `power` | số | có | | Số mũ |

**Trả về:** Kết quả của `arg` mũ `power`.

**Ví dụ**

```cms
$kq = POW(2, 10)
PRINT($kq) // 1024
HALT
```

---

## ABS

Lấy giá trị tuyệt đối của một số.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ABS (arg)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Số đầu vào |

**Trả về:** Giá trị tuyệt đối (không âm) của `arg`.

**Ví dụ**

```cms
$kq = ABS(-25)
PRINT($kq) // 25
HALT
```

---

## ROUND

Làm tròn một số đến hàng thập phân hoặc hàng đơn vị/chục/trăm chỉ định.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ROUND (arg, prec)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `arg` | số | có | | Số cần làm tròn |
| `prec` | số | có | | Độ chính xác cần làm tròn (dương: phần nguyên; âm: phần thập phân; `0`: số nguyên gần nhất) |

**Trả về:** Giá trị của `arg` sau khi đã làm tròn.

**Ví dụ**

```cms
$r = ROUND(1236, 1)   // $r = 1240
$r = ROUND(1236, 2)   // $r = 1200
$r = ROUND(1.236, -2) // $r = 1.24
$r = ROUND(1.236, -1) // $r = 1.2
$r = ROUND(1.236, 0)  // $r = 1
PRINT($r)
HALT
```

**Lưu ý**

- Help ghi: "Việc làm tròn diễn ra theo hướng ra xa số 0. Tức là `prec = 2` sẽ làm tròn số đến hàng trăm, còn `prec = -2` đến hàng phần trăm (hai chữ số sau dấu chấm). Việc làm tròn diễn ra theo quy tắc chuẩn `0.5`."
- Cách hiểu câu trên của help: vế giải thích ngay sau cụm "theo hướng ra xa số 0" (`prec = 2` là hàng trăm, `prec = -2` là hàng phần trăm) cho thấy tác giả có thể đang mô tả chiều của tham số `prec` tính từ vị trí hàng đơn vị (`prec = 0`) đi ra hai phía, nhưng cũng có thể hiểu là cách làm tròn số âm khi gặp `.5` (ví dụ `ROUND(-1.5, 0)` ra `-2` hay `-1`). Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#cach-lam-tron-so-am-cua-round).

---

## ARRPUSH

Thêm một phần tử mới vào cuối mảng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ARRPUSH ($var, value)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | mảng | có | | Tên mảng cần thêm phần tử |
| `value` | số / chuỗi | có | | Giá trị (số hoặc chuỗi) muốn thêm vào cuối mảng |

**Ví dụ**

```cms
ARRPUSH($arr, 435)
ARRPUSH($arr, 532)
ARRPUSH($arr, 943)

PRINT($arr[0])
PRINT($arr[1])
PRINT($arr[2])
HALT
```

---

## ARRPOP

Lấy ra phần tử cuối cùng của mảng và xóa luôn phần tử đó khỏi mảng.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ARRPOP ($var)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | mảng | có | | Tên mảng cần lấy phần tử cuối |

**Trả về:** Giá trị của phần tử nằm ở cuối mảng `$var`.

**Ví dụ**

```cms
ARRPUSH($arr, 435)
ARRPUSH($arr, 532)
ARRPUSH($arr, 943)

PRINT(ARRPOP($arr))
PRINT(ARRPOP($arr))
PRINT(ARRPOP($arr))
HALT
```

**Lưu ý**

- Mỗi lần gọi `ARRPOP`, phần tử cuối vừa được trả về cũng đồng thời bị xóa khỏi mảng (kích thước mảng giảm đi `1`).

---

## ARRSIZE

Đếm số lượng phần tử hiện có trong mảng.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ARRSIZE ($var)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | mảng | có | | Tên mảng cần kiểm tra kích thước |

**Trả về:** Tổng số phần tử hiện có trong mảng `$var`.

**Ví dụ**

```cms
ARRPUSH($arr, 435)
ARRPUSH($arr, 532)
ARRPUSH($arr, 943)

PRINT(ARRSIZE($arr))
PRINT(ARRPOP($arr))
PRINT(ARRSIZE($arr))
HALT
```

**Lưu ý**

- Chỉ số của mảng luôn bắt đầu từ `0`, nên phần tử cuối cùng của mảng sẽ có chỉ số là `ARRSIZE($var) - 1`.

---

## ARRSORT

Sắp xếp các phần tử trong mảng theo thứ tự tăng dần.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ARRSORT ($var)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | mảng | có | | Tên mảng cần sắp xếp |

**Ví dụ**

```cms
// Tạo mảng gồm 5 số ngẫu nhiên
FOR($a=0, $a < 5)
   $var[$a] = RND(0, 9)
   PRINT($var[$a])
END_CYC

// Sắp xếp tăng dần
ARRSORT($var)
PRINT("Sau khi sap xep:")

// In kết quả
FOR($a=0, $a < 5)
   PRINT($var[$a])
END_CYC

HALT
```

---

## SETVAR

Gán giá trị cho một biến thông qua chuỗi chứa tên của biến đó.

**Loại:** thủ tục · **Trạng thái:** 🟠 Chưa thống nhất

```cms
SETVAR ($var, value)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | chuỗi | có | | Chuỗi văn bản chứa tên biến (ví dụ `"$var"`) |
| `value` | số / chuỗi | có | | Giá trị muốn gán cho biến đó |

**Ví dụ**

```cms
// Chương trình con nhân ba giá trị của một biến bất kỳ
// Tên biến được truyền vào dưới dạng chuỗi
SUB(nhan_ba, $triple_var)
   $tmp = GETVAR($triple_var)
   SETVAR($triple_var, $tmp * 3)
END_SUB

// Khởi tạo biến trước khi gọi
$var = 10

// Gọi chương trình con với tên biến dạng chuỗi "$var"
nhan_ba("$var")

// In giá trị biến sau khi đã cập nhật (30)
PRINT($var)
HALT
```

**Lưu ý**

- Theo help, tại thời điểm gọi `SETVAR`, biến có tên nêu trong chuỗi `$var` **phải tồn tại từ trước**.
- 🟠 **Điểm chưa thống nhất khi so sánh giữa help và sách của Chô tô:**
  - **Theo help:** Biến được gán phải được khởi tạo hoặc khai báo trước khi gọi `SETVAR`.
  - **Theo sách của Chô tô (tr. 42):** Ví dụ trong sách viết `define($var)` nhưng dòng sau lại gọi `setvar("$x", 5)` (khai báo biến `$var` nhưng lại gán cho biến `$x` chưa từng tồn tại). Bạn không nên làm theo ví dụ lệch này của sách; hãy luôn khởi tạo đúng biến trước khi gọi `SETVAR`. Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#setvar-khi-bien-chua-ton-tai-truoc-khi-goi).

---

## GETVAR

Lấy giá trị của một biến thông qua chuỗi chứa tên của biến đó.

**Loại:** hàm · **Trạng thái:** 🟠 Chưa thống nhất

```cms
GETVAR ($var)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | chuỗi | có | | Chuỗi văn bản chứa tên biến cần lấy giá trị (ví dụ `"$var"`) |

**Trả về:** Giá trị hiện tại của biến có tên được truyền vào.

**Ví dụ**

```cms
$var = 10
$ten_bien = "$var"
$ket_qua = GETVAR($ten_bien)
PRINT("Gia tri lay qua GETVAR: ", $ket_qua)
HALT
```

**Lưu ý**

- Tại thời điểm gọi `GETVAR`, biến có tên nêu trong tham số phải tồn tại từ trước (xem thêm ví dụ kết hợp tại [`SETVAR`](#setvar)).
- 🟠 **Điểm chưa thống nhất khi so sánh giữa help và sách của Chô tô:**
  - **Theo help:** `GETVAR` là một **hàm** nhận tham số là **chuỗi tên biến** (như `"$var"`) và trả về giá trị của biến đó: `$tmp = getvar($triple_var)`.
  - **Theo sách của Chô tô (tr. 42):** Sách mô tả tên biến không cần ngoặc kép và đưa ra ví dụ `define($var, 5)`, `getvar($x)`, `print($x)`. Ví dụ trong sách bị sai ở cả 3 điểm: khai báo `$var` nhưng đọc `$x`, truyền biến trực tiếp thay vì chuỗi tên biến, và gọi như thủ tục (bỏ qua giá trị trả về của hàm). Không viết theo sách ở mục này. Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#cach-truyen-tham-so-va-gia-tri-tra-ve-cua-getvar).
