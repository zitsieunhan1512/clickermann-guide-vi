# Ngôn ngữ script

Trang này trình bày các khái niệm nền tảng của ngôn ngữ script trong Clickermann v4.13: cấu trúc dòng lệnh, thủ tục và hàm, biến và kiểu dữ liệu, điều kiện và vòng lặp, phép toán, mảng, hằng số, chỉ thị tiền xử lý và bảng biến hệ thống.

## Cấu trúc một script

Script trong Clickermann là một dãy các dòng văn bản được thực thi tuần tự từ trên xuống dưới. Mỗi dòng chỉ được chứa tối đa một câu lệnh và thuộc một trong các dạng sau:

- Lời gọi một **thủ tục** (ví dụ `LCLICK(100, 200)`).
- Một **phép gán** giá trị cho biến (ví dụ `$count = $count + 1`).
- Một dòng **chú thích** bắt đầu bằng `//` (chương trình sẽ bỏ qua phần từ sau `//` tới hết dòng).
- Một **chỉ thị tiền xử lý** bắt đầu bằng dấu `#` (ví dụ `#name "Kich ban 1"`).
- Một dòng trống (để phân tách code cho dễ đọc).

Khi chạy xong dòng cuối cùng của script, chương trình sẽ tự động quay lại dòng đầu tiên và chạy lặp lại từ đầu (trừ khi gặp lệnh [`HALT`](/lenh/kich-ban#halt)).

## Thủ tục và hàm

Khi đọc tài liệu hoặc viết script, bạn sẽ gặp hai loại lệnh có cặp ngoặc tròn `( )` đi kèm:

- **Thủ tục:** Là câu lệnh yêu cầu Clickermann thực hiện một hành động (như `LCLICK(100, 200)`, `WAIT(1)`). Thủ tục đứng độc lập trên một dòng và không trả về giá trị trực tiếp tại chỗ gọi. Các giá trị truyền vào bên trong ngoặc tròn gọi là **tham số**.
- **Hàm:** Cũng có tên và các tham số trong ngoặc tròn như thủ tục, nhưng **trả về một giá trị** ngay tại vị trí gọi nó (tương tự như một biến). Bạn có thể gán kết quả của hàm cho biến (`$so = RND(1, 10)`) hoặc truyền thẳng hàm làm tham số bên trong một lệnh khác (ví dụ `WAIT(RND(3, 5))`).

## Biến và kiểu dữ liệu

Tên biến trong Clickermann luôn bắt đầu bằng ký hiệu đô la `$` nối liền với tên định danh gồm các chữ cái Latin `a..z`, chữ số `0..9` và dấu gạch dưới `_`, ví dụ `$var1`, `$total_sum`.

- 🟠 **Chữ hoa / chữ thường trong tên biến:**
  - **Nên làm:** Hãy viết tên biến thống nhất một kiểu chữ (ưu tiên chữ thường, ví dụ `$dem`, `$tong`) trong suốt script; không đặt hai biến chỉ khác nhau ở chữ hoa và chữ thường.
  ::: details Vì sao chưa chắc
  Help không nói rõ tên biến có phân biệt chữ hoa và chữ thường hay không (Suy luận: có khả năng không phân biệt hoa thường, vì trong Lịch sử phiên bản của help ghi biến hệ thống là `$_DATE_Y`, còn trong phần Giới thiệu ngôn ngữ của help lại ghi là `$_date_y` — xem mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#ten-bien-co-phan-biet-chu-hoa-va-chu-thuong-khong)).
  :::

- **Giá trị mặc định:** Nếu bạn đọc một biến chưa từng được gán giá trị trước đó, biến sẽ tự động mang giá trị bằng `0`.
- **Hai kiểu dữ liệu chính:**
  - **Kiểu số:** Được chương trình tính toán giá trị khi thực thi. Biến chứa một số hoặc kết quả trả về của hàm số học được coi là kiểu số.
  - **Kiểu chuỗi (văn bản đặt trong cặp dấu ngoặc kép `"..."`):** Không bị chương trình tính toán hay xử lý, ngay cả khi bên trong ngoặc kép có chứa tên biến hay phép tính số học. Biến chứa một chuỗi hoặc kết quả của hàm chuỗi được coi là kiểu chuỗi.

Ví dụ phân biệt chuỗi và biến:

```cms
$count = 0
// Chuỗi "$count = " trong ngoặc kép được giữ nguyên
// Biến $count ở ngoài ngoặc kép được lấy giá trị (0)
PRINT("$count = ", $count)
// Kết quả in ra cửa sổ nhật ký: $count = 0
HALT
```

### Biến khi script tự lặp lại

Khi script chạy hết dòng cuối cùng và tự động quay lại dòng đầu tiên để chạy lượt tiếp theo, **mọi biến vẫn giữ nguyên giá trị của lượt chạy trước**.

::: warning Cẩn thận lỗi đặt lại biến đếm ở đầu script
Nếu bạn đặt dòng `$count = 0` ngay ở đầu một script tự lặp lại, thì sang mỗi lượt lặp mới `$count` lại bị xóa về `0`, khiến dòng `$count = $count + 1` phía dưới không bao giờ tăng quá `1`.
:::

Nếu muốn khởi tạo giá trị ban đầu cho biến ở lần chạy đầu tiên mà không làm mất giá trị ở các vòng lặp tiếp theo, bạn có hai cách:

- **Cách 1:** Không gán `$count = 0` ở đầu script nếu giá trị khởi điểm là `0` (vì biến chưa khai báo tự mang giá trị `0`).
- **Cách 2:** Dùng lệnh [`DEFINE($var, [value])`](/lenh/so#define). Lệnh `DEFINE` chỉ tạo biến và gán giá trị ban đầu nếu biến đó **chưa tồn tại**; từ vòng lặp thứ hai trở đi, vì biến đã tồn tại nên `DEFINE` sẽ bỏ qua không ghi đè:

```cms
// Chỉ gán $dem = 10 ở vòng chạy đầu tiên; các vòng lặp sau giữ nguyên giá trị đang có
DEFINE($dem, 10)
$dem = $dem + 1
PRINT("Gia tri dem: ", $dem)
WAIT(1)
```

*(Lưu ý: biến có giữ giá trị cũ sau khi bạn bấm nút Dừng, bấm Áp dụng hoặc đổi sang tệp script khác hay không hiện chưa được xác minh — xem [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#gia-tri-bien-sau-khi-bam-dung-bam-ap-dung-hoac-doi-script)).*

### Các biến hệ thống hay dùng nhất

Clickermann có sẵn các biến hệ thống bắt đầu bằng `$_` do chương trình tự động cập nhật (bạn chỉ đọc các biến này, **không tự gán giá trị mới cho chúng**). Khi mới học, bạn chỉ cần nhớ 3 nhóm biến phổ biến nhất sau:

- **`$_xmouse`, `$_ymouse`:** Tọa độ `X` và `Y` hiện tại của con trỏ chuột.
- **`$_return1`, `$_return2`:** Nhận kết quả trả về (thường là tọa độ `X` và `Y` vừa tìm thấy) từ các lệnh tìm màu [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if) hoặc tìm ảnh [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if).
- **`$_time_h`, `$_time_m`, `$_time_s`, `$_time_str`:** Giờ, phút, giây và chuỗi thời gian hiện tại của đồng hồ máy tính (dùng khi cần hẹn giờ bấm chuột).

*(Bảng tra cứu toàn bộ biến hệ thống nằm ở [cuối trang này](#bang-bien-he-thong-day-du)).*

## Điều kiện và vòng lặp

Để điều khiển thứ tự chạy linh hoạt thay vì chỉ đi thẳng từ trên xuống dưới, Clickermann cung cấp các cấu trúc khối lệnh (xem cú pháp và ví dụ đầy đủ tại [Điều kiện, vòng lặp, chương trình con](/lenh/cau-truc)):

- **Kiểm tra điều kiện [`IF ... ELSE ... END_IF`](/lenh/cau-truc#if-end-if):** Chỉ chạy khối lệnh bên trong khi điều kiện đúng; nếu sai thì chuyển sang chạy khối sau `ELSE` (nếu có).
- **Vòng lặp đếm số lần [`FOR ... END_CYC`](/lenh/cau-truc#for-end-cyc):** Lặp lại một khối lệnh với số lần xác định trước (ví dụ lặp 5 lần).
- **Vòng lặp chờ điều kiện [`WHILE ... END_CYC`](/lenh/cau-truc#while-end-cyc):** Lặp đi lặp lại khối lệnh chừng nào điều kiện vẫn còn đúng (rất hay dùng để đứng chờ tới đúng giờ hẹn hoặc chờ một màu xuất hiện).

## Các phép toán số học

Bạn có thể viết biểu thức tính toán ở vế phải của phép gán hoặc viết trực tiếp bên trong tham số của hàm/thủ tục. Thứ tự ưu tiên từ cao xuống thấp:

| Phép toán | Ký hiệu | Độ ưu tiên | Ví dụ |
|---|---|---|---|
| Ngoặc tròn ưu tiên | `( )` | 1 (cao nhất) | `$var = (1 + 2) * 2` |
| Nhân | `*` | 2 | `$var = 1 * 2` |
| Chia | `/` | 2 | `$var = 1 / 2` |
| Cộng | `+` | 3 | `$var = 1 + 2` |
| Trừ | `-` | 3 | `$var = 1 - 2` |

## Phép so sánh và phép toán logic

Trong các cấu trúc điều kiện như [`IF`](/lenh/cau-truc#if-end-if) hay [`WHILE`](/lenh/cau-truc#while-end-cyc), biểu thức điều kiện trả về đúng (`1` / khác `0`) hoặc sai (`0`).

### Bảng các phép so sánh

| Ý nghĩa | Ký hiệu trong Clickermann |
|---|---|
| Lớn hơn | `>` |
| Nhỏ hơn | `<` |
| Bằng | `==` hoặc `=` |
| Khác (không bằng) | `!=` hoặc `!` |
| Lớn hơn hoặc bằng | `>=` |
| Nhỏ hơn hoặc bằng | `<=` |

::: tip Phân biệt dấu = khi gán và khi so sánh
Trong Clickermann, dấu `=` đứng ở dòng lệnh thường là **phép gán giá trị** (`$a = 5`), nhưng khi nằm bên trong ngoặc của `IF($a = 5)` hoặc `WHILE($a = 5)` thì nó đóng vai trò là **phép so sánh bằng**. Để tránh nhầm lẫn khi đọc code, bạn có thể viết hai dấu bằng `==` khi so sánh (`IF($a == 5)`).
:::

### Bảng các phép toán logic

Khi cần kết hợp nhiều phép so sánh cùng lúc, hãy bọc từng điều kiện nhỏ trong cặp ngoặc tròn `( )` và nối bằng phép toán logic:

| Phép logic | Ký hiệu | Khi nào trả về Đúng (`1`)? |
|---|---|---|
| **VÀ** (AND) | `AND` hoặc `&` | Khi **cả hai** vế đều đúng |
| **HOẶC** (OR) | `OR` hoặc `\|` | Khi **ít nhất một** trong hai vế đúng |
| **HOẶC LOẠI TRỪ** (XOR) | `XOR` hoặc `^` | Khi **chỉ đúng một** trong hai vế đúng (nếu cả hai cùng đúng hoặc cùng sai thì trả về sai) |

```cms
// Ví dụ kết hợp các phép toán logic
IF((5 > 3) AND (3 > 5))
   PRINT("dung")
ELSE
   PRINT("sai") // in ra "sai" vì 3 > 5 là sai
END_IF

IF((5 > 3) OR (3 > 5))
   PRINT("dung") // in ra "dung" vì 5 > 3 là đúng
ELSE
   PRINT("sai")
END_IF

HALT
```

## Mảng (Arrays)

**Mảng** là tập hợp nhiều biến có chung một tên nhưng phân biệt từng phần tử bằng **chỉ số (index)** đặt trong cặp ngoặc vuông `[ ]`. Chỉ số của mảng luôn **bắt đầu từ `0`**.

```cms
// Gán giá trị cho 3 phần tử của mảng $var
$var[0] = 1
$var[1] = 2
$var[2] = 3

// Tính tổng các phần tử bằng vòng lặp FOR
$result = 0
FOR($i=0, $i < 3)
   $result = $result + $var[$i]
END_CYC

PRINT($result) // Kết quả: 6
HALT
```

Xem thêm các lệnh thao tác mảng chuyên dụng: [`ARRPUSH`](/lenh/so#arrpush), [`ARRPOP`](/lenh/so#arrpop), [`ARRSIZE`](/lenh/so#arrsize), [`ARRSORT`](/lenh/so#arrsort), [`TFREADARR`](/lenh/chuoi-file#tfreadarr), [`SCANPXL`](/lenh/man-hinh#scanpxl).

## Hằng số (Constants)

Hằng số đóng vai trò tương tự biến nhưng có giá trị cố định không thể thay đổi trong lúc chạy và luôn bắt đầu bằng dấu `#` (ví dụ `#TRUE`, `#FALSE`, `#SPACE`, `#ENTER`, `#CTRL`).

Danh sách các hằng số được nạp lúc Clickermann khởi động từ tệp `data/const.txt` trong thư mục chương trình. Xem bảng tra cứu đầy đủ tại [Bảng mã phím và hằng số](/phu-luc/ma-phim).

## Chỉ thị tiền xử lý (Preprocessor Directives)

Các chỉ thị tiền xử lý bắt đầu bằng dấu `#`, chỉ được xử lý một lần duy nhất vào thời điểm nạp script và không tốn thời gian thực thi khi script đang chạy:

| Chỉ thị | Ý nghĩa | Ví dụ |
|---|---|---|
| `#name` | Đặt tên hiển thị cho script trên thanh tiêu đề của chương trình | `#name "Cong cu van phong v1.2"` |
| `#include` | Chèn nội dung của một tệp văn bản/script khác (trong thư mục dự án) vào đúng vị trí đặt chỉ thị | `#include "mylib.cms"` |
| `#logfile` | 🟠 Bật chế độ ghi tệp nhật ký trong thư mục dự án, sao chép toàn bộ nội dung xuất qua `LOGWRITE` / `PRINT` (xem lưu ý ngay bên dưới bảng) | `#logfile "debug.txt"` |
| `#autorun` | Tự động chạy script ngay sau khi tệp `.cms` được mở bằng Clickermann | `#autorun` |
| `#define` | Thay thế một cụm văn bản bằng cụm văn bản khác theo mẫu `#define <tìm>:<thay>` (xem kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#chi-thi-tien-xu-ly-define)) | Suy luận: `#define @pause:WAITMS(100)` |
| `#ps2_keyboard`, `#ps2_mouse` | Chế độ bàn phím và chuột PS/2 (tài liệu này không hướng dẫn phần đó) | |

- 🟠 **Lưu ý về chỉ thị `#logfile`:**
  - **Nên làm:** Khi cần ghi nhật ký ra tệp, hãy viết rõ tên tệp phía sau như `#logfile "debug.txt"` và tìm tệp này trong thư mục dự án (cùng chỗ với tệp `.cms`).
  ::: details Vì sao chưa chắc
  Trong help, phần Giới thiệu ngôn ngữ viết ví dụ `#logfile "debug.txt"` và Lịch sử phiên bản ghi bản v4.13.014 cho phép đặt tên tệp nhật ký tùy ý, còn mục Xuất thông tin (`LOGWRITE`) lại ghi khi có `#logfile` thì chương trình ghi ra tệp `log.txt` trong thư mục dự án. Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#ten-tep-nhat-ky-cua-logwrite-va-chi-thi-logfile).
  :::

## Cách viết số hệ thập lục phân (Hexadecimal)

Ngoài cách viết số nguyên ở hệ thập phân thông thường, bạn có thể viết các số nguyên dương ở hệ thập lục phân (cơ số 16) với tiền tố bắt buộc là `0x`. Ví dụ:

- Số `255` viết là `0xFF`.
- Số `2018` viết là `0x07E2`.

Cách viết này chỉ áp dụng cho các số nguyên dương.

## Bảng biến hệ thống đầy đủ

Bảng dưới đây liệt kê toàn bộ các biến hệ thống (bắt đầu bằng `$_`) trong Clickermann. Nhắc lại: **không tự gán giá trị mới vào các biến hệ thống này**.

| Biến hệ thống | Ý nghĩa |
|---|---|
| `$_xmouse` | Tọa độ hiện tại của con trỏ chuột theo trục X |
| `$_ymouse` | Tọa độ hiện tại của con trỏ chuột theo trục Y |
| `$_xmax` | 🟠 Giá trị tọa độ X lớn nhất cho phép (xem chi tiết bên dưới bảng) |
| `$_ymax` | 🟠 Giá trị tọa độ Y lớn nhất cho phép (xem chi tiết bên dưới bảng) |
| `$_xmin` | 🟠 Giá trị tọa độ X nhỏ nhất cho phép (xem chi tiết bên dưới bảng) |
| `$_ymin` | 🟠 Giá trị tọa độ Y nhỏ nhất cho phép (xem chi tiết bên dưới bảng) |
| `$_return1` | Biến nhận kết quả trả về thứ nhất từ một số lệnh (như `IF_PIXEL_IN` trả X, `CALL` trả kết quả plugin) |
| `$_return2` | Biến nhận kết quả trả về thứ hai từ một số lệnh (như `IF_PIXEL_IN` trả Y) |
| `$_cursor` | Mã số hình dạng hiện tại của con trỏ chuột (mũi tên, bàn tay, con trỏ soạn thảo...) |
| `$_ms` | 🟠 Bộ đếm thời gian tính bằng mili-giây (xem chi tiết bên dưới bảng) |
| `$_time_t` | Thời gian hiện tại theo định dạng Unix timestamp (số giây) |
| `$_time_h` | Giờ hiện tại |
| `$_time_m` | Phút hiện tại |
| `$_time_s` | Giây hiện tại |
| `$_date_y` | Năm hiện tại |
| `$_date_m` | Tháng hiện tại |
| `$_date_d` | Ngày hiện tại trong tháng |
| `$_time_str` | Chuỗi thời gian hiện tại |
| `$_date_str` | Chuỗi ngày tháng hiện tại |
| `$_hwnd` | Mã `hwnd` của phần tử đang khóa hiện tại (bằng `0` nếu không bật chế độ khóa cửa sổ) |
| `$_hwnd_self` | Mã `hwnd` của chính cửa sổ chương trình Clickermann |
| `$_pdir` | Thư mục làm việc hiện tại |
| `$_ver_self` | Phiên bản của chương trình Clickermann |
| `$_ver_sys` | Phiên bản hệ điều hành |
| `$_arch_sys` | Kiến trúc bit của hệ điều hành (32-bit / 64-bit) |
| `$_param_str` | Chuỗi các tham số dòng lệnh khi khởi chạy chương trình, phân cách nhau bằng dấu `;` |
| `$_line` | Số thứ tự dòng lệnh đang thực thi trong script (được nhắc trong Lịch sử phiên bản v3.2 beta và script mẫu đi kèm chương trình; không có trong bảng biến hệ thống của help, chưa rõ còn chạy không) |

- 🟠 **Chi tiết về `$_xmax`, `$_ymax`, `$_xmin`, `$_ymin`:**
  - **Nên làm:** Khi chạy ở chế độ thường, bạn có thể dùng `$_xmax`, `$_ymax` làm giới hạn phải-dưới của màn hình. Khi đang bật khóa cửa sổ, hãy thử `PRINT($_xmin, ", ", $_ymin, " - ", $_xmax, ", ", $_ymax)` ra nhật ký để kiểm tra trước, hoặc truyền trực tiếp kích thước vùng cần quét.
  ::: details Vì sao chưa chắc
  Trong help (phần Giới thiệu ngôn ngữ), cả bốn biến `$_xmax`, `$_ymax`, `$_xmin`, `$_ymin` đều được giải thích là tọa độ lớn nhất và nhỏ nhất cho phép **tính từ cấu hình màn hình desktop**. Trong khi đó, sách của Chô tô (tr. 26) ghi `$_xmax`, `$_ymax` là tọa độ X, Y lớn nhất của cửa sổ và `$_xmin`, `$_ymin` là tọa độ X, Y nhỏ nhất (ở góc trái trên) của cửa sổ. Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#gia-tri-cua-xmax-va-ymax-khi-khoa-cua-so).
  :::

- 🟠 **Chi tiết về biến đếm mili-giây `$_ms`:**
  - **Nên làm:** Chỉ dùng `$_ms` để đo **khoảng thời gian chênh lệch** giữa hai thời điểm trong cùng một lần chạy (ví dụ `$bat_dau = $_ms` rồi lấy `$_ms - $bat_dau`), không phụ thuộc vào giá trị tuyệt đối của `$_ms`.
  ::: details Vì sao chưa chắc
  Theo help (phần Giới thiệu ngôn ngữ), `$_ms` là bộ đếm hệ thống của Windows tính từ lúc khởi động hệ điều hành (Suy luận: Lịch sử phiên bản có sửa lỗi khi máy tính chạy liên tục quá 49 ngày, khớp với bộ đếm mili-giây 32-bit của Windows). Ngược lại, sách của Chô tô (tr. 26) ghi `$_ms` đếm thời gian từ khi Clickermann bắt đầu chạy. Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#goc-thoi-gian-cua-bien-he-thong-ms).
  :::

---

*Nguồn: Tài liệu trợ giúp `help.chm` (phần Giới thiệu ngôn ngữ, Làm việc với số, Cấu trúc lệnh, Xuất thông tin và Lịch sử phiên bản); tham khảo đối chiếu sách của Chô tô (tr. 26).*
