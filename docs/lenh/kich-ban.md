# Điều khiển script và hệ thống

Trang này hướng dẫn các thủ tục và hàm dùng để tạm dừng chờ, nhảy nhãn, dừng hẳn script, hiển thị hộp thoại tương tác với người dùng, gọi chương trình ngoài, nạp plugin DLL và liệt kê tệp/thư mục.

## WAIT

Tạm dừng việc thực thi script trong một khoảng thời gian tính bằng giây.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WAIT (delay)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `delay` | số | có | | Thời gian chờ tính bằng giây (chấp nhận cả số thập phân) |

**Ví dụ**

```cms
LOGWRITE("Bat dau cho 1.25 giay...")
WAIT(1.25)
LOGWRITE("Da cho xong")
HALT
```

**Lưu ý**

- Thời gian chờ thực tế luôn có một độ sai số nhỏ phụ thuộc vào một số yếu tố; thông thường sai số này không vượt quá `5` mili-giây (`0.005` giây).
- Bạn có thể truyền số thập phân vào `delay`, ví dụ `1.25` tương ứng với 1 giây và 250 mili-giây.

---

## WAITMS

Tạm dừng việc thực thi script trong một khoảng thời gian tính bằng mili-giây.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
WAITMS (delay)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `delay` | số | có | | Thời gian chờ tính bằng mili-giây (`1` giây = `1000` mili-giây) |

**Ví dụ**

```cms
WAITMS(500)
HALT
```

**Lưu ý**

- Một giây bằng `1000` mili-giây.
- Độ trễ có một sai số nhỏ không tránh khỏi, phụ thuộc vào một số yếu tố; trên thực tế sai số thường không vượt quá `5` mili-giây (`0.005` giây).

---

## GOTO

Nhảy luồng thực thi của script tới dòng có đặt nhãn (label) chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
GOTO (label)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `label` | tên nhãn | có | | Tên của nhãn đích cần nhảy tới (viết không có dấu ngoặc kép) |

**Ví dụ**

```cms
GOTO(bo_qua)
LOGWRITE("dong nay bi bo qua")

bo_qua:
LOGWRITE("dong nay duoc chay")
HALT
```

**Lưu ý**

- Việc nhảy tới nhãn chỉ được phép thực hiện trong phạm vi các khối lệnh có **cùng cấp độ lồng nhau**.
- Tên nhãn viết không có ngoặc kép; tại dòng đích trong script, theo sau tên nhãn bắt buộc phải có dấu hai chấm `:` (ví dụ `bo_qua:`) và nhãn phải đứng riêng trên một dòng.

---

## CALL

Gọi một tệp plugin ngoài (thư viện DLL) và truyền các tham số số nguyên cho plugin đó.

**Loại:** thủ tục · **Trạng thái:** 🟠 Chưa thống nhất

```cms
CALL ("filename", par1, ...)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `filename` | chuỗi | có | | Tên tệp plugin `.dll` cần gọi |
| `par1, ...` | số nguyên | không | | Danh sách các tham số số nguyên truyền vào plugin |

**Trả về:** Giá trị kết quả của hàm `execute` trong plugin được ghi vào biến hệ thống `$_return1`.

**Ví dụ**

```cms
CALL("plugin_example.dll", 5, 2, 3)
LOGWRITE($_return1)
HALT
```

**Lưu ý**

- Nên đọc thêm bài viết [Plugin mở rộng](/khai-niem/plugin) trong tài liệu. Clickermann sẽ đứng chờ cho đến khi plugin thực thi xong rồi mới chạy tiếp dòng lệnh kế tiếp trong script.
- Kết quả trả về của plugin được lưu vào biến hệ thống `$_return1`.
- 🟠 **Điểm chưa thống nhất trong help và khi so sánh giữa help với sách của Chô tô:**
  - **Trong trang lệnh `CALL` (help, mục Script và plugin):** Ghi rằng `filename` là tên tệp plugin tính tương đối từ thư mục `%Clickermann%/plugins`.
  - **Trong bài viết "Plugin" (help, bài Plugin):** Ghi rằng tệp DLL của plugin phải đặt trong thư mục dự án, nằm cạnh script đang chạy hoặc trong thư mục con; nếu không tìm thấy tệp theo tên đã cho ở đó thì lệnh `CALL` sẽ âm thầm kết thúc.
  - **Trong sách của Chô tô (tr. 104):** Chỉ ghi rằng tệp DLL đặt cùng thư mục với file script.
  - Xem script kiểm chứng đường dẫn nạp DLL tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#thu-muc-nap-plugin-dll-cua-call).

---

## EXECUTE

Chạy một tệp chương trình bên ngoài hoặc thực thi lệnh dòng lệnh (console).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
EXECUTE (filename, [param])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `filename` | chuỗi | có | | Tên tệp hoặc lệnh cần chạy (đường dẫn tương đối hoặc tuyệt đối) |
| `param` | chuỗi | không | | Chuỗi các tham số dòng lệnh truyền kèm theo |

**Ví dụ**

```cms
// Chạy một tệp batch
EXECUTE("some.bat")

