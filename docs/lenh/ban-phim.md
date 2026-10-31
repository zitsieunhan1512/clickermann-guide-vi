# Bàn phím

Trang này hướng dẫn các thủ tục và hàm dùng để bấm phím, giữ phím, gõ chuỗi văn bản, kiểm tra phím đang được nhấn và đổi ngôn ngữ bộ gõ của cửa sổ. Mỗi phím trên bàn phím có một mã số riêng (ví dụ phím cách là `32`, hoặc dùng hằng số `#SPACE`; xem danh sách đầy đủ tại [Bảng mã phím](/phu-luc/ma-phim)). Lưu ý rằng thao tác bấm phím của chương trình là thông điệp phím ảo gửi bằng phần mềm nên đôi khi có hành vi khác với việc nhấn phím vật lý trên bàn phím thật.

## KEYPRESS

Nhấn xuống rồi nhả ra ngay một phím trên bàn phím.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
KEYPRESS (keycode)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `keycode` | số / hằng | có | | [Mã phím](/phu-luc/ma-phim) cần bấm |

**Ví dụ**

```cms
// Bấm phím cách bằng mã số
KEYPRESS(32)

// Bấm phím cách bằng hằng số
KEYPRESS(#SPACE)
HALT
```

---

## KEYDOWN

Nhấn và giữ một phím trên bàn phím ở trạng thái đang đè xuống.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
KEYDOWN (keycode)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `keycode` | số / hằng | có | | [Mã phím](/phu-luc/ma-phim) cần nhấn giữ |

**Ví dụ**

```cms
// Bấm tổ hợp phím Ctrl + S
KEYDOWN(#CTRL)
KEYPRESS(#S)
KEYUP(#CTRL)
HALT
```

**Lưu ý**

- Không thể dùng `KEYDOWN` để tạo hiệu ứng đè phím tự lặp ký tự liên tục giống như khi đè phím trên bàn phím vật lý, vì việc tự lặp khi đè phím trên bàn phím thật do bộ điều khiển phần cứng (controller) của bàn phím đảm nhiệm.

---

## KEYUP

Nhả một phím đã được nhấn giữ trước đó.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
KEYUP (keycode)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `keycode` | số / hằng | có | | [Mã phím](/phu-luc/ma-phim) cần nhả ra |

**Ví dụ**

```cms
KEYDOWN(#CTRL)
KEYPRESS(#S)
KEYUP(#CTRL)
HALT
```

---

## KEYSTRING

Bấm lần lượt các phím tương ứng với từng ký tự trong chuỗi đầu vào.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
KEYSTRING (keystring, [delay])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `keystring` | chuỗi | có | | Chuỗi văn bản cần gõ |
| `delay` | số | không | | Độ trễ (tính bằng mili-giây) giữa mỗi lần gõ một ký tự |

**Ví dụ**

```cms
KEYSTRING("hello world")
HALT
```

**Lưu ý**

- Thủ tục này không chép thẳng chuỗi chữ vào ô nhập theo kiểu dán văn bản, mà thực hiện **bấm phím lần lượt** ứng với từng ký tự trong chuỗi `keystring`.
- Lệnh này **không bấm được các phím không phải ký tự** (như phím chức năng, phím điều hướng).
- Kết quả gõ ra **phụ thuộc vào bộ gõ / kiểu bàn phím (keyboard layout) hiện tại** đang bật trên cửa sổ.

---

## ISKEYDOWN

Kiểm tra xem một phím (hoặc nút chuột) có đang được nhấn giữ tại thời điểm gọi hàm hay không.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
ISKEYDOWN (keycode)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `keycode` | số / hằng | có | | [Mã phím](/phu-luc/ma-phim) (hoặc nút chuột) cần kiểm tra |

**Trả về:** `1` nếu phím đang được nhấn giữ tại thời điểm gọi hàm; `0` nếu không.

**Ví dụ**

