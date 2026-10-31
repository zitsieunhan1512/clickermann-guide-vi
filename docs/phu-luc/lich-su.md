# Lịch sử phát triển phiên bản

Trang này dịch các ý chính trong lịch sử các phiên bản của Clickermann từ bản v1.0 đến v4.13.014 theo phần Lịch sử phiên bản trong help chính thức, giúp tra cứu xem lệnh hoặc tính năng nào xuất hiện hay bị loại bỏ từ phiên bản nào.

## Phiên bản v4.13.014 (16.05.2018)

- **Nhân chương trình (Core):**
  - Chuyển sang bảng mã Unicode, các tệp văn bản nay sử dụng mã hóa UTF-8.
  - Tạo thêm phiên bản 64-bit của chương trình.
  - Cải thiện hỗ trợ màn hình mở rộng (nhiều màn hình).
  - Sửa lỗi treo/sập khi hệ điều hành chạy liên tục quá 49 ngày không khởi động lại.
- **Trình soạn thảo:**
  - Khóa chỉnh sửa mã nguồn trong lúc script đang chạy.
  - Tăng tốc độ hoạt động của kính lúp.
  - Sửa lỗi các menu thả xuống, lỗi tính năng tự động chú thích dòng (auto-commenting) và lỗi thu nhỏ/phóng to cửa sổ.
  - Sửa lỗi sập chương trình khi phần tử đang khóa bị đóng.
  - Cửa sổ trình soạn thảo nay ghi nhớ vị trí khi chuyển qua lại với cửa sổ chính.
  - Thêm phím tắt `Ctrl + S` để lưu nhanh; thêm `Tab` và `Shift + Tab` để thụt lề theo khối.
  - Cho phép đặt mẫu script mặc định qua tệp `\data\default.txt`.
  - Thêm tính năng chụp nhanh ảnh `100×100` quanh vị trí con trỏ (ảnh chụp kính lúp) cùng phím tắt toàn cục `Alt + G` (có thể đổi được).
