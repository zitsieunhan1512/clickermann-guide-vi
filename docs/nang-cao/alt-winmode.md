# Thư viện alt_winmode

Trang này giới thiệu thư viện cộng đồng `alt_winmode` (`alt_winmode.cms`), giúp một script Clickermann gửi thao tác chuột, bàn phím và đọc màu/ảnh trên nhiều cửa sổ khác nhau thông qua mã `hwnd` của từng phần tử mà không cần bật chế độ khóa cửa sổ bằng `HSET`.

::: warning Tính năng cộng đồng, chưa chạy thử
- **Trạng thái:** `🟡 Chưa chạy thử` (mọi đoạn mã và ví dụ trên trang này đều chưa chạy thử thực tế trên máy Windows).
- `alt_winmode` **không phải là tính năng chính thức** của Clickermann và tài liệu `help.chm` không nhắc tới thư viện này. Đây là bộ chương trình con (`SUB`) được chia sẻ công khai trên diễn đàn Clickermann (ghi ở đầu tệp là `alternative windowed mode v1.1`, chưa rõ tác giả).
- Cũng giống như [chế độ khóa cửa sổ](/khai-niem/khoa-cua-so) trong help, khả năng nhận thao tác qua `alt_winmode` **tùy thuộc vào cách từng ứng dụng đích được viết** (không phải ứng dụng nào cũng nhận).
:::

## Thư viện alt_winmode là gì và khi nào nên dùng?

