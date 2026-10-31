# Tra cứu lệnh theo việc cần làm

Trang này giúp bạn tìm nhanh câu lệnh Clickermann v4.13 theo nhu cầu thực tế ("muốn làm việc X thì dùng lệnh nào"), kèm liên kết trực tiếp tới mục tra cứu chi tiết của từng lệnh.

## Cách đọc một mục lệnh

Trong các trang tra cứu lệnh chi tiết, mỗi mục lệnh đều được trình bày theo cùng một cấu trúc thống nhất:

- **Cặp ngoặc vuông `[ ]` trong cú pháp:** Cho biết tham số đó là **tùy chọn (không bắt buộc)**. Nếu bạn bỏ qua không truyền, Clickermann sẽ tự dùng giá trị mặc định ghi trong bảng tham số (ví dụ với `WAITMS(500)` thì `500` là bắt buộc, còn với `INC($var, [value])` thì có thể viết gọn là `INC($var)`). *(Lưu ý: khi gõ lệnh thật vào script, bạn **không** gõ dấu ngoặc vuông `[ ]`).*
- **Dấu ba chấm `...` trong cú pháp:** Cho biết bạn có thể truyền tiếp **nhiều tham số không giới hạn số lượng** ở phía sau, cách nhau bằng dấu phẩy (ví dụ `PRINT("A", $x, "B")` hoặc `IF_PIXEL_IN(0, 0, 100, 100, 255, 65280)`).
- **Loại lệnh:**
  - **Thủ tục:** Câu lệnh thực hiện một hành động và đứng riêng trên một dòng (ví dụ `LCLICK(100, 200)`).
  - **Hàm:** Câu lệnh tính toán và **trả về một giá trị** ngay tại vị trí gọi nó để gán vào biến hoặc đặt bên trong biểu thức khác (ví dụ `$so = RND(1, 10)`).
  - **Cấu trúc lệnh:** Khối lệnh gồm nhiều dòng, có dòng mở đầu và dòng từ khóa đóng khối (như `IF ... END_IF`, `FOR ... END_CYC`).
- **Trạng thái kiểm chứng:** `🟡 Theo help, chưa chạy thử` (sát theo `help.chm` v4.13.014) hoặc `🟠 Chưa thống nhất` (có điểm khác biệt giữa các nguồn tài liệu, kèm hướng dẫn **"Nên làm"**).
- **Trả về:** Giá trị kết quả mà hàm trả về, hoặc các biến hệ thống (`$_return1`, `$_return2`) được lệnh cập nhật sau khi chạy.

## Nhóm trang tra cứu lệnh

- [Số, biến và mảng](/lenh/so) — Biến, toán học, lượng giác, làm tròn, số ngẫu nhiên và mảng.
- [Chuỗi, tệp tin, bộ nhớ tạm và HTTP](/lenh/chuoi-file) — Xử lý chuỗi, tệp `.ini`, tệp `.txt`, Clipboard và truy vấn HTTP.
- [Chuột](/lenh/chuot) — Bấm chuột trái/phải/giữa, nhấp đúp, kéo thả, di chuyển và cuộn chuột.
- [Bàn phím](/lenh/ban-phim) — Bấm phím, giữ phím, gõ chuỗi, kiểm tra phím đang nhấn và đổi kiểu bàn phím.
- [Điều kiện, vòng lặp, chương trình con](/lenh/cau-truc) — Cấu trúc rẽ nhánh `IF`, `SWITCH`, vòng lặp `FOR`, `WHILE`, `SUB` và đa luồng `THREAD`.
- [Màn hình và màu sắc](/lenh/man-hinh) — Chụp bộ đệm ảnh, đọc/tìm màu, tìm ảnh `.bmp`, giảm màu và lưu ảnh chụp.
- [Nhật ký và âm báo](/lenh/nhat-ky) — Ghi nhật ký, hiện/ẩn cửa sổ nhật ký, phát âm thanh `.wav`, tiếng bíp và thông báo ở khay hệ thống.
- [Điều khiển script và hệ thống](/lenh/kich-ban) — Tạm dừng chờ, nhảy nhãn, hộp thoại, gọi lệnh ngoài, nạp plugin DLL và quét thư mục.
- [Cửa sổ và WinAPI](/lenh/winapi) — Tìm cửa sổ, khóa cửa sổ, đổi vị trí/kích thước và gửi/nhận thông điệp Windows.