```cms
// Kiểm tra phím cách có đang được nhấn không
IF(ISKEYDOWN(#SPACE) = 1)
   LOGWRITE("Dang nhan phim cach!")
END_IF

// Kiểm tra nhấn giữ đồng thời phím cách và phím A
IF((ISKEYDOWN(#SPACE) = 1) & (ISKEYDOWN(#A) = 1))
   LOGWRITE("Dang nhan phim cach va A!")
END_IF
```

**Lưu ý**

- Ví dụ theo dõi phím không đặt `HALT` vì script tự lặp nên kiểm tra liên tục, dừng bằng tay.
- Hàm này cũng dùng được để kiểm tra trạng thái các nút bấm của chuột (xem [Bảng mã phím](/phu-luc/ma-phim)).

---

## GETKBLAYOUT

Lấy mã định danh ngôn ngữ bàn phím (layout) hiện tại của một cửa sổ cụ thể.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
GETKBLAYOUT (hwnd)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã định danh `hwnd` của cửa sổ cần kiểm tra |

**Trả về:** Mã số định danh ngôn ngữ bàn phím (keyboard layout) của cửa sổ đó.

**Ví dụ**

```cms
// Lấy hwnd của cửa sổ Notepad đang chạy
$hwnd = WNDFIND("Notepad")

// In ra mã ngôn ngữ bàn phím của cửa sổ đó
PRINT(GETKBLAYOUT($hwnd))
HALT
```

**Lưu ý**

- Trên các hệ điều hành Windows hiện đại, mỗi cửa sổ ứng dụng lưu trạng thái ngôn ngữ bàn phím riêng của cửa sổ đó.

---

## SETKBLAYOUT

Thiết lập ngôn ngữ bàn phím (layout) cho một cửa sổ cụ thể.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SETKBLAYOUT (hwnd, lang)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `hwnd` | số | có | | Mã định danh `hwnd` của cửa sổ |
| `lang` | số | có | | Mã định danh ngôn ngữ bàn phím muốn đặt |

**Ví dụ**

```cms
$hwnd = WNDFIND("Notepad")

// Chuyển sang kiểu bàn phím tiếng Anh (1033)
SETKBLAYOUT($hwnd, 1033)
HALT
```

---

## GETKEYSDOWN

Đưa danh sách mã của tất cả các phím đang được nhấn giữ tại thời điểm gọi lệnh vào một mảng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
GETKEYSDOWN ($arr)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$arr` | mảng | có | | Mảng nhận danh sách [mã phím](/phu-luc/ma-phim) đang được nhấn |

**Ví dụ**

```cms
// Ví dụ 1: In ra nhật ký mã của tất cả các phím đang nhấn
GETKEYSDOWN($kvar)
FOR($i=0, $i < ARRSIZE($kvar))
   PRINT($kvar[$i])
END_CYC
WAITMS(100)
LOGCLEAR
```

```cms
// Ví dụ 2: Kiểm tra phím đang nhấn bằng SWITCH
// Dựa trên đặc điểm $kvar tương đương với phần tử đầu tiên $kvar[0]
GETKEYSDOWN($kvar)
SWITCH($kvar)
CASE(#Q)
   PRINT("Q")
CASE(#W)
   PRINT("W")
CASE(#E)
   PRINT("E")
END_SWITCH
WAITMS(100)
```

**Lưu ý**

- Hai ví dụ theo dõi phím ở trên không đặt `HALT` vì script tự lặp nên kiểm tra liên tục, dừng bằng tay.
- Mỗi lần gọi `GETKEYSDOWN`, mảng `$arr` truyền vào sẽ tự động được xóa sạch trước khi điền dữ liệu mới.
- Các phím đang nhấn được xếp vào mảng theo thứ tự mã phím của chúng (xem [Bảng mã phím](/phu-luc/ma-phim)).
- Giống như [`ISKEYDOWN`](#iskeydown), thủ tục này nhận diện được cả các phím trên bàn phím lẫn các nút bấm chuột.