// Chạy lệnh ping với tham số
EXECUTE("ping", "127.0.0.1 -n 10")
HALT
```

**Lưu ý**

- Lệnh này mở tệp bất kỳ dựa theo liên kết định dạng tệp (file association) đã đăng ký trong Windows, tương tự như khi bạn mở hộp thoại **Run** (`Win + R`) của Windows.
- Ngay sau khi phát lệnh mở tệp ngoài, `EXECUTE` trả quyền điều khiển về cho script chạy tiếp ngay lập tức mà **không chờ** chương trình ngoài khởi động hay chạy xong.

---

## INPUTBOX

Hiển thị một hộp thoại cho phép người dùng nhập vào một chuỗi văn bản.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
INPUTBOX (message, default, [delay])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `message` | chuỗi | có | | Lời nhắc hiển thị trên hộp thoại |
| `default` | chuỗi | có | | Giá trị mặc định |
| `delay` | số | không | `5` | Thời gian chờ tự động đóng hộp thoại (tính bằng giây) |

**Trả về:** Chuỗi do người dùng nhập vào (hoặc chuỗi `default` nếu hết thời gian chờ; trả về chuỗi rỗng `""` nếu bấm hủy).

**Ví dụ**

```cms
$str = INPUTBOX("Nhap noi dung:", "xin chao")
PRINT($str)
HALT
```

**Lưu ý**

- Hộp thoại hiện trên màn hình trong `delay` giây (mặc định là `5` giây). Nếu hết thời gian này mà người dùng chưa bắt đầu gõ hoặc chưa bấm nút nào, hàm sẽ tự đóng hộp thoại và trả về giá trị `default`.
- Nếu người dùng bấm nút hủy (Cancel) hoặc phím `Esc`, hàm trả về chuỗi rỗng `""`. Người dùng có thể nhấn phím `Enter` để xác nhận nhập.

---

## DIALOGBOX

Hiển thị một hộp thoại thông báo có các nút bấm lựa chọn và trả về mã nút mà người dùng đã bấm.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
DIALOGBOX (message, buttons, [icon])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `message` | chuỗi | có | | Nội dung thông báo trong hộp thoại |
| `buttons` | số | có | | Mã bộ nút bấm hiển thị (`0..5`) |
| `icon` | số | không | `0` | Mã biểu tượng hiển thị trên hộp thoại (`0..4`) |

**Trả về:** Mã số của nút mà người dùng đã bấm (`1..7`).

**Ví dụ**

```cms
// Hiển thị hộp thoại gồm hai nút Yes và No (mã bộ nút = 4)
$mr = DIALOGBOX("Ban co dong y khong?", 4)
IF($mr = 6)
   PRINT("Ban da chon Yes")
ELSE
   PRINT("Ban da chon No")
