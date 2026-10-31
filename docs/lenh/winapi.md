# Cửa sổ và WinAPI

Trang này hướng dẫn các thủ tục và hàm làm việc với các cửa sổ Windows và phần tử con bên trong chúng. Mỗi cửa sổ hoặc phần tử trên Windows đều có một mã định danh duy nhất dạng số gọi là `hwnd`; khi biết mã `hwnd` này, script có thể khóa cửa sổ, đổi vị trí/kích thước, đọc/ghi văn bản hoặc gửi thông điệp hệ thống trực tiếp tới phần tử đó.

## HGET

Trả về mã định danh `hwnd` của phần tử nằm tại tọa độ màn hình chỉ định.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HGET (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm ảnh thuộc về phần tử cần lấy `hwnd` |

**Trả về:** Mã số `hwnd` của phần tử tại tọa độ `(x, y)`.

**Ví dụ**

```cms
// Lấy hwnd của phần tử tại tọa độ (44, 1010)
$h = HGET(44, 1010)

// In văn bản trên phần tử đó
PRINT(HGETTEXT($h))
HALT
```

---

## HSET

Thiết lập phần tử đang khóa mới cho chế độ khóa cửa sổ của Clickermann.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HSET (hwnd, state)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của phần tử cần khóa |
| `state` | số | có | | Trạng thái chế độ khóa cửa sổ (`1` — bật khóa cửa sổ; `0` — tắt khóa cửa sổ) |

**Ví dụ**

```cms
// Lấy hwnd của phần tử tại tọa độ (44, 1010)
$h = HGET(44, 1010)

// Bật chế độ khóa cửa sổ nhắm vào phần tử này
HSET($h, 1)
HALT
```

**Lưu ý**

- Nếu bạn chỉ muốn chuyển sang một phần tử đang khóa khác trong khi đã ở chế độ khóa cửa sổ, không cần phải tắt khóa cửa sổ bằng cờ `0` trước; chỉ cần gọi thẳng `HSET($hwnd_moi, 1)` với `hwnd` mới ở tham số đầu tiên.

---

## HGETPID

Trả về mã tiến trình (`pid`) của chương trình sở hữu phần tử cửa sổ theo mã `hwnd`.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HGETPID (hwnd)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ hoặc phần tử con |

**Trả về:** Mã số định danh tiến trình (`pid`) của tiến trình cha.

**Ví dụ**

```cms
// Lấy PID của chính chương trình Clickermann
$h = HGETPID($_hwnd_self)
PRINT($h)
HALT
```

---

## HGETTEXT

Trả về chuỗi văn bản trên các phần tử điều khiển trong cửa sổ Windows.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HGETTEXT (hwnd)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của phần tử |

**Trả về:** Chuỗi văn bản hiện có trên phần tử đó.

**Ví dụ**

```cms
// Ví dụ 1
$h = HGET(44, 1010)
PRINT(HGETTEXT($h))

// Ví dụ 2 (qua biến chuỗi)
$h = HGET(44, 1010)
$text = HGETTEXT($h)
PRINT($text)
HALT
```

---

## HSETTEXT

Đặt chuỗi văn bản trên các phần tử điều khiển trong cửa sổ Windows.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HSETTEXT (hwnd, text)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của phần tử |
| `text` | chuỗi | có | | Chuỗi văn bản muốn đặt |

**Ví dụ**

```cms
$h = HGET(44, 1010)
HSETTEXT($h, "van ban moi")
HALT
```

---

## WNDFIND

Tìm cửa sổ theo chuỗi tiêu đề và trả về mã `hwnd` của cửa sổ đó.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WNDFIND (title, [begin])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `title` | chuỗi | có | | Tiêu đề cửa sổ hoặc một phần của tiêu đề |
| `begin` | số | không | Help không nói rõ | Cờ báo chuỗi `title` chỉ được nằm ở đầu tiêu đề cửa sổ |

**Trả về:** Mã số `hwnd` của cửa sổ tìm thấy (trả về `0` nếu không tìm thấy cửa sổ nào thỏa điều kiện).

**Ví dụ**

```cms
// Tìm cửa sổ có tiêu đề chứa chữ "Notepad"
// và đưa nó về góc trái trên màn hình (cách lề 10 pixel)
WNDPOS(WNDFIND("Notepad"), 10, 10)

// Tìm cửa sổ "Notepad" và đổi tiêu đề của nó thành "May tinh"
HSETTEXT(WNDFIND("Notepad"), "May tinh")
HALT
```

**Lưu ý**

- Chuỗi tiêu đề `title` viết càng đầy đủ thì càng ít nguy cơ bắt nhầm sang cửa sổ khác.
- Nếu không tìm thấy cửa sổ nào thỏa điều kiện, hàm trả về `0`.
- Hàm này không dùng được để tìm các phần tử con riêng lẻ của cửa sổ (như nút bấm, ô nhập, nhãn chữ).

---

## WNDPOS

Di chuyển cửa sổ tới vị trí tọa độ chỉ định trên màn hình.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WNDPOS (hwnd, x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ cần di chuyển |
| `x, y` | số | có | | Tọa độ vị trí mới của cửa sổ trên màn hình |

**Ví dụ**

```cms
// Tìm cửa sổ có tiêu đề chứa "Notepad" và đặt vào vị trí 10:10
WNDPOS(WNDFIND("Notepad"), 10, 10)
HALT
```

---

## WNDSIZE

Thay đổi kích thước chiều rộng và chiều cao của cửa sổ.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WNDSIZE (hwnd, w, h)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ |
| `w, h` | số | có | | Chiều rộng (`w`) và chiều cao (`h`) của cửa sổ |

**Ví dụ**

```cms
// Tìm cửa sổ "Notepad" và đổi kích thước thành hình vuông 300x300
WNDSIZE(WNDFIND("Notepad"), 300, 300)
HALT
```

**Lưu ý**

- Không thể thu nhỏ cửa sổ xuống 1 pixel, vì biểu tượng và vài chữ của tiêu đề sẽ cản lại.

---

## WNDGETINFO

Lấy thông tin của cửa sổ và ghi vào các biến chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WNDGETINFO (hwnd, $var1, $var2, $var3, $var4)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ |
| `$var1` | biến | có | | Biến nhận tọa độ X của cửa sổ |
| `$var2` | biến | có | | Biến nhận tọa độ Y của cửa sổ |
| `$var3` | biến | có | | Biến nhận chiều rộng của cửa sổ |
| `$var4` | biến | có | | Biến nhận chiều cao của cửa sổ |

**Ví dụ**

```cms
$hwnd = WNDFIND("Notepad")
WNDGETINFO($hwnd, $var1, $var2, $var3, $var4)
PRINT("X=", $var1, " Y=", $var2, " W=", $var3, " H=", $var4)
HALT
```

---

## WNDSETINFO

Cập nhật thông tin vị trí và kích thước của cửa sổ.

**Loại:** thủ tục · **Trạng thái:** 🟠 Chưa thống nhất

```cms
WNDSETINFO (hwnd, $var1, $var2, $var3, $var4)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ cần cập nhật |
| `$var1` | biến (🟠 xem lưu ý về truyền số trực tiếp) | có | | Tọa độ X |
| `$var2` | biến (🟠 xem lưu ý về truyền số trực tiếp) | có | | Tọa độ Y |
| `$var3` | biến (🟠 xem lưu ý về truyền số trực tiếp) | có | | Chiều rộng |
| `$var4` | biến (🟠 xem lưu ý về truyền số trực tiếp) | có | | Chiều cao |

**Ví dụ**

```cms
// Thử nghiệm với cửa sổ Calculator
$hwnd = WNDFIND("Calculator")

// Lấy thông tin
WNDGETINFO($hwnd, $var1, $var2, $var3, $var4)

// Ghi lại kích thước cửa sổ
$var3 = 100
$var4 = 100

// Cập nhật thông tin
WNDSETINFO($hwnd, $var1, $var2, $var3, $var4)
HALT
```

**Lưu ý**

- 🟠 **Điểm cần kiểm chứng khi truyền tham số cho `WNDSETINFO`:**
  - **Nên làm:** Hãy gán tọa độ và kích thước vào 4 biến (`$var1`, `$var2`, `$var3`, `$var4`) rồi truyền biến vào `WNDSETINFO($hwnd, $var1, $var2, $var3, $var4)` giống như ví dụ trong help (hoặc dùng [`WNDPOS`](#wndpos) và [`WNDSIZE`](#wndsize) nếu muốn truyền số trực tiếp).
  ::: details Vì sao chưa chắc
  - **Theo help:** Cú pháp ghi các tham số là `$var1, $var2, $var3, $var4` và ví dụ trong help chỉ truyền biến (sau khi lấy từ `WNDGETINFO`).
  - **Theo sách của Chô tô (tr. 117):** Sách truyền số trực tiếp vào `WNDSETINFO`.
  - Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#truyen-so-truc-tiep-vao-wndsetinfo).
  :::

---

## WNDSTATE

Thu nhỏ (hoặc mở ra) cửa sổ.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WNDSTATE (hwnd, state)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ |
| `state` | số | có | | Trạng thái cửa sổ (`0` — thu nhỏ; `1` — mở ra; help không nói rõ là khôi phục kích thước cũ hay phóng to) |

**Ví dụ**

```cms
// Tìm cửa sổ có tiêu đề chứa "Notepad" và thu nhỏ nó xuống
WNDSTATE(WNDFIND("Notepad"), 0)
WAIT(1)

// ... rồi mở ra lại
WNDSTATE(WNDFIND("Notepad"), 1)
WAIT(1)
HALT
```

---

## WNDBUMP

Đưa cửa sổ được chỉ định lên lớp trên cùng (tiền cảnh).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WNDBUMP (hwnd)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ cần đưa lên trước |

**Ví dụ**

```cms
WNDBUMP(WNDFIND("Notepad"))
HALT
```

---

## SENDMESSAGE, POSTMESSAGE

Gửi thông điệp hệ thống tới cửa sổ.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SENDMESSAGE / POSTMESSAGE (hwnd, message, wParam, lParam)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã `hwnd` của cửa sổ |
| `message` | số | có | | Mã thông điệp gửi tới cửa sổ (viết bằng số thập phân) |
| `wParam, lParam` | số | có | | Hai tham số của thông điệp |

**Ví dụ**

```cms
$h = WNDFIND("Clickermann")
POSTMESSAGE($h, 1024, 123, 321)
HALT
```

**Lưu ý**

- Hai thủ tục này thực chất là lớp bọc cho hai hàm WinAPI cùng tên; chi tiết xem tài liệu Microsoft (MSDN).
- Vì chương trình không có đủ các hằng số `"WM_"`, tham số `message` cần được truyền bằng số thập phân. Xem thêm ví dụ tại [`GETMESSAGE`](#getmessage).

---

## GETMESSAGE

Nhận thông điệp hệ thống `1024` (`WM_USER`) được gửi tới cửa sổ chính của Clickermann.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
GETMESSAGE (wParam, lParam, [isnew])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `wParam, lParam` | biến | có | | Các biến nhận tham số của thông điệp nhận được |
| `isnew` | biến | không | | Biến nhận cờ báo có thông điệp mới (`1` — vừa có thông điệp mới; `0` — chưa có thêm thông điệp mới) |

**Ví dụ**

```cms
// Tìm cửa sổ chính của Clickermann
$h = WNDFIND("Clickermann")

// Gửi thông điệp tới cửa sổ Clickermann
POSTMESSAGE($h, 1024, 123, 321)

// Nhận thông điệp
GETMESSAGE($var1, $var2)
PRINT("wParam:", $var1, " lParam:", $var2)
```

**Lưu ý**

- Thủ tục này chỉ nhận các thông điệp có `message = 1024` (xem [`SENDMESSAGE, POSTMESSAGE`](#sendmessage-postmessage)) và chỉ lấy được các tham số của thông điệp cuối cùng nhận được. Thông điệp chỉ được nhận trong lúc script đang chạy.
- Tại thời điểm nhận được thông điệp mới từ chương trình khác, cờ `isnew` bằng `1`. Ở các lần gọi lại thủ tục trước khi có thông điệp mới tiếp theo, cờ `isnew` bằng `0`, nhưng hai tham số `wParam`, `lParam` vẫn giữ nguyên giá trị cũ.
- Mã thông điệp `message` cần bắt có thể đổi trong `config.ini` (tham số `msg_hook`).
- Ví dụ trên giữ nguyên như trong help (không có `HALT`). Cần kiểm tra thêm trên Windows xem gọi `POSTMESSAGE` rồi `GETMESSAGE` ngay trong cùng một lượt chạy có nhận được thông điệp ngay hay phải sang vòng lặp sau (xem [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#postmessage-roi-getmessage-ngay-trong-cung-luot)).
