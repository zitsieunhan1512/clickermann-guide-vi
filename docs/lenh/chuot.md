# Chuột

Trang này hướng dẫn các thủ tục điều khiển con trỏ chuột trên màn hình (di chuyển, bấm chuột trái/phải/giữa, nhấp đúp, kéo thả và cuộn con lăn). Hầu hết các lệnh chuột đều nhận hai tham số tọa độ `x` và `y`: chương trình sẽ đưa con trỏ tới điểm đó rồi mới thực hiện thao tác; nếu muốn thao tác ngay tại vị trí con trỏ hiện tại mà không di chuyển chuột, hãy truyền biến hệ thống `$_xmouse` và `$_ymouse`.

## LCLICK

Bấm và thả nút chuột trái tại tọa độ chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
LCLICK (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm cần bấm trên màn hình |

**Ví dụ**

```cms
// Bấm chuột trái vào tọa độ 10:10
LCLICK(10, 10)

// Bấm chuột trái ngay tại vị trí con trỏ hiện tại
LCLICK($_xmouse, $_ymouse)
HALT
```

---

## LDOWN

Nhấn và giữ nút chuột trái tại tọa độ chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
LDOWN (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm cần nhấn giữ chuột trái trên màn hình |

**Ví dụ**

```cms
// Kéo thả (drag & drop) từ điểm 10:10 sang điểm 20:20
LDOWN(10, 10)
WAITMS(300)
LUP(20, 20)
HALT
```

---

## LUP

Nhả nút chuột trái tại tọa độ chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
LUP (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm cần nhả chuột trái trên màn hình |

**Ví dụ**

```cms
LDOWN(10, 10)
WAITMS(300)
LUP(20, 20)
HALT
```

---

## RCLICK, RDOWN, RUP

Bấm, nhấn giữ hoặc nhả nút chuột phải tại tọa độ chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
RCLICK (x, y)
RDOWN (x, y)
RUP (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm thao tác trên màn hình |

**Ví dụ**

```cms
// Bấm chuột phải vào tọa độ 100:100
RCLICK(100, 100)
HALT
```

**Lưu ý**

- Cách hoạt động tương tự [`LCLICK`](#lclick), [`LDOWN`](#ldown) và [`LUP`](#lup), nhưng áp dụng cho nút chuột phải.

---

## MCLICK, MDOWN, MUP

Bấm, nhấn giữ hoặc nhả nút chuột giữa (con lăn) tại tọa độ chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
MCLICK (x, y)
MDOWN (x, y)
MUP (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm thao tác trên màn hình |

**Ví dụ**

```cms
// Bấm nút chuột giữa tại tọa độ 100:100
MCLICK(100, 100)
HALT
```

**Lưu ý**

- Cách hoạt động tương tự [`LCLICK`](#lclick), [`LDOWN`](#ldown) và [`LUP`](#lup), nhưng áp dụng cho nút chuột giữa.

---

## DBLCLICK

Nhấp đúp (bấm hai lần liên tiếp) nút chuột trái tại tọa độ chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
DBLCLICK (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm cần nhấp đúp trên màn hình |

**Ví dụ**

```cms
DBLCLICK(50, 50)
HALT
```

---

## MOVE

Di chuyển con trỏ chuột tới tọa độ chỉ định mà không bấm nút.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
MOVE (x, y)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `x, y` | số | có | | Tọa độ điểm đích trên màn hình |

**Ví dụ**

```cms
MOVE(200, 150)
HALT
```

---

## MOVER

Dịch chuyển con trỏ chuột một khoảng tương đối so với vị trí hiện tại.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
MOVER (rx, ry)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `rx, ry` | số | có | | Độ lệch cần dịch chuyển theo trục ngang (X) và trục dọc (Y) |

**Ví dụ**

```cms
MOVER(50, 50)
HALT
```

**Lưu ý**

- Lệnh này **không hoạt động** ở chế độ khóa cửa sổ.
- Dù có vẻ giống `MOVE($_xmouse + rx, $_ymouse + ry)`, `MOVER` dùng cơ chế khác và thực thi nhanh hơn một chút.
- Cảnh báo từ help: thực tế thủ tục này hoạt động hơi lạ và không dịch chuyển con trỏ đúng số pixel như đã truyền vào; bạn cần tự thử nghiệm thực tế để căn chỉnh mức dịch chuyển mong muốn.

---

## WHEELDOWN

Cuộn con lăn chuột xuống dưới (về phía người dùng).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WHEELDOWN ( [mult] )
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `mult` | số | không | `1` | Hệ số nhân tốc độ cuộn |

**Ví dụ**

```cms
WHEELDOWN(3)
HALT
```

**Lưu ý**

- Mỗi nấc cuộn sẽ trượt đi một số dòng mặc định theo cài đặt trong Control Panel của Windows (thường mặc định là 3 dòng văn bản).
- Tham số `mult` giúp nhân tốc độ cuộn lên; mặc định `mult` bằng `1`.

---

## WHEELUP

Cuộn con lăn chuột lên trên (ra xa người dùng).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WHEELUP ( [mult] )
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `mult` | số | không | `1` | Hệ số nhân tốc độ cuộn |

**Ví dụ**

```cms
WHEELUP(3)
HALT
```

**Lưu ý**

- Mỗi nấc cuộn sẽ trượt đi một số dòng mặc định theo cài đặt trong Control Panel của Windows (thường mặc định là 3 dòng văn bản).
- Tham số `mult` giúp nhân tốc độ cuộn lên; mặc định `mult` bằng `1`.
