# Điều kiện, vòng lặp, chương trình con

Trang này hướng dẫn các cấu trúc điều khiển giúp script kiểm tra điều kiện, lặp lại thao tác, tách chương trình con và chạy nhiều luồng song song. Các cấu trúc này giúp script ngắn gọn, dễ đọc và xử lý linh hoạt theo tình huống.

*(Các đoạn code ví dụ dưới đây có thêm lệnh `HALT` ở cuối để chỉ chạy một lần khi thử nghiệm — bản gốc trong help không có `HALT`; riêng ví dụ của `THREAD` để nguyên không có `HALT` để các luồng lặp liên tục, và ở `SETTHREAD`, `SWITCH` bản gốc trong help cũng tự lặp lại liên tục).*

## IF ... END_IF

Kiểm tra một biểu thức điều kiện và chỉ chạy khối lệnh bên trong nếu điều kiện đúng.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
IF (expression)
...
END_IF
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `expression` | biểu thức logic | có | | Biểu thức điều kiện; nếu đúng (khác `0`) thì khối lệnh bên trong được thực thi |

**Ví dụ**

```cms
// Ví dụ đơn giản
$var = 5

IF($var > 3)
   LOGWRITE("dung") // chạy vì $var lớn hơn 3
END_IF

// Ví dụ kết hợp nhiều điều kiện
$var = 5

IF(($var > 3) & ($var < 10))
   LOGWRITE("dung") // chạy khi $var nằm từ 4 đến 9
END_IF

HALT
```

**Lưu ý**