END_IF
HALT
```

**Lưu ý**

- Script sẽ tạm dừng chờ cho đến khi người dùng bấm vào một trong các nút trên hộp thoại.
- **Bảng mã bộ nút bấm (`buttons`):**

| Mã | Các nút hiển thị |
|---|---|
| `0` | OK |
| `1` | OK, CANCEL |
| `2` | ABORT, RETRY, IGNORE |
| `3` | YES, NO, CANCEL |
| `4` | YES, NO |
| `5` | RETRY, CANCEL |

- **Bảng mã biểu tượng (`icon`):**

| Mã | Biểu tượng |
|---|---|
| `0` | Không có biểu tượng |
| `1` | Lỗi (Error) |
| `2` | Câu hỏi (Question) |
| `3` | Cảnh báo (Warning) |
| `4` | Thông tin (Information) |

- **Bảng mã kết quả trả về:**

| Mã trả về | Nút người dùng đã bấm |
|---|---|
| `1` | OK |
| `2` | CANCEL |
| `3` | ABORT |
| `4` | RETRY |
| `5` | IGNORE |
| `6` | YES |
| `7` | NO |

---

## RADIOBOX

Hiển thị hộp thoại chứa danh sách các nút chọn tròn (radio buttons) để người dùng chọn một mục.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
RADIOBOX (message, radio1, ...)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `message` | chuỗi | có | | Nội dung tiêu đề / câu hỏi trên hộp thoại |
| `radio1, ...` | chuỗi | có | | Chuỗi mô tả từng mục lựa chọn (số lượng tham số không giới hạn) |

**Trả về:** Số thứ tự của mục được chọn (Suy từ ví dụ: tính từ 1), hoặc `0` nếu người dùng bấm CANCEL.

**Ví dụ**

```cms
$res = RADIOBOX("Chon mot muc", "1 Thit", "2 Gia cam", "3 Ca")
IF($res > 0)
   PRINT("Ban da chon muc so: ", $res)
ELSE
   PRINT("Ban khong chon muc nao")
END_IF
HALT
```

**Lưu ý**

- Script sẽ dừng chờ cho đến khi người dùng bấm nút OK hoặc CANCEL trên hộp thoại. Nếu bấm CANCEL, hàm trả về `0`.

---

## HALT

Dừng hẳn việc thực thi script (hoặc đóng luôn chương trình Clickermann).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HALT ([close])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `close` | số | không | Help không nói rõ | Nếu bằng `1`, chương trình Clickermann sẽ đóng hoàn toàn |

**Ví dụ**

```cms
LOGWRITE("Chay mot lan roi dung han")
HALT
```

---

## READMEM

Đọc một giá trị số nguyên từ địa chỉ bộ nhớ của một tiến trình dựa theo mã `pid`.

**Loại:** hàm · **Trạng thái:** 🟠 Chưa thống nhất

```cms
READMEM (pid, addr, [size])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `pid` | số | có | | Mã định danh tiến trình (Process ID) |
| `addr` | 🟠 chuỗi / số nguyên | có | | Địa chỉ vùng nhớ cần đọc (🟠 help tự mâu thuẫn: dòng tham số ghi là chuỗi, dòng ghi chú bên dưới nói là số nguyên ở hệ thập phân hoặc hệ thập lục phân) |
| `size` | số | không | `4` | Kích thước số nguyên cần đọc tính theo byte (`1`, `2`, `4` hoặc `8`) |

**Trả về:** Giá trị số nguyên đọc được tại địa chỉ bộ nhớ `addr`.

**Lưu ý**

