# Cần kiểm tra trên Windows

Trang này tổng hợp các điểm có trạng thái `🟠 Chưa thống nhất` và các điểm cần chạy kiểm chứng trong tài liệu (đối chiếu giữa `help.chm` chính thức v4.13.014 và sách của Chô tô, các điểm help tự mâu thuẫn hoặc help không nói rõ, cùng các kịch bản cẩm nang), kèm theo hướng dẫn hoặc đoạn script để kiểm chứng trực tiếp trên máy Windows.

## Tóm tắt các mục cần kiểm chứng

| Mục | Sách của Chô tô | Help chính thức (`help.chm`) | Đánh giá |
|---|---|---|---|
| [`THREAD`](/lenh/cau-truc#thread-end-thread)<br>*(tr. 82)* | Không ghi `init_state` thì luồng đang tắt (`0`), phải bật bằng `SETTHREAD`. | Ví dụ dùng `thread(t1)` không tham số `init_state` và mô tả các luồng cùng chạy ngay. Muốn luồng dừng sẵn lúc đầu thì ví dụ khác viết `thread(t1, 0)`. | **Mâu thuẫn**<br>Suy từ ví dụ của help (help không ghi thẳng giá trị mặc định trong dòng mô tả tham số). |
| [`SETTHREAD`](/lenh/cau-truc#setthread)<br>*(tr. 83)* | Chỉ nêu hai giá trị: `0` tắt luồng, `1` bật luồng. | Có 3 giá trị: `0` tạm dừng; `1` chạy tiếp từ chỗ đã dừng; **`2`** tạm dừng và lần sau chạy lại từ đầu. | **Sách thiếu**<br>"Tắt" trong sách thực chất là tạm dừng. |
| [`$_ms`](/khai-niem/ngon-ngu#bang-bien-he-thong)<br>*(tr. 26)* | Đếm từ khi Clickermann chạy. | Bộ đếm của Windows, tính từ lúc hệ điều hành khởi động. | **Mâu thuẫn**<br>[Lịch sử phiên bản](/phu-luc/lich-su) có sửa lỗi "máy chạy quá 49 ngày", khớp với cách nói của help (suy luận). |
| [`GETVAR`](/lenh/so#getvar)<br>*(tr. 42)* | Tên biến không cần ngoặc kép. Ví dụ: `define($var, 5)`, `getvar($x)`, `print($x)`. | Tham số là **chuỗi** chứa tên biến, hàm trả về giá trị: `$tmp = getvar($triple_var)` với `$triple_var` mang chuỗi `"$var"`. | **Ví dụ sách sai**<br>Khai báo `$var` nhưng đọc `$x`, và bỏ qua giá trị trả về của hàm. |
| [`SETVAR`](/lenh/so#setvar)<br>*(tr. 42)* | Ví dụ: `define($var)` rồi `setvar("$x", 5)`. | Biến có tên đã cho phải tồn tại trước khi gọi. | **Ví dụ lệch**<br>Dấu ngoặc kép thì đúng, nhưng khai báo nhầm biến. |
| [`SCREENSHOT`, `SCREENSHOTEX`](/lenh/man-hinh#screenshotex)<br>*(tr. 94)* | Lưu vào thư mục `screen`; ở `SCREENSHOT` nói lưu dạng jpeg; ở `SCREENSHOTEX` nói lưu dạng bmp dù cũng liệt kê `format` 1 là jpeg. | Lưu vào thư mục `screens`; `SCREENSHOT` lưu `.bmp`; ở `SCREENSHOTEX` thì `format` `0` là bmp, `1` là jpeg nhưng phần ghi chú chỉ ghi tên dạng `pref0000.bmp`, không nói rõ đuôi file khi `format = 1`. | **Khác tên thư mục & cần thử đuôi file** |
| [`$_xmax`, `$_ymax`, `$_xmin`, `$_ymin`](/khai-niem/toa-do#hai-bien-he-thong-xmax-va-ymax)<br>*(tr. 26)* | Tọa độ lớn nhất của cửa sổ. | Tính từ cấu hình màn hình desktop. | **Cần thử**<br>Có thể khác nhau khi đang khóa vào cửa sổ. |
| [`CALL`](/lenh/kich-ban#call)<br>*(tr. 104)* | DLL để cùng thư mục file script. | Trang `CALL` (help, mục Script và plugin) ghi `%Clickermann%/plugins`; trang [Plugin](/khai-niem/plugin) (help, bài Plugin) ghi cạnh script hoặc thư mục con, không tìm thấy thì âm thầm kết thúc. | **Help tự mâu thuẫn**<br>Sách khớp bài Plugin. |
| [`WNDSETINFO`](/lenh/winapi#wndsetinfo)<br>*(tr. 117)* | Truyền số trực tiếp. | Ví dụ chỉ truyền biến. | **Cần thử**<br>Không hẳn mâu thuẫn. |
| [Trình duyệt, máy ảo](/khai-niem/khoa-cua-so#gioi-han-va-giai-phap-dung-may-ao)<br>*(tr. 19)* | Thuộc loại cửa sổ không nhận tool. | Khung Flash trong trình duyệt là một "cửa sổ" riêng, khóa được hay không tùy cách ứng dụng được viết. Với máy ảo, help gợi ý cài tool bên trong máy ảo. | **Sách nói quá chung** |
| [`LOGWRITE` và `#logfile`](/lenh/nhat-ky#logwrite-print) | — | Help, mục Xuất thông tin ghi khi có `#logfile` thì ghi thêm vào `%thu_muc_du_an%/log.txt`; phần Giới thiệu ngôn ngữ và Lịch sử phiên bản cho phép đặt tên tùy ý như `#logfile "debug.txt"`. | **Help chưa thống nhất**<br>Cần thử `#logfile` không kèm tên file có ghi ra `log.txt` không. |
| [`ROUND`](/lenh/so#round) | — | Help, mục Làm việc với số ghi "làm tròn theo hướng ra xa số 0" rồi giải thích `prec = 2` là hàng trăm, `prec = -2` là hàng phần trăm, theo quy tắc chuẩn `0.5`. | **Cần thử**<br>Kiểm tra `ROUND(-1.5, 0)` ra `-2` hay `-1`. |
| [`READMEM`, `WRITEMEM` (`addr`)](/lenh/kich-ban#readmem) | — | Help, mục Script và plugin: dòng tham số của `READMEM` ghi `addr` là chuỗi; phần ghi chú của cả hai lệnh lại ghi `addr` là số nguyên thông thường ở dạng thập phân hoặc thập lục phân. | **Help tự mâu thuẫn**<br>Chỉ ghi nhận mâu thuẫn tài liệu, không viết script kiểm tra. |
| [`GETMESSAGE`](/lenh/winapi#getmessage) | — | Ví dụ trong help, mục WinAPI gọi `POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng một lượt chạy và không có `HALT`. | **Cần thử**<br>`POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng lượt có nhận được không. |
| [`FOR` lồng nhau](/lenh/cau-truc#for-end-cyc) | — | Help, mục Cấu trúc lệnh nói biến giữ giá trị nếu không gán `=value`, nhưng ví dụ vòng lặp lồng nhau viết `FOR($x, $x < 3)` và `FOR($y, $y < 3)`. | **Cần thử**<br>In ra 9 dòng hay chỉ 3 dòng. |
| [Tên biến hoa / thường](/khai-niem/ngon-ngu#bien-va-kieu-du-lieu) | — | Help không nói rõ; Lịch sử phiên bản ghi `$_DATE_Y`, còn phần Giới thiệu ngôn ngữ ghi `$_date_y`. | **Help không nói rõ**<br>Cần thử `$Var` và `$var`. |
| [Khung chế độ chạy](/bat-dau/man-hinh-chinh#bang-thong-tin-va-che-do-chay) | — | Help, bài Màn hình chính nói có khung trên cửa sổ chính; Lịch sử phiên bản (v4.7.000) nói đã bỏ khỏi form và (v4.7.000 SE) nói trở lại dạng cửa sổ riêng. | **Help tự mâu thuẫn**<br>Cần mở giao diện v4.13.014 để kiểm tra. |
| [Chỉ thị `#define`](/khai-niem/ngon-ngu#chi-thi-tien-xu-ly-preprocessor-directives) | — | Help, phần Giới thiệu ngôn ngữ chỉ ghi mẫu `#define <tìm>:<thay>`, không có ví dụ cụ thể. | **Cần thử**<br>Kiểm tra ví dụ `#define @pause:WAITMS(100)`. |
| [Nơi lưu ảnh `Alt + G`](/cam-nang/tim-anh#buoc-1-chuan-bi-tep-anh-mau-bmp) | — | Help, bài Trình soạn thảo chỉ nói ảnh `100×100` được lưu dạng `.bmp`, không nói rõ lưu ở thư mục nào. | **Help không nói rõ**<br>Cần nhấn `Alt + G` để xem thư mục lưu. |
| [Kéo chuột vẽ trong Paint](/cam-nang/tu-ve) | — | Ví dụ kéo thả trong help, mục Chuột chỉ có `ldown`, `waitms`, `lup` (không có `MOVE`). | **Suy luận cần thử**<br>Kiểm tra `LDOWN` -> `MOVE` -> `LUP` trong Paint. |
| [Các kịch bản cẩm nang](/cam-nang/click-theo-lich) | — | 5 trang trong `cam-nang/*` được biên soạn theo cú pháp help nhưng chưa chạy trên máy Windows. | **Cần thử thực tế** |

---

## Trạng thái mặc định của THREAD khi bỏ qua init_state

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread)

### Hai cách hiểu hiện tại

1. **Theo ví dụ trong help:** Trong help, mục Cấu trúc lệnh, phần `THREAD ... END_THREAD` đưa ra ví dụ khai báo `thread(t1)` và `thread(t2)` mà không truyền `init_state`, kèm lời giải thích rằng cả 3 luồng (script chính và 2 luồng con) đều chạy đồng thời và in thông báo theo nhịp riêng. Sang mục `SETTHREAD`, để minh họa một luồng đang dừng sẵn, help mới viết rõ `thread(t1, 0)`. Từ đó suy ra khi bỏ trống `init_state`, giá trị mặc định là `1` (chạy ngay).
2. **Theo sách của Chô tô (tr. 82):** Sách ghi rằng nếu không truyền `init_state` thì chương trình hiểu là luồng đang tắt (`0`), chưa chạy và cần gọi `SETTHREAD(ten_luong, 1)` mới bắt đầu chạy.

### Script kiểm tra trên Windows

Lưu ý khi viết script kiểm tra: không gán `$da_chay = 0` ở script chính vì nếu luồng chạy ngay và đặt `$da_chay = 1` trước, dòng gán ở script chính có thể ghi đè lại thành `0` dẫn tới kết luận ngược (theo help, phần Giới thiệu ngôn ngữ, biến chưa từng được gán sẽ tự động đọc ra `0`). Trong thân luồng cũng dùng vòng chờ ngắn đặt lại cờ thay vì `WAIT(10)`:

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

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#bang-bien-he-thong)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (phần Giới thiệu ngôn ngữ):** `$_ms` là bộ đếm thời gian hệ thống của Windows, đếm số mili-giây tính từ **thời điểm hệ điều hành Windows khởi động**. Trong [Lịch sử phiên bản](/phu-luc/lich-su) v4.13.014 cũng có ghi nhận sửa lỗi sập khi hệ thống chạy quá 49 ngày không khởi động lại (Suy luận theo kiến thức Windows: bộ đếm mili-giây 32-bit không dấu của Windows tràn sau `2^32` ms ≈ 49,7 ngày).
2. **Theo sách của Chô tô (tr. 26):** Ghi rằng `$_ms` đếm thời gian tính từ **lúc chương trình Clickermann bắt đầu chạy**.

### Script kiểm tra trên Windows

Cách kiểm chứng chắc chắn nhất: chạy script dưới đây lần 1 để ghi giá trị `$_ms` vào tệp `kiemtra_ms.ini`, sau đó **đóng hẳn chương trình Clickermann rồi mở lại ngay** và chạy lại script lần 2 để so sánh hai giá trị:

```cms
// Kiểm tra gốc thời gian của $_ms bằng cách đóng và mở lại Clickermann
LOGCLEAR
LOGSHOW(1)

$ms_hien_tai = $_ms
$ms_lan_truoc = INT(INIREAD("kiemtra_ms.ini", "ms_lan_1", "TEST"))

IF($ms_lan_truoc = 0)
   INIWRITE("kiemtra_ms.ini", "ms_lan_1", $ms_hien_tai, "TEST")
   LOGWRITE("Lan chay 1 -> Da luu $_ms = ", $ms_hien_tai, " ms.")
   LOGWRITE("Bay gio hay DONG HAN Clickermann, mo lai chuong trinh va chay script nay lan 2!")
ELSE
   LOGWRITE("Lan chay 1 (truoc khi dong tool): ", $ms_lan_truoc, " ms")
   LOGWRITE("Lan chay 2 (sau khi mo lai tool): ", $ms_hien_tai, " ms")
   // Xóa giá trị cũ để có thể thử lại từ đầu nếu cần
   INIWRITE("kiemtra_ms.ini", "ms_lan_1", 0, "TEST")
   IF($ms_hien_tai > $ms_lan_truoc)
      LOGWRITE("KET LUAN: $_ms tiep tuc tang sau khi mo lai tool -> Tinh tu luc Windows khoi dong (khop voi help).")
   ELSE
      LOGWRITE("KET LUAN: $_ms quay ve so nho sau khi mo lai tool -> Tinh tu luc Clickermann chay (khop voi sach Cho to, tr. 26).")
   END_IF
END_IF

HALT
```

---

## Cách truyền tham số và giá trị trả về của GETVAR

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`GETVAR`](/lenh/so#getvar)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (mục Làm việc với số):** `GETVAR($var)` là một **hàm** nhận tham số là **chuỗi chứa tên biến** (ví dụ `"$goc"`) và trả về giá trị của biến đó.
2. **Theo sách của Chô tô (tr. 42):** Sách ghi tên biến không cần dấu ngoặc kép và viết ví dụ `define($var, 5)`, `getvar($x)`, `print($x)` (vừa khai báo lệch tên biến, vừa không hứng giá trị trả về của hàm).

### Script kiểm tra trên Windows

Đoạn script dưới đây thử cả hai cách (truyền chuỗi tên biến `"$goc"` theo help và truyền trực tiếp biến `$goc` không ngoặc kép theo sách) rồi in kết luận:

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
$r2 = GETVAR($goc)
LOGWRITE("Cach 2 - GETVAR($goc) khong ngoac kep: ", $r2)

IF(($ket_qua = 42) & ($r2 != 42))
   LOGWRITE("KET LUAN: GETVAR nhan chuoi chua ten bien (khop voi help).")
END_IF
IF($r2 = 42)
   LOGWRITE("KET LUAN: GETVAR($goc) khong ngoac kep cung tra ve 42 (khop voi sach).")
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

1. **Theo help chính thức (mục Màn hình):** Cả `SCREENSHOT` và `SCREENSHOTEX` đều lưu ảnh vào thư mục con `screens` (có chữ `s` ở cuối) bên trong thư mục của script hiện tại. `SCREENSHOT` lưu ảnh dạng `.bmp`. Với `SCREENSHOTEX`, tham số `format` bằng `0` là BMP, bằng `1` là JPEG; tuy nhiên ở phần ghi chú, help chỉ ghi tên file dạng `pref0000.bmp`, không nói rõ đuôi file khi `format = 1`.
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

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Hệ tọa độ màn hình và phần tử](/khai-niem/toa-do#hai-bien-he-thong-xmax-va-ymax), [Ngôn ngữ script](/khai-niem/ngon-ngu#bang-bien-he-thong)

### Hai cách hiểu hiện tại

1. **Theo help chính thức (phần Giới thiệu ngôn ngữ):** Bảng biến hệ thống mô tả `$_xmax`, `$_ymax`, `$_xmin`, `$_ymin` là giá trị tọa độ X, Y lớn nhất và nhỏ nhất cho phép, được **tính từ cấu hình màn hình desktop**.
2. **Theo sách của Chô tô (tr. 26):** Ghi rằng `$_xmax` và `$_ymax` là **tọa độ lớn nhất của cửa sổ**.

### Script kiểm tra trên Windows

Mở một cửa sổ Notepad nhỏ (ví dụ kích thước `400×300`), sau đó chạy script dưới đây để so sánh cả 4 biến `$_xmin`, `$_ymin`, `$_xmax`, `$_ymax` trước và sau khi bật chế độ khóa cửa sổ bằng `HSET`:

```cms
// Kiểm tra $_xmin, $_ymin, $_xmax, $_ymax khi tắt và khi bật chế độ khóa cửa sổ
LOGCLEAR
LOGSHOW(1)

// 1. Khi chưa khóa cửa sổ (chế độ thường)
HSET(0, 0)
$xmax_thuong = $_xmax
$ymax_thuong = $_ymax
LOGWRITE("Che do thuong -> $_xmin=", $_xmin, ", $_ymin=", $_ymin, ", $_xmax=", $_xmax, ", $_ymax=", $_ymax)

// 2. Tìm cửa sổ Notepad, đặt kích thước 400x300 và khóa vào cửa sổ đó
$h = WNDFIND("Notepad")
IF($h > 0)
   WNDSIZE($h, 400, 300)
   WAITMS(300)
   HSET($h, 1)
   LOGWRITE("Khi khoa cua so Notepad (400x300) -> $_xmin=", $_xmin, ", $_ymin=", $_ymin, ", $_xmax=", $_xmax, ", $_ymax=", $_ymax)
   IF(($_xmax = $xmax_thuong) & ($_ymax = $ymax_thuong))
      LOGWRITE("KET LUAN: $_xmax, $_ymax giu nguyen theo man hinh desktop (khop voi help).")
   ELSE
      LOGWRITE("KET LUAN: $_xmax, $_ymax thay doi theo kich thuoc cua so dang khoa (khop voi sach tr. 26).")
   END_IF
   HSET(0, 0)
ELSE
   LOGWRITE("Hay mo cua so Notepad truoc khi chay script nay.")
END_IF

HALT
```

---

## Thư mục nạp plugin DLL của CALL

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`CALL`](/lenh/kich-ban#call) · **Trang khái niệm:** [Plugin mở rộng](/khai-niem/plugin)

### Ba nguồn thông tin hiện tại

1. **Theo trang lệnh `CALL` (help, mục Script và plugin):** Đường dẫn tệp `filename` trong `CALL("filename", ...)` được tính tương đối từ thư mục `%Clickermann%/plugins`.
2. **Theo bài viết Plugin (help, bài Plugin):** Tệp DLL của plugin đặt trong thư mục dự án (nằm cạnh tệp script đang chạy hoặc trong thư mục con của dự án); nếu không tìm thấy tệp theo tên đã cho ở đó thì lệnh `CALL` âm thầm kết thúc.
3. **Theo sách của Chô tô (tr. 104):** Chỉ ghi rằng tệp DLL đặt cùng thư mục với file script.

### Script kiểm tra trên Windows

Lưu ý: người kiểm tra cần tự chuẩn bị trước một tệp plugin `plugin_test.dll` xuất hàm `int execute(int* _arr, int _size)` trả về `$_arr[0] * 2` (tức nhân đôi tham số đầu tiên truyền vào). Không gán giá trị trực tiếp vào biến hệ thống `$_return1` vì help (phần Giới thiệu ngôn ngữ) khuyến cáo rất không nên gán vào biến hệ thống.

Đặt tệp `plugin_test.dll` lần lượt ở thư mục `%Clickermann%/plugins` (Lần 1) và ở cùng thư mục với file script `.cms` (Lần 2), mỗi lần chạy đoạn script dưới đây:

```cms
// Kiểm tra vị trí nạp tệp DLL của lệnh CALL
// Yêu cầu: cần tự chuẩn bị tệp plugin_test.dll trả về (tham số đầu * 2)
LOGCLEAR
LOGSHOW(1)

$so_ngau_nhien = RND(10, 99)
$ky_vong = $so_ngau_nhien * 2

CALL("plugin_test.dll", $so_ngau_nhien)
LOGWRITE("Tham so truyen vao: ", $so_ngau_nhien, " | Ky vong $_return1 = ", $ky_vong)
LOGWRITE("Gia tri $_return1 thuc te: ", $_return1)

IF($_return1 = $ky_vong)
   LOGWRITE("KET LUAN: CALL da nap va chay thanh cong plugin_test.dll tai vi tri dat file hien tai!")
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

### Script kiểm tra trên Windows

Mở sẵn một cửa sổ Notepad trên Windows rồi chạy script dưới đây để xem `WNDSETINFO` có chấp nhận số trực tiếp hay bắt buộc phải truyền biến:

```cms
// Kiểm tra truyền số trực tiếp vào WNDSETINFO trên cửa sổ Notepad
LOGCLEAR
LOGSHOW(1)

$hwnd = WNDFIND("Notepad")
IF($hwnd > 0)
   // Thử truyền trực tiếp các số: X=50, Y=50, Rộng=400, Cao=300
   WNDSETINFO($hwnd, 50, 50, 400, 300)
   WAITMS(500)

   // Đọc lại thông tin cửa sổ để kiểm chứng
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

1. **Theo sách của Chô tô (tr. 19):** Sách liệt kê chung trình duyệt web và máy ảo vào nhóm cửa sổ không nhận tool khi dùng chế độ khóa cửa sổ.
2. **Theo help chính thức (bài Khóa cửa sổ và phần FAQ):**
   - **Với trình duyệt:** Help giải thích mỗi thành phần bên trong trình duyệt (như khung Flash trong cửa sổ trình duyệt) là một phần tử con riêng có `HWND` riêng; việc chế độ khóa cửa sổ có hoạt động hay không **tùy cách ứng dụng được viết** (ví dụ trong help, phần FAQ: có trường hợp chạy được trên Firefox nhưng không chạy trên Google Chrome).
   - **Với máy ảo (MS Virtual PC, VMware...):** Help gợi ý cài hệ điều hành, ứng dụng và Clickermann **vào bên trong máy ảo**, rồi chạy Clickermann ở chế độ thường bên trong máy ảo đó và thu nhỏ cửa sổ máy ảo xuống trên máy thật để vừa tự động hóa vừa làm việc khác.

### Script kiểm tra trên Windows

Để kiểm tra xem một phần tử trong trình duyệt có đọc được màu và nhận thao tác bấm chuột ở chế độ khóa cửa sổ khi bị cửa sổ khác che khuất hay không:

1. Mở trình duyệt tới một trang có nút bấm hoặc ô nhập liệu tại tọa độ tương đối `(100, 100)` của phần tử nội dung.
2. Đưa trỏ chuột vào phần tử nội dung của trình duyệt và nhấn `Alt + W` để khóa.
3. Mở một cửa sổ khác (ví dụ Notepad) **đặt đè lên che khuất vị trí `(100, 100)`** của trình duyệt (nhưng không thu nhỏ trình duyệt xuống Taskbar).
4. Chạy đoạn script dưới đây và kiểm tra cả màu sắc đọc được lẫn việc nút/ô tại `(100, 100)` trong trình duyệt có thực sự nhận được cú bấm `LCLICK` hay không:

```cms
// Kiểm tra đọc màu và bấm chuột trên phần tử trình duyệt đang khóa ($_hwnd) khi bị cửa sổ khác che
LOGCLEAR
LOGSHOW(1)

IF($_hwnd > 0)
   LOGWRITE("Dang khoa vao phan tu HWND = ", $_hwnd)
   LOGWRITE("Hay dam bao da dat mot cua so khac che len trinh duyet (khong thu nho trinh duyet)...")
   WAIT(2)
   GETSCREEN
   $mau = PXL(100, 100)
   LOGWRITE("Ma mau doc duoc tai (100, 100) cua phan tu: ", $mau)
   LOGWRITE("-> Hay doi chieu voi kinh lup trong Trinh soan thao xem mau va hinh anh co hien dung khong.")
   LCLICK(100, 100)
   LOGWRITE("Da goi LCLICK(100, 100). Hay kiem tra xem nut/o tai (100, 100) trong trinh duyet co nhan thao tac bam khong.")
ELSE
   LOGWRITE("Chua bat che do khoa cua so! Hay tro chuot vao phan tu va nhan Alt + W truoc.")
END_IF

HALT
```

---

## Tên file nhật ký của LOGWRITE và chỉ thị #logfile

**Trạng thái:** 🟠 Chưa thống nhất · **Trang lệnh:** [`LOGWRITE (PRINT)`](/lenh/nhat-ky#logwrite-print) · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#chi-thi-tien-xu-ly-preprocessor-directives)

### Hai chỗ ghi trong help

1. **Theo bảng chỉ thị tiền xử lý (help, phần Giới thiệu ngôn ngữ) và Lịch sử phiên bản (v4.13.014):** Bản v4.13.014 nâng cấp `#logfile` cho phép đặt tên tệp nhật ký tùy ý (ví dụ `#logfile "debug.txt"`).
2. **Theo mục `LOGWRITE` (help, mục Xuất thông tin):** Ghi rằng khi có chỉ thị `#logfile` thì thông báo được ghi thêm vào file `log.txt` trong thư mục dự án (`%thu_muc_du_an%/log.txt`). Câu hỏi cần kiểm tra là khi viết `#logfile` **không kèm tên file** thì chương trình có tự ghi vào `log.txt` hay không.

### Script kiểm tra trên Windows

Lưu lần lượt hai đoạn script dưới đây vào thư mục dự án và chạy thử:

**Biến thể A — `#logfile` không kèm tên file:**

```cms
#logfile

LOGCLEAR
LOGSHOW(1)
LOGWRITE("Thu nghiem #logfile khong kem ten file")

GETFILELIST($ds_txt, "*.txt")
FOR($i=0, $i < ARRSIZE($ds_txt))
   LOGWRITE("Tim thay file .txt: ", $ds_txt[$i])
END_CYC

HALT
```

**Biến thể B — `#logfile "debug.txt"` có đặt tên file riêng:**

```cms
#logfile "debug.txt"

LOGCLEAR
LOGSHOW(1)
LOGWRITE("Thu nghiem #logfile co ten file debug.txt")

GETFILELIST($ds_txt, "*.txt")
FOR($i=0, $i < ARRSIZE($ds_txt))
   LOGWRITE("Tim thay file .txt: ", $ds_txt[$i])
END_CYC

HALT
```

---

## Cách làm tròn số âm của ROUND

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang lệnh:** [`ROUND`](/lenh/so#round)

### Mô tả trong help

Trong help, mục Làm việc với số (lệnh `ROUND`), help ghi: "Việc làm tròn diễn ra theo hướng ra xa số 0. Tức là `prec = 2` sẽ làm tròn số đến hàng trăm, còn `prec = -2` đến hàng phần trăm (hai chữ số sau dấu chấm). Việc làm tròn diễn ra theo quy tắc chuẩn `0.5`."

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

- Trong help, mục Script và plugin (phần liệt kê tham số của `READMEM`), help ghi `addr` là "chuỗi, địa chỉ bộ nhớ".
- Tuy nhiên, ngay ở phần ghi chú bên dưới của cả `READMEM` và `WRITEMEM` cũng như trong ví dụ của help (`0x0006F2B7`), help lại ghi rõ địa chỉ là "số nguyên thông thường ở dạng thập phân hoặc thập lục phân" (không đặt trong dấu ngoặc kép).

*(Theo quy tắc của tài liệu, mục này chỉ ghi nhận điểm tự mâu thuẫn trong help, không viết script kiểm tra cho `READMEM` và `WRITEMEM`).*

---

## POSTMESSAGE rồi GETMESSAGE ngay trong cùng lượt

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang lệnh:** [`GETMESSAGE`](/lenh/winapi#getmessage)

### Câu hỏi cần kiểm tra

Ví dụ trong help, mục WinAPI gọi `POSTMESSAGE($h, 1024, 123, 321)` rồi gọi `GETMESSAGE($var1, $var2)` ngay ở dòng tiếp theo và không có lệnh `HALT` ở cuối. Cần kiểm tra xem `POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng một lượt chạy (vòng đầu tiên) có nhận được thông điệp `123, 321` ngay lập tức không, hay cần chờ ngắn / sang lượt lặp tiếp theo mới nhận được.

### Script kiểm tra trên Windows

```cms
LOGCLEAR
LOGSHOW(1)

$h = WNDFIND("Clickermann")
POSTMESSAGE($h, 1024, 123, 321)
GETMESSAGE($var1, $var2, $isnew)
PRINT("Ngay trong cung luot -> isnew:", $isnew, " wParam:", $var1, " lParam:", $var2)

IF($isnew = 1)
   PRINT("KET LUAN: GETMESSAGE nhan duoc thong diep ngay lap tuc sau POSTMESSAGE.")
ELSE
   WAITMS(100)
   GETMESSAGE($var1, $var2, $isnew)
   PRINT("Sau WAITMS(100) -> isnew:", $isnew, " wParam:", $var1, " lParam:", $var2)
   PRINT("KET LUAN: Can co do tre hoac sang luot sau GETMESSAGE moi nhan duoc thong diep.")
END_IF
HALT
```

---

## Vòng lặp FOR lồng nhau không gán giá trị đầu

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang lệnh:** [`FOR ... END_CYC`](/lenh/cau-truc#for-end-cyc)

### Câu hỏi cần kiểm tra

Trong help, mục Cấu trúc lệnh (và Lịch sử phiên bản v4.11.000), help mô tả rằng nếu biến đếm `$var` đã được khởi tạo trước khi vào vòng lặp `FOR` và câu lệnh `FOR` không ghi `=value`, vòng lặp sẽ không tự đưa biến về `0` mà bắt đầu từ giá trị hiện tại của biến đó (trong khi trước đó ở bản v4.2.000, Lịch sử phiên bản từng ghi tham số `FOR` được đưa về `0` sau khi kết thúc vòng lặp). Ngay ở ví dụ vòng lặp lồng nhau trong help, mục Cấu trúc lệnh, help lại viết `FOR($x, $x < 3)` bên ngoài và `FOR($y, $y < 3)` bên trong mà không viết `$y=0`.

Cần chạy thử để xem đoạn code nguyên bản trong help in ra đủ `9` dòng hay chỉ `3` dòng:

### Script kiểm tra trên Windows

```cms
LOGCLEAR
LOGSHOW(1)

$so_dong = 0
LOGWRITE("=== Chay thu vi du FOR long nhau nguyen ban trong help ===")
FOR($x, $x < 3)
   FOR($y, $y < 3)
      PRINT($x, ":", $y)
      INC($so_dong)
   END_CYC
END_CYC

LOGWRITE("Tong so dong da in: ", $so_dong)
IF($so_dong = 9)
   LOGWRITE("KET LUAN: In du 9 dong (vong FOR ben trong van chay lai tu 0 o moi luot ngoai).")
END_IF
IF($so_dong = 3)
   LOGWRITE("KET LUAN: Chi in 3 dong (bien $y giu gia tri 3 sau luot dau, can viet FOR($y=0, $y < 3)).")
END_IF

HALT
```

---

## Tên biến có phân biệt chữ hoa và chữ thường không

**Trạng thái:** 🟠 Chưa thống nhất · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#bien-va-kieu-du-lieu)

### Điểm help không nói rõ

Trong help, phần Giới thiệu ngôn ngữ, help chỉ quy định tên biến bắt đầu bằng `$` nối với chữ cái Latin `a..z`, chữ số `0..9` và `_`, không nói rõ tên biến có phân biệt chữ hoa và chữ thường hay không. (Suy luận: trong help, Lịch sử phiên bản ghi tên biến hệ thống là `$_DATE_Y`, còn trong phần Giới thiệu ngôn ngữ lại ghi là `$_date_y`, nên nhiều khả năng không phân biệt chữ hoa và chữ thường).

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

- Trong help, bài Màn hình chính, help ghi ngoài các nút bấm, cửa sổ chính còn có khung thông tin chế độ khóa cửa sổ và **khung thiết lập chế độ thực thi script**.
- Tuy nhiên trong help, Lịch sử phiên bản (bản v4.7.000), lịch sử ghi đã bỏ các chế độ hoạt động khỏi cửa sổ chính; và đến bản v4.7.000 SE lại ghi các chế độ thực thi trở lại dưới dạng **một cửa sổ riêng**.

### Cách kiểm tra trên Windows

Mở chương trình Clickermann v4.13.014 trên máy Windows và quan sát trực tiếp:

1. Xem các tùy chọn chế độ chạy script nằm ngay trên cửa sổ chính hay mở ra một cửa sổ phụ riêng khi bấm nút trên hàng nút phía trên.
2. Chụp ảnh giao diện thực tế để bổ sung vào trang [Màn hình chính](/bat-dau/man-hinh-chinh).

---

## Chỉ thị tiền xử lý #define

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang khái niệm:** [Ngôn ngữ script](/khai-niem/ngon-ngu#chi-thi-tien-xu-ly-preprocessor-directives)

### Điểm cần kiểm tra

Trong help, phần Giới thiệu ngôn ngữ, bảng chỉ thị tiền xử lý chỉ ghi ngắn gọn cú pháp `#define <tìm>:<thay>` ("Thay thế một văn bản bằng văn bản khác") mà không có đoạn code ví dụ hoàn chỉnh. Cần chạy thử ví dụ suy luận `#define @pause:WAITMS(100)` trên Windows để xác nhận cách hoạt động:

```cms
#define @pause:WAITMS(100)

LOGCLEAR
LOGSHOW(1)

$t1 = $_ms
@pause
$t2 = $_ms

LOGWRITE("Thoi gian truoc va sau @pause: ", $t2 - $t1, " ms")
LOGWRITE("KET LUAN: Neu script chay khong bao loi va co do tre ~100ms thi #define @pause:WAITMS(100) hoat dong dung.")
HALT
```

---

## Nơi lưu ảnh chụp nhanh 100x100 của phím tắt Alt + G

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang cẩm nang:** [Tìm hình ảnh mẫu trên màn hình](/cam-nang/tim-anh#buoc-1-chuan-bi-tep-anh-mau-bmp)

### Điểm help không nói rõ

Trong help, bài Trình soạn thảo, help mô tả tổ hợp phím `Alt + G` giúp chụp nhanh vùng `100×100` pixel mà kính lúp đang nhìn thấy và lưu ở định dạng `.bmp`, nhưng không nói rõ tệp `.bmp` này được lưu ở thư mục nào (thư mục dự án, thư mục con `screens\` hay thư mục gốc của Clickermann) và tên tệp đặt theo mẫu nào.

### Cách kiểm tra trên Windows

1. Mở một script trong một thư mục dự án, bật [Trình soạn thảo](/bat-dau/trinh-soan-thao) và bật **Kính lúp**.
2. Nhấn tổ hợp phím `Alt + G`.
3. Chạy đoạn script dưới đây để kiểm tra xem tệp `.bmp` mới xuất hiện ở thư mục dự án hay thư mục `screens\`:

```cms
LOGCLEAR
LOGSHOW(1)

GETFILELIST($bmp_du_an, "*.bmp")
GETFILELIST($bmp_screens, "screens\*.bmp")

LOGWRITE("Cac tep .bmp trong thu muc du an: ", ARRSIZE($bmp_du_an))
FOR($i=0, $i < ARRSIZE($bmp_du_an))
   LOGWRITE(" - Thu muc du an: ", $bmp_du_an[$i])
END_CYC

LOGWRITE("Cac tep .bmp trong thu muc screens\: ", ARRSIZE($bmp_screens))
FOR($j=0, $j < ARRSIZE($bmp_screens))
   LOGWRITE(" - screens\: ", $bmp_screens[$j])
END_CYC

HALT
```

---

## Kéo chuột vẽ nét liền bằng LDOWN, MOVE, LUP trong Paint

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Trang cẩm nang:** [Tự động vẽ hình trong Paint](/cam-nang/tu-ve)

### Điểm cần kiểm tra

Trong help, mục Chuột, ví dụ kéo thả chuột của help chỉ viết `ldown(100, 100)`, `waitms(50)`, `lup(200, 200)` mà không có lệnh `MOVE` ở giữa. Trong trang [Tự động vẽ hình trong Paint](/cam-nang/tu-ve), tài liệu suy luận rằng việc giữ `LDOWN` rồi gọi liên tiếp các lệnh `MOVE(x, y)` kèm `WAITMS` trước khi `LUP` sẽ làm Paint vẽ các đoạn thẳng nối tiếp nhau.

### Cách kiểm tra trên Windows

1. Mở chương trình **Paint**, chọn công cụ **Cọ vẽ (Brushes)** màu đen, đặt cửa sổ Paint sao cho vùng giấy trắng bao phủ tọa độ `(200, 200)` đến `(400, 350)`.
2. Chạy thử cả hai cách trong đoạn script dưới đây:

```cms
// Kiểm tra vẽ nét kéo chuột trong Paint: có MOVE và không có MOVE
WAIT(2)

// 1. Cách viết trong ví dụ của help (LDOWN -> WAITMS -> LUP tại tọa độ mới, không có MOVE)
LDOWN(200, 200)
WAITMS(50)
LUP(350, 200)

WAIT(1)

// 2. Cách viết có MOVE ở giữa (LDOWN -> MOVE -> LUP) tại dòng bên dưới (Y = 260)
LDOWN(200, 260)
WAITMS(50)
MOVE(275, 310)
WAITMS(50)
MOVE(350, 260)
WAITMS(50)
LUP(350, 260)

HALT
```

---

## Kiểm tra các kịch bản thực hành trong mục Cẩm nang

**Trạng thái:** 🟡 Theo help, chưa chạy thử · **Các trang:** [`cam-nang/*`](/cam-nang/click-theo-lich)

Toàn bộ các kịch bản mẫu trong 5 trang cẩm nang đều được biên soạn từ các lệnh chuẩn của help nhưng chưa chạy thử thực tế trên máy Windows:

1. [Bấm chuột theo lịch và chu kỳ](/cam-nang/click-theo-lich): Kịch bản lặp cố định, lặp `FOR` `N` lần và chờ đúng giờ/phút bằng `$_time_h`, `$_time_m`.
2. [Tìm màu trên màn hình rồi bấm chuột](/cam-nang/tim-mau): Kịch bản `GETSCREEN` + `IF_PIXEL_IN`, vòng lặp `WHILE` chờ màu xuất hiện rồi bấm nút Đóng, và quét nhiều điểm bằng `SCANPXL` + `ARRPOP`.
3. [Tìm hình ảnh mẫu trên màn hình](/cam-nang/tim-anh): Kịch bản chụp mẫu bằng `Alt + G`, tìm bằng `IF_PICTURE_IN` với `bgcolor`, `currency` và `COLORMODE`.
4. [Đọc và ghi tệp `.txt` và `.ini`](/cam-nang/doc-ghi-file): Kịch bản `INIWRITE`/`INIREAD`, tách chuỗi bằng `TFREAD` + `STRPOS` + `STRCUT2`, và đọc mảng bằng `TFREADARR` + `STRSEPARATE`.
5. [Tự động vẽ hình trong Paint](/cam-nang/tu-ve): Kịch bản vẽ đoạn thẳng, hình vuông, đường tròn (`SIN`, `COS`) và vẽ đa giác từ tệp `diem_ve.txt`.