- Các câu lệnh nằm giữa `IF` và `END_IF` chỉ chạy dựa trên giá trị của `expression` sau khi tính toán: nếu bằng `0` thì bỏ qua, mọi giá trị khác `0` đều được coi là đúng và khối lệnh sẽ chạy.
- `expression` có thể là phép tính số học, phép so sánh logic hoặc kết quả trả về của một hàm. Xem thêm chi tiết ở phần [Ngôn ngữ script](/khai-niem/ngon-ngu#phep-so-sanh-va-phep-toan-logic).

---

## ELSE

Khai báo nhánh lệnh dự phòng, chỉ chạy khi điều kiện ở khối lệnh kiểm tra phía trên bị sai.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
IF (expression)
...
ELSE
...
END_IF
```

**Ví dụ**

```cms
// Câu điều kiện không có nhánh ELSE
// Vì 5 < 3 là sai nên không làm gì cả
IF(5 < 3)
   LOGWRITE("dung")
END_IF

// Cùng điều kiện trên nhưng có thêm nhánh ELSE
// Vì 5 < 3 là sai nên sẽ in ra "sai"
IF(5 < 3)
   LOGWRITE("dung")
ELSE
   LOGWRITE("sai")
END_IF

HALT
```

**Lưu ý**

- `ELSE` là phần tùy chọn, đặt nằm giữa dòng mở đầu điều kiện và `END_IF`.
- Khối lệnh sau `ELSE` chỉ chạy khi điều kiện chính bị sai và khối lệnh chính không được thực thi.
- `ELSE` dùng được cho cả 3 cấu trúc điều kiện: `IF`, `IF_PICTURE_IN` và `IF_PIXEL_IN`.

---

## SWITCH ... END_SWITCH

Đối chiếu giá trị của một biểu thức với nhiều trường hợp (`CASE`) để chạy nhánh lệnh tương ứng.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SWITCH (var)
CASE (result1)
...
CASE (result2)
...
[DEFAULT]
[...]
END_SWITCH
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `var` | số / biến | có | | Giá trị đầu vào cần đem ra so sánh |
| `result1`, `result2` | số / biến | có | | Giá trị của từng trường hợp `CASE` để khớp với `var` |

**Ví dụ**

```cms
// Tạo một số ngẫu nhiên từ 1 đến 5
$var = RND(1, 5)
PRINT("$var = ", $var)

// Kiểm tra giá trị của biến $var
// Xử lý riêng các trường hợp 1, 2, 3 và gom phần còn lại vào DEFAULT
SWITCH($var)
CASE(1)
   PRINT("mot")
CASE(2)
   PRINT("hai")
CASE(3)
   PRINT("ba")
DEFAULT
   PRINT("gia tri khac")
END_SWITCH

HALT
```

**Lưu ý**

- Nên dùng `SWITCH` khi cần kiểm tra nhiều trường hợp của cùng một giá trị, giúp tránh việc dùng **quá nhiều lệnh `IF`** gây khó đọc.
- Các tham số của các lệnh nêu trên có thể là **số hoặc biến**.
- Nhánh `DEFAULT` là tùy chọn; khối lệnh sau `DEFAULT` chỉ chạy khi không có nhánh `CASE` nào khớp với giá trị hiện tại của `var`.

---

## FOR ... END_CYC

Lặp lại khối lệnh khi điều kiện còn đúng và tự động tăng biến đếm sau mỗi vòng lặp.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟠 Chưa thống nhất

```cms
FOR ($var [=value], expression, [step])
...
END_CYC
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$var` | biến | có | giá trị hiện có (hoặc `0` nếu biến mới) | Biến đếm của vòng lặp, tự tăng thêm `step` sau mỗi lần chạy thân vòng lặp |
| `value` | số | không | | Giá trị khởi tạo ban đầu gán cho `$var` khi bắt đầu vòng lặp |
| `expression` | biểu thức logic | có | | Điều kiện tiếp tục lặp; vòng lặp dừng khi biểu thức này sai |
| `step` | số | không | `1` | Bước nhảy cộng thêm vào `$var` sau mỗi vòng lặp |

**Ví dụ**

```cms
// Ví dụ đơn giản với thông số tối thiểu ($var mới sẽ bắt đầu từ 0)
FOR($var, $var < 5)
   LOGWRITE("var: ", $var)
END_CYC

// Có gán giá trị bắt đầu cho biến đếm
FOR($var=5, $var < 10)
   LOGWRITE("var: ", $var)
END_CYC

// Có giá trị bắt đầu và bước nhảy bằng 10
FOR($var=10, $var < 100, 10)
   LOGWRITE("var: ", $var)
END_CYC

// Vòng lặp lồng nhau (gán rõ =0 cho biến đếm)
FOR($x=0, $x < 3)
   FOR($y=0, $y < 3)
      PRINT($x, ":", $y)
   END_CYC
END_CYC

// Vòng lặp với điều kiện kết hợp (gán rõ =0 cho $x vì $x đã dùng ở trên)
$y = 0
FOR($x=0, ($y < 10) & ($x < 10))
   PRINT("x:", $x, " y:", $y)
   INC($y, 5)
END_CYC

HALT
```

**Lưu ý**

- Ở mỗi vòng, nếu `expression` đúng thì thân vòng lặp (các lệnh giữa `FOR` và `END_CYC`) sẽ chạy, sau đó `$var` tăng thêm `step` rồi kiểm tra lại `expression`. Vòng lặp kết thúc khi `expression` nhận giá trị sai.
- Nếu không viết `=value`: trường hợp `$var` là biến mới chưa từng dùng thì nó tự nhận giá trị `0`; nhưng nếu `$var` đã có giá trị từ trước (kể cả từ chính vòng lặp đó ở lượt chạy trước), vòng lặp sẽ dùng tiếp giá trị hiện tại của `$var`.
- 🟠 **Lưu ý khi lồng vòng lặp `FOR` hoặc dùng lại biến đếm:**
  - **Nên làm:** Hãy luôn gán rõ giá trị khởi đầu (như `FOR($x=0, $x < 3)` và `FOR($y=0, $y < 3)`) cho biến đếm ở mọi vòng lặp `FOR`.
  ::: details Vì sao chưa chắc
   ở hai ví dụ cuối (vòng lặp lồng nhau và điều kiện kết hợp), bản trong help viết `for($x, $x < 3)`, `for($y, $y < 3)` và `for($x, ($y < 10) & ($x < 10))` không có `=0`. Theo mô tả ngay phía trên của help, biến giữ giá trị cũ nên vòng trong `$y` (khi `$x` sang `1`, `2`) hoặc vòng sau dùng lại `$x` có thể không chạy, vì vậy ở đây gán rõ `=0`. Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#vong-lap-for-long-nhau-khong-gan-gia-tri-dau).
  :::

---

## WHILE ... END_CYC

Lặp lại khối lệnh chừng nào biểu thức điều kiện đầu vòng lặp còn đúng.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WHILE (expression)
...
END_CYC
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `expression` | biểu thức logic | có | | Điều kiện lặp; thân vòng lặp chạy khi biểu thức này đúng |

**Ví dụ**

```cms
// Vòng lặp WHILE đơn giản
$var = 1

WHILE($var < 5)
   LOGWRITE("var: ", $var)
   INC($var)
END_CYC

// Vòng lặp WHILE với điều kiện kết hợp
$x = 0
$y = 0

WHILE(($x < 5) & ($y < 5))
   PRINT($x, ",", $y)
   INC($x, 1)
   INC($y, 2)
END_CYC

PRINT("ket thuc: ", $x, ",", $y)
HALT
```

**Lưu ý**

- `WHILE` là dạng rút gọn của `FOR` khi không có sẵn biến đếm và bước nhảy tự động.
- Vì biến không tự tăng, rất dễ xảy ra lỗi lặp vô tận (treo logic) nếu điều kiện luôn đúng. Bạn cần đảm bảo bên trong thân vòng lặp có câu lệnh làm thay đổi dữ liệu để đến lúc nào đó `expression` trở thành sai và vòng lặp kết thúc.

---

## SUB ... END_SUB

Định nghĩa một chương trình con để gom nhóm các câu lệnh và gọi lại nhiều lần theo tên.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟠 Chưa thống nhất

```cms
SUB (sub_name, [$par1, $par2, ...])
...
END_SUB
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `sub_name` | tên | có | | Tên duy nhất của chương trình con |
| `$par1, $par2, ...` | biến | không | | Danh sách các tham số truyền vào chương trình con |

**Ví dụ**

```cms
// Ví dụ 1: Định nghĩa và gọi chương trình con không có tham số
SUB(thong_bao)
   FOR($i=0, $i < 3)
      PRINT("Lan thu ", $i)
   END_CYC
END_SUB

// Gọi chương trình con (bắt buộc có cặp ngoặc tròn)
thong_bao()

// Ví dụ 2: Chương trình con nhân hai số ngẫu nhiên
SUB(nhan_hai_so, $par1, $par2)
   PRINT("par1: ", $par1)
   PRINT("par2: ", $par2)
   PRINT("par1 * par2 = ", $par1 * $par2)
END_SUB

// Gọi chương trình con 3 lần
FOR($i=0, $i < 3)
   nhan_hai_so(RND(1, 5), RND(1, 5))
END_CYC

// Ví dụ 3: Chương trình con nhận tham số chuỗi
SUB(xin_chao, $name)
   PRINT("Xin chao, ", $name)
END_SUB

xin_chao("An")
HALT
```

*(Lưu ý về vòng lặp trong Ví dụ 1 và 2: bản trong help viết `for($i, $i < 3)` không có `=0`. Theo mô tả của help, biến giữ giá trị cũ nên vòng sau có thể không chạy, vì vậy ở đây gán rõ `=0`).*

**Lưu ý**

- Khối lệnh trong `SUB ... END_SUB` không tự chạy khi script đi ngang qua, mà chỉ chạy khi bạn gọi tên `sub_name(...)` trong script.
- Có thể khai báo chương trình con ở **bất kỳ đâu trong script**, miễn là phần định nghĩa `SUB` nằm **trước (phía trên)** mọi lời gọi tới nó. Vì vậy nên đặt các khối `SUB` ở ngay đầu script.
- Sau khi thực thi xong chương trình con, script tiếp tục chạy từ chỗ gọi; các biến cục bộ (các tham số `$par1, $par2, ...`) của chương trình con **khi đó** sẽ bị hủy.
- Số lượng tham số lúc gọi phải khớp chính xác với số lượng tham số lúc khai báo `SUB`. Nếu chương trình con không có tham số, khi gọi vẫn phải viết cặp ngoặc tròn rỗng `sub_name()`.
- 🟠 **Điểm chưa thống nhất về việc đặt `SUB` trong tệp `#include`:**
  - **Nên làm:** Khi mới viết script hoặc khi gặp lỗi không rõ nguyên nhân với `#include`, hãy đặt các khối `SUB ... END_SUB` ngay ở đầu tệp script `.cms` chính.
  ::: details Vì sao chưa chắc
  - **Theo help (mục Cấu trúc lệnh):** Ghi rằng *"Việc tách phần thân các chương trình con ra một tệp riêng bên ngoài rồi nạp qua chỉ thị `#include` được coi là thói quen tốt"*.
  - **Theo sách của Chô tô (tr. 81):** Lại khuyên hạn chế để `SUB` ở tệp ngoài rồi nạp qua `#include` vì đôi lúc bị lỗi.
  - Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#dat-sub-trong-tep-include).
  :::

---

## THREAD ... END_THREAD

Định nghĩa một luồng chạy độc lập, hoạt động song song với script chính và các luồng khác.

**Loại:** cấu trúc lệnh · **Trạng thái:** 🟠 Chưa thống nhất

```cms
THREAD (thread_name, [init_state])
...
END_THREAD
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `thread_name` | tên | có | | Tên của luồng |
| `init_state` | số | không | 🟠 *Chưa thống nhất* (xem lưu ý) | Trạng thái ban đầu của luồng (`1` — chạy ngay, `0` — tạm dừng) |

**Ví dụ**

```cms
// Ví dụ từ help: chạy đồng thời script chính và hai luồng con
// Mỗi luồng in thông báo theo nhịp thời gian riêng, không làm nghẽn nhau
//-----------------------------------------
// Luồng thứ nhất
THREAD(t1)
   PRINT("luong #1 tich-tac")
   WAIT(5)
END_THREAD

//-----------------------------------------
// Luồng thứ hai
THREAD(t2)
   PRINT("luong #2 tich-tac")
   WAIT(3)
END_THREAD

//-----------------------------------------
// Script chính
PRINT("Script chinh tich-tac")
WAIT(10)
```

**Lưu ý**

- Mỗi luồng có hai trạng thái: đang chạy (thực thi thân luồng) và tạm dừng (không thực thi). Có thể tạm dừng hoặc cho chạy tiếp bằng thủ tục `SETTHREAD`.
- Mỗi luồng có bộ đếm thời gian riêng: các lệnh chờ (`WAIT`, `WAITMS`) hoặc độ trễ của lệnh trong luồng này không làm chậm script chính hay các luồng khác.
- Chương trình con (`SUB`) dùng trong luồng nào phải được khai báo và gọi ngay bên trong thân của chính luồng đó. Không được khai báo `SUB` ở ngoài rồi gọi từ trong luồng (hoặc ngược lại) vì sẽ gây lỗi.
- Mọi luồng và script chính dùng chung một phạm vi dữ liệu: tất cả đều đọc/ghi chung các biến và dùng chung **bộ đệm ảnh**.
- Khi bấm chạy script chính từ giao diện, các luồng sẽ mang trạng thái ban đầu lúc khai báo; khi tạm dừng hoặc dừng hẳn script chính, tất cả các luồng cũng tạm dừng hoặc dừng theo.
- 🟠 **Điểm chưa thống nhất về giá trị mặc định của `init_state`:**
  - **Nên làm:** Hãy luôn truyền rõ `THREAD(ten, 1)` (nếu muốn luồng chạy ngay) hoặc `THREAD(ten, 0)` (nếu muốn luồng tạm dừng lúc đầu) để không phụ thuộc vào giá trị mặc định.
  ::: details Vì sao chưa chắc
  - **Theo help:** Phần mô tả cú pháp không ghi thẳng số mặc định khi bỏ qua `init_state`, nhưng ví dụ của help viết `thread(t1)` và `thread(t2)` không truyền `init_state` và giải thích rằng cả hai luồng con này cùng chạy song song ngay với script chính; còn khi muốn tạo luồng ở trạng thái tạm dừng thì ví dụ ở mục `SETTHREAD` viết rõ `thread(t1, 0)`. **Suy luận:** Như vậy theo ví dụ của help, bỏ trống `init_state` thì luồng tự chạy (`1`).
  - **Theo sách của Chô tô (tr. 82):** Sách lại ghi rằng nếu không ghi `init_state` thì luồng đang ở trạng thái tắt (`0`), chưa chạy và bắt buộc phải bật bằng lệnh `SETTHREAD`.
  - Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#trang-thai-mac-dinh-cua-thread-khi-bo-qua-init-state).
  :::

---

## SETTHREAD

Đổi trạng thái hoạt động của một luồng (tạm dừng, chạy tiếp hoặc đặt lại về đầu).

**Loại:** thủ tục · **Trạng thái:** 🟠 Chưa thống nhất

```cms
SETTHREAD (thread_name, state)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `thread_name` | tên | có | | Tên của luồng cần đổi trạng thái |
| `state` | số | có | | Trạng thái muốn đặt cho luồng (`0`, `1` hoặc `2`) |

**Ví dụ**

```cms
//-----------------------------------------
// Khai báo một luồng đang ở trạng thái tạm dừng
THREAD(t1, 0)
   PRINT("luong #1 tich-tac")
   WAIT(5)
END_THREAD
//-----------------------------------------

// Cho luồng chạy từ trạng thái tạm dừng
SETTHREAD(t1, 1)
WAIT(10)
HALT
```

**Lưu ý**

- Ý nghĩa các giá trị của tham số `state`:
  - `0` — Đưa luồng vào trạng thái tạm dừng (giữ nguyên vị trí dòng lệnh đang chạy dở).
  - `1` — Gỡ tạm dừng để luồng chạy tiếp từ đúng vị trí đã dừng trước đó.
  - `2` — Đưa luồng vào trạng thái tạm dừng, đồng thời đặt lại vị trí về đầu luồng; ở lần gọi `SETTHREAD(thread_name, 1)` tiếp theo, luồng sẽ chạy lại từ dòng đầu tiên bất kể trước đó dừng ở đâu.
- 🟠 **Điểm chưa thống nhất khi so sánh giữa help và sách của Chô tô:**
  - **Nên làm:** Dùng `state = 0` khi muốn tạm dừng giữ vị trí, `state = 1` để chạy tiếp, và `state = 2` khi muốn tạm dừng đồng thời đặt lại luồng về dòng đầu tiên.
  ::: details Vì sao chưa chắc
  - **Theo help:** `SETTHREAD` hỗ trợ 3 giá trị `state` là `0` (tạm dừng, giữ vị trí), `1` (chạy tiếp từ chỗ dừng) và `2` (tạm dừng và đặt lại về đầu luồng cho lần chạy sau).
  - **Theo sách của Chô tô (tr. 83):** Sách chỉ liệt kê hai giá trị là `0` (tắt luồng) và `1` (bật luồng), thiếu hẳn giá trị `2`, và cách gọi "tắt luồng" dễ gây nhầm lẫn với việc dừng hẳn từ đầu trong khi thực chất `0` trong help là tạm dừng tại chỗ.
  - Xem chi tiết và script kiểm chứng hành vi `state = 0` so với `state = 2` tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#cac-gia-tri-state-cua-setthread).
  :::