- Mã tiến trình `pid` có thể xem trong Task Manager của Windows, trong phần thông tin chế độ khóa cửa sổ của Clickermann, hoặc lấy bằng hàm [`HGETPID`](/lenh/winapi#hgetpid).
- Tham số `size` chỉ định kích thước kiểu số nguyên: `1`, `2`, `4` hoặc `8` byte (nếu bỏ qua thì nhận là `4`).
- 🟠 **Điểm tự mâu thuẫn trong help (mục Script và plugin):** Tại mục `READMEM`, phần liệt kê tham số ghi `addr` là "chuỗi, địa chỉ bộ nhớ", nhưng phần ghi chú ngay bên dưới và ví dụ lại nói địa chỉ là "số nguyên thông thường ở dạng thập phân hoặc thập lục phân" (`0x0006F2B7`). Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#kieu-tham-so-addr-cua-readmem-va-writemem).

---

## WRITEMEM

Ghi một giá trị số nguyên vào địa chỉ bộ nhớ của một tiến trình dựa theo mã `pid`.

**Loại:** thủ tục · **Trạng thái:** 🟠 Chưa thống nhất

```cms
WRITEMEM (pid, addr, value, [size])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `pid` | số | có | | Mã định danh tiến trình (Process ID) |
| `addr` | 🟠 số nguyên | có | | Địa chỉ vùng nhớ cần ghi (viết ở hệ thập phân hoặc hệ thập lục phân `0x...`; xem lưu ý 🟠 về mâu thuẫn kiểu dữ liệu với `READMEM` trong help) |
| `value` | số | có | | Giá trị số cần ghi vào bộ nhớ |
| `size` | số | không | `4` | Kích thước số nguyên tính theo byte (`1`, `2`, `4` hoặc `8`) |

**Lưu ý**

- Mã tiến trình `pid` có thể xem trong Task Manager của Windows, trong phần thông tin chế độ khóa cửa sổ của Clickermann, hoặc lấy bằng hàm [`HGETPID`](/lenh/winapi#hgetpid).
- Tham số `size` chỉ định kích thước kiểu số nguyên: `1`, `2`, `4` hoặc `8` byte (nếu bỏ qua thì nhận là `4`).
- 🟠 **Điểm tự mâu thuẫn trong help (mục Script và plugin):** Ở `READMEM`, phần tham số trong help ghi `addr` là "chuỗi, địa chỉ bộ nhớ", nhưng ở phần ghi chú của cả `READMEM` và `WRITEMEM` lại ghi `addr` là số nguyên thông thường ở dạng thập phân hoặc thập lục phân. Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#kieu-tham-so-addr-cua-readmem-va-writemem).

---

## GETFILELIST

Lấy danh sách tên các tệp tin khớp với mẫu tìm kiếm (mask) và lưu vào mảng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
GETFILELIST ($arr, [dir])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$arr` | mảng | có | | Mảng nhận danh sách các tệp tin tìm thấy |
| `dir` | chuỗi | không | `"*"` | Đường dẫn kèm theo ký tự đại diện lọc tệp (mask) |

**Ví dụ**

```cms
// Ví dụ 1: In danh sách tất cả các tệp trong ổ C:
GETFILELIST($arr, "C:\*.*")
FOR($i=0, $i < ARRSIZE($arr))
   PRINT($arr[$i])
END_CYC
HALT
```

```cms
// Ví dụ 2: Chỉ liệt kê các tệp .sys trong ổ C:
GETFILELIST($arr, "C:\*.sys")
FOR($i=0, $i < ARRSIZE($arr))
   PRINT($arr[$i])
END_CYC
HALT
```

**Lưu ý**

- Đường dẫn truyền vào `dir` bắt buộc phải có ký tự đại diện (mask, ví dụ `*.*` hoặc `*.txt`). Mặc định `dir` là `"*"`.

---

## GETDIRLIST

Lấy danh sách tên các thư mục khớp với mẫu tìm kiếm (mask) và lưu vào mảng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
GETDIRLIST ($arr, [dir])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `$arr` | mảng | có | | Mảng nhận danh sách các thư mục tìm thấy |
| `dir` | chuỗi | không | `"*"` | Đường dẫn kèm theo ký tự đại diện lọc thư mục (mask) |

**Ví dụ**

```cms
// In danh sách tất cả các thư mục ở ổ C:
GETDIRLIST($arr, "C:\*")
FOR($i=0, $i < ARRSIZE($arr))
   PRINT($arr[$i])
END_CYC
HALT
```

**Lưu ý**

- Đường dẫn truyền vào `dir` bắt buộc phải có ký tự đại diện (mask, ví dụ `"C:\*"`). Mặc định `dir` là `"*"`.
