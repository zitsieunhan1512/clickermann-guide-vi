# Ngôn ngữ script

Trang này trình bày toàn bộ các khái niệm nền tảng của ngôn ngữ script trong Clickermann v4.13: cấu trúc dòng lệnh, biến và kiểu dữ liệu, bảng biến hệ thống, phép toán, phép so sánh và logic, mảng, hằng số, chỉ thị tiền xử lý và cách viết số hệ thập lục phân.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Cấu trúc một script

Script trong Clickermann là một dãy các dòng văn bản được thực thi tuần tự từ trên xuống dưới. Mỗi dòng chỉ được chứa tối đa một câu lệnh và thuộc một trong các dạng sau:

- Lời gọi một **thủ tục** (ví dụ `LCLICK(100, 200)`).
- Một **phép gán** giá trị cho biến (ví dụ `$count = $count + 1`).
- Một dòng **chú thích** bắt đầu bằng `//` (chương trình sẽ bỏ qua phần từ sau `//` tới hết dòng).
- Một **chỉ thị tiền xử lý** bắt đầu bằng dấu `#` (ví dụ `#name "Kich ban 1"`).
- Một dòng trống (để phân tách code cho dễ đọc).

Khi chạy xong dòng cuối cùng của script, chương trình sẽ tự động quay lại dòng đầu tiên và chạy lặp lại từ đầu (trừ khi gặp lệnh [`HALT`](/lenh/kich-ban#halt)).

## Biến và kiểu dữ liệu

Tên biến trong Clickermann luôn bắt đầu bằng ký hiệu đô la `$` nối liền với tên định danh gồm các chữ cái Latin `a..z`, chữ số `0..9` và dấu gạch dưới `_`, ví dụ `$var1`, `$total_sum` (theo help, phần Giới thiệu ngôn ngữ).

- 🟠 **Chữ hoa / chữ thường trong tên biến:** Help không nói rõ tên biến có phân biệt chữ hoa và chữ thường hay không (Suy luận: có khả năng không phân biệt hoa thường, vì trong help, Lịch sử phiên bản ghi biến hệ thống là `$_DATE_Y`, còn trong help, phần Giới thiệu ngôn ngữ lại ghi là `$_date_y` — xem mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#ten-bien-co-phan-biet-chu-hoa-va-chu-thuong-khong)).

- **Giá trị mặc định:** Nếu bạn đọc một biến chưa từng được gán giá trị trước đó, biến sẽ tự động mang giá trị bằng `0`.
- **Hai kiểu dữ liệu chính (theo help, phần Giới thiệu ngôn ngữ):**
  - **Kiểu số:** Được chương trình tính toán (xử lý) giá trị khi thực thi. Biến chứa một số hoặc kết quả trả về của hàm số học được coi là kiểu số.
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

## Bảng biến hệ thống

Clickermann cung cấp sẵn các **biến hệ thống** (bắt đầu bằng `$_`) được chương trình tự động cập nhật giá trị khi bạn đọc chúng. **Rất không nên tự gán giá trị mới vào các biến hệ thống này** để tránh gây lỗi (theo help, phần Giới thiệu ngôn ngữ); chỉ dùng chúng để đọc thông tin:

| Biến hệ thống | Ý nghĩa theo help (phần Giới thiệu ngôn ngữ / Lịch sử phiên bản) |
|---|---|
| `$_xmouse` | Tọa độ hiện tại của con trỏ chuột theo trục X |
| `$_ymouse` | Tọa độ hiện tại của con trỏ chuột theo trục Y |
| `$_xmax` | 🟠 Giá trị tọa độ X lớn nhất cho phép (theo help: tính từ cấu hình màn hình desktop; theo sách Chô tô tr. 26: tọa độ lớn nhất của cửa sổ — xem [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#gia-tri-cua-xmax-va-ymax-khi-khoa-cua-so)) |
| `$_ymax` | 🟠 Giá trị tọa độ Y lớn nhất cho phép (tương tự `$_xmax`) |
| `$_xmin` | 🟠 Giá trị tọa độ X nhỏ nhất cho phép (theo help: tính từ cấu hình màn hình desktop; xem kiểm tra cùng `$_xmax` tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#gia-tri-cua-xmax-va-ymax-khi-khoa-cua-so)) |
| `$_ymin` | 🟠 Giá trị tọa độ Y nhỏ nhất cho phép (tương tự `$_xmin`) |
| `$_return1` | Biến nhận kết quả trả về thứ nhất từ một số lệnh (như `IF_PIXEL_IN` trả X, `CALL` trả kết quả plugin) |
| `$_return2` | Biến nhận kết quả trả về thứ hai từ một số lệnh (như `IF_PIXEL_IN` trả Y) |
| `$_cursor` | Mã số hình dạng hiện tại của con trỏ chuột (mũi tên, bàn tay, con trỏ soạn thảo...) |
| `$_ms` | 🟠 Bộ đếm thời gian tính bằng mili-giây (theo help: bộ đếm hệ thống của Windows tính từ lúc khởi động hệ điều hành; theo sách Chô tô tr. 26: đếm từ khi Clickermann chạy; suy luận: lịch sử phiên bản có sửa lỗi "máy chạy quá 49 ngày", khớp với cách nói của help — xem [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#goc-thoi-gian-cua-bien-he-thong-ms)) |
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
| `$_pdir` | Thư mục làm việc hiện tại (theo help, phần Giới thiệu ngôn ngữ) |
| `$_ver_self` | Phiên bản của chương trình Clickermann |
| `$_ver_sys` | Phiên bản hệ điều hành |
| `$_arch_sys` | Kiến trúc bit của hệ điều hành (32-bit / 64-bit) |
| `$_param_str` | Chuỗi các tham số dòng lệnh khi khởi chạy chương trình, phân cách nhau bằng dấu `;` |
| `$_line` | Số thứ tự dòng lệnh đang thực thi trong script (được nhắc trong help, Lịch sử phiên bản v3.2 beta và script mẫu đi kèm tool) |

## Thủ tục và hàm

- **Thủ tục (Procedure):** Là câu lệnh yêu cầu Clickermann thực hiện một hành động (như `LCLICK(100, 200)`, `WAIT(1)`). Thủ tục đứng độc lập trên một dòng và không trả về giá trị trực tiếp tại chỗ gọi.
- **Hàm (Function):** Cũng có tên và các tham số trong ngoặc tròn như thủ tục, nhưng **trả về một giá trị** ngay tại vị trí gọi nó (tương tự như một biến). Bạn có thể gán kết quả của hàm cho biến hoặc truyền thẳng hàm làm tham số bên trong một lệnh khác (ví dụ `WAIT(RND(3, 5))`).

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

Danh sách các hằng số được nạp lúc Clickermann khởi động từ file hằng trong thư mục `data` của tool. Xem bảng tra cứu đầy đủ tại [Bảng mã phím và hằng số](/phu-luc/ma-phim).

## Chỉ thị tiền xử lý (Preprocessor Directives)

Các chỉ thị tiền xử lý bắt đầu bằng dấu `#`, chỉ được xử lý một lần duy nhất vào thời điểm nạp script và không tốn thời gian thực thi khi script đang chạy:

| Chỉ thị | Ý nghĩa | Ví dụ |
|---|---|---|
| `#name` | Đặt tên hiển thị cho script trên thanh tiêu đề của chương trình | `#name "Cong cu van phong v1.2"` |
| `#include` | Chèn nội dung của một tệp văn bản/script khác (trong thư mục dự án) vào đúng vị trí đặt chỉ thị | `#include "mylib.cms"` |
| `#logfile` | 🟠 Bật chế độ ghi tệp nhật ký trong thư mục dự án, sao chép toàn bộ nội dung xuất qua `LOGWRITE` / `PRINT` (help, phần Giới thiệu ngôn ngữ viết ví dụ `#logfile "debug.txt"`, help, Lịch sử phiên bản ghi v4.13.014 cho phép đặt tên tệp nhật ký tùy ý, còn help, mục Xuất thông tin ghi khi có `#logfile` thì ghi ra `log.txt` — xem [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#ten-file-nhat-ky-cua-logwrite-va-chi-thi-logfile)) | `#logfile "debug.txt"` |
| `#autorun` | Tự động chạy script ngay sau khi tệp `.cms` được mở bằng Clickermann | `#autorun` |
| `#define` | Thay thế một cụm văn bản bằng cụm văn bản khác theo mẫu `#define <tìm>:<thay>` (theo help, phần Giới thiệu ngôn ngữ; xem kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#chi-thi-tien-xu-ly-define)) | Suy luận: `#define @pause:WAITMS(100)` |
| `#ps2_keyboard`, `#ps2_mouse` | Chế độ bàn phím và chuột PS/2 (tài liệu này không hướng dẫn phần đó) | |

## Cách viết số hệ thập lục phân (Hexadecimal)

Ngoài cách viết số nguyên ở hệ thập phân thông thường, bạn có thể viết các số nguyên dương ở hệ thập lục phân (cơ số 16) với tiền tố bắt buộc là `0x`. Ví dụ:

- Số `255` viết là `0xFF`.
- Số `2018` viết là `0x07E2`.

Cách viết này chỉ áp dụng cho các số nguyên dương.