Ở [chế độ khóa cửa sổ](/khai-niem/khoa-cua-so) mặc định của Clickermann (bật bằng phím tắt `Alt + W` hoặc lệnh [`HSET(hwnd, 1)`](/lenh/winapi#hset)), tại mỗi thời điểm chương trình chỉ khóa vào **một phần tử đang khóa** duy nhất (`$_hwnd`). Nếu muốn điều khiển nhiều cửa sổ cùng lúc bằng chế độ khóa cửa sổ tích hợp, bạn phải liên tục gọi `HSET` để chuyển đổi qua lại giữa các phần tử.

Thư viện `alt_winmode.cms` giải quyết bài toán này bằng cách viết sẵn các chương trình con (`SUB`) bọc lệnh [`POSTMESSAGE`](/lenh/winapi#sendmessage-postmessage) và [`WNDGETINFO`](/lenh/winapi#wndgetinfo):

- **Với chuột và bàn phím:** Thay vì dùng chuột/phím thật hoặc khóa cố định một cửa sổ qua `HSET`, mỗi lệnh `A_LCLICK`, `A_KEYPRESS`... đều nhận trực tiếp tham số `$A_hwnd` ở cuối và gửi thông điệp hệ thống (`POSTMESSAGE`) thẳng tới phần tử có `hwnd` đó. Nhờ vậy, **một script có thể điều khiển nhiều cửa sổ hoặc nhiều phần tử cùng lúc** chỉ bằng cách truyền mã `$hwnd` tương ứng vào từng lời gọi lệnh.
- **Với màn hình và màu sắc:** Các lệnh `A_GETSCREEN`, `A_PXL`, `A_IFPIXELIN`... tự động lấy tọa độ góc trái trên của cửa sổ trên màn hình bằng `WNDGETINFO`, sau đó cộng độ lệch để quy đổi từ **tọa độ tương đối bên trong phần tử** sang **tọa độ màn hình** trước khi gọi các lệnh đồ họa chuẩn của Clickermann.

**Khi nào nên dùng `alt_winmode`:**

- Khi một script cần gửi thao tác chuột hoặc phím lần lượt tới **hai hay nhiều cửa sổ ứng dụng** (ví dụ hai cửa sổ Notepad) mà không muốn gọi `HSET` đổi mục tiêu liên tục.
- Khi muốn gửi click chuột hoặc phím ngầm qua `POSTMESSAGE` tới một phần tử con cụ thể theo `hwnd` trong khi các lệnh khác của script vẫn làm việc ở chế độ thường.

## Cách nạp thư viện vào dự án

Để sử dụng `alt_winmode`, bạn thực hiện theo 3 bước:

1. Tạo một tệp văn bản có tên **`alt_winmode.cms`** đặt trong **cùng thư mục dự án** với tệp script chính của bạn, rồi chép đoạn mã nguồn ở mục tiếp theo vào tệp đó.
2. Ở đầu tệp script chính, thêm chỉ thị tiền xử lý `#include "alt_winmode.cms"`:
   ```cms
   #include "alt_winmode.cms"
   ```
   *(Lưu ý: theo quy tắc của [`SUB`](/lenh/cau-truc#sub-end-sub) trong help, mọi định nghĩa `SUB` phải nằm ở phía trên trước khi được gọi, nên dòng `#include "alt_winmode.cms"` cần đặt ở đầu script trước các lời gọi `A_*`).*
3. **Lưu ý về độ trễ bấm `$A_press_delay` và khi dùng trong luồng (`THREAD`):**
   - Dòng cuối cùng của tệp `alt_winmode.cms` gán biến toàn cục **`$A_press_delay = 30`** (tức chờ `30` mili-giây giữa lúc nhấn xuống và nhả ra trong các lệnh `A_LCLICK`, `A_RCLICK`, `A_MCLICK`, `A_KEYPRESS`). Bạn có thể đổi giá trị biến `$A_press_delay` này trong script nếu ứng dụng đích cần khoảng giữ phím/chuột dài hơn.
   - Theo quy tắc của [`THREAD ... END_THREAD`](/lenh/cau-truc#thread-end-thread) trong help, chương trình con (`SUB`) dùng trong luồng nào thì **bắt buộc phải được khai báo ngay bên trong thân của chính luồng đó** (không gọi được `SUB` khai báo ở ngoài luồng). Vì vậy, nếu bạn gọi các lệnh `A_*` bên trong một khối `THREAD`, hãy đặt dòng `#include "alt_winmode.cms"` ở ngay đầu bên trong thân `THREAD` đó (xem thêm mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#dat-sub-trong-tep-include)).

## Mã nguồn thư viện `alt_winmode.cms` (26 chương trình con)

Dưới đây là nguyên văn 26 chương trình con (`SUB`) và dòng khởi tạo `$A_press_delay = 30` của thư viện `alt_winmode v1.1`:

```cms
//alternative windowed mode v1.1

//-----------------------------------------------------------
//A_LCLICK
SUB(A_LCLICK, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0201,0x0001,$A_x+($A_y*65536))
   waitms($A_press_delay)
   postmessage($A_hwnd,0x0202,0x0001,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_LDOWN
SUB(A_LDOWN, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0201,0x0001,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_LUP
SUB(A_LUP, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0202,0x0001,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_DBLCLICK
SUB(A_DBLCLICK, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0203,0x0001,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
// A_RCLICK
SUB(A_RCLICK, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0204,0x0002,$A_x+($A_y*65536))
   waitms($A_press_delay)
   postmessage($A_hwnd,0x0205,0x0002,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_RDOWN
SUB(A_RDOWN, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0204,0x0002,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_RUP
SUB(A_RUP, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0205,0x0002,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
// A_MCLICK
SUB(A_MCLICK, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0207,0x0010,$A_x+($A_y*65536))
   waitms($A_press_delay)
   postmessage($A_hwnd,0x0208,0x0010,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_MDOWN
SUB(A_MDOWN, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0207,0x0010,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_MUP
SUB(A_MUP, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0208,0x0010,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_MOVE
SUB(A_MOVE, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd,0x0200,0,$A_x+($A_y*65536))
END_SUB
//-----------------------------------------------------------
//A_KEYPRESS
SUB(A_KEYPRESS, $A_key, $A_hwnd)
   postmessage($A_hwnd,0x0100,$A_key,0)
   waitms($A_press_delay)
   postmessage($A_hwnd,0x0101,$A_key,0)
END_SUB
//-----------------------------------------------------------
//A_KEYDOWN
SUB(A_KEYDOWN, $A_key, $A_hwnd)
   postmessage($A_hwnd,0x0100,$A_key,0)
END_SUB
//-----------------------------------------------------------
//A_KEYUP
SUB(A_KEYUP, $A_key, $A_hwnd)
   postmessage($A_hwnd,0x0101,$A_key,0)
END_SUB
//-----------------------------------------------------------
//A_GETSCREEN
SUB(A_GETSCREEN, $A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   IF($A_x1+$A_y1+$A_x2+$A_y2 = 0)
      $A_x2 = $A_width
      $A_y2 = $A_height
   END_IF
   GETSCREEN($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2)
END_SUB
//-----------------------------------------------------------
//A_SCREENSHOTEX
SUB(A_SCREENSHOTEX, $A_x1, $A_y1, $A_x2, $A_y2, $A_pref, $A_format, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   IF(($A_x1+$A_y1+$A_x2+$A_y2) = 0)
      $A_x2 = $A_width
      $A_y2 = $A_height
   END_IF
   SCREENSHOTEX($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2,$A_pref,$A_format)
END_SUB
//-----------------------------------------------------------
//A_PXL
SUB(A_PXL, $A_x, $A_y, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   $A_return1 = PXL($A_x0+$A_x, $A_y0+$A_y)
END_SUB
//-----------------------------------------------------------
//A_PXLCOUNT
SUB(A_PXLCOUNT, $A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   $A_return1 = PXLCOUNT ($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2, $A_color)
END_SUB
//-----------------------------------------------------------
//A_PXLXOR
SUB(A_PXLXOR, $A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   $A_return1 = PXLXOR($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2)
END_SUB
//-----------------------------------------------------------
//A_PXLCRC
SUB(A_PXLCRC, $A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   $A_return1 = PXLCRC($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2)
END_SUB
//-----------------------------------------------------------
//A_IFPIXELIN
SUB(A_IFPIXELIN, $A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   IF_PIXEL_IN($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2, $A_color)
      $A_return1 = $_return1-$A_x0
      $A_return2 = $_return2-$A_y0
   else
      $A_return1 = 0
      $A_return2 = 0
   END_IF
END_SUB
//-----------------------------------------------------------
//A_IFPICTUREIN
SUB(A_IFPICTUREIN, $A_x1, $A_y1, $A_x2, $A_y2, $A_file, $A_bgcolor, $A_currency, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   IF_PICTURE_IN($A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2, $A_file, $A_bgcolor, $A_currency)
      $A_return1 = $_return1-$A_x0
      $A_return2 = $_return2-$A_y0
   else
      $A_return1 = 0
      $A_return2 = 0
   END_IF
END_SUB
//-----------------------------------------------------------
//A_SCANPICTURE
SUB(A_SCANPICTURE, $A_x1, $A_y1, $A_x2, $A_y2, $A_file, $A_bgcolor, $A_currency, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   SCANPICTURE($A_var,$A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2,$A_file,$A_bgcolor,$A_currency)
   FOR($i=0, $i < ARRSIZE($A_var),2)
      $A_var[$i] = $A_var[$i]-$A_x0
      $A_var[$i+1] = $A_var[$i+1]-$A_y0
   END_CYC
END_SUB
//-----------------------------------------------------------
//A_SCANPXL
SUB(A_SCANPXL, $A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   SCANPXL($A_var,$A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2,$A_color)
   FOR($i=0, $i < ARRSIZE($A_var),2)
      $A_var[$i] = $A_var[$i]-$A_x0
      $A_var[$i+1] = $A_var[$i+1]-$A_y0
   END_CYC
END_SUB
//-----------------------------------------------------------
//A_COLORMODE
SUB(A_COLORMODE, $A_mode, $A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   IF(($A_x1+$A_y1+$A_x2+$A_y2) = 0)
      $A_x2 = $A_width
      $A_y2 = $A_height
   END_IF
   COLORMODE ($A_mode, $A_x0+$A_x1,$A_y0+$A_y1,$A_x0+$A_x2,$A_y0+$A_y2)
END_SUB
//-----------------------------------------------------------
//A_CHECK_PXL
SUB(A_CHECK_PXL,$A_hwnd)
   WNDGETINFO ($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
   GETSCREEN
   print("(",$_xmouse-$A_x0,",",$_ymouse-$A_y0,") // ",PXL($_xmouse,$_ymouse))
END_SUB
//-----------------------------------------------------------
$A_press_delay = 30
```

::: info Vì sao lược bỏ A_KEYSTRING khỏi khối mã trên?
Trong tệp `alt_winmode.cms` gốc trên diễn đàn còn có chương trình con thứ 27 là `A_KEYSTRING($A_str, $A_delay, $A_hwnd)`. Chương trình con này được lược bỏ ở đây vì hai lý do:
1. Nó gọi `TFREADARR("keys.txt", $A_keys_arr)` để đọc bảng ánh xạ ký tự từ một tệp `keys.txt` bên ngoài, nhưng tệp `keys.txt` này không có sẵn đi kèm.
2. Nó ép đổi bộ gõ của cửa sổ đích sang tiếng Nga (`SETKBLAYOUT($A_hwnd, 1049)`) và kiểm tra mã băm MD5 riêng cho ký tự tiếng Nga, nên không dùng được cho tiếng Việt hay tiếng Anh khi thiếu tệp `keys.txt`.
:::

## Bảng tra cứu các chương trình con `A_*`

### Giải thích công thức ghép tọa độ `$A_x + ($A_y * 65536)`

Trong tất cả các lệnh chuột của `alt_winmode`, tham số thứ tư (`lParam`) của `POSTMESSAGE` đều được tính bằng biểu thức:

```cms
$A_x + ($A_y * 65536)
```

**Kiến thức Windows:** Trong các thông điệp chuột của Windows (như `WM_LBUTTONDOWN`, `WM_MOUSEMOVE`...), tham số `lParam` là một số nguyên 32-bit chứa cả hai tọa độ tương đối `(X, Y)` bên trong phần tử: 16 bit thấp lưu tọa độ `X` và 16 bit cao lưu tọa độ `Y`. Vì `2^16 = 65536`, phép nhân `$A_y * 65536` chính là dịch giá trị `Y` lên 16 bit cao rồi cộng với `$A_x` ở 16 bit thấp.

### Nhóm lệnh chuột

Mọi tọa độ `$A_x, $A_y` truyền vào nhóm này đều là **tọa độ tương đối** tính từ góc trái trên `(0, 0)` của phần tử `$A_hwnd`.

| Chương trình con và tham số | Tác dụng | Thông điệp Windows gửi qua `POSTMESSAGE` (Kiến thức Windows) |
|---|---|---|
| `A_LCLICK($A_x, $A_y, $A_hwnd)` | Bấm chuột trái 1 lần (nhấn xuống, chờ `$A_press_delay` ms rồi nhả ra) | `0x0201` (`WM_LBUTTONDOWN`, `wParam = 0x0001` / `MK_LBUTTON`), chờ `$A_press_delay`, rồi `0x0202` (`WM_LBUTTONUP`, `wParam = 0x0001`) |
| `A_LDOWN($A_x, $A_y, $A_hwnd)` | Nhấn giữ nút chuột trái tại `($A_x, $A_y)` | `0x0201` (`WM_LBUTTONDOWN`, `wParam = 0x0001`) |
| `A_LUP($A_x, $A_y, $A_hwnd)` | Nhả nút chuột trái tại `($A_x, $A_y)` | `0x0202` (`WM_LBUTTONUP`, `wParam = 0x0001`) |
| `A_DBLCLICK($A_x, $A_y, $A_hwnd)` | Nhấp đúp chuột trái tại `($A_x, $A_y)` | `0x0203` (`WM_LBUTTONDBLCLK`, `wParam = 0x0001`) |
| `A_RCLICK($A_x, $A_y, $A_hwnd)` | Bấm chuột phải 1 lần (nhấn xuống, chờ `$A_press_delay` ms rồi nhả ra) | `0x0204` (`WM_RBUTTONDOWN`, `wParam = 0x0002` / `MK_RBUTTON`), chờ `$A_press_delay`, rồi `0x0205` (`WM_RBUTTONUP`, `wParam = 0x0002`) |
| `A_RDOWN($A_x, $A_y, $A_hwnd)` | Nhấn giữ nút chuột phải tại `($A_x, $A_y)` | `0x0204` (`WM_RBUTTONDOWN`, `wParam = 0x0002`) |
| `A_RUP($A_x, $A_y, $A_hwnd)` | Nhả nút chuột phải tại `($A_x, $A_y)` | `0x0205` (`WM_RBUTTONUP`, `wParam = 0x0002`) |
| `A_MCLICK($A_x, $A_y, $A_hwnd)` | Bấm chuột giữa 1 lần (nhấn xuống, chờ `$A_press_delay` ms rồi nhả ra) | `0x0207` (`WM_MBUTTONDOWN`, `wParam = 0x0010` / `MK_MBUTTON`), chờ `$A_press_delay`, rồi `0x0208` (`WM_MBUTTONUP`, `wParam = 0x0010`) |
| `A_MDOWN($A_x, $A_y, $A_hwnd)` | Nhấn giữ nút chuột giữa tại `($A_x, $A_y)` | `0x0207` (`WM_MBUTTONDOWN`, `wParam = 0x0010`) |
| `A_MUP($A_x, $A_y, $A_hwnd)` | Nhả nút chuột giữa tại `($A_x, $A_y)` | `0x0208` (`WM_MBUTTONUP`, `wParam = 0x0010`) |
| `A_MOVE($A_x, $A_y, $A_hwnd)` | Báo di chuyển chuột tới `($A_x, $A_y)` (không giữ nút chuột) | `0x0200` (`WM_MOUSEMOVE`, `wParam = 0` — xem bẫy khi kéo vẽ ở mục dưới) |

### Nhóm lệnh bàn phím

Tham số `$A_key` là mã phím ảo thập phân hoặc hằng số phím (xem [Bảng mã phím và hằng số](/phu-luc/ma-phim)).

| Chương trình con và tham số | Tác dụng | Thông điệp Windows gửi qua `POSTMESSAGE` (Kiến thức Windows) |
|---|---|---|
| `A_KEYPRESS($A_key, $A_hwnd)` | Bấm và nhả một phím (nhấn phím xuống, chờ `$A_press_delay` ms rồi nhả phím) | `0x0100` (`WM_KEYDOWN`, `wParam = $A_key`, `lParam = 0`), chờ `$A_press_delay`, rồi `0x0101` (`WM_KEYUP`, `wParam = $A_key`, `lParam = 0`) |
| `A_KEYDOWN($A_key, $A_hwnd)` | Nhấn giữ phím `$A_key` | `0x0100` (`WM_KEYDOWN`, `wParam = $A_key`, `lParam = 0`) |
| `A_KEYUP($A_key, $A_hwnd)` | Nhả phím `$A_key` | `0x0101` (`WM_KEYUP`, `wParam = $A_key`, `lParam = 0`) |

### Nhóm lệnh đọc màn hình và màu sắc

Nhóm này không dùng `POSTMESSAGE` mà gọi [`WNDGETINFO($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)`](/lenh/winapi#wndgetinfo) để lấy tọa độ góc trái trên `($A_x0, $A_y0)` của cửa sổ trên màn hình, rồi cộng vào tọa độ tương đối trước khi gọi các lệnh màn hình chuẩn.

| Chương trình con và tham số | Tác dụng | Biến nhận kết quả trả về |
|---|---|---|
| `A_GETSCREEN($A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)` | Chụp vùng tương đối `($A_x1, $A_y1) - ($A_x2, $A_y2)` của cửa sổ `$A_hwnd` vào bộ đệm ảnh. Nếu truyền `0, 0, 0, 0` thì chụp toàn bộ kích thước cửa sổ (`$A_width`, `$A_height`). | *(Cập nhật vào bộ đệm ảnh)* |
| `A_SCREENSHOTEX($A_x1, $A_y1, $A_x2, $A_y2, $A_pref, $A_format, $A_hwnd)` | Lưu ảnh chụp vùng tương đối của cửa sổ ra đĩa bằng [`SCREENSHOTEX`](/lenh/man-hinh#screenshotex). Nếu truyền `0, 0, 0, 0` thì lưu cả cửa sổ. | *(Lưu tệp ảnh ra đĩa)* |
| `A_PXL($A_x, $A_y, $A_hwnd)` | Đọc mã màu tại tọa độ tương đối `($A_x, $A_y)` của cửa sổ từ bộ đệm ảnh. | `$A_return1` (mã màu) |
| `A_PXLCOUNT($A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)` | Đếm số điểm ảnh có màu `$A_color` trong vùng tương đối của cửa sổ. | `$A_return1` (số điểm ảnh) |
| `A_PXLXOR($A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)` | Tính mã kiểm tra `PXLXOR` của vùng tương đối trong cửa sổ. | `$A_return1` (mã XOR) |
| `A_PXLCRC($A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)` | Tính mã kiểm tra `PXLCRC` (CRC32) của vùng tương đối trong cửa sổ. | `$A_return1` (mã CRC32) |
| `A_IFPIXELIN($A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)` | Tìm điểm ảnh có màu `$A_color` trong vùng tương đối và đổi kết quả về tọa độ tương đối của cửa sổ. | `$A_return1` (X tương đối), `$A_return2` (Y tương đối); nếu không thấy thì cả hai bằng `0` |
| `A_IFPICTUREIN($A_x1, $A_y1, $A_x2, $A_y2, $A_file, $A_bgcolor, $A_currency, $A_hwnd)` | Tìm ảnh mẫu `.bmp` trong vùng tương đối và đổi kết quả về tọa độ tương đối của cửa sổ. | `$A_return1` (X tương đối), `$A_return2` (Y tương đối); nếu không thấy thì cả hai bằng `0` |
| `A_SCANPICTURE($A_x1, $A_y1, $A_x2, $A_y2, $A_file, $A_bgcolor, $A_currency, $A_hwnd)` | Tìm mọi vị trí của ảnh `.bmp` trong vùng tương đối và trừ `$A_x0, $A_y0` để đổi sang tọa độ tương đối. | Mảng `$A_var` (các cặp X, Y tương đối) |
| `A_SCANPXL($A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)` | Tìm mọi điểm ảnh có màu `$A_color` trong vùng tương đối và trừ `$A_x0, $A_y0` để đổi sang tọa độ tương đối. | Mảng `$A_var` (các cặp X, Y tương đối) |
| `A_COLORMODE($A_mode, $A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)` | Áp dụng giảm màu `COLORMODE` cho vùng tương đối của cửa sổ (truyền `0, 0, 0, 0` là cả cửa sổ). | *(Biến đổi bộ đệm ảnh)* |
| `A_CHECK_PXL($A_hwnd)` | Công cụ hỗ trợ lấy tọa độ tương đối và mã màu tại vị trí trỏ chuột hiện tại rồi in ra cửa sổ nhật ký theo dạng `(x,y) // màu`. | *(In ra cửa sổ nhật ký)* |

::: warning Lưu ý về biến kết quả dùng chung giữa các luồng
Khác với hàm chuẩn của Clickermann, các chương trình con `A_*` lưu kết quả vào các biến **`$A_return1`**, **`$A_return2`**, mảng **`$A_var`** và dùng các biến tạm như `$A_x0`, `$A_y0`, `$A_width`, `$A_height`.

**Suy luận** (từ phần phạm vi biến của [`THREAD`](/khai-niem/luong) trong help — mọi luồng đều đọc và ghi chung một phạm vi biến toàn cục): Nếu hai luồng (`THREAD`) cùng gọi các lệnh `A_*` vào cùng một thời điểm, các biến chung `$A_return1`, `$A_return2`, `$A_var` và `$A_x0`, `$A_y0` của luồng này có thể bị luồng kia **ghi đè lên nhau**. Để tránh xung đột khi dùng đa luồng, chỉ nên để một luồng gọi các lệnh đọc màn hình `A_*`, hoặc tự tạo bản sao `SUB` với tên biến riêng cho từng luồng.
:::

## Các bẫy dễ gặp và cách phòng tránh

Khi dùng `alt_winmode`, có 7 điểm kỹ thuật rất dễ gây lỗi ngầm nếu bạn không biết trước:

### Bẫy khi kéo chuột vẽ nền: `A_MOVE` không giữ nút chuột trái

- **Nguyên nhân:** Trong `alt_winmode.cms`, lệnh `A_MOVE` gửi thông điệp `0x0200` (`WM_MOUSEMOVE`) với tham số **`wParam = 0`**, tức là báo cho cửa sổ biết con trỏ chuột di chuyển trong trạng thái **không có nút chuột nào đang được nhấn giữ**.
- **Kiến thức Windows:** Khi kéo chuột để vẽ nét cọ (như trong Paint) hoặc kéo chọn vùng, ứng dụng kiểm tra cờ `MK_LBUTTON` (`0x0001`) trong `wParam` của thông điệp `WM_MOUSEMOVE` (`0x0200`) để biết nút chuột trái vẫn đang được giữ trong lúc di chuyển. Nếu gọi `A_LDOWN` rồi gọi `A_MOVE` (`wParam = 0`), ứng dụng sẽ hiểu là chuột di chuyển mà không giữ nút trái nên không vẽ ra nét.
- **Cách tránh:** Tự định nghĩa thêm một chương trình con **`A_DRAG`** giống `A_MOVE` nhưng thay `wParam` từ `0` thành **`0x0001`**:
  ```cms
  // Chương trình con di chuyển chuột trong khi vẫn giữ nút chuột trái (wParam = 0x0001)
  SUB(A_DRAG, $A_x, $A_y, $A_hwnd)
     postmessage($A_hwnd, 0x0200, 0x0001, $A_x + ($A_y * 65536))
  END_SUB
  ```
  *(Xem kịch bản kiểm chứng thực tế giữa `A_MOVE` và `A_DRAG` tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#kiem-tra-cac-diem-can-luu-y-cua-thu-vien-alt-winmode)).*

### Bẫy ở `A_IFPIXELIN` và `A_IFPICTUREIN` khi màu hoặc ảnh nằm ở cột `x = 0`

- **Nguyên nhân:** Khi không tìm thấy màu hoặc ảnh, `A_IFPIXELIN` và `A_IFPICTUREIN` gán `$A_return1 = 0` và `$A_return2 = 0`. Nếu bạn kiểm tra kết quả bằng điều kiện `IF($A_return1 > 0)`, thì trường hợp tìm thấy thật ở ngay mép trái phần tử (**cột tương đối `x = 0`**, khiến `$_return1 - $A_x0 = 0`) cũng cho `$A_return1 = 0` và **bị nhầm thành không tìm thấy**.
- **Cách tránh:**
  - **Cách 1 (đơn giản nhất):** Luôn đặt tọa độ bắt đầu vùng tìm kiếm từ cột `1` trở đi (ví dụ `$A_x1 >= 1`) để vùng quét không bao giờ chứa cột `0`.
  - **Cách 2:** Tự viết một chương trình con có thêm biến cờ **`$A_thay`** (`1` là tìm thấy, `0` là không tìm thấy) để kiểm tra chính xác kể cả tại tọa độ `(0, 0)`:
    ```cms
    SUB(A_IFPIXELIN_SAFE, $A_x1, $A_y1, $A_x2, $A_y2, $A_color, $A_hwnd)
       WNDGETINFO($A_hwnd, $A_x0, $A_y0, $A_width, $A_height)
       $A_thay = 0
       IF_PIXEL_IN($A_x0 + $A_x1, $A_y0 + $A_y1, $A_x0 + $A_x2, $A_y0 + $A_y2, $A_color)
          $A_thay = 1
          $A_return1 = $_return1 - $A_x0
          $A_return2 = $_return2 - $A_y0
       END_IF
    END_SUB
    ```

### Bẫy khi gọi `A_SCANPXL` hoặc `A_SCANPICTURE` nhiều lần liên tiếp

- **Nguyên nhân:** Trong help, phần mô tả [`SCANPXL`](/lenh/man-hinh#scanpxl) và [`SCANPICTURE`](/lenh/man-hinh#scanpicture) nói tọa độ các điểm tìm thấy được "thêm vào mảng `$var`", nhưng không nói rõ mảng cũ có tự động được xóa trước mỗi lần gọi hay không. Trong khi đó, `A_SCANPXL` và `A_SCANPICTURE` chạy vòng lặp `FOR($i=0, $i < ARRSIZE($A_var), 2)` để trừ `$A_x0` và `$A_y0` cho toàn bộ phần tử trong `$A_var`. Nếu `SCANPXL` không tự xóa mảng cũ và bạn chưa rút hết phần tử bằng `ARRPOP`, lần gọi thứ hai sẽ khiến các tọa độ cũ còn sót lại trong `$A_var` **bị trừ `$A_x0, $A_y0` hai lần** dẫn tới sai lệch hoàn toàn.
- **Cách tránh:** Luôn gọi **`UNDEFINE($A_var)`** ngay trước mỗi lần gọi `A_SCANPXL` hoặc `A_SCANPICTURE` (xem mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#kiem-tra-cac-diem-can-luu-y-cua-thu-vien-alt-winmode)):
  ```cms
  UNDEFINE($A_var)
  A_SCANPXL(10, 10, 200, 200, 255, $hwnd)
  ```

### Bẫy khi cửa sổ bị che khuất với `A_GETSCREEN` và `A_PXL`

- **Nguyên nhân:** Các lệnh đồ họa trong `alt_winmode` (`A_GETSCREEN`, `A_PXL`, `A_IFPIXELIN`...) không bật chế độ khóa cửa sổ của Clickermann mà chỉ dùng `WNDGETINFO` để đổi tọa độ tương đối sang tọa độ màn hình chung rồi gọi `GETSCREEN` ở chế độ thường.
- **Suy luận:** Vì `GETSCREEN` đang chụp ở chế độ màn hình thường theo tọa độ desktop `($A_x0 + $A_x1, ...)`, **cửa sổ đích bắt buộc phải đang hiển thị trên màn hình và không bị cửa sổ khác đè lên che khuất** (nếu bị cửa sổ khác che, `A_GETSCREEN` và `A_PXL` sẽ chụp và đọc nhầm màu của cửa sổ đang nằm đè ở phía trên — khác với [chế độ khóa cửa sổ](/khai-niem/khoa-cua-so) vốn có thể đọc màu khi bị che tùy ứng dụng).
- Ngoài ra, vì `A_GETSCREEN($A_x1, $A_y1, $A_x2, $A_y2, $A_hwnd)` chỉ cập nhật đúng vùng chữ nhật được chỉ định trong bộ đệm ảnh, các vùng khác ngoài khu vực đó vẫn giữ nguyên hình ảnh từ lần chụp trước (theo mô tả của [`GETSCREEN`](/lenh/man-hinh#getscreen) trong help).
- **Cách tránh:** Khi cần kết hợp cả đọc màu bằng `A_*` và điều khiển nhiều cửa sổ, hãy sắp xếp các cửa sổ nằm cạnh nhau trên màn hình để không cửa sổ nào che khuất vùng cần đọc màu của cửa sổ kia (xem kỹ thuật xếp cửa sổ tại [Thực chiến: kỹ thuật viết script](/cam-nang/thuc-chien#xep-nhieu-cua-so-khong-chong-len-nhau-va-lay-phan-tu-con-bang-hget)).

### Lưu ý về tham số `0, 0, 0, 0` ở `A_GETSCREEN` và lệnh nhấp đúp `A_DBLCLICK`

- **Tham số `0, 0, 0, 0`:** Trong `A_GETSCREEN`, `A_SCREENSHOTEX` và `A_COLORMODE`, điều kiện `IF($A_x1 + $A_y1 + $A_x2 + $A_y2 = 0)` sẽ tự động gán `$A_x2 = $A_width` và `$A_y2 = $A_height`. Nhờ đó, truyền `0, 0, 0, 0` có nghĩa là thao tác trên **toàn bộ diện tích của cửa sổ/phần tử `$A_hwnd`**.
- **Lưu ý về `A_DBLCLICK`:** Chương trình con `A_DBLCLICK` chỉ gửi duy nhất một thông điệp `0x0203` (`WM_LBUTTONDBLCLK`). **Suy luận:** Một số ứng dụng trong thực tế có thể đòi hỏi đầy đủ chuỗi sự kiện nhấn-nhả-nhấp đúp-nhả mới nhận diện thao tác nhấp đúp, nên chỉ gửi một thông điệp `0x0203` có thể không đủ với mọi ứng dụng; nếu `A_DBLCLICK` không tác dụng, hãy thử gọi hai lần `A_LCLICK` liên tiếp cách nhau `WAITMS(50)`.

### Bẫy với lệnh bàn phím (`lParam = 0`) và tổ hợp phím `Ctrl`, `Alt`

- **Nguyên nhân:** Các lệnh `A_KEYPRESS`, `A_KEYDOWN`, `A_KEYUP` đều gửi `POSTMESSAGE` với tham số thứ tư **`lParam = 0`**, và thư viện không có hàm riêng cho các tổ hợp phím như `Ctrl + A`, `Ctrl + S` hay `Alt + F4`.
- **Kiến thức Windows:** Trong thông điệp bàn phím `WM_KEYDOWN` (`0x0100`) và `WM_KEYUP` (`0x0101`), tham số `lParam` chứa nhiều trường bit phụ như số lần lặp (repeat count), mã quét phím cứng (scan code), cờ phím mở rộng và trạng thái phím trước đó; đồng thời việc kiểm tra phím `Ctrl`, `Shift` đang giữ thường dựa vào trạng thái bàn phím chung của luồng giao diện chứ không chỉ qua một thông điệp `POSTMESSAGE` đơn lẻ. Vì vậy, một số ứng dụng kiểm tra kỹ `lParam` hoặc kiểm tra trạng thái phím `Ctrl`/`Alt` toàn cục sẽ bỏ qua thông điệp có `lParam = 0` hoặc không nhận tổ hợp phím ghép bằng `A_KEYDOWN(#CTRL)` + `A_KEYPRESS(...)`.
- **Cách tránh:** Hãy thử nghiệm trước với từng phím đơn (như phím chữ, phím `Enter`, `Space`, phím `F1..F12`). Với ô nhập văn bản chuẩn của Windows, bạn cũng có thể thử lệnh [`HSETTEXT(hwnd, text)`](/lenh/winapi#hsettext) để đặt thẳng chuỗi văn bản.

### Không phải ứng dụng nào cũng nhận thông điệp

- Trong bài [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so), help nêu rõ chế độ cửa sổ có hoạt động hay không hoàn toàn phụ thuộc vào cách ứng dụng đích được lập trình. Điều này cũng có khả năng đúng với `alt_winmode`: nếu một ứng dụng tự đọc trạng thái chuột/phím ở tầng thấp mà bỏ qua thông điệp `POSTMESSAGE`, các lệnh `A_*` sẽ không có tác dụng trên ứng dụng đó.
- Đặc biệt, như help giải thích ở bài Khóa cửa sổ, mỗi thành phần bên trong một cửa sổ lớn (như khung soạn thảo của Notepad hay trang giấy vẽ của Paint) là một **phần tử con** có mã `hwnd` riêng. Bạn cần truyền `hwnd` của **đúng phần tử con nhận thao tác** (lấy bằng [`HGET(x, y)`](/lenh/winapi#hget)), chứ không phải `hwnd` của khung cửa sổ cha ngoài cùng lấy từ `WNDFIND`.

## Ví dụ thực hành (chưa chạy thử)

### Ví dụ: Gõ phím vào cửa sổ Notepad bằng `HGET` và `A_KEYPRESS`

**Trạng thái:** 🟡 Chưa chạy thử

Trong Notepad, khung trắng nơi gõ chữ là một phần tử con nằm bên trong cửa sổ chính. Ví dụ dưới đây tìm cửa sổ Notepad bằng `WNDFIND`, đặt cửa sổ về vị trí cố định `(100, 100)` với kích thước `500×400`, sau đó dùng `HGET(250, 250)` để lấy `hwnd` của khung soạn thảo bên trong rồi gửi các phím `A`, `B`, `C` tới phần tử đó qua `A_KEYPRESS`:

```cms
#include "alt_winmode.cms"

// 1. Tìm cửa sổ chính của Notepad và cố định vị trí, kích thước
$hwnd_cha = WNDFIND("Notepad")
IF($hwnd_cha = 0)
   PRINT("Khong tim thay cua so Notepad! Hay mo Notepad truoc.")
   HALT
END_IF

WNDPOS($hwnd_cha, 100, 100)
WNDSIZE($hwnd_cha, 500, 400)
WAITMS(300)

// 2. Lấy hwnd của phần tử con (khung soạn thảo) tại tọa độ màn hình (250, 250)
// Điểm (250, 250) nằm gọn bên trong vùng soạn thảo của cửa sổ vừa đặt ở (100, 100)
$hwnd_soan_thao = HGET(250, 250)
PRINT("HWND cua so cha: ", $hwnd_cha, " | HWND khung soan thao: ", $hwnd_soan_thao)

// 3. Gửi lần lượt các phím A (65), B (66), C (67) vào khung soạn thảo
A_KEYPRESS(#A, $hwnd_soan_thao)
WAITMS(100)
A_KEYPRESS(#B, $hwnd_soan_thao)
WAITMS(100)
A_KEYPRESS(#C, $hwnd_soan_thao)

PRINT("Da gui xong 3 phim A, B, C qua A_KEYPRESS.")
HALT
```

### Ví dụ: Kéo chuột vẽ nét trong Paint bằng `A_LDOWN`, `A_DRAG`, `A_LUP`

**Trạng thái:** 🟡 Chưa chạy thử

Như đã phân tích ở mục bẫy phía trên, để kéo chuột vẽ nét trong vùng giấy vẽ của Paint qua `POSTMESSAGE`, bạn cần định nghĩa thêm chương trình con `A_DRAG` gửi `wParam = 0x0001` (cờ giữ nút chuột trái).

Trước khi chạy script, hãy mở sẵn cửa sổ **Paint** và chọn công cụ **Bút chì (Pencil)** hoặc **Cọ vẽ (Brushes)**:

```cms
#include "alt_winmode.cms"

// Định nghĩa thêm A_DRAG giữ cờ nút chuột trái (wParam = 0x0001) khi di chuyển
SUB(A_DRAG, $A_x, $A_y, $A_hwnd)
   postmessage($A_hwnd, 0x0200, 0x0001, $A_x + ($A_y * 65536))
END_SUB

// 1. Tìm cửa sổ Paint và đặt ở vị trí (50, 50), kích thước 700x550
$hwnd_paint = WNDFIND("Paint")
IF($hwnd_paint = 0)
   PRINT("Khong tim thay cua so Paint! Hay mo Paint truoc.")
   HALT
END_IF

WNDPOS($hwnd_paint, 50, 50)
WNDSIZE($hwnd_paint, 700, 550)
WAITMS(500)

// 2. Lấy hwnd của phần tử trang giấy vẽ tại tọa độ màn hình (300, 350)
$hwnd_giay_ve = HGET(300, 350)
PRINT("HWND trang giay ve cua Paint: ", $hwnd_giay_ve)

// 3. Vẽ một đoạn thẳng ngang trên trang giấy vẽ (tọa độ tương đối bên trong phần tử giấy vẽ)
// Nhấn giữ chuột trái tại (50, 80), kéo qua (150, 80) -> (250, 80) rồi nhả chuột
A_LDOWN(50, 80, $hwnd_giay_ve)
WAITMS(50)
A_DRAG(150, 80, $hwnd_giay_ve)
WAITMS(50)
A_DRAG(250, 80, $hwnd_giay_ve)
WAITMS(50)
A_LUP(250, 80, $hwnd_giay_ve)

PRINT("Da gui xong thao tac keo ve qua A_LDOWN -> A_DRAG -> A_LUP.")
HALT
```

---

*Nguồn: Thư viện cộng đồng `alt_winmode.cms` (`alternative windowed mode v1.1`, công khai trên diễn đàn Clickermann, chưa rõ tác giả) và tài liệu trợ giúp `help.chm` (bài Khóa cửa sổ, mục WinAPI, mục Cấu trúc lệnh và mục Màn hình).*
