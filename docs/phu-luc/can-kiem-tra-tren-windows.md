# Cần kiểm tra trên Windows

::: info Trang dành cho người có Windows muốn giúp kiểm chứng; người mới không cần đọc
Trang này tổng hợp các điểm có trạng thái `🟠 Chưa thống nhất`, các chi tiết `help.chm` không nói rõ và các kịch bản cần chạy thử thực tế trên máy Windows. Nếu bạn mới học Clickermann, bạn có thể bỏ qua trang này và chỉ cần làm theo dòng gợi ý **"Nên làm"** trên từng trang bài học.
:::

## Tóm tắt các mục cần kiểm chứng

| Mục | Sách của Chô tô | Help chính thức (`help.chm`) | Đánh giá |
|---|---|---|---|
| [`THREAD`](/lenh/cau-truc#thread-end-thread)<br>*(tr. 82)* | Không ghi `init_state` thì luồng đang tắt (`0`), phải bật bằng `SETTHREAD`. | Ví dụ dùng `thread(t1)` không tham số `init_state` và mô tả các luồng cùng chạy ngay. Muốn luồng dừng sẵn lúc đầu thì ví dụ khác viết `thread(t1, 0)`. | **Mâu thuẫn**<br>Suy từ ví dụ của help (help không ghi thẳng giá trị mặc định trong dòng mô tả tham số). |
| [`SETTHREAD`](/lenh/cau-truc#setthread)<br>*(tr. 83)* | Chỉ nêu hai giá trị: `0` tắt luồng, `1` bật luồng. | Có 3 giá trị: `0` tạm dừng; `1` chạy tiếp từ chỗ đã dừng; **`2`** tạm dừng và lần sau chạy lại từ đầu. | **Sách thiếu**<br>"Tắt" trong sách thực chất là tạm dừng. |
| [`$_ms`](/khai-niem/ngon-ngu#bang-bien-he-thong-day-du)<br>*(tr. 26)* | Đếm từ khi Clickermann chạy. | Bộ đếm của Windows, tính từ lúc hệ điều hành khởi động. | **Mâu thuẫn**<br>[Lịch sử phiên bản](/phu-luc/lich-su) có sửa lỗi "máy chạy quá 49 ngày", khớp với cách nói của help (suy luận). |
| [`GETVAR`](/lenh/so#getvar)<br>*(tr. 42)* | Tên biến không cần ngoặc kép. Ví dụ: `define($var, 5)`, `getvar($x)`, `print($x)`. | Tham số là **chuỗi** chứa tên biến, hàm trả về giá trị: `$tmp = getvar($triple_var)` với `$triple_var` mang chuỗi `"$var"`. | **Ví dụ sách sai**<br>Khai báo `$var` nhưng đọc `$x`, và bỏ qua giá trị trả về của hàm. |
| [`SETVAR`](/lenh/so#setvar)<br>*(tr. 42)* | Ví dụ: `define($var)` rồi `setvar("$x", 5)`. | Biến có tên đã cho phải tồn tại trước khi gọi. | **Ví dụ lệch**<br>Dấu ngoặc kép thì đúng, nhưng khai báo nhầm biến. |
| [`SCREENSHOT`, `SCREENSHOTEX`](/lenh/man-hinh#screenshotex)<br>*(tr. 94)* | Lưu vào thư mục `screen`; ở `SCREENSHOT` nói lưu dạng jpeg; ở `SCREENSHOTEX` nói lưu dạng bmp dù cũng liệt kê `format` 1 là jpeg. | Lưu vào thư mục `screens`; `SCREENSHOT` lưu `.bmp`; ở `SCREENSHOTEX` thì `format` `0` là bmp, `1` là jpeg nhưng phần ghi chú chỉ ghi tên dạng `pref0000.bmp`, không nói rõ đuôi tệp khi `format = 1`. | **Khác tên thư mục & cần thử đuôi tệp** |
| [`$_xmax`, `$_ymax`, `$_xmin`, `$_ymin`](/khai-niem/toa-do#cac-bien-he-thong-gioi-han-toa-do-xmax-ymax-xmin-ymin)<br>*(tr. 26)* | `$_xmax`, `$_ymax`: tọa độ lớn nhất của cửa sổ; `$_xmin`, `$_ymin`: tọa độ nhỏ nhất (góc trái trên) của cửa sổ. | Tính từ cấu hình màn hình desktop. | **Cần thử**<br>Có thể khác nhau khi đang khóa vào cửa sổ. |
| [`CALL`](/lenh/kich-ban#call)<br>*(tr. 104)* | DLL để cùng thư mục tệp script. | Trang `CALL` (mục Script và plugin) ghi `%Clickermann%/plugins`; bài [Plugin](/khai-niem/plugin) ghi cạnh script hoặc thư mục con trong thư mục dự án, không tìm thấy thì âm thầm kết thúc. | **Help tự mâu thuẫn**<br>Sách khớp bài Plugin. |
| [`WNDSETINFO`](/lenh/winapi#wndsetinfo)<br>*(tr. 117)* | Truyền số trực tiếp. | Ví dụ chỉ truyền biến. | **Cần thử**<br>Không hẳn mâu thuẫn. |
| [Trình duyệt, máy ảo](/khai-niem/khoa-cua-so#gioi-han-va-giai-phap-dung-may-ao)<br>*(tr. 19)* | Thuộc loại cửa sổ không nhận Clickermann. | Khung Flash trong trình duyệt là một phần tử con riêng, khóa được hay không tùy cách ứng dụng được viết. Với máy ảo, help gợi ý cài Clickermann bên trong máy ảo. | **Sách nói quá chung** |
| [`SUB` trong `#include`](/lenh/cau-truc#sub-end-sub)<br>*(tr. 81)* | Khuyên hạn chế để `SUB` ở tệp ngoài rồi `#include` vì đôi lúc bị lỗi. | Mục Cấu trúc lệnh ghi việc tách phần thân các chương trình con ra tệp riêng bên ngoài rồi nạp qua `#include` được coi là thói quen tốt. | **Mâu thuẫn**<br>Cần thử gọi `SUB` đặt trong tệp `#include`. |
| [`LOGWRITE` và `#logfile`](/lenh/nhat-ky#logwrite-print) | — | Mục Xuất thông tin ghi khi có `#logfile` thì ghi thêm vào `%thu_muc_du_an%/log.txt`; phần Giới thiệu ngôn ngữ và Lịch sử phiên bản cho phép đặt tên tùy ý như `#logfile "debug.txt"`. | **Help chưa thống nhất**<br>Cần thử `#logfile` không kèm tên tệp có ghi ra `log.txt` không. |
| [`ROUND`](/lenh/so#round) | — | Mục Làm việc với số ghi "làm tròn theo hướng ra xa số 0" rồi giải thích `prec = 2` là hàng trăm, `prec = -2` là hàng phần trăm, theo quy tắc chuẩn `0.5`. | **🟠 Chưa thống nhất**<br>Kiểm tra `ROUND(-1.5, 0)` ra `-2` hay `-1`. |
| [`READMEM`, `WRITEMEM` (`addr`)](/lenh/kich-ban#readmem) | — | Mục Script và plugin: dòng tham số của `READMEM` ghi `addr` là chuỗi; phần ghi chú của cả hai lệnh lại ghi `addr` là số nguyên thông thường ở dạng thập phân hoặc thập lục phân. | **Help tự mâu thuẫn**<br>Chỉ ghi nhận mâu thuẫn tài liệu, không viết script kiểm tra. |
| [`GETMESSAGE`](/lenh/winapi#getmessage) | — | Ví dụ ở mục WinAPI gọi `POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng một lượt chạy và không có `HALT`. | **Cần thử**<br>`POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng lượt có nhận được không. |
| [`FOR` lồng nhau và dùng lại biến đếm](/lenh/cau-truc#for-end-cyc) | — | Mục Cấu trúc lệnh nói biến giữ giá trị nếu không gán `=value`, nhưng ví dụ vòng lặp lồng nhau và ví dụ `SUB` viết `FOR($x, $x < 3)`, `FOR($y, $y < 3)`, `FOR($i, $i < 3)` không có `=0`. | **🟠 Chưa thống nhất**<br>Kiểm tra số dòng in ra khi không gán `=0`. |
| [Mã phím `PrintScreen` (`154` và `44`)](/phu-luc/ma-phim#bang-ma-phim-chuot-va-phim-dieu-khien) | — | Bảng mã phím trong help và tệp `data/const.txt` đều ghi `#PRINTSCREEN` là `154` (`0x9A`), trong khi mã `VK_SNAPSHOT` chuẩn của Windows thường là `44` (`0x2C`). | **🟠 Cần thử**<br>Kiểm tra `ISKEYDOWN(154)` và `ISKEYDOWN(44)`. |
| [Quy luật mã `KEYDOWN`](/phu-luc/ma-phim#khi-keydown-can-ma-khac) | — | Help dùng chung một bảng mã phím cho `KEYPRESS`, `KEYDOWN`, `KEYUP`; bảng tự dò của Mai Bảo Long ghi nhận `KEYDOWN`/`KEYUP` cần mã có mã quét bằng mã phím đích (ví dụ `KEYDOWN(75)` ra mũi tên trái `37`). | **🟠 Cần thử**<br>Kiểm tra `KEYDOWN(75)` trên Notepad ở cả chế độ thường và khóa cửa sổ. |
| [Cách tắt khóa cửa sổ (`HSET` và `Alt + W`)](/khai-niem/khoa-cua-so#tat-khoa-cua-so) | — | Mục `HSET` ghi `HSET(hwnd, state)` với `state = 0` là tắt khóa cửa sổ; không nói rõ `HSET(0, 0)` hay nhấn `Alt + W` lần nữa có tắt được không. | **Cần thử**<br>Kiểm tra `HSET($_hwnd, 0)`, `HSET(0, 0)` và `Alt + W`. |
| [Tên biến hoa / thường](/khai-niem/ngon-ngu#bien-va-kieu-du-lieu) | — | Help không nói rõ; Lịch sử phiên bản ghi `$_DATE_Y`, còn phần Giới thiệu ngôn ngữ ghi `$_date_y`. | **Help không nói rõ**<br>Cần thử `$Var` và `$var`. |
| [Khung chế độ chạy](/bat-dau/man-hinh-chinh#bang-thong-tin-va-che-do-chay) | — | Bài Màn hình chính nói có khung trên cửa sổ chính; Lịch sử phiên bản (v4.7.000) nói đã bỏ khỏi cửa sổ chính và (v4.7.000 SE) nói trở lại dạng cửa sổ riêng. | **Help tự mâu thuẫn**<br>Cần mở giao diện v4.13.014 để kiểm tra. |
| [Chỉ thị `#define`](/khai-niem/ngon-ngu#chi-thi-tien-xu-ly-preprocessor-directives) | — | Phần Giới thiệu ngôn ngữ chỉ ghi mẫu `#define <tìm>:<thay>`, không có ví dụ cụ thể. | **Cần thử**<br>Kiểm tra ví dụ `#define @pause:WAITMS(100)`. |
| [Nơi lưu ảnh `Alt + G`](/cam-nang/tim-anh#buoc-1-chuan-bi-tep-anh-mau-bmp) | — | Bài Trình soạn thảo chỉ nói ảnh `100×100` được lưu dạng `.bmp`, không nói rõ lưu ở thư mục nào. | **Help không nói rõ**<br>Cần nhấn `Alt + G` để xem thư mục lưu. |
| [Kéo chuột vẽ trong Paint](/cam-nang/tu-ve) | — | Ví dụ kéo thả ở mục Chuột chỉ có `ldown(10, 10)`, `waitms(300)`, `lup(20, 20)` (không có `MOVE`). | **Suy luận cần thử**<br>Kiểm tra `LDOWN` -> `MOVE` -> `LUP` trong Paint. |
| [Hành vi thực tế cho người mới](#gia-tri-bien-sau-khi-bam-dung-bam-ap-dung-hoac-doi-script) | — | Giá trị biến sau khi Dừng/Áp dụng, đường dẫn khi chưa `Ctrl + S`, tệp chưa tồn tại (`TFCOUNT`/`TFWRITE`/`INIREAD`), mảng gọi lặp (`SCANPXL`/`SCANPICTURE`/`TFREADARR`), `Alt + Q`, ngoặc rỗng & chữ thường, giao diện & UTF-8, thu phóng màn hình Windows. | **Cần thử thực tế** |
| [Các tình huống cẩm nang](/cam-nang/click-theo-lich) | — | Các trang trong `cam-nang/*` được biên soạn theo cú pháp help nhưng chưa chạy trên máy Windows. | **Cần thử thực tế** |
| [Thư viện cộng đồng `alt_winmode`](/nang-cao/alt-winmode) | — | Kiểm tra `A_DRAG` và `A_MOVE` khi kéo vẽ trong Paint; `A_IFPIXELIN` khi màu nằm ở cột `0`; `A_SCANPXL` gọi hai lần liên tiếp; `A_PXL` khi cửa sổ bị che khuất. | **Cần thử thực tế** |

---

## Trạng thái mặc định của THREAD khi bỏ qua init_state

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread)

### Hai cách hiểu hiện tại

1. **Theo ví dụ trong help:** Ở mục Cấu trúc lệnh, phần `THREAD ... END_THREAD` đưa ra ví dụ khai báo `thread(t1)` và `thread(t2)` mà không truyền `init_state`, kèm lời giải thích rằng cả 3 luồng (script chính và 2 luồng con) đều chạy đồng thời và in thông báo theo nhịp riêng. Sang mục `SETTHREAD`, để minh họa một luồng đang dừng sẵn, help mới viết rõ `thread(t1, 0)`. Từ đó suy ra khi bỏ trống `init_state`, giá trị mặc định là `1` (chạy ngay).
2. **Theo sách của Chô tô (tr. 82):** Sách ghi rằng nếu không truyền `init_state` thì chương trình hiểu là luồng đang tắt (`0`), chưa chạy và cần gọi `SETTHREAD(ten_luong, 1)` mới bắt đầu chạy.

### Script kiểm tra trên Windows

Lưu ý khi viết script kiểm tra: không gán `$da_chay = 0` ở script chính vì nếu luồng chạy ngay và đặt `$da_chay = 1` trước, dòng gán ở script chính có thể ghi đè lại thành `0` dẫn tới kết luận ngược (biến chưa từng được gán sẽ tự động đọc ra `0`). Trong thân luồng cũng dùng vòng chờ ngắn đặt lại cờ thay vì `WAIT(10)`:

```cms
// Kiểm tra trạng thái mặc định của THREAD khi không truyền init_state
LOGSHOW(1)
LOGWRITE("Bat dau kiem tra THREAD khong truyen init_state...")

// Khai báo luồng KHÔNG có tham số init_state
// Không gán $da_chay = 0 ở script chính để tránh ghi đè cờ của luồng
THREAD(luong_thu)
   $da_chay = 1
   WAITMS(100)
END_THREAD

// Chờ 1 giây ở script chính mà không gọi SETTHREAD
WAIT(1)
SETTHREAD(luong_thu, 0)

IF($da_chay = 1)
   LOGWRITE("KET LUAN: Mac dinh init_state = 1 (luong tu chay ngay, khop voi vi du trong help).")
ELSE
   LOGWRITE("KET LUAN: Mac dinh init_state = 0 (luong dang tat, khop voi sach Cho to, tr. 82).")
END_IF

HALT
```

---

## Các giá trị state của SETTHREAD

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`SETTHREAD`](/lenh/cau-truc#setthread)

### Hai cách hiểu hiện tại

1. **Theo help chính thức:** Tham số `state` của `SETTHREAD(thread_name, state)` có 3 giá trị:
   - `0`: Tạm dừng luồng tại vị trí hiện tại; khi gọi lại `SETTHREAD(thread_name, 1)`, luồng chạy tiếp từ câu lệnh ngay sau chỗ vừa dừng.
   - `1`: Gỡ tạm dừng để luồng chạy tiếp.
   - `2`: Tạm dừng luồng và đặt lại vị trí về đầu luồng; khi gọi lại `SETTHREAD(thread_name, 1)`, luồng sẽ chạy lại từ câu lệnh đầu tiên trong thân `THREAD`.
2. **Theo sách của Chô tô (tr. 83):** Chỉ liệt kê `0` là tắt luồng và `1` là bật luồng (không đề cập giá trị `2` và không phân biệt giữa tạm dừng giữ vị trí với dừng và quay lại từ đầu).

### Script kiểm tra trên Windows

Đoạn script dưới đây kiểm tra sự khác biệt giữa `SETTHREAD(..., 0)` và `SETTHREAD(..., 2)` khi luồng đang chạy dở ở giữa thân luồng:

```cms
// Kiểm tra sự khác nhau giữa state = 0 và state = 2 của SETTHREAD
LOGCLEAR
LOGSHOW(1)
LOGWRITE("=== Kiem tra SETTHREAD state 0 va state 2 ===")

THREAD(luong_dem, 0)
   LOGWRITE("Luong: Buoc 1 (dau luong)")
   WAIT(2)
   LOGWRITE("Luong: Buoc 2 (giua luong)")
   WAIT(2)
   LOGWRITE("Luong: Buoc 3 (cuoi luong)")
   WAIT(10)
END_THREAD

// --- Phần A: Kiểm tra state = 0 (tạm dừng rồi chạy tiếp) ---
LOGWRITE("[Phan A] Bat luong (state = 1), cho 1 giay roi tam dung bang state = 0")
SETTHREAD(luong_dem, 1)
WAIT(1)

// Luồng vừa in xong Bước 1 và đang chờ ở WAIT(2) đầu tiên
SETTHREAD(luong_dem, 0)
LOGWRITE("[Phan A] Da goi SETTHREAD(luong_dem, 0). Cho 2 giay...")
WAIT(2)

LOGWRITE("[Phan A] Goi SETTHREAD(luong_dem, 1) -> Ky vong in tiep 'Luong: Buoc 2 (giua luong)':")
SETTHREAD(luong_dem, 1)
WAIT(2)

// --- Phần B: Kiểm tra state = 2 (tạm dừng và đặt lại về đầu luồng) ---
LOGWRITE("[Phan B] Goi SETTHREAD(luong_dem, 2) de tam dung va dat lai ve dau luong")
SETTHREAD(luong_dem, 2)
WAIT(2)

LOGWRITE("[Phan B] Goi SETTHREAD(luong_dem, 1) -> Ky vong in lai 'Luong: Buoc 1 (dau luong)':")
SETTHREAD(luong_dem, 1)
WAIT(2)

SETTHREAD(luong_dem, 0)
LOGWRITE("=== Ket thuc kiem tra ===")
HALT
```

---

## Gốc thời gian của biến hệ thống $_ms

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#bang-bien-he-thong-day-du)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (phần Giới thiệu ngôn ngữ):** `$_ms` là bộ đếm thời gian hệ thống của Windows, đếm số mili-giây tính từ **thời điểm hệ điều hành Windows khởi động**. Trong [Lịch sử phiên bản](/phu-luc/lich-su) v4.13.014 cũng có ghi nhận sửa lỗi sập khi hệ thống chạy quá 49 ngày không khởi động lại (Suy luận theo kiến thức Windows: bộ đếm mili-giây 32-bit không dấu của Windows tràn sau `2^32` ms ≈ 49,7 ngày).
2. **Theo sách của Chô tô (tr. 26):** Ghi rằng `$_ms` đếm thời gian tính từ **lúc chương trình Clickermann bắt đầu chạy**.

### Script kiểm tra trên Windows

Để kết quả không bị nhập nhằng do thời gian mở lại chương trình, bạn hãy thực hiện đúng các bước sau:

1. Lưu tệp script vào một thư mục dự án riêng.
2. **Để cửa sổ Clickermann mở sẵn ít nhất 5 phút** (`300 000` ms) trước khi bấm chạy **Lần 1** (để giá trị `$_ms` ở Lần 1 chắc chắn lớn hơn `300 000`).
3. Ngay sau khi Lần 1 chạy xong, **đóng hẳn chương trình Clickermann, mở lại ngay và bấm chạy Lần 2 trong vòng 30 giây** (`30 000` ms). *(Lưu ý: tham số giá trị của `INIWRITE` là kiểu chuỗi nên script dùng `STRCONCAT("", $ms_hien_tai)` và `"0"`).*

```cms
// Kiểm tra gốc thời gian của $_ms bằng cách đóng và mở lại Clickermann
// Chuẩn bị: để Clickermann mở ít nhất 5 phút trước khi chạy Lần 1;
// sau đó đóng hẳn, mở lại và chạy Lần 2 trong vòng 30 giây.
LOGCLEAR
LOGSHOW(1)

$ms_hien_tai = $_ms
$ms_lan_truoc = INT(INIREAD("kiemtra_ms.ini", "ms_lan_1", "TEST"))

IF($ms_lan_truoc = 0)
   INIWRITE("kiemtra_ms.ini", "ms_lan_1", STRCONCAT("", $ms_hien_tai), "TEST")
   LOGWRITE("Lan chay 1 -> Da luu $_ms = ", $ms_hien_tai, " ms.")
   LOGWRITE("Neu Clickermann da mo du 5 phut (> 300000 ms), hay DONG HAN Clickermann, mo lai va chay lan 2 trong vong 30 giay!")
ELSE
   LOGWRITE("Lan chay 1 (truoc khi dong Clickermann): ", $ms_lan_truoc, " ms")
   LOGWRITE("Lan chay 2 (sau khi mo lai Clickermann): ", $ms_hien_tai, " ms")
   // Xóa giá trị cũ về "0" để có thể thử lại từ đầu nếu cần
   INIWRITE("kiemtra_ms.ini", "ms_lan_1", "0", "TEST")
   IF($ms_hien_tai > $ms_lan_truoc)
      LOGWRITE("KET LUAN: $_ms tiep tuc tang sau khi mo lai Clickermann -> Tinh tu luc Windows khoi dong (khop voi help).")
   ELSE
      IF($ms_hien_tai < 60000)
         LOGWRITE("KET LUAN: $_ms quay ve so nho (< 60000 ms) sau khi mo lai -> Tinh tu luc Clickermann chay (khop voi sach Cho to, tr. 26).")
      ELSE
         LOGWRITE("Chua du dieu kien ket luan: hay dam bao Clickermann mo it nhat 5 phut truoc Lan 1 va chay Lan 2 trong vong 30 giay sau khi mo lai.")
      END_IF
   END_IF
END_IF

HALT
```

---

## Cách truyền tham số và giá trị trả về của GETVAR

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`GETVAR`](/lenh/so#getvar)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục Làm việc với số):** `GETVAR($var)` là một **hàm** nhận tham số là **chuỗi chứa tên biến** (ví dụ `"$goc"`) và trả về giá trị của biến đó. Biến được đọc phải tồn tại tại thời điểm gọi hàm.
2. **Theo sách của Chô tô (tr. 42):** Sách ghi tên biến không cần dấu ngoặc kép và viết ví dụ `define($var, 5)`, `getvar($x)`, `print($x)` (vừa khai báo lệch tên biến, vừa không hứng giá trị trả về của hàm).

### Script kiểm tra trên Windows

Đoạn script dưới đây thử cả hai cách (truyền chuỗi tên biến `"$goc"` theo help và truyền trực tiếp biến `$goc` không ngoặc kép theo sách).

*(Lưu ý: khi gọi `GETVAR($goc)` ở Cách 2, giá trị của `$goc` là `42` nên nếu Clickermann tìm biến tên `"42"` không tồn tại và **báo lỗi dừng script ngay tại dòng đó**, thì việc báo lỗi dừng script đó cũng chính là kết quả kiểm chứng cho thấy Cách 2 không hợp lệ).*

```cms
// Kiểm tra GETVAR theo cách của help (chuỗi tên biến) và cách của sách (biến không ngoặc kép)
LOGCLEAR
LOGSHOW(1)

$goc = 42
$ten_bien = "$goc"

// Cách 1 (theo help): truyền chuỗi chứa tên biến "$goc"
$ket_qua = GETVAR($ten_bien)
LOGWRITE("Cach 1 - GETVAR truyen chuoi ten bien: ", $ket_qua)

// Cách 2 (theo sách tr. 42): truyền trực tiếp biến $goc không ngoặc kép
// (Nếu dòng dưới báo lỗi dừng script thì chứng tỏ Cách 2 sai cú pháp)
$r2 = GETVAR($goc)
LOGWRITE("Cach 2 - GETVAR($goc) khong ngoac kep: ", $r2)

IF(($ket_qua = 42) & ($r2 != 42))
   LOGWRITE("KET LUAN: GETVAR nhan chuoi chua ten bien (khop voi help).")
ELSE
   IF($r2 = 42)
      LOGWRITE("KET LUAN: GETVAR($goc) khong ngoac kep cung tra ve 42 (khop voi sach).")
   ELSE
      LOGWRITE("KET LUAN KHAC: ket_qua=", $ket_qua, ", r2=", $r2)
   END_IF
END_IF

HALT
```

---

## SETVAR khi biến chưa tồn tại trước khi gọi

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`SETVAR`](/lenh/so#setvar)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục Làm việc với số):** Ghi chú của `SETVAR` nêu rõ biến có tên được truyền vào **phải tồn tại trước** thời điểm gọi `SETVAR`.
2. **Theo sách của Chô tô (tr. 42):** Ví dụ của sách lại viết `define($var)` rồi gọi `setvar("$x", 5)` (tức biến `$x` chưa từng được khai báo trước khi gọi `SETVAR`).

### Script kiểm tra trên Windows

*(Lưu ý: nếu dòng `SETVAR("$chua_co", 55)` làm Clickermann hiện thông báo lỗi và dừng script ngay vì biến `$chua_co` chưa tồn tại, thì việc dừng báo lỗi đó cũng chính là kết quả xác nhận ghi chú trong help).*

```cms
// Kiểm tra SETVAR với biến đã tồn tại và biến chưa tồn tại
LOGCLEAR
LOGSHOW(1)

// Trường hợp 1: Biến đã tồn tại trước (đúng theo help)
$da_co = 10
SETVAR("$da_co", 99)
LOGWRITE("Bien da ton tai sau SETVAR (ky vong 99): ", $da_co)

// Trường hợp 2: Biến chưa tồn tại trước khi gọi SETVAR
SETVAR("$chua_co", 55)
LOGWRITE("Bien chua khai bao truoc khi goi SETVAR: ", $chua_co)

IF($chua_co = 55)
   LOGWRITE("KET LUAN: SETVAR tu tao bien moi ngay ca khi bien chua ton tai truoc do.")
ELSE
   LOGWRITE("KET LUAN: Bien bat buoc phai ton tai truoc khi goi SETVAR (khop voi ghi chu trong help).")
END_IF

HALT
```

---

## Thư mục lưu ảnh của SCREENSHOTEX

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`SCREENSHOT`](/lenh/man-hinh#screenshot), [`SCREENSHOTEX`](/lenh/man-hinh#screenshotex)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục Màn hình):** Cả `SCREENSHOT` và `SCREENSHOTEX` đều lưu ảnh vào thư mục con `screens` (có chữ `s` ở cuối) bên trong thư mục của script hiện tại. `SCREENSHOT` lưu ảnh dạng `.bmp`. Với `SCREENSHOTEX`, tham số `format` bằng `0` là BMP, bằng `1` là JPEG; tuy nhiên ở phần ghi chú, help chỉ ghi tên tệp dạng `pref0000.bmp`, không nói rõ đuôi tệp khi `format = 1`.
2. **Theo sách của Chô tô (tr. 94):** Ghi tên thư mục lưu ảnh của cả `SCREENSHOT` và `SCREENSHOTEX` là `screen` (không có chữ `s`); ở `SCREENSHOT` sách ghi ảnh lưu định dạng `jpeg`, còn ở `SCREENSHOTEX` phần lời mô tả nói ảnh lưu dạng `.bmp` dù vẫn liệt kê `format = 1` là JPEG.

### Script kiểm tra trên Windows

Lưu script dưới đây vào một thư mục dự án trống rồi chạy để kiểm tra xem `SCREENSHOT` và `SCREENSHOTEX` tạo thư mục `screens` hay `screen`, cũng như kiểm tra đuôi tệp thực tế được tạo ra:

```cms
// Kiểm tra thư mục và đuôi tệp tạo bởi SCREENSHOT và SCREENSHOTEX
LOGCLEAR
LOGSHOW(1)

GETSCREEN
// 1. Gọi SCREENSHOT
SCREENSHOT("kiemtra_shot_")

// 2. Gọi SCREENSHOTEX với format = 0 (BMP) và format = 1 (JPEG)
SCREENSHOTEX(0, 0, 50, 50, "kiemtra_ex_bmp_", 0)
SCREENSHOTEX(0, 0, 50, 50, "kiemtra_ex_jpeg_", 1)

GETFILELIST($ds_screens, "screens\*.*")
GETFILELIST($ds_screen, "screen\*.*")

LOGWRITE("So tep trong thu muc screens\: ", ARRSIZE($ds_screens))
FOR($i=0, $i < ARRSIZE($ds_screens))
   LOGWRITE(" - screens: ", $ds_screens[$i])
END_CYC

LOGWRITE("So tep trong thu muc screen\: ", ARRSIZE($ds_screen))
FOR($j=0, $j < ARRSIZE($ds_screen))
   LOGWRITE(" - screen: ", $ds_screen[$j])
END_CYC

IF(ARRSIZE($ds_screens) > 0)
   LOGWRITE("KET LUAN: Anh chup duoc luu vao thu muc screens (co chu s, khop voi help).")
END_IF
IF(ARRSIZE($ds_screen) > 0)
   LOGWRITE("KET LUAN: Anh chup duoc luu vao thu muc screen (khong co chu s, khop voi sach tr. 94).")
END_IF

HALT
```

---

## Giá trị của $_xmax và $_ymax khi khóa cửa sổ

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Hệ tọa độ màn hình và phần tử](/khai-niem/toa-do#cac-bien-he-thong-gioi-han-toa-do-xmax-ymax-xmin-ymin), [Ngôn ngữ script](/khai-niem/ngon-ngu#bang-bien-he-thong-day-du)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (phần Giới thiệu ngôn ngữ):** Bảng biến hệ thống mô tả cả 4 biến `$_xmax`, `$_ymax`, `$_xmin`, `$_ymin` là giá trị tọa độ X, Y lớn nhất và nhỏ nhất cho phép, được **tính từ cấu hình màn hình desktop**.
2. **Theo sách của Chô tô (tr. 26):** Ghi rằng `$_xmax` và `$_ymax` là **tọa độ lớn nhất của cửa sổ**, còn `$_xmin` và `$_ymin` là **tọa độ X, Y nhỏ nhất (ở góc trái trên) của cửa sổ**.

### Script kiểm tra trên Windows

Mở một cửa sổ Notepad nhỏ, đặt ở vị trí lệch khỏi góc trái trên màn hình (ví dụ đặt tại `(120, 120)` với kích thước `400×300`), sau đó chạy script dưới đây để so sánh cả 4 biến `$_xmin`, `$_ymin`, `$_xmax`, `$_ymax` trước và sau khi bật chế độ khóa cửa sổ bằng `HSET`:

```cms
// Kiểm tra $_xmin, $_ymin, $_xmax, $_ymax khi tắt và khi bật chế độ khóa cửa sổ
LOGCLEAR
LOGSHOW(1)

// 1. Khi chưa khóa cửa sổ (chế độ thường)
$xmin_thuong = $_xmin
$ymin_thuong = $_ymin
$xmax_thuong = $_xmax
$ymax_thuong = $_ymax
LOGWRITE("Che do thuong -> $_xmin=", $_xmin, ", $_ymin=", $_ymin, ", $_xmax=", $_xmax, ", $_ymax=", $_ymax)

// 2. Tìm cửa sổ Notepad, đặt vị trí (120, 120), kích thước 400x300 và khóa vào cửa sổ đó
$h = WNDFIND("Notepad")
IF($h > 0)
   WNDPOS($h, 120, 120)
   WNDSIZE($h, 400, 300)
   WAITMS(300)
   HSET($h, 1)
   LOGWRITE("Khi khoa cua so Notepad (tai 120,120 - 400x300) -> $_xmin=", $_xmin, ", $_ymin=", $_ymin, ", $_xmax=", $_xmax, ", $_ymax=", $_ymax)
   IF(($_xmin = $xmin_thuong) & ($_ymin = $ymin_thuong) & ($_xmax = $xmax_thuong) & ($_ymax = $ymax_thuong))
      LOGWRITE("KET LUAN: $_xmin, $_ymin, $_xmax, $_ymax giu nguyen theo man hinh desktop (khop voi help).")
   ELSE
      LOGWRITE("KET LUAN: Cac bien gioi han toa do thay doi theo cua so dang khoa (khop voi sach tr. 26).")
   END_IF
   HSET($h, 0)
ELSE
   LOGWRITE("Hay mo cua so Notepad truoc khi chay script nay.")
END_IF

HALT
```

---

## Thư mục nạp plugin DLL của CALL

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`CALL`](/lenh/kich-ban#call) · **Trang khái niệm:** [Plugin mở rộng](/khai-niem/plugin)

### Ba nguồn thông tin hiện tại

1. **Theo trang lệnh `CALL` (mục Script và plugin):** Đường dẫn tệp `filename` trong `CALL("filename", ...)` được tính tương đối từ thư mục `%Clickermann%/plugins`.
2. **Theo bài viết Plugin (bài Plugin):** Tệp DLL của plugin đặt trong thư mục dự án (nằm cạnh tệp script đang chạy hoặc trong thư mục con của dự án); nếu không tìm thấy tệp theo tên đã cho ở đó thì lệnh `CALL` âm thầm kết thúc.
3. **Theo sách của Chô tô (tr. 104):** Chỉ ghi rằng tệp DLL đặt cùng thư mục với tệp script.

### Script kiểm tra trên Windows

Lưu ý: người kiểm tra cần tự chuẩn bị trước một tệp plugin `plugin_test.dll` xuất hàm `int execute(int* _arr, int _size)` trả về `_arr[0] * 2` (tức nhân đôi phần tử đầu tiên của mảng tham số `_arr`). Không gán giá trị trực tiếp vào biến hệ thống `$_return1` vì help khuyến cáo rất không nên gán vào biến hệ thống.

Hãy thử lần lượt **3 vị trí** dưới đây. **Quan trọng: trước khi thử vị trí tiếp theo, hãy xóa bản sao `plugin_test.dll` ở vị trí vừa thử trước đó** để tránh nhận nhầm kết quả từ vị trí cũ:

- **Lần 1:** Chỉ đặt `plugin_test.dll` trong thư mục `%Clickermann%/plugins/` rồi chạy script (gọi `CALL("plugin_test.dll", ...)`).
- **Lần 2:** Xóa tệp ở `%Clickermann%/plugins/`, đặt `plugin_test.dll` ngay trong **thư mục dự án** (cùng chỗ với tệp `.cms`) rồi chạy lại script.
- **Lần 3:** Xóa tệp ở thư mục dự án, tạo một **thư mục con** bên trong thư mục dự án (ví dụ ` plugins_con\plugin_test.dll`) rồi thử cả `CALL("plugin_test.dll", ...)` lẫn `CALL("plugins_con\plugin_test.dll", ...)`. *(Nếu khi không tìm thấy tệp DLL mà Clickermann hiện hộp thoại báo lỗi dừng script thay vì âm thầm kết thúc, hãy ghi nhận luôn hành vi đó).*

```cms
// Kiểm tra vị trí nạp tệp DLL của lệnh CALL
// Yêu cầu: chuẩn bị plugin_test.dll trả về (_arr[0] * 2) và xóa bản sao ở vị trí cũ trước mỗi lần thử
LOGCLEAR
LOGSHOW(1)

$so_ngau_nhien = RND(10, 99)
$ky_vong = $so_ngau_nhien * 2

CALL("plugin_test.dll", $so_ngau_nhien)
LOGWRITE("Tham so truyen vao: ", $so_ngau_nhien, " | Ky vong $_return1 = ", $ky_vong)
LOGWRITE("Gia tri $_return1 thuc te: ", $_return1)

IF($_return1 = $ky_vong)
   LOGWRITE("KET LUAN: CALL da nap va chay thanh cong plugin_test.dll tai vi tri dat tep hien tai!")
ELSE
   LOGWRITE("KET LUAN: CALL khong tim thay plugin_test.dll o vi tri hien tai (am tham ket thuc).")
END_IF

HALT
```

---

## Truyền số trực tiếp vào WNDSETINFO

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`WNDSETINFO`](/lenh/winapi#wndsetinfo)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục WinAPI):** Cú pháp ghi `WNDSETINFO(hwnd, $var1, $var2, $var3, $var4)` và ví dụ trong help chỉ truyền 4 biến vào lệnh.
2. **Theo sách của Chô tô (tr. 117):** Có thể truyền trực tiếp các con số hằng vào 4 tham số vị trí và kích thước của `WNDSETINFO`.

Gợi ý: script thực tế của người biên soạn có dùng cách này (dạng `WNDSETINFO($h, 0, 0, $w, $h2)`) và báo chạy tốt, chưa kiểm chứng lại. Vẫn cần chạy script dưới đây.

### Script kiểm tra trên Windows

Mở sẵn một cửa sổ Notepad trên Windows rồi chạy script dưới đây. Để tránh trường hợp cửa sổ Notepad tình cờ đang nằm sẵn ở đúng tọa độ `(50, 50)` với kích thước `400×300`, script sẽ chuyển Notepad sang vị trí `(120, 120)` và kích thước `500×350` trước bằng `WNDPOS` / `WNDSIZE`, sau đó mới gọi `WNDSETINFO` với các số trực tiếp:

```cms
// Kiểm tra truyền số trực tiếp vào WNDSETINFO trên cửa sổ Notepad
LOGCLEAR
LOGSHOW(1)

$hwnd = WNDFIND("Notepad")
IF($hwnd > 0)
   // Bước 1: Đưa cửa sổ về vị trí và kích thước khác trước (120, 120, 500, 350)
   WNDPOS($hwnd, 120, 120)
   WNDSIZE($hwnd, 500, 350)
   WAITMS(300)

   // Bước 2: Thử truyền trực tiếp các số: X=50, Y=50, Rộng=400, Cao=300 vào WNDSETINFO
   WNDSETINFO($hwnd, 50, 50, 400, 300)
   WAITMS(500)

   // Bước 3: Đọc lại thông tin cửa sổ để kiểm chứng
   WNDGETINFO($hwnd, $x, $y, $w, $h)
   LOGWRITE("Sau khi goi WNDSETINFO voi so truc tiep -> X=", $x, " Y=", $y, " W=", $w, " H=", $h)
   IF(($x = 50) & ($y = 50) & ($w = 400) & ($h = 300))
      LOGWRITE("KET LUAN: WNDSETINFO chap nhan truyen so truc tiep (khop voi sach tr. 117).")
   ELSE
      LOGWRITE("KET LUAN: WNDSETINFO khong doi dung thong so khi truyen so truc tiep.")
   END_IF
ELSE
   LOGWRITE("Hay mo cua so Notepad truoc khi chay script nay.")
END_IF

HALT
```

---

## Chế độ khóa cửa sổ với trình duyệt và máy ảo

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so#gioi-han-va-giai-phap-dung-may-ao)

### Hai cách hiểu hiện tại

1. **Theo sách của Chô tô (tr. 19):** Sách liệt kê chung trình duyệt web và máy ảo vào nhóm cửa sổ không nhận Clickermann khi dùng chế độ khóa cửa sổ.
2. **Theo help chính thức (bài Khóa cửa sổ và phần FAQ):**
   - **Với trình duyệt:** Help giải thích mỗi thành phần bên trong trình duyệt (như khung Flash trong cửa sổ trình duyệt) là một phần tử con riêng có `HWND` riêng; việc chế độ khóa cửa sổ có hoạt động hay không **tùy cách ứng dụng được viết** (ví dụ: có trường hợp chạy được trên Firefox nhưng không chạy trên Google Chrome).
   - **Với máy ảo (MS Virtual PC, VMware...):** Help gợi ý cài hệ điều hành, ứng dụng và Clickermann **vào bên trong máy ảo**, rồi chạy Clickermann ở chế độ thường bên trong máy ảo đó và thu nhỏ cửa sổ máy ảo xuống trên máy thật để vừa tự động hóa vừa làm việc khác.

### Script kiểm tra trên Windows

Để kiểm tra đầy đủ xem phần tử nội dung trong trình duyệt có đọc được màu khi bị cửa sổ khác che khuất và có cập nhật màu mới khi nội dung bên trong trình duyệt thay đổi như help mô tả hay không:

1. Mở trình duyệt tới một trang có nút bấm đổi màu hoặc cuộn trang tại tọa độ tương đối `(100, 100)` của phần tử nội dung.
2. Đưa trỏ chuột vào phần tử nội dung của trình duyệt và nhấn `Alt + W` để khóa.
3. Chạy script dưới đây:
   - **Bước A:** Khi trình duyệt **chưa bị che**, script chụp `GETSCREEN` và lưu mã màu `$mau_truoc = PXL(100, 100)`.
   - **Bước B:** Trong 5 giây chờ của script, bạn kéo một cửa sổ khác (như Notepad) **đè lên che khuất vị trí `(100, 100)`** của trình duyệt (không thu nhỏ trình duyệt xuống thanh tác vụ). Script sẽ chụp lại `GETSCREEN` và đọc `$mau_sau_che = PXL(100, 100)` để so sánh với `$mau_truoc`.
   - **Bước C:** Trong khi trình duyệt **vẫn đang bị Notepad che khuất**, script gửi lệnh `LCLICK(100, 100)` và `WHEELDOWN(3)` để làm thay đổi nội dung tại `(100, 100)` của trình duyệt, sau đó gọi lại `GETSCREEN` và đọc `$mau_sau_doi = PXL(100, 100)` xem màu có đổi theo nội dung mới của trình duyệt hay không:

```cms
// Kiểm tra đọc màu trước khi che, sau khi bị che và sau khi nội dung trình duyệt thay đổi
LOGCLEAR
LOGSHOW(1)

IF($_hwnd > 0)
   LOGWRITE("Dang khoa vao phan tu HWND = ", $_hwnd)

   // Bước A: Đọc màu khi phần tử trình duyệt CHƯA bị cửa sổ khác che
   GETSCREEN
   $mau_truoc = PXL(100, 100)
   LOGWRITE("[Buoc A] Ma mau tai (100, 100) khi CHUA bi che: ", $mau_truoc)

   LOGWRITE("-> Bay gio hay keo cua so Notepad DE LEN che khuat diem (100, 100) cua trinh duyet trong 5 giay...")
   WAIT(5)

   // Bước B: Đọc lại màu sau khi đã bị Notepad đè lên che khuất
   GETSCREEN
   $mau_sau_che = PXL(100, 100)
   LOGWRITE("[Buoc B] Ma mau tai (100, 100) SAU KHI bi Notepad che: ", $mau_sau_che)

   // Bước C: Tác động làm đổi nội dung trình duyệt tại (100, 100) trong khi vẫn bị Notepad che
   LCLICK(100, 100)
   WAITMS(300)
   WHEELDOWN(3)
   WAIT(1)

   GETSCREEN
   $mau_sau_doi = PXL(100, 100)
   LOGWRITE("[Buoc C] Ma mau tai (100, 100) SAU KHI bam chuot & cuon trang (van bi che): ", $mau_sau_doi)

   IF(($mau_sau_che = $mau_truoc) & ($mau_sau_doi != $mau_sau_che))
      LOGWRITE("KET LUAN: Doc duoc dung mau cua trinh duyet khi bi che va cap nhat duoc mau moi khi noi dung doi!")
   ELSE
      LOGWRITE("Hay doi chieu 3 ma mau tren va kiem tra them bang kinh lup trong Trinh soan thao.")
   END_IF
ELSE
   LOGWRITE("Chua bat che do khoa cua so! Hay tro chuot vao phan tu noi dung trinh duyet va nhan Alt + W truoc.")
END_IF

HALT
```

---

## Đặt SUB trong tệp #include

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`SUB ... END_SUB`](/lenh/cau-truc#sub-end-sub)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục Cấu trúc lệnh):** Ghi rằng việc tách phần thân các chương trình con (`SUB ... END_SUB`) ra một tệp riêng bên ngoài rồi nạp vào qua chỉ thị `#include` được coi là thói quen tốt.
2. **Theo sách của Chô tô (tr. 81):** Lại khuyên không nên đặt `SUB` ở tệp ngoài rồi `#include` vào vì đôi lúc bị lỗi.

Gợi ý: script thực tế của người biên soạn có dùng cách này (đặt `SUB` ở tệp ngoài qua `#include` và đặt cả `#include`, `SUB` bên trong thân `THREAD`) và báo chạy tốt, chưa kiểm chứng lại. Vẫn cần chạy script dưới đây.

### Script kiểm tra trên Windows

Trong một thư mục dự án, trước tiên bạn chạy đoạn script tạo tệp thư viện `thu_vien_sub.cms` chứa chương trình con `SUB(cong_hai_so, $a, $b)` như bên dưới:

```cms
// Bước 1: Chạy một lần để tạo tệp thu_vien_sub.cms chứa SUB(cong_hai_so, $a, $b)
STRWRITELN("thu_vien_sub.cms", "SUB(cong_hai_so, $a, $b)", 1)
TFWRITE("thu_vien_sub.cms", "   $tong_sub = $a + $b")
TFWRITE("thu_vien_sub.cms", "   PRINT($tong_sub)")
TFWRITE("thu_vien_sub.cms", "END_SUB")

PRINT("Da tao xong tep thu_vien_sub.cms. Hay chay tiep doan code #include ben duoi.")
HALT
```

Sau khi tệp `thu_vien_sub.cms` đã được tạo trong thư mục dự án, bạn thay nội dung trong Trình soạn thảo bằng đoạn mã dưới đây để nạp `thu_vien_sub.cms` qua `#include` và gọi `cong_hai_so(15, 27)`:

```text
#include "thu_vien_sub.cms"

LOGCLEAR
LOGSHOW(1)

cong_hai_so(15, 27)

IF($tong_sub = 42)
   PRINT("KET LUAN: Goi SUB dat trong tep #include hoat dong binh thuong (khop voi help).")
ELSE
   PRINT("KET LUAN: Goi SUB trong tep #include gap loi hoac khong cap nhat dung ket qua.")
END_IF

HALT
```

Ngoài ra, bạn có thể thử thêm trường hợp đặt `#include "thu_vien_sub.cms"` và `SUB` ngay bên trong thân một khối `THREAD` (theo quy tắc của help là `SUB` dùng trong luồng nào thì khai báo trong thân luồng đó):

```text
THREAD(luong_include, 1)
   #include "thu_vien_sub.cms"
   cong_hai_so(10, 20)
   SETTHREAD(luong_include, 0)
END_THREAD

WAIT(1)
IF($tong_sub = 30)
   PRINT("KET LUAN: #include va SUB ben trong than THREAD chay binh thuong.")
END_IF
HALT
```

---

## Tên tệp nhật ký của LOGWRITE và chỉ thị #logfile

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`LOGWRITE (PRINT)`](/lenh/nhat-ky#logwrite-print) · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#chi-thi-tien-xu-ly-preprocessor-directives)

### Hai chỗ ghi trong help

1. **Theo bảng chỉ thị tiền xử lý (phần Giới thiệu ngôn ngữ) và Lịch sử phiên bản (v4.13.014):** Bản v4.13.014 nâng cấp `#logfile` cho phép đặt tên tệp nhật ký tùy ý (ví dụ `#logfile "debug.txt"`).
2. **Theo mục `LOGWRITE` (mục Xuất thông tin):** Ghi rằng khi có chỉ thị `#logfile` thì thông báo được ghi thêm vào tệp `log.txt` trong thư mục dự án (`%thu_muc_du_an%/log.txt`). Câu hỏi cần kiểm tra là khi viết `#logfile` **không kèm tên tệp** thì chương trình có tự ghi vào `log.txt` hay không.

### Script kiểm tra trên Windows

Hãy lưu tệp script vào một **thư mục dự án trống không có sẵn bất kỳ tệp `.txt` nào** (và nhớ xóa mọi tệp `.txt` vừa sinh ra trước khi chạy biến thể tiếp theo):

**Biến thể A — `#logfile` không kèm tên tệp:**
- *Kỳ vọng:* Nếu theo mô tả ở mục `LOGWRITE`, chương trình sẽ tự tạo tệp **`log.txt`** trong thư mục dự án; nếu bắt buộc phải có tên tệp, thư mục sẽ không có tệp `.txt` nào (hoặc báo lỗi).

```cms
#logfile

LOGCLEAR
LOGSHOW(1)
LOGWRITE("Thu nghiem #logfile khong kem ten tep")

GETFILELIST($ds_txt, "*.txt")
LOGWRITE("So tep .txt tim thay trong thu muc du an: ", ARRSIZE($ds_txt))
FOR($i=0, $i < ARRSIZE($ds_txt))
   LOGWRITE(" - Tim thay tep .txt: ", $ds_txt[$i])
END_CYC

HALT
```

**Biến thể B — `#logfile "debug.txt"` có đặt tên tệp riêng (nhớ xóa `log.txt` nếu có trước khi chạy):**
- *Kỳ vọng:* Chương trình tạo ra đúng tệp **`debug.txt`** trong thư mục dự án.

```cms
#logfile "debug.txt"

LOGCLEAR
LOGSHOW(1)
LOGWRITE("Thu nghiem #logfile co ten tep debug.txt")

GETFILELIST($ds_txt, "*.txt")
LOGWRITE("So tep .txt tim thay trong thu muc du an: ", ARRSIZE($ds_txt))
FOR($i=0, $i < ARRSIZE($ds_txt))
   LOGWRITE(" - Tim thay tep .txt: ", $ds_txt[$i])
END_CYC

HALT
```

---

## Cách làm tròn số âm của ROUND

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`ROUND`](/lenh/so#round)

### Mô tả trong help

Ở mục Làm việc với số (lệnh `ROUND`), help ghi: "Việc làm tròn diễn ra theo hướng ra xa số 0. Tức là `prec = 2` sẽ làm tròn số đến hàng trăm, còn `prec = -2` đến hàng phần trăm (hai chữ số sau dấu chấm). Việc làm tròn diễn ra theo quy tắc chuẩn `0.5`."

Cần kiểm tra xem với số âm ở chính giữa (`.5`) như `ROUND(-1.5, 0)`, Clickermann làm tròn ra xa số `0` thành `-2` hay làm tròn về phía dương thành `-1`.

### Script kiểm tra trên Windows

```cms
LOGCLEAR
LOGSHOW(1)

$kq = ROUND(-1.5, 0)
LOGWRITE("ROUND(-1.5, 0) = ", $kq)
IF($kq = -2)
   LOGWRITE("KET LUAN: ROUND(-1.5, 0) lam tron ra xa so 0 thanh -2.")
ELSE
   LOGWRITE("KET LUAN: ROUND(-1.5, 0) cho ket qua la ", $kq)
END_IF
HALT
```

---

## Kiểu tham số addr của READMEM và WRITEMEM

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`READMEM`](/lenh/kich-ban#readmem), [`WRITEMEM`](/lenh/kich-ban#writemem)

### Điểm tự mâu thuẫn trong help

- Ở mục Script và plugin (phần liệt kê tham số của `READMEM`), help ghi `addr` là "chuỗi, địa chỉ bộ nhớ".
- Tuy nhiên, ngay ở phần ghi chú bên dưới của cả `READMEM` và `WRITEMEM` cũng như trong ví dụ của help (`0x0006F2B7`), help lại ghi rõ địa chỉ là "số nguyên thông thường ở dạng thập phân hoặc thập lục phân" (không đặt trong dấu ngoặc kép).

*(Mục này chỉ ghi nhận điểm tự mâu thuẫn trong help, không viết script kiểm tra cho `READMEM` và `WRITEMEM`).*

---

## POSTMESSAGE rồi GETMESSAGE ngay trong cùng lượt

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang lệnh:** [`GETMESSAGE`](/lenh/winapi#getmessage)

### Câu hỏi cần kiểm tra

Ví dụ ở mục WinAPI gọi `POSTMESSAGE($h, 1024, 123, 321)` rồi gọi `GETMESSAGE($var1, $var2)` ngay ở dòng tiếp theo và không có lệnh `HALT` ở cuối. Cần kiểm tra xem `POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng một lượt chạy (vòng đầu tiên) có nhận được thông điệp `123, 321` ngay lập tức không, hay cần chờ ngắn (`WAITMS`) hoặc sang lượt lặp tiếp theo mới nhận được.

### Script kiểm tra trên Windows

Script 1 dưới đây dùng biến hệ thống `$_hwnd_self` (mã `hwnd` của chính cửa sổ Clickermann) để kiểm tra ngay trong cùng lượt và sau khi chờ `WAITMS(100)`:

```cms
LOGCLEAR
LOGSHOW(1)

POSTMESSAGE($_hwnd_self, 1024, 123, 321)
GETMESSAGE($var1, $var2, $isnew)
PRINT("Ngay trong cung luot -> isnew:", $isnew, " wParam:", $var1, " lParam:", $var2)

IF($isnew = 1)
   PRINT("KET LUAN: GETMESSAGE nhan duoc thong diep ngay lap tuc sau POSTMESSAGE.")
ELSE
   WAITMS(100)
   GETMESSAGE($var1, $var2, $isnew)
   PRINT("Sau WAITMS(100) -> isnew:", $isnew, " wParam:", $var1, " lParam:", $var2)
   IF($isnew = 1)
      PRINT("KET LUAN: Can co do tre WAITMS(100) thi GETMESSAGE moi nhan duoc thong diep.")
   ELSE
      PRINT("Chua nhan duoc thong diep sau WAITMS(100) (isnew = 0), hay thu tiep Script 2 ben duoi.")
   END_IF
END_IF
HALT
```

**Script 2 — Kiểm tra trường hợp không có `HALT` để xem thông điệp có nhận ở lượt lặp tiếp theo của script không:**

```cms
DEFINE($luot, 0)
INC($luot)

IF($luot = 1)
   LOGCLEAR
   LOGSHOW(1)
   POSTMESSAGE($_hwnd_self, 1024, 123, 321)
END_IF

GETMESSAGE($var1, $var2, $isnew)
PRINT("Luot ", $luot, " -> isnew:", $isnew, " wParam:", $var1, " lParam:", $var2)

IF(($isnew = 1) | ($luot >= 5))
   HALT
END_IF
WAITMS(50)
```

---

## Vòng lặp FOR lồng nhau không gán giá trị đầu

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`FOR ... END_CYC`](/lenh/cau-truc#for-end-cyc), [`SUB ... END_SUB`](/lenh/cau-truc#sub-end-sub)

### Câu hỏi cần kiểm tra

Ở mục Cấu trúc lệnh (và Lịch sử phiên bản v4.11.000), help mô tả rằng nếu biến đếm `$var` đã được khởi tạo trước khi vào vòng lặp `FOR` và câu lệnh `FOR` không ghi `=value`, vòng lặp sẽ không tự đưa biến về `0` mà bắt đầu từ giá trị hiện tại của biến đó (trong khi trước đó ở bản v4.2.000, Lịch sử phiên bản từng ghi tham số `FOR` được đưa về `0` sau khi kết thúc vòng lặp).

Tuy nhiên, ngay trong các ví dụ của help ở mục `FOR` và `SUB`, tác giả lại viết:
- Vòng lặp lồng nhau: `FOR($x, $x < 3)` bên ngoài và `FOR($y, $y < 3)` bên trong mà không viết `$y=0`.
- Dùng lại cùng biến `$i` ở hai vòng `FOR($i, $i < 3)` liên tiếp trong ví dụ của `SUB`.

### Script kiểm tra trên Windows

```cms
LOGCLEAR
LOGSHOW(1)

// Phần 1: Kiểm tra FOR lồng nhau không gán =0
$so_dong = 0
LOGWRITE("=== Phan 1: FOR long nhau nguyen ban trong help ===")
FOR($x, $x < 3)
   FOR($y, $y < 3)
      PRINT($x, ":", $y)
      INC($so_dong)
   END_CYC
END_CYC

LOGWRITE("Tong so dong da in o Phan 1: ", $so_dong)
IF($so_dong = 9)
   LOGWRITE("-> Phan 1 in du 9 dong (vong FOR ben trong tu chay lai tu 0).")
END_IF
IF($so_dong = 3)
   LOGWRITE("-> Phan 1 chi in 3 dong (bien $y giu gia tri 3 sau luot dau, can viet FOR($y=0, $y < 3)).")
END_IF

// Phần 2: Kiểm tra dùng lại biến $i ở hai vòng FOR($i, $i < 3) liên tiếp như ví dụ mục SUB
$dem_vong_2 = 0
FOR($i, $i < 3)
   INC($dem_vong_2)
END_CYC
FOR($i, $i < 3)
   INC($dem_vong_2)
END_CYC

LOGWRITE("Tong so luot chay cua 2 vong FOR($i, $i < 3) lien tiep (ky vong 6 neu tu ve 0, hoac 3 neu giu gia tri): ", $dem_vong_2)
HALT
```

---

## Mã phím PrintScreen (154 và 44)

**Trạng thái:** 🟠 Chưa thống nhất · **Trang phụ lục:** [Bảng mã phím và hằng số](/phu-luc/ma-phim#bang-ma-phim-chuot-va-phim-dieu-khien)

### Điểm cần kiểm tra

Trong cả bảng mã phím của help lẫn tệp `data/const.txt` đi kèm chương trình, hằng số `#PRINTSCREEN` đều được ghi giá trị là **`154`** (`0x9A`). Trong khi đó, theo chuẩn mã phím ảo của Windows (`VK_SNAPSHOT`), phím `PrintScreen` thường có mã là **`44`** (`0x2C`).

### Script kiểm tra trên Windows

Chạy đoạn script dưới đây, sau đó nhấn phím **PrintScreen** (`PrtScn`) trên bàn phím vài lần trong vòng 10 giây để xem Clickermann bắt được phím này ở mã `154` hay `44`:

```cms
LOGCLEAR
LOGSHOW(1)
PRINT("Hay nhan phim PrintScreen (PrtScn) tren ban phim trong vong 10 giay...")

FOR($i=0, $i < 200)
   IF(ISKEYDOWN(154) = 1)
      PRINT("Phat hien nhan PrintScreen voi ma 154 (#PRINTSCREEN trong help)!")
   END_IF
   IF(ISKEYDOWN(44) = 1)
      PRINT("Phat hien nhan PrintScreen voi ma 44 (VK_SNAPSHOT chuan Windows)!")
   END_IF
   WAITMS(50)
END_CYC

PRINT("Ket thuc 10 giay kiem tra PrintScreen.")
HALT
```

---

## Quy luật mã `KEYDOWN`

**Trạng thái:** 🟠 Chưa thống nhất · **Trang phụ lục:** [Bảng mã phím và hằng số](/phu-luc/ma-phim#khi-keydown-can-ma-khac) · **Trang lệnh:** [`KEYDOWN`](/lenh/ban-phim#keydown), [`KEYUP`](/lenh/ban-phim#keyup)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục Bàn phím và phần Mã phím):** Các lệnh `KEYPRESS`, `KEYDOWN` và `KEYUP` dùng chung một bảng mã phím ảo (ví dụ `75` là phím `K`, `37` là phím mũi tên trái).
2. **Theo bảng tự dò của Mai Bảo Long (kèm quy luật suy luận):** Có trường hợp `KEYDOWN` và `KEYUP` phải truyền mã của phím có **mã quét (Scan Code) bằng mã phím đích** thì ứng dụng mới nhận đúng phím. **Kiến thức Windows:** mã quét của phím `K` (`75`) là `37` (trùng với mã phím ảo của mũi tên trái), nên theo quy luật này `KEYDOWN(75)` sẽ tạo ra phím mũi tên trái thay vì chữ `k`.

### Script kiểm tra trên Windows

Chuẩn bị: mở một cửa sổ **Notepad trống**, tắt phím **Caps Lock**, đặt con trỏ soạn thảo vào vùng trắng của Notepad trong 3 giây chờ đầu tiên:

```cms
WAIT(3)
KEYPRESS(65)
WAITMS(300)
KEYDOWN(75)
WAITMS(100)
KEYUP(75)
WAITMS(300)
KEYPRESS(88)
HALT
```

- **Kết quả mong đợi:**
  - Nếu trong Notepad hiện ra chuỗi **`akx`**: nghĩa là `KEYDOWN(75)` gõ ra chữ `k`, tức hoạt động theo **mã thường** trong help.
  - Nếu trong Notepad hiện ra chuỗi **`xa`**: nghĩa là sau khi `KEYPRESS(65)` gõ chữ `a`, lệnh `KEYDOWN(75)` đã bấm phím **mũi tên trái** đưa con trỏ về đứng trước chữ `a` rồi `KEYPRESS(88)` mới gõ chữ `x` vào đầu dòng — tức **quy luật đúng trong điều kiện đó**.
- **Yêu cầu khi kiểm tra:**
  - Phải chạy thử ở **cả hai chế độ**:
    1. **Chế độ thường** (không khóa cửa sổ, bấm chuột chọn vùng soạn thảo Notepad trong 3 giây chờ).
    2. **Chế độ khóa cửa sổ** vào đúng vùng soạn thảo của Notepad (đưa trỏ chuột vào vùng soạn thảo trắng của Notepad rồi nhấn `Alt + W`).
  - Ghi lại rõ kết quả của cả hai chế độ, và thử thêm trên một ứng dụng khác ngoài Notepad nếu được.
  - Lưu ý: script này chỉ kiểm tra hành vi trong điều kiện thử nghiệm trên, không tự động kết luận cho mọi ứng dụng.

---

## Cách tắt chế độ khóa cửa sổ

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang khái niệm:** [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so#tat-khoa-cua-so) · **Trang lệnh:** [`HSET`](/lenh/winapi#hset)

### Điểm cần kiểm tra

Ở mục `HSET`, help ghi cú pháp `HSET(hwnd, state)` với `state = 1` là bật và `state = 0` là tắt chế độ khóa cửa sổ, nhưng không có ví dụ minh họa dòng lệnh tắt khóa cửa sổ và không nói rõ:
1. Gọi `HSET($_hwnd, 0)` (truyền đúng `hwnd` đang khóa) và gọi `HSET(0, 0)` (truyền `hwnd = 0`) có cùng đưa biến hệ thống `$_hwnd` về `0` (tắt khóa cửa sổ) hay không?
2. Khi đang ở chế độ khóa cửa sổ, nhấn lại phím tắt **`Alt + W`** trên giao diện có tắt khóa cửa sổ hay chỉ đổi sang khóa phần tử mới dưới trỏ chuột?

### Script kiểm tra trên Windows

Mở sẵn cửa sổ Notepad rồi chạy script dưới đây:

```cms
LOGCLEAR
LOGSHOW(1)

$h = WNDFIND("Notepad")
IF($h > 0)
   // 1. Bật khóa vào Notepad và thử tắt bằng HSET(0, 0)
   HSET($h, 1)
   PRINT("Sau HSET($h, 1) -> $_hwnd = ", $_hwnd)

   HSET(0, 0)
   PRINT("Sau HSET(0, 0) -> $_hwnd = ", $_hwnd, " (neu bang 0 la HSET(0, 0) tat duoc khoa cua so)")

   // 2. Bật khóa lại vào Notepad và thử tắt bằng HSET($_hwnd, 0)
   HSET($h, 1)
   PRINT("Bat lai HSET($h, 1) -> $_hwnd = ", $_hwnd)

   HSET($_hwnd, 0)
   PRINT("Sau HSET($_hwnd, 0) -> $_hwnd = ", $_hwnd, " (neu bang 0 la HSET($_hwnd, 0) tat duoc khoa cua so)")
ELSE
   PRINT("Hay mo cua so Notepad truoc khi chay script nay.")
END_IF

HALT
```

---

## Tên biến có phân biệt chữ hoa và chữ thường không

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#bien-va-kieu-du-lieu)

### Điểm help không nói rõ

Ở phần Giới thiệu ngôn ngữ, help chỉ quy định tên biến bắt đầu bằng `$` nối với chữ cái Latin `a..z`, chữ số `0..9` và `_`, không nói rõ tên biến có phân biệt chữ hoa và chữ thường hay không. (Suy luận: trong Lịch sử phiên bản ghi tên biến hệ thống là `$_DATE_Y`, còn trong phần Giới thiệu ngôn ngữ lại ghi là `$_date_y`, nên nhiều khả năng không phân biệt chữ hoa và chữ thường).

### Script kiểm tra trên Windows

```cms
LOGCLEAR
LOGSHOW(1)

$var_thu = 123
LOGWRITE("Gia tri cua $var_thu: ", $var_thu)
LOGWRITE("Gia tri khi doc bang $VAR_THU (viet hoa): ", $VAR_THU)

IF($VAR_THU = 123)
   LOGWRITE("KET LUAN: Ten bien KHONG phan biet chu hoa va chu thuong.")
ELSE
   LOGWRITE("KET LUAN: Ten bien CO phan biet chu hoa va chu thuong.")
END_IF

HALT
```

---

## Vị trí khung thiết lập chế độ chạy script

**Trạng thái:** 🟠 Chưa thống nhất · **Trang bắt đầu:** [Màn hình chính](/bat-dau/man-hinh-chinh#bang-thong-tin-va-che-do-chay)

### Điểm chưa thống nhất trong help

- Ở bài Màn hình chính, help ghi ngoài các nút bấm, cửa sổ chính còn có khung thông tin chế độ khóa cửa sổ và **khung thiết lập chế độ thực thi script**.
- Tuy nhiên ở Lịch sử phiên bản (bản v4.7.000), lịch sử ghi đã bỏ các chế độ hoạt động khỏi cửa sổ chính; và đến bản v4.7.000 SE lại ghi các chế độ thực thi trở lại dưới dạng **một cửa sổ riêng**.

### Cách kiểm tra trên Windows

Mở chương trình Clickermann v4.13.014 trên máy Windows và quan sát trực tiếp:

1. Xem các tùy chọn chế độ chạy script nằm ngay trên cửa sổ chính hay mở ra một cửa sổ phụ riêng khi bấm nút trên hàng nút phía trên.
2. Chụp ảnh giao diện thực tế để bổ sung vào trang [Màn hình chính](/bat-dau/man-hinh-chinh).

---

## Chỉ thị tiền xử lý #define

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#chi-thi-tien-xu-ly-preprocessor-directives)

### Điểm cần kiểm tra

Ở phần Giới thiệu ngôn ngữ, bảng chỉ thị tiền xử lý chỉ ghi ngắn gọn cú pháp `#define <tìm>:<thay>` ("Thay thế một văn bản bằng văn bản khác") mà không có đoạn code ví dụ hoàn chỉnh. Cần chạy thử ví dụ suy luận `#define @pause:WAITMS(100)` trên Windows để xác nhận cách hoạt động:

```cms
#define @pause:WAITMS(100)

LOGCLEAR
LOGSHOW(1)

$t1 = $_ms
@pause
$t2 = $_ms

$do_tre = $t2 - $t1
LOGWRITE("Thoi gian truoc va sau @pause: ", $do_tre, " ms")
IF($do_tre >= 80)
   LOGWRITE("KET LUAN: #define @pause:WAITMS(100) da thay the va chay dung (do tre >= 80 ms).")
ELSE
   LOGWRITE("KET LUAN: Do tre qua nho (", $do_tre, " ms), can kiem tra lai cu phap #define.")
END_IF
HALT
```

---

## Nơi lưu ảnh chụp nhanh 100x100 của phím tắt Alt + G

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang cẩm nang:** [Tìm hình ảnh mẫu trên màn hình](/cam-nang/tim-anh#buoc-1-chuan-bi-tep-anh-mau-bmp)

### Điểm help không nói rõ

Ở bài Trình soạn thảo, help mô tả tổ hợp phím `Alt + G` giúp chụp nhanh vùng `100×100` điểm ảnh mà kính lúp đang nhìn thấy và lưu ở định dạng `.bmp`, nhưng không nói rõ tệp `.bmp` này được lưu ở thư mục nào (thư mục dự án, thư mục con `screens\` hay thư mục chương trình Clickermann) và tên tệp đặt theo mẫu nào.

### Cách kiểm tra trên Windows

1. Tạo một **thư mục dự án trống** (chưa có tệp `.bmp` nào), lưu script dưới đây vào đó, mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) và bật **Kính lúp**.
2. Nhấn tổ hợp phím `Alt + G`.
3. Chạy đoạn script dưới đây để kiểm tra cả 3 nơi (thư mục dự án, thư mục con `screens\` và thư mục làm việc `$_pdir`), đồng thời mở thư mục chương trình Clickermann trong File Explorer xem tệp `.bmp` mới xuất hiện ở đâu:

```cms
LOGCLEAR
LOGSHOW(1)

GETFILELIST($bmp_du_an, "*.bmp")
GETFILELIST($bmp_screens, "screens\*.bmp")
GETFILELIST($bmp_pdir, STRCONCAT($_pdir, "*.bmp"))

LOGWRITE("Thu muc hien tai ($_pdir): ", $_pdir)
LOGWRITE("1. Cac tep .bmp trong thu muc du an: ", ARRSIZE($bmp_du_an))
FOR($i=0, $i < ARRSIZE($bmp_du_an))
   LOGWRITE(" - Thu muc du an: ", $bmp_du_an[$i])
END_CYC

LOGWRITE("2. Cac tep .bmp trong thu muc screens\: ", ARRSIZE($bmp_screens))
FOR($j=0, $j < ARRSIZE($bmp_screens))
   LOGWRITE(" - screens\: ", $bmp_screens[$j])
END_CYC

LOGWRITE("3. Cac tep .bmp theo $_pdir: ", ARRSIZE($bmp_pdir))
LOGWRITE("-> Neu ca 3 muc tren deu bang 0, hay kiem tra thu muc chuong trinh Clickermann (noi chua tep .exe).")

HALT
```

---

## Kéo chuột vẽ nét liền bằng LDOWN, MOVE, LUP trong Paint

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang cẩm nang:** [Tự động vẽ hình trong Paint](/cam-nang/tu-ve)

### Điểm cần kiểm tra

Ở mục Chuột, ví dụ kéo thả chuột của help chỉ viết `ldown(10, 10)`, `waitms(300)`, `lup(20, 20)` mà không có lệnh `MOVE` ở giữa. Trong trang [Tự động vẽ hình trong Paint](/cam-nang/tu-ve), tài liệu suy luận rằng việc giữ `LDOWN` rồi gọi liên tiếp các lệnh `MOVE(x, y)` kèm `WAITMS` trước khi `LUP` sẽ làm Paint vẽ các đoạn thẳng nối tiếp nhau.

### Cách kiểm tra trên Windows

1. Mở chương trình **Paint**, chọn công cụ **Cọ vẽ (Brushes)** màu đen, đặt cửa sổ Paint sao cho vùng giấy trắng bao phủ tọa độ `(200, 220)` đến `(400, 360)`.
2. Chạy đoạn script dưới đây và quan sát kết quả trên trang giấy vẽ của Paint:
   - **Nét 1 (ở dòng trên `Y = 230`, không có `MOVE`, chỉ `LDOWN` -> `WAITMS(300)` -> `LUP` tại điểm mới):** Kiểm tra xem trên giấy vẽ xuất hiện một đoạn thẳng ngang nối từ `(200, 230)` sang `(350, 230)` hay chỉ có chấm rời ở điểm đầu/cuối.
   - **Nét 2 (ở dòng dưới `Y = 280..330`, có các lệnh `MOVE` ở giữa trước khi `LUP`):** Kiểm tra xem trên giấy vẽ có xuất hiện đường gấp khúc hình chữ V nối liền qua cả 3 điểm `(200, 280)` -> `(275, 330)` -> `(350, 280)` hay không.

```cms
// Kiểm tra vẽ nét kéo chuột trong Paint: không có MOVE (Nét 1) và có MOVE (Nét 2)
WAIT(2)

// Nét 1: Cách viết trong ví dụ của help (LDOWN -> WAITMS(300) -> LUP tại tọa độ mới, không có MOVE)
LDOWN(200, 230)
WAITMS(300)
LUP(350, 230)

WAIT(1)

// Nét 2: Cách viết có MOVE ở giữa (LDOWN -> MOVE -> MOVE -> LUP) tạo hình chữ V
LDOWN(200, 280)
WAITMS(50)
MOVE(275, 330)
WAITMS(50)
MOVE(350, 280)
WAITMS(50)
LUP(350, 280)

HALT
```

---

## Giá trị biến sau khi bấm Dừng, bấm Áp dụng hoặc đổi script

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#bien-khi-script-tu-lap-lai) · **Trang cẩm nang:** [Thực chiến: kỹ thuật viết script](/cam-nang/thuc-chien#khoi-tao-mot-lan-o-dau-vong-lap-bang-define-init-0)

### Câu hỏi cần kiểm tra

Khi script tự quay lại đầu vòng lặp, biến vẫn giữ giá trị cũ (thường dùng kết hợp `DEFINE($init, 0)` và `IF($init == 0) ... $init = 1 END_IF` để chỉ khởi tạo ở lượt đầu).

Gợi ý: script thực tế của người biên soạn có dùng cách này (biến giữ giá trị qua các lượt lặp với `DEFINE` và `$init`) và báo chạy tốt, chưa kiểm chứng lại. Vẫn cần chạy script dưới đây.

Ngoài ra, cần kiểm tra thêm trên Windows xem giá trị biến (`$dem`, `$init`) được tự động xóa về `0` hay vẫn giữ giá trị cũ trong 3 tình huống sau:
1. Người dùng bấm nút **Dừng** (`Alt + S`) rồi bấm **Chạy** (`Alt + A`) lại.
2. Người dùng bấm nút **Áp dụng** trong Trình soạn thảo rồi bấm **Chạy**.
3. Người dùng mở nạp một tệp `.cms` khác có biến trùng tên `$dem`.

```cms
// Chạy vài giây rồi bấm Dừng (Alt + S), sau đó bấm Chạy lại (Alt + A)
// để xem $dem bắt đầu lại từ 1 hay đếm tiếp từ số cũ
INC($dem)
PRINT("Gia tri $dem = ", $dem)
WAIT(1)
```

---

## Đường dẫn tương đối khi script mới chưa lưu và nút Áp dụng

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang bắt đầu:** [Viết script đầu tiên](/bat-dau/script-dau-tien#chay-mot-script)

### Câu hỏi cần kiểm tra

1. Khi vừa mở Clickermann, tạo script mới tinh trong Trình soạn thảo mà **chưa nhấn `Ctrl + S` để lưu thành tệp `.cms`**, nếu bấm **Áp dụng** và chạy ngay thì biến `$_pdir` và các đường dẫn tệp tương đối (như `TFWRITE("thu.txt", "abc")`) sẽ trỏ về đâu (thư mục chương trình `%Clickermann%` hay thư mục mở gần nhất)?
2. Khi đang sửa một tệp `.cms` đã lưu:
   - Nhấn `Ctrl + S` trong Trình soạn thảo có tự động cập nhật kịch bản chạy (thay cho nút **Áp dụng**) không?
   - Ngược lại, bấm nút **Áp dụng** có tự động ghi đè nội dung mới vào tệp `.cms` đang mở trên đĩa (ngoài việc lưu vào `backup.cms` theo Lịch sử phiên bản v4.1.000) không?

```cms
LOGCLEAR
LOGSHOW(1)
PRINT("Thu muc lam viec hien tai ($_pdir): ", $_pdir)
HALT
```

---

## Hành vi của TFCOUNT, TFWRITE, INIREAD khi tệp chưa tồn tại

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang lệnh:** [Chuỗi, tệp tin, bộ nhớ tạm và HTTP](/lenh/chuoi-file)

### Câu hỏi cần kiểm tra

Trong một thư mục dự án trống (chưa có tệp `chua_co.txt` và `chua_co.ini`), cần chạy thử để xác nhận:
1. `TFCOUNT("chua_co.txt")` trả về `0` hay báo lỗi dừng script?
2. `TFWRITE("chua_co.txt", "Dong 1")` có tự động tạo tệp mới giống như `STRWRITELN` không?
3. `INIREAD("chua_co.ini", "KhoaKhongCo", "MUC")` khi tệp hoặc khóa chưa tồn tại sẽ trả về chuỗi rỗng `""` hay `"0"`?

```cms
LOGCLEAR
LOGSHOW(1)

$so_dong = TFCOUNT("chua_co.txt")
PRINT("1. TFCOUNT tren tep chua ton tai: ", $so_dong)

TFWRITE("chua_co.txt", "Dong thu nghiem")
PRINT("2. TFCOUNT sau khi goi TFWRITE: ", TFCOUNT("chua_co.txt"))

$gia_tri_ini = INIREAD("chua_co.ini", "KhoaKhongCo", "MUC")
PRINT("3. INIREAD khi tep/khoa chua ton tai -> do dai chuoi: ", STRLEN($gia_tri_ini), " | gia tri: '", $gia_tri_ini, "'")

HALT
```

---

## Hành vi của SCANPXL, SCANPICTURE, TFREADARR khi gọi lặp trên cùng một mảng

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang lệnh:** [`SCANPXL`](/lenh/man-hinh#scanpxl), [`SCANPICTURE`](/lenh/man-hinh#scanpicture), [`TFREADARR`](/lenh/chuoi-file#tfreadarr)

### Câu hỏi cần kiểm tra

Ở mục [`GETKEYSDOWN`](/lenh/ban-phim#getkeysdown), help ghi rõ mảng kết quả sẽ tự động được làm rỗng trước mỗi lần gọi. Còn ở `SCANPXL`, `SCANPICTURE` và `TFREADARR`, help không ghi rõ: nếu gọi lệnh lần thứ hai trên cùng một biến mảng `$arr` (mà chưa rút hết bằng `ARRPOP` hoặc chưa xóa bằng `UNDEFINE($arr)`), chương trình sẽ tự xóa mảng cũ trước khi ghi mới hay nối thêm vào cuối mảng cũ?

```cms
LOGCLEAR
LOGSHOW(1)

STRWRITELN("thu_mang.txt", "Dong 1", 1)
TFWRITE("thu_mang.txt", "Dong 2")

TFREADARR("thu_mang.txt", $arr_dong)
$lan_1 = ARRSIZE($arr_dong)

// Gọi lại lần 2 trên cùng mảng $arr_dong mà không UNDEFINE
TFREADARR("thu_mang.txt", $arr_dong)
$lan_2 = ARRSIZE($arr_dong)

PRINT("Kich thuoc mang sau lan 1: ", $lan_1, " | sau lan 2: ", $lan_2)
IF($lan_2 = $lan_1)
   PRINT("KET LUAN: Mang cu tu dong duoc xoa truoc khi ghi moi.")
ELSE
   PRINT("KET LUAN: Du lieu moi bi noi them vao cuoi mang cu (can goi UNDEFINE($arr) truoc).")
END_IF

HALT
```

---

## Nội dung chèn nhanh của phím tắt Alt + Q

**Trạng thái:** 🟠 Chưa thống nhất · **Trang bắt đầu:** [Trình soạn thảo và kính lúp](/bat-dau/trinh-soan-thao#khung-thong-tin-thoi-gian-thuc-va-phim-tat-alt-q)

### Cách kiểm tra trên Windows

Gợi ý: script thực tế của người biên soạn có dùng cách này (có dòng dạng `LCLICK(x, y)  // màu`) và báo chạy tốt, chưa kiểm chứng lại. Vẫn cần chạy script dưới đây. Suy luận: đây có thể là định dạng do `Alt + Q` chèn.

1. Mở [Trình soạn thảo](/bat-dau/trinh-soan-thao), đặt con trỏ soạn thảo vào một dòng trống.
2. Đưa chuột tới một điểm bất kỳ và nhấn **`Alt + Q`** để ghi nhận chính xác định dạng chuỗi lệnh được chèn vào (ví dụ `LCLICK(100, 200)  // 16777215` hay định dạng nào).
3. Bấm nút có biểu tượng **Clipboard** ở cột bên trái rồi nhấn lại **`Alt + Q`**, sau đó dán (`Ctrl + V`) ra để xem nội dung được chép vào bộ nhớ tạm.

---

## Cú pháp ngoặc rỗng của thủ tục và tên lệnh viết chữ thường

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [Tra cứu lệnh](/lenh/)

### Điểm cần kiểm tra

Trong các ví dụ của help, tên lệnh và cặp ngoặc rỗng của thủ tục không tham số được viết theo nhiều kiểu (ví dụ `GETSCREEN` không ngoặc hoặc `GETSCREEN()`, `LOGCLEAR` hoặc `LOGCLEAR()`, `HALT`, và tên lệnh viết thường hoặc viết lẫn hoa thường như `lclick`, `waitms`, `print`).

Gợi ý: script thực tế của người biên soạn có dùng cách này (tên lệnh chữ thường, viết lẫn hoa thường) và báo chạy tốt, chưa kiểm chứng lại. Vẫn cần chạy script dưới đây.

Chạy đoạn script dưới đây để xác nhận bộ thông dịch v4.13.014 chấp nhận tất cả các cách viết này:

```cms
// Kiểm tra tên lệnh chữ thường và cặp ngoặc rỗng trên thủ tục không tham số
getscreen()
logclear()
logshow(1)
print("Thu nghiem ten lenh chu thuong va ngoac rong GETSCREEN(), LOGCLEAR()")
waitms(100)
halt()
```

---

## Giao diện thực tế, mã màu, tiếng Việt có dấu và thu phóng màn hình Windows

**Trạng thái:** 🟡 Theo help, chưa chạy thử

Khi có máy Windows chạy Clickermann v4.13.014, cần kiểm tra và ghi nhận thêm các chi tiết thực tế sau:

1. **Đóng gói, tên tệp `.exe` và ngôn ngữ giao diện:**
   - Bộ tải về từ trang chủ có dạng tệp nén `.zip` hay bộ cài `.exe`? Tên tệp chạy 32-bit và 64-bit được đặt như thế nào?
   - Khi mở lần đầu, ngôn ngữ giao diện mặc định là tiếng Nga hay tiếng Anh? Cách chuyển ngôn ngữ giao diện trong phần cài đặt và nhãn thực tế của các nút trên cửa sổ chính, Trình soạn thảo, Quản lý cửa sổ.
   - Mã màu hiển thị ở cột bên trái của Trình soạn thảo mặc định là hệ thập phân (ví dụ `255`) hay hệ thập lục phân?
2. **Tiếng Việt có dấu (UTF-8) trong chuỗi và chú thích:**
   - Bản v4.13.014 ghi đã chuyển sang UTF-8. Cần thử viết chú thích tiếng Việt có dấu và chạy `PRINT("Thử nghiệm tiếng Việt có dấu")` xem cửa sổ nhật ký và trình soạn thảo có hiển thị đúng dấu tiếng Việt không.
3. **Tỷ lệ thu phóng màn hình Windows (Display Scaling 125%, 150%) và trạng thái nút chuột khi dừng giữa `LDOWN` / `LUP`:**
   - **Thu phóng màn hình (DPI Scaling):** Kiểm tra khi Windows đặt tỷ lệ hiển thị 125% hoặc 150% thì tọa độ chuột trong Trình soạn thảo, `LCLICK` và vùng chụp `GETSCREEN` có bị lệch so với mức 100% không *(Tham khảo: sách của Chô tô, tr. 25 khuyên đặt tỷ lệ hiển thị màn hình ở mức 100%)*.
   - **Trạng thái chuột khi dừng khẩn cấp:** Kiểm tra nếu script vừa chạy lệnh `LDOWN(x, y)` (đang nhấn giữ chuột trái) mà người dùng nhấn `Alt + S` để dừng hẳn script trước khi tới lệnh `LUP`, thì nút chuột trái của Windows có bị giữ kẹt cho tới khi bấm chuột tay một lần hay Clickermann tự động nhả chuột ra.

---

## Kiểm tra các kịch bản thực hành trong mục Cẩm nang

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Các trang:** [`cam-nang/*`](/cam-nang/click-theo-lich)

Toàn bộ các tình huống mẫu trong 5 trang cẩm nang đều được biên soạn từ các lệnh chuẩn của help nhưng chưa chạy thử thực tế trên máy Windows:

1. [Bấm chuột theo lịch và chu kỳ](/cam-nang/click-theo-lich): Tình huống lặp cố định, lặp `FOR` `N` lần và chờ đúng giờ/phút bằng `$_time_h`, `$_time_m`.
2. [Tìm màu trên màn hình rồi bấm chuột](/cam-nang/tim-mau): Tình huống `GETSCREEN` + `IF_PIXEL_IN`, vòng lặp `WHILE` chờ màu xuất hiện rồi bấm nút Đóng, và quét nhiều điểm bằng `SCANPXL` + `ARRPOP`.
3. [Tìm hình ảnh mẫu trên màn hình](/cam-nang/tim-anh): Tình huống cắt mẫu bằng `SCREENSHOTFIX` hoặc chụp qua `Alt + G`, tìm bằng `IF_PICTURE_IN` và bấm vào tâm ảnh, kết hợp `bgcolor`, `currency` và `COLORMODE`.
4. [Đọc và ghi tệp `.txt` và `.ini`](/cam-nang/doc-ghi-file): Tình huống tách riêng script ghi và đọc `INIWRITE`/`INIREAD`, tạo tệp mẫu bằng `STRWRITELN(..., 1)` + `TFWRITE`, đọc từng dòng bằng `TFREAD` + `STRPOS` + `STRCUT2`, và đọc mảng bằng `TFREADARR` + `STRSEPARATE`.
5. [Tự động vẽ hình trong Paint](/cam-nang/tu-ve): Tình huống vẽ đoạn thẳng, hình vuông, đường tròn (`SIN`, `COS`) và vẽ đa giác từ tệp `diem_ve.txt` ở vùng tọa độ `Y >= 220`.
6. [Thực chiến: kỹ thuật viết script](/cam-nang/thuc-chien): Các ví dụ kiểm tra 1 điểm ảnh, vòng lặp theo trạng thái màn hình, khởi tạo 1 lần bằng `DEFINE($init, 0)`, xếp 2 cửa sổ Notepad và lấy `HGET`, luồng giám sát `THREAD`, tách 3 tệp `#include`.

---

## Kiểm tra các điểm cần lưu ý của thư viện alt_winmode

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang nâng cao:** [Thư viện alt_winmode](/nang-cao/alt-winmode)

Khi chạy thử thư viện cộng đồng `alt_winmode.cms` trên máy Windows, cần kiểm chứng 5 hành vi thực tế dưới đây:

### Kéo vẽ trong Paint bằng `A_DRAG` và `A_MOVE`

- **Câu hỏi cần kiểm tra:** Trong Paint (đã chọn công cụ Cọ vẽ hoặc Bút chì màu đen), khi gửi thông điệp tới `hwnd` của trang giấy vẽ:
  1. Gọi `A_LDOWN` -> `A_MOVE` (`wParam = 0`) -> `A_LUP` có vẽ được nét trên trang giấy không?
  2. Gọi `A_LDOWN` -> `A_DRAG` (`wParam = 0x0001` / `MK_LBUTTON`) -> `A_LUP` có vẽ được nét liền trên trang giấy không?

```cms
#include "alt_winmode.cms"

SUB(A_DRAG, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd, 0x0200, 0x0001, $A_x + ($A_y * 65536))
END_SUB

LOGCLEAR
LOGSHOW(1)

$w_paint = WNDFIND("Paint")
IF($w_paint > 0)
   WNDPOS($w_paint, 50, 50)
   WNDSIZE($w_paint, 700, 550)
   WAITMS(500)
   $h_canvas = HGET(300, 350)

   // Thử 1: Dùng A_MOVE (wParam = 0) ở dòng Y = 60
   A_LDOWN(50, 60, $h_canvas)
   WAITMS(50)
   A_MOVE(200, 60, $h_canvas)
   WAITMS(50)
   A_LUP(200, 60, $h_canvas)

   WAITMS(300)

   // Thử 2: Dùng A_DRAG (wParam = 0x0001) ở dòng Y = 120
   A_LDOWN(50, 120, $h_canvas)
   WAITMS(50)
   A_DRAG(200, 120, $h_canvas)
   WAITMS(50)
   A_LUP(200, 120, $h_canvas)

   PRINT("Da thu A_MOVE (Y=60) va A_DRAG (Y=120). Hay quan sat trang giay Paint!")
ELSE
   PRINT("Hay mo cua so Paint va chon cong cu Co ve truoc khi chay.")
END_IF

HALT
```

### Kết quả của `A_IFPIXELIN` khi điểm màu khớp nằm ở cột `x = 0`

- **Câu hỏi cần kiểm tra:** Trong `A_IFPIXELIN`, khi tìm thấy điểm ảnh tại đúng mép trái của cửa sổ/phần tử (tức `$_return1 = $A_x0`, làm `$A_return1 = $_return1 - $A_x0 = 0`), giá trị `$A_return1` bằng `0` có trùng với giá trị trả về khi không tìm thấy màu (`$A_return1 = 0`) hay không.

```cms
#include "alt_winmode.cms"

LOGCLEAR
LOGSHOW(1)

$w = WNDFIND("Notepad")
IF($w > 0)
   WNDPOS($w, 100, 100)
   WNDSIZE($w, 400, 300)
   WAITMS(300)
   $h_edit = HGET(250, 250)

   // Chụp vùng phần tử soạn thảo và lấy mã màu thực tế tại cột tương đối x = 0, y = 10
   A_GETSCREEN(0, 0, 100, 100, $h_edit)
   A_PXL(0, 10, $h_edit)
   $mau_cot_0 = $A_return1

   // Tìm chính mã màu đó tại vùng bắt đầu từ cột 0: (0, 10) -> (50, 20)
   A_IFPIXELIN(0, 10, 50, 20, $mau_cot_0, $h_edit)
   PRINT("Tim mau co that o cot x = 0 -> $A_return1 = ", $A_return1, ", $A_return2 = ", $A_return2)
   IF($A_return1 = 0)
      PRINT("KET LUAN: Khi mau nam o cot x = 0, $A_return1 bang 0 (giong het truong hop khong tim thay).")
   END_IF
ELSE
   PRINT("Hay mo Notepad truoc khi chay.")
END_IF

HALT
```

### Gọi `A_SCANPXL` hai lần liên tiếp mà không `UNDEFINE($A_var)`

- **Câu hỏi cần kiểm tra:** Nếu gọi `A_SCANPXL` hai lần liên tiếp mà không gọi `UNDEFINE($A_var)` ở giữa, mảng `$A_var` có bị nối thêm phần tử và các phần tử của lần 1 có bị trừ `$A_x0, $A_y0` lần thứ hai hay không.

```cms
#include "alt_winmode.cms"

LOGCLEAR
LOGSHOW(1)

$w = WNDFIND("Notepad")
IF($w > 0)
   WNDPOS($w, 100, 100)
   WNDSIZE($w, 400, 300)
   WAITMS(300)
   $h_edit = HGET(250, 250)

   A_GETSCREEN(0, 0, 50, 50, $h_edit)
   A_PXL(10, 10, $h_edit)
   $mau = $A_return1

   UNDEFINE($A_var)
   A_SCANPXL(10, 10, 12, 10, $mau, $h_edit)
   $size_lan_1 = ARRSIZE($A_var)
   $x_lan_1 = $A_var[0]

   // Gọi lần 2 liên tiếp KHÔNG có UNDEFINE($A_var)
   A_SCANPXL(10, 10, 12, 10, $mau, $h_edit)
   $size_lan_2 = ARRSIZE($A_var)
   $x_lan_2 = $A_var[0]

   PRINT("Lan 1: ARRSIZE = ", $size_lan_1, ", $A_var[0] = ", $x_lan_1)
   PRINT("Lan 2 (khong UNDEFINE): ARRSIZE = ", $size_lan_2, ", $A_var[0] = ", $x_lan_2)
   IF($x_lan_2 != $x_lan_1)
      PRINT("KET LUAN: Goi A_SCANPXL lan 2 khong UNDEFINE lam toa do cu bi tru $A_x0 hai lan!")
   END_IF
ELSE
   PRINT("Hay mo Notepad truoc khi chay.")
END_IF

HALT
```

### Đọc màu bằng `A_GETSCREEN` và `A_PXL` khi cửa sổ bị cửa sổ khác che khuất

- **Câu hỏi cần kiểm tra:** Vì `A_GETSCREEN` và `A_PXL` chỉ quy đổi tọa độ bằng `WNDGETINFO` rồi gọi `GETSCREEN` ở chế độ màn hình thường, hãy kiểm tra khi kéo một cửa sổ khác đè lên che khuất cửa sổ đích thì `A_PXL` đọc ra màu của cửa sổ đích hay màu của cửa sổ đang nằm đè ở phía trên.

```cms
#include "alt_winmode.cms"

LOGCLEAR
LOGSHOW(1)

$w = WNDFIND("Notepad")
IF($w > 0)
   WNDPOS($w, 100, 100)
   WNDSIZE($w, 400, 300)
   WAITMS(300)
   $h_edit = HGET(250, 250)

   // Bước 1: Đọc màu khi Notepad chưa bị che
   A_GETSCREEN(0, 0, 200, 200, $h_edit)
   A_PXL(50, 50, $h_edit)
   $mau_truoc = $A_return1
   PRINT("Ma mau A_PXL(50, 50) khi Notepad CHUA bi che: ", $mau_truoc)

   PRINT("-> Trong 5 giay toi, hay keo mot cua so khac co mau khac DE LEN che khuat Notepad...")
   WAIT(5)

   // Bước 2: Đọc lại màu sau khi Notepad đã bị cửa sổ khác đè lên
   A_GETSCREEN(0, 0, 200, 200, $h_edit)
   A_PXL(50, 50, $h_edit)
   $mau_sau = $A_return1
   PRINT("Ma mau A_PXL(50, 50) SAU KHI Notepad bi che: ", $mau_sau)

   IF($mau_sau != $mau_truoc)
      PRINT("KET LUAN: Khi cua so bi che, A_GETSCREEN / A_PXL doc mau cua cua so nam de phia tren (cua so dich phai hien tren man hinh).")
   END_IF
ELSE
   PRINT("Hay mo Notepad truoc khi chay.")
END_IF

HALT
```