---

## Lấy thông tin thường dùng (giờ giấc, tọa độ chuột, chờ màu)

| Việc cần làm | Cách thực hiện trong Clickermann | Xem hướng dẫn |
|---|---|---|
| Xem giờ, phút, giây hiện tại | Đọc các biến hệ thống `$_time_h` (giờ), `$_time_m` (phút), `$_time_s` (giây), `$_time_str` (chuỗi giờ) | [Ngôn ngữ script](/khai-niem/ngon-ngu#cac-bien-he-thong-hay-dung-nhat), [Bấm chuột theo lịch](/cam-nang/click-theo-lich) |
| Xem ngày, tháng, năm hiện tại | Đọc các biến hệ thống `$_date_d`, `$_date_m`, `$_date_y`, `$_date_str` | [Bảng biến hệ thống](/khai-niem/ngon-ngu#bang-bien-he-thong-day-du) |
| Xem vị trí con trỏ chuột hiện tại | Đọc hai biến hệ thống `$_xmouse` (X) và `$_ymouse` (Y) | [Ngôn ngữ script](/khai-niem/ngon-ngu#cac-bien-he-thong-hay-dung-nhat) |
| Đọc mã màu của 1 điểm trên màn hình | Gọi [`GETSCREEN`](/lenh/man-hinh#getscreen) rồi gọi hàm [`PXL(x, y)`](/lenh/man-hinh#pxl) | [Màn hình và màu sắc](/lenh/man-hinh#pxl) |
| Chờ tới khi một màu xuất hiện trên màn hình | Đặt [`GETSCREEN`](/lenh/man-hinh#getscreen) + [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if) bên trong vòng lặp [`WHILE ... END_CYC`](/lenh/cau-truc#while-end-cyc) | [Cẩm nang tìm màu](/cam-nang/tim-mau#tinh-huong-2-cho-cho-toi-khi-mau-xuat-hien-roi-moi-di-tiep) |

---

## Thao tác chuột và bàn phím

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Bấm chuột trái 1 lần | [`LCLICK`](/lenh/chuot#lclick) | Đưa trỏ tới `(x, y)` rồi bấm trái |
| Nhấp đúp chuột trái | [`DBLCLICK`](/lenh/chuot#dblclick) | Bấm đúp trái tại `(x, y)` |
| Kéo thả chuột (drag & drop) | [`LDOWN`](/lenh/chuot#ldown), [`LUP`](/lenh/chuot#lup) | Nhấn giữ ở điểm đầu, chờ ngắn rồi nhả ở điểm đích |
| Bấm / giữ / nhả chuột phải | [`RCLICK, RDOWN, RUP`](/lenh/chuot#rclick-rdown-rup) | Tương tự chuột trái nhưng cho nút phải |
| Bấm / giữ / nhả chuột giữa | [`MCLICK, MDOWN, MUP`](/lenh/chuot#mclick-mdown-mup) | Tương tự chuột trái nhưng cho nút giữa |
| Di chuyển con trỏ tới tọa độ | [`MOVE`](/lenh/chuot#move) | Chỉ đưa trỏ chuột tới `(x, y)`, không bấm |
| Dịch chuột tương đối | [`MOVER`](/lenh/chuot#mover) | Không chạy ở chế độ khóa cửa sổ |
| Cuộn con lăn chuột xuống / lên | [`WHEELDOWN`](/lenh/chuot#wheeldown), [`WHEELUP`](/lenh/chuot#wheelup) | Có hệ số nhân tốc độ cuộn `mult` |
| Bấm 1 phím bàn phím | [`KEYPRESS`](/lenh/ban-phim#keypress) | Truyền mã số hoặc hằng như `#SPACE` |
| Nhấn giữ / nhả phím (tổ hợp phím) | [`KEYDOWN`](/lenh/ban-phim#keydown), [`KEYUP`](/lenh/ban-phim#keyup) | Dùng để bấm tổ hợp như `Ctrl + S` |
| Gõ một chuỗi ký tự | [`KEYSTRING`](/lenh/ban-phim#keystring) | Phụ thuộc bộ gõ; không bấm được phím không phải ký tự |
| Kiểm tra 1 phím có đang được nhấn | [`ISKEYDOWN`](/lenh/ban-phim#iskeydown) | Kiểm tra được cả phím bàn phím và nút chuột |
| Lấy danh sách mọi phím đang nhấn | [`GETKEYSDOWN`](/lenh/ban-phim#getkeysdown) | Đổ danh sách mã phím đang nhấn vào mảng |
| Xem / đổi ngôn ngữ bàn phím của cửa sổ | [`GETKBLAYOUT`](/lenh/ban-phim#getkblayout), [`SETKBLAYOUT`](/lenh/ban-phim#setkblayout) | Làm việc theo `hwnd` của cửa sổ |

---

## Màn hình, màu sắc và tìm ảnh

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Chụp màn hình vào bộ đệm ảnh | [`GETSCREEN`](/lenh/man-hinh#getscreen) | Gọi trước khi đọc; gọi lại khi cần ảnh mới |
| Xem mã màu của 1 điểm ảnh | [`PXL`](/lenh/man-hinh#pxl) | Trả về mã màu tại `(x, y)` |
| Tìm 1 điểm màu trong vùng | [`IF_PIXEL_IN ... END_IF`](/lenh/man-hinh#if-pixel-in-end-if) | Trả tọa độ tìm thấy vào `$_return1`, `$_return2` |
| Tìm tất cả điểm màu trong vùng | [`SCANPXL`](/lenh/man-hinh#scanpxl) | Đổ toàn bộ các cặp tọa độ X, Y vào mảng |
| Đếm số điểm ảnh có màu chỉ định | [`PXLCOUNT`](/lenh/man-hinh#pxlcount) | Trả về số điểm ảnh khớp màu trong vùng |
| Tìm 1 ảnh mẫu `.bmp` trên màn hình | [`IF_PICTURE_IN ... END_IF`](/lenh/man-hinh#if-picture-in-end-if) | Hỗ trợ màu nền trong suốt và độ chính xác `%` |
| Tìm tất cả vị trí của ảnh mẫu `.bmp` | [`SCANPICTURE`](/lenh/man-hinh#scanpicture) | Đổ toàn bộ các cặp tọa độ X, Y vào mảng |
| Kiểm tra vùng ảnh có thay đổi không | [`PXLCRC`](/lenh/man-hinh#pxlcrc), [`PXLXOR`](/lenh/man-hinh#pxlxor) | Tính mã kiểm tra (hash) của vùng điểm ảnh |
| Giảm số màu để dễ nhận diện | [`COLORMODE`](/lenh/man-hinh#colormode) | Dải `0..8` (`0` là ảnh gốc, mức lọc `1..8`, nút xem thử dưới kính lúp tới `7`) |
| Đổi màu điểm ảnh trong bộ đệm ảnh | [`PXLREPLACE`](/lenh/man-hinh#pxlreplace) | Thay màu `color` thành `newcolor` |
| Ghép hoặc tách kênh màu Đỏ, Xanh lá, Xanh dương | [`COLORGEN`](/lenh/man-hinh#colorgen), [`COLORR, COLORG, COLORB`](/lenh/man-hinh#colorr-colorg-colorb) | Chuyển đổi giữa mã màu và 3 kênh RGB (`0..255`) |
| Lưu ảnh chụp màn hình ra tệp | [`SCREENSHOT`](/lenh/man-hinh#screenshot), [`SCREENSHOTEX`](/lenh/man-hinh#screenshotex), [`SCREENSHOTFIX`](/lenh/man-hinh#screenshotfix) | Lưu toàn bộ hoặc cắt vùng, tự đánh số hoặc ghi đè |

---

## Điều kiện, vòng lặp, chương trình con và luồng

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Kiểm tra điều kiện đúng / sai | [`IF ... END_IF`](/lenh/cau-truc#if-end-if), [`ELSE`](/lenh/cau-truc#else) | `ELSE` dùng được cho cả `IF`, `IF_PIXEL_IN`, `IF_PICTURE_IN` |
| Rẽ nhánh theo nhiều giá trị | [`SWITCH ... END_SWITCH`](/lenh/cau-truc#switch-end-switch) | Thay cho việc dùng quá nhiều lệnh `IF` |
| Lặp với biến đếm tăng tự động | [`FOR ... END_CYC`](/lenh/cau-truc#for-end-cyc) | 🟠 Nên gán rõ giá trị đầu `=0` (hoặc `=1`) cho biến đếm |
| Lặp chừng nào điều kiện còn đúng | [`WHILE ... END_CYC`](/lenh/cau-truc#while-end-cyc) | Cần cập nhật biến trong thân vòng lặp để tránh treo |
| Gom nhóm lệnh thành chương trình con | [`SUB ... END_SUB`](/lenh/cau-truc#sub-end-sub) | 🟠 Phải khai báo ở phía trên nơi gọi |
| Chạy tác vụ song song ở luồng riêng | [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread) | 🟠 Nên truyền rõ `init_state` là `0` hoặc `1` |
| Tạm dừng / bật lại / đặt lại luồng | [`SETTHREAD`](/lenh/cau-truc#setthread) | 🟠 Hỗ trợ trạng thái `0`, `1` và `2` |

---

## Số, biến và mảng

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Khai báo biến (nếu chưa có) / xóa biến | [`DEFINE`](/lenh/so#define), [`UNDEFINE`](/lenh/so#undefine) | `UNDEFINE` xóa được cả mảng |
| Tăng / giảm giá trị biến | [`INC`](/lenh/so#inc) | Mặc định cộng thêm `1` |
| Lấy số ngẫu nhiên hoặc chọn ngẫu nhiên | [`RND`](/lenh/so#rnd), [`RNDFROM`](/lenh/so#rndfrom) | `RND` lấy trong đoạn `[from, to]`; `RNDFROM` chọn từ danh sách |
| Lấy phần nguyên / làm tròn số | [`INT`](/lenh/so#int), [`ROUND`](/lenh/so#round) | `INT` cũng dùng để ép chuỗi thành số; `ROUND` 🟠 lưu ý khi làm tròn số âm |
| Tính khoảng cách giữa 2 tọa độ | [`DIST`](/lenh/so#dist) | Trả về số thực khoảng cách giữa `(x1, y1)` và `(x2, y2)` |
| Tính căn bậc hai, lũy thừa, trị tuyệt đối | [`SQRT`](/lenh/so#sqrt), [`POW`](/lenh/so#pow), [`ABS`](/lenh/so#abs) | Các hàm toán học cơ bản |
| Tính lượng giác (theo độ) | [`SIN`](/lenh/so#sin), [`COS`](/lenh/so#cos), [`ARCSIN`](/lenh/so#arcsin), [`ARCCOS`](/lenh/so#arccos) | Góc tính bằng đơn vị độ |
| Thêm / lấy phần tử cuối của mảng | [`ARRPUSH`](/lenh/so#arrpush), [`ARRPOP`](/lenh/so#arrpop) | `ARRPOP` vừa trả về vừa xóa phần tử cuối |
| Đếm số phần tử / sắp xếp mảng | [`ARRSIZE`](/lenh/so#arrsize), [`ARRSORT`](/lenh/so#arrsort) | Chỉ số mảng chạy từ `0` đến `ARRSIZE - 1` |
| Đọc / gán biến qua chuỗi tên biến | [`GETVAR`](/lenh/so#getvar), [`SETVAR`](/lenh/so#setvar) | 🟠 Biến phải tồn tại trước; truyền tên dạng chuỗi `"$var"` |

---

## Chuỗi, tệp tin, bộ nhớ tạm và mạng

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Nối chuỗi / đo độ dài chuỗi | [`STRCONCAT`](/lenh/chuoi-file#strconcat), [`STRLEN`](/lenh/chuoi-file#strlen) | Ghép nhiều chuỗi (không giới hạn số lượng) hoặc đếm số ký tự |
| Cắt chuỗi con | [`STRCUT`](/lenh/chuoi-file#strcut), [`STRCUT2`](/lenh/chuoi-file#strcut2) | Cắt theo độ dài (`STRCUT`) hoặc vị trí cuối (`STRCUT2`) |
| Tìm vị trí chuỗi con / thay thế chuỗi | [`STRPOS`](/lenh/chuoi-file#strpos), [`STRREPLACE`](/lenh/chuoi-file#strreplace) | Tìm hoặc đổi chuỗi con trong chuỗi gốc |
| Lọc ký tự / tách chuỗi vào mảng | [`STRFILTER`](/lenh/chuoi-file#strfilter), [`STRSEPARATE`](/lenh/chuoi-file#strseparate) | Xóa/giữ ký tự theo mặt nạ hoặc tách theo dấu phân cách |
| Lấy ký tự từ mã Unicode / băm MD5 | [`CHAR`](/lenh/chuoi-file#char), [`STRMD5`](/lenh/chuoi-file#strmd5) | Chuyển mã Unicode thành ký tự hoặc tạo mã MD5 |
| Đọc / ghi tệp cấu hình `.ini` | [`INIREAD`](/lenh/chuoi-file#iniread), [`INIWRITE`](/lenh/chuoi-file#iniwrite) | Mặc định dùng phân mục `"default"` |
| Đọc / ghi / xóa dòng trong tệp `.txt` | [`TFREAD`](/lenh/chuoi-file#tfread), [`TFWRITE`](/lenh/chuoi-file#tfwrite), [`TFDELETE`](/lenh/chuoi-file#tfdelete), [`TFCLEAR`](/lenh/chuoi-file#tfclear), [`TFCOUNT`](/lenh/chuoi-file#tfcount) | Bộ lệnh thao tác tệp văn bản theo dòng (cũng có [`STRREADLN`](/lenh/chuoi-file#strreadln), [`STRWRITELN`](/lenh/chuoi-file#strwriteln)) |
| Đọc / ghi cả tệp `.txt` với mảng | [`TFREADARR`](/lenh/chuoi-file#tfreadarr), [`TFWRITEARR`](/lenh/chuoi-file#tfwritearr) | Chuyển nhanh giữa các dòng trong tệp và phần tử mảng |
| Đọc / ghi bộ nhớ tạm (Clipboard) | [`FROMCLIP`](/lenh/chuoi-file#fromclip), [`TOCLIP`](/lenh/chuoi-file#toclip) | Trao đổi văn bản với Clipboard của Windows |
| Gửi truy vấn web HTTP GET | [`HTTPGET`](/lenh/chuoi-file#httpget) | Gửi yêu cầu HTTP và nhận chuỗi phản hồi |

---

## Nhật ký, âm báo, hộp thoại và điều khiển script

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Ghi thông báo ra cửa sổ nhật ký | [`LOGWRITE (PRINT)`](/lenh/nhat-ky#logwrite-print) | `PRINT` là bí danh của `LOGWRITE` |
| Xóa / hiện hoặc ẩn cửa sổ nhật ký | [`LOGCLEAR`](/lenh/nhat-ky#logclear), [`LOGSHOW`](/lenh/nhat-ky#logshow) | Quản lý cửa sổ nhật ký khi chạy script |
| Phát âm thanh `.wav` hoặc tiếng bíp | [`SOUND`](/lenh/nhat-ky#sound), [`BEEP`](/lenh/nhat-ky#beep) | Phát âm thanh cảnh báo cho người dùng |
| Hiện thông báo ở khay hệ thống | [`HINTPOPUP`](/lenh/nhat-ky#hintpopup) | Hiện thông báo nổi ở khay hệ thống |
| Tạm dừng chờ theo giây / mili-giây | [`WAIT`](/lenh/kich-ban#wait), [`WAITMS`](/lenh/kich-ban#waitms) | `1` giây = `1000` mili-giây |
| Nhảy tới nhãn / dừng hẳn script | [`GOTO`](/lenh/kich-ban#goto), [`HALT`](/lenh/kich-ban#halt) | `HALT(1)` đóng luôn cả chương trình Clickermann |
| Hiện hộp thoại nhập chữ / nút bấm / chọn mục | [`INPUTBOX`](/lenh/kich-ban#inputbox), [`DIALOGBOX`](/lenh/kich-ban#dialogbox), [`RADIOBOX`](/lenh/kich-ban#radiobox) | Nhận dữ liệu hoặc quyết định từ người dùng |
| Chạy chương trình ngoài / gọi plugin DLL | [`EXECUTE`](/lenh/kich-ban#execute), [`CALL`](/lenh/kich-ban#call) | `EXECUTE` không chờ; `CALL` chờ plugin trả kết quả vào `$_return1` |
| Lấy danh sách tệp / thư mục theo mẫu | [`GETFILELIST`](/lenh/kich-ban#getfilelist), [`GETDIRLIST`](/lenh/kich-ban#getdirlist) | Đổ tên các tệp hoặc thư mục khớp mask vào mảng |
| Đọc / ghi bộ nhớ tiến trình theo PID | [`READMEM`](/lenh/kich-ban#readmem), [`WRITEMEM`](/lenh/kich-ban#writemem) | Đọc hoặc ghi số nguyên (`1`, `2`, `4`, `8` byte) theo địa chỉ bộ nhớ |

---

## Cửa sổ Windows và WinAPI

| Việc cần làm | Lệnh nên dùng | Ghi chú nhanh |
|---|---|---|
| Tìm cửa sổ theo tiêu đề | [`WNDFIND`](/lenh/winapi#wndfind) | Trả về `hwnd` của cửa sổ theo tiêu đề (không tìm phần tử con) |
| Lấy `hwnd` của phần tử tại tọa độ `(x, y)` | [`HGET`](/lenh/winapi#hget) | Trả về `hwnd` của phần tử nằm tại tọa độ màn hình `(x, y)` |
| Bật / tắt chế độ khóa cửa sổ bằng lệnh | [`HSET`](/lenh/winapi#hset) | Đặt phần tử đang khóa (`state = 1` bật, `state = 0` tắt) |
| Đưa cửa sổ lên trước / thu nhỏ hoặc mở lại | [`WNDBUMP`](/lenh/winapi#wndbump), [`WNDSTATE`](/lenh/winapi#wndstate) | Điều khiển trạng thái hiển thị của cửa sổ |
| Đổi vị trí / kích thước cửa sổ | [`WNDPOS`](/lenh/winapi#wndpos), [`WNDSIZE`](/lenh/winapi#wndsize), [`WNDGETINFO`](/lenh/winapi#wndgetinfo), [`WNDSETINFO`](/lenh/winapi#wndsetinfo) | Đọc hoặc đặt tọa độ và chiều rộng/cao của cửa sổ |
| Đọc / đặt văn bản trên phần tử điều khiển | [`HGETTEXT`](/lenh/winapi#hgettext), [`HSETTEXT`](/lenh/winapi#hsettext) | `HGETTEXT` trả về văn bản trên phần tử theo `hwnd`; `HSETTEXT` đặt văn bản mới |
| Lấy mã tiến trình (`pid`) từ `hwnd` | [`HGETPID`](/lenh/winapi#hgetpid) | Tìm `pid` của tiến trình sở hữu cửa sổ |
| Gửi / nhận thông điệp hệ thống Windows | [`SENDMESSAGE, POSTMESSAGE`](/lenh/winapi#sendmessage-postmessage), [`GETMESSAGE`](/lenh/winapi#getmessage) | Giao tiếp qua thông điệp WinAPI (như `1024` / `WM_USER`) |