- **Trình thông dịch:**
  - Thêm bước kiểm tra cú pháp cơ bản.
  - Thêm các lệnh mới: [`HGETPID`](/lenh/winapi#hgetpid), [`ARRSORT`](/lenh/so#arrsort), [`GETMESSAGE`](/lenh/winapi#getmessage), [`CHAR`](/lenh/chuoi-file#char).
  - Thêm các biến hệ thống: `$_pdir`, `$_hwnd`, `$_hwnd_self`, `$_time_str`, `$_date_str`, `$_ver_self`, `$_ver_sys`, `$_arch_sys`, `$_param_str`.
  - Các sửa đổi và nâng cấp:
    - Cải tiến toàn bộ phần toán học, bổ sung các phép toán mới.
    - Nâng cấp các hàm tìm kiếm đồ họa, tăng nhẹ tốc độ tìm kiếm.
    - Thay đổi tham số của [`WRITEMEM`](/lenh/kich-ban#writemem) và [`READMEM`](/lenh/kich-ban#readmem); nâng cấp `READMEM()` thành hàm trả về giá trị.
    - Nâng cấp [`STRPOS`](/lenh/chuoi-file#strpos), thêm tham số độ lệch bắt đầu tìm (`offset`).
    - Nâng cấp [`DIST`](/lenh/so#dist), hỗ trợ tham số số thập phân có dấu chấm.
    - Nâng cấp [`KEYSTRING`](/lenh/ban-phim#keystring), nay tự động nhấn giữ phím `Shift` khi cần.
    - Sửa lỗi [`GETFILELIST`](/lenh/kich-ban#getfilelist) và [`GETDIRLIST`](/lenh/kich-ban#getdirlist).
    - Sửa một số lỗi liên quan tới dấu ngoặc kép trong chuỗi trả về.
    - Ở chế độ khóa cửa sổ, hình ảnh không còn bị trượt lệch.
    - [`SCREENSHOTFIX`](/lenh/man-hinh#screenshotfix) không còn tự tạo thư mục rỗng.
    - Sửa một số lỗi của luồng (`THREAD`).
    - Cảnh báo khi tệp nêu trong `#include` không tồn tại.
    - Nâng cấp `#logfile`, cho phép đặt tên tệp nhật ký tùy ý.
    - Các thủ tục điều khiển con trỏ chuột không còn bấm tại vị trí hiện tại nếu cả hai tọa độ đều mang số âm.
- **Khác:**
  - Loại bỏ sự phụ thuộc vào thư viện `httpwork.dll`.
  - Cập nhật lại tài liệu hướng dẫn (`help.chm`) và tối ưu hóa chung.

## Phiên bản v4.12.001 (25.03.2016)

- **Trình thông dịch:**
  - Thêm các lệnh: [`RADIOBOX`](/lenh/kich-ban#radiobox), [`GETKEYSDOWN`](/lenh/ban-phim#getkeysdown), [`GETDIRLIST`](/lenh/kich-ban#getdirlist), [`GETFILELIST`](/lenh/kich-ban#getfilelist), [`SETVAR`](/lenh/so#setvar), [`GETVAR`](/lenh/so#getvar), [`SCREENSHOTFIX`](/lenh/man-hinh#screenshotfix), [`PXLREPLACE`](/lenh/man-hinh#pxlreplace).
  - Loại bỏ lệnh: `LOAD`.
  - Thay đổi lệnh: [`SETTHREAD`](/lenh/cau-truc#setthread).
- **Khác:**
  - Sửa lỗi với các chuỗi có chứa ký tự `$`.
  - Sửa lỗi rò rỉ bộ nhớ (memory leak) khi bật chế độ khóa cửa sổ.
  - Sửa lỗi treo chương trình trong một số trường hợp khi đọc chuỗi.
  - Sửa lỗi lệnh [`INC`](/lenh/so#inc).
  - Khi bỏ tạm dừng (Resume) chương trình, các luồng đã bị dừng bởi script trước đó sẽ không tự động chạy lại.
  - Hiệu chỉnh lại tính năng ghi thao tác (Record) và tối ưu hóa.

## Phiên bản v4.11.000 (15.10.2014)

- **Nhân chương trình:** Thêm hỗ trợ đa luồng (multithreading).
- **Giao diện:**
  - Giao diện cài đặt phím tắt mới (không tương thích với tệp `config.ini` cũ).
  - Thêm nút "Luôn nổi trên cùng" (Always on top) trên cửa sổ chính.
  - Thanh trạng thái ở cửa sổ chính hiển thị dòng nhật ký mới nhất.
  - Trong cài đặt có thêm nút đăng ký và gỡ liên kết định dạng tệp `.cms` (trước đây tự ghi vào Registry mỗi khi khởi động).
- **Trình thông dịch:**
  - Thêm các lệnh: [`TFREADARR`](/lenh/chuoi-file#tfreadarr), [`TFWRITEARR`](/lenh/chuoi-file#tfwritearr), [`STRSEPARATE`](/lenh/chuoi-file#strseparate), [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread), [`SETTHREAD`](/lenh/cau-truc#setthread), [`ARCSIN`](/lenh/so#arcsin), [`ARCCOS`](/lenh/so#arccos), [`WNDGETINFO`](/lenh/winapi#wndgetinfo), [`WNDSETINFO`](/lenh/winapi#wndsetinfo), [`WNDBUMP`](/lenh/winapi#wndbump).
  - Thêm các tham số tọa độ vùng cho [`GETSCREEN`](/lenh/man-hinh#getscreen).
  - Thêm macro cho bộ tiền xử lý (`#define`).
  - Sửa lỗi: lồng nhiều `SWITCH` không còn làm treo chương trình; "Thay thế tất cả" trong trình soạn thảo không làm treo chương trình; vòng lặp `FOR` không tự đưa biến đếm về `0` nếu biến đó đã được khởi tạo từ trước.
- **Khác:** Gộp hai tệp hướng dẫn thành một tệp `help.chm` duy nhất.

## Phiên bản v4.10.000 (03.04.2014)

- **Nhân chương trình:**
  - Độ dài dữ liệu lưu trong biến không còn bị giới hạn ở 255 ký tự.
  - Viết lại hoàn toàn cơ chế ghi thao tác (Record) chính xác hơn.
  - Hỗ trợ đầy đủ màn hình mở rộng (Extended Desktop).
- **Trình thông dịch:**
  - Viết lại phần xử lý logic: thêm phép toán bit và hỗ trợ ngoặc tròn ưu tiên `( )`.
  - Thêm mức lọc thứ 8 cho [`COLORMODE`](/lenh/man-hinh#colormode).
  - Vòng lặp [`FOR`](/lenh/cau-truc#for-end-cyc) cho phép gán giá trị khởi tạo ban đầu ngay ở tham số đầu tiên.

## Phiên bản v4.9 (31.12.2013)

- **Trình thông dịch:**
  - Thêm cấu trúc [`SWITCH`](/lenh/cau-truc#switch-end-switch).
  - Thay đổi cách khai báo và gọi chương trình con [`SUB`](/lenh/cau-truc#sub-end-sub), nay hỗ trợ truyền tham số (không còn dùng `callsub`).
  - Thay đổi vòng lặp `FOR`: lượt lặp đầu tiên bắt đầu từ `0`.
  - Hàm [`DIST`](/lenh/so#dist) trả về số thực dấu chấm động.
  - Viết lại [`DIALOGBOX`](/lenh/kich-ban#dialogbox) và [`INPUTBOX`](/lenh/kich-ban#inputbox) (hỗ trợ phím `Enter` và `Esc`).
  - Nâng cấp [`HALT`](/lenh/kich-ban#halt), cho phép đóng hoàn toàn chương trình Clickermann.
  - Sửa lỗi dòng trống, lỗi 6 tham số, lỗi hàm `SIN` và `COS`, lỗi tính toán số có nhiều chữ số thập phân; mảng nay chứa được cả phần tử chuỗi lẫn số.

## Phiên bản v4.8.000 (01.10.2013)

- **Nhân chương trình:** Thêm chế độ PS/2.
- **Trình thông dịch:**
  - Thêm các chỉ thị: `#logfile`, `#autorun`, `#ps2_mouse`, `#ps2_keyboard`.
  - Thêm hỗ trợ mảng và các lệnh: [`ARRPUSH`](/lenh/so#arrpush), [`ARRPOP`](/lenh/so#arrpop), [`ARRSIZE`](/lenh/so#arrsize), [`SCANPXL`](/lenh/man-hinh#scanpxl), [`SCANPICTURE`](/lenh/man-hinh#scanpicture), [`DIALOGBOX`](/lenh/kich-ban#dialogbox).
  - [`WAIT`](/lenh/kich-ban#wait) nhận được số thập phân (ví dụ `wait(1.5)` tương đương `waitms(1500)`).
- **Giao diện:** Thêm lịch sử các tệp đã mở.

## Phiên bản v4.7.000 SE (05.12.2012)

- **Trình thông dịch:**
  - Bộ phân tích cú pháp không còn cố tính toán bên trong chuỗi văn bản.
  - Sửa lỗi `PXLCRC`, `ROUND`, `WNDFIND`, lỗi cộng nhiều hàm, lỗi so sánh số thập phân trong câu điều kiện và lỗi chỉ thị có chú thích đi sau.
  - Thêm các lệnh: [`POW`](/lenh/so#pow), [`TFREAD`](/lenh/chuoi-file#tfread), [`TFWRITE`](/lenh/chuoi-file#tfwrite), [`TFDELETE`](/lenh/chuoi-file#tfdelete), [`TFCLEAR`](/lenh/chuoi-file#tfclear), [`TFCOUNT`](/lenh/chuoi-file#tfcount), [`GETKBLAYOUT`](/lenh/ban-phim#getkblayout), [`SETKBLAYOUT`](/lenh/ban-phim#setkblayout).
  - Nâng cấp [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if).
  - Thêm biến hệ thống: `$_DATE_Y`, `$_DATE_M`, `$_DATE_D`.
- **Trình soạn thảo & Giao diện:** Thêm menu chèn nhanh lệnh, menu mẫu code thả xuống; bật kính lúp tự làm chậm tốc độ con trỏ chuột; các chế độ thực thi trở lại dưới dạng một cửa sổ riêng.

## Phiên bản v4.7.000 (12.10.2012)

- **Nhân chương trình:**
  - Thêm tính năng tạm dừng (Pause) script.
  - Cho phép dùng đường dẫn tuyệt đối tới tệp (đường dẫn tương đối vẫn được tính từ thư mục dự án hiện tại), viết số hệ 16 (`0x...`) và số thập phân có dấu chấm.
  - Hợp nhất kiểu biến: biến có thể nhận số nguyên, số thực hoặc chuỗi.
- **Trình thông dịch:**
  - Hỗ trợ viết `AND`, `OR`, `XOR` trong điều kiện (thay cho `&`, `|`, `^`).
  - Thay đổi cơ chế giảm màu và thủ tục [`COLORMODE`](/lenh/man-hinh#colormode).
  - Thêm các lệnh: [`MCLICK`](/lenh/chuot#mclick-mdown-mup), `MDOWN`, `MUP`, [`INIREAD`](/lenh/chuoi-file#iniread), [`INIWRITE`](/lenh/chuoi-file#iniwrite), [`PXLCRC`](/lenh/man-hinh#pxlcrc), [`SIN`](/lenh/so#sin), [`COS`](/lenh/so#cos), [`SQRT`](/lenh/so#sqrt), [`ROUND`](/lenh/so#round), [`INT`](/lenh/so#int).
  - Thêm biến hệ thống `$_hwnd`; loại bỏ hai lệnh `TOINT`, `TOSTR`.
- **Trình soạn thảo & Giao diện:** Thêm nút chuyển chế độ chép tọa độ vào Clipboard, tìm kiếm/thay thế, tự động căn lề, đổi mức giảm màu trên kính lúp, xem/sửa giá trị biến khi đang tạm dừng; gỡ bỏ các chế độ hoạt động khỏi cửa sổ chính.

## Các phiên bản từ v1.0 đến v4.6.000 (2006 – 2012)

- **v4.6.000 (09.03.2012):** Đưa vào khái niệm "thư mục dự án" — nay mọi đường dẫn đều được tính tương đối theo thư mục chứa tệp script đang nạp; thêm `#include`, `#name`, [`HINTPOPUP`](/lenh/nhat-ky#hintpopup), [`STRMD5`](/lenh/chuoi-file#strmd5), [`STRCUT2`](/lenh/chuoi-file#strcut2); thêm mẫu code trong trình soạn thảo.
- **v4.5.000 (16.09.2011):** Hỗ trợ lưu ảnh chụp JPEG; thêm [`INPUTBOX`](/lenh/kich-ban#inputbox), [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if), [`ISKEYDOWN`](/lenh/ban-phim#iskeydown), [`HTTPGET`](/lenh/chuoi-file#httpget); cho phép nhập tay `HWND` trong Quản lý cửa sổ.
- **v4.4.000 (20.07.2011):** Giảm mạnh sai số của `WAIT`, `WAITMS`; thêm kính lúp màn hình; `GOTO` chỉ còn dùng nhãn chữ; thêm bộ lệnh chuỗi (`STRFILTER`, `STRCUT`, `STRLEN`, `STRCONCAT`, `STRREPLACE`, `STRREADLN`, `STRWRITELN`), bộ lệnh cửa sổ (`WNDFIND`, `WNDSIZE`, `WNDPOS`, `WNDSTATE`, `POSTMESSAGE`, `SENDMESSAGE`), bộ lệnh kênh màu (`COLORGEN`, `COLORR`, `COLORG`, `COLORB`) và `BEEP`.
- **v4.3.000 (26.11.2010):** Hỗ trợ đa ngôn ngữ giao diện; thêm `$_time_h`, `$_time_m`, `$_time_s`, `HSET`, `HSETTEXT`, `HGET`, `HGETTEXT`.
- **v4.2.000 (05.10.2010):** Hỗ trợ điều kiện phức hợp cho `IF`, `FOR`, `WHILE`; tham số vòng lặp `FOR` được đưa về `0` sau khi kết thúc vòng lặp; thêm `COLORMODE`, `MOVER`, `$_xmax`, `$_ymax`, `$_time_t`.
- **v4.1.000 (02.09.2010):** Thêm giảm màu; thêm `DIST`, `READMEM`, `WRITEMEM`, `SUB ... END_SUB`, `GOSUB`; tự lưu `backup.cms` khi bấm Áp dụng.
- **v4.0.002 (11.06.2010):** Hỗ trợ plugin DLL, biến chuỗi, nhánh `ELSE`, nhãn chữ cho `GOTO`, file hằng trong thư mục `data` của tool; thêm `PXL`, `PXLXOR`, `PXLCOUNT`, `RND`, `RNDFROM`, `FROMCLIP`, `BREAK`, `CALL`.
- **v3.2 RC1 & v3.2 beta (02–03.2010):** Thêm `IF ... END_IF`, `DEFINE`, `UNDEFINE`, vòng lặp `FOR`, `WHILE`, phân tích màn hình ở chế độ khóa cửa sổ, biến `$_line`, `$_cursor`, lệnh `IF_KEYDOWN`, `TOCLIP`.
- **v3.1 (12.2009 – 01.2010):** Thêm chế độ khóa cửa sổ, cửa sổ nhật ký (`LOGSHOW`, `LOGCLEAR`, `LOGWRITE`), `GETSCREEN`, `SCREENSHOT`, `INC`, `HALT`, `$_return1`, `$_return2`, `IF_PIXEL_IN`, `SOUND`, `KEYSTRING`, `$_xmouse`, `$_ymouse`, `IF_TIME`.
- **v1.0 – v3.0 (2006 – 09.2009):** Các phiên bản đầu tiên: đổi tên thành Clickermann (v1.1), thêm các lệnh chuột `LCLICK`, `RCLICK`, `LDOWN`, `LUP`, chức năng ghi thao tác (v1.3), tô màu cú pháp và chú thích `//` (v2.1), hỗ trợ biến và `GOTO` (v3.0).
