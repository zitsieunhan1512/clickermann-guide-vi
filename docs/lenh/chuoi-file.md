# Chuỗi, tệp tin, bộ nhớ tạm và HTTP

Trang này hướng dẫn các thủ tục và hàm dùng để xử lý chuỗi văn bản, đọc/ghi tệp cấu hình `.ini` và tệp văn bản `.txt`, trao đổi dữ liệu qua bộ nhớ tạm (Clipboard) và gửi truy vấn HTTP. Trong Clickermann, chuỗi là bất kỳ dãy ký tự in được; chuỗi hằng là dãy ký tự đặt trong cặp dấu ngoặc kép (ví dụ `"xin chao"`), và kết quả của hàm văn bản cũng là chuỗi.

## INIREAD

Đọc giá trị của một tham số từ tệp cấu hình (`*.ini`).

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
INIREAD (filename, parname, [section])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `filename` | chuỗi | có | | Tên tệp `.ini` cần đọc |
| `parname` | chuỗi | có | | Tên tham số (khóa) trong tệp `.ini` |
| `section` | chuỗi | không | `"default"` | Tên phân mục (`[section]`) chứa tham số trong tệp `.ini` |

**Trả về:** Chuỗi giá trị của tham số đọc được từ tệp `.ini`.

**Ví dụ**

```cms
$str = INIREAD("config.ini", "var")
PRINT($str)
HALT
```

**Lưu ý**

- Nếu bỏ qua tham số `section`, chương trình mặc định tìm trong phân mục `"default"`.

---

## INIWRITE

Ghi giá trị của một tham số vào tệp cấu hình (`*.ini`).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
INIWRITE (filename, parname, value, [section])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `filename` | chuỗi | có | | Tên tệp `.ini` cần ghi |
| `parname` | chuỗi | có | | Tên tham số (khóa) trong tệp `.ini` |
| `value` | chuỗi | có | | Giá trị muốn ghi vào tham số |
| `section` | chuỗi | không | `"default"` | Tên phân mục (`[section]`) trong tệp `.ini` |

**Ví dụ**

```cms
INIWRITE("config.ini", "var", "23")
HALT
```

**Lưu ý**

- Nếu bỏ qua tham số `section`, chương trình mặc định ghi vào phân mục `"default"`.

---

## STRLEN

Tính độ dài (số lượng ký tự) của một chuỗi văn bản.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRLEN (str)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi đầu vào cần đếm số ký tự |

**Trả về:** Số ký tự có trong chuỗi `str`.

**Ví dụ**

```cms
PRINT(STRLEN("xin"))
// kết quả "3"
HALT
```

---

## STRCUT

Cắt lấy một chuỗi con từ chuỗi đầu vào, tính theo vị trí bắt đầu và số lượng ký tự cần lấy.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRCUT (str, begin, size)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi đầu vào |
| `begin` | số | có | | Vị trí ký tự bắt đầu sao chép (tính từ `1`) |
| `size` | số | có | | Số lượng ký tự cần sao chép |

**Trả về:** Chuỗi con đã cắt ra.

**Ví dụ**

```cms
PRINT(STRCUT("hello2000", 6, 2))
// kết quả "20"
HALT
```

---

## STRCUT2

Cắt lấy một chuỗi con từ chuỗi đầu vào, tính từ vị trí bắt đầu đến vị trí kết thúc.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRCUT2 (str, begin, end)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi đầu vào |
| `begin` | số | có | | Vị trí ký tự bắt đầu sao chép (tính từ `1`) |
| `end` | số | có | | Vị trí ký tự kết thúc sao chép |

**Trả về:** Chuỗi con nằm từ vị trí `begin` đến `end`.

**Ví dụ**

```cms
PRINT(STRCUT2("hello2000", 2, 5))
// kết quả "ello"
HALT
```

---

## STRFILTER

Lọc bỏ hoặc chỉ giữ lại một tập hợp các ký tự chỉ định trong chuỗi đầu vào.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRFILTER (str, set, mode)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi đầu vào cần lọc |
| `set` | chuỗi | có | | Chuỗi mặt nạ liệt kê các ký tự dùng để lọc |
| `mode` | số | có | | Chế độ lọc (`0` hoặc `1`) |

**Trả về:** Chuỗi kết quả sau khi đã lọc ký tự.

**Ví dụ**

```cms
PRINT(STRFILTER("hello2000", "20", 0))
// kết quả "hello"

PRINT(STRFILTER("hello2000", "20", 1))
// kết quả "2000"
HALT
```

**Lưu ý**

- Hai chế độ lọc của `mode`:
  - `mode = 0`: Xóa bỏ mọi ký tự có mặt trong `set` khỏi chuỗi đầu vào.
  - `mode = 1`: Xóa bỏ tất cả ký tự, **chỉ giữ lại** những ký tự có mặt trong `set`.

---

## STRPOS

Tìm vị trí xuất hiện đầu tiên của một chuỗi con bên trong chuỗi đầu vào.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRPOS (str, substr, [offset])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi đầu vào cần tìm kiếm trên đó |
| `substr` | chuỗi | có | | Chuỗi con cần tìm |
| `offset` | số | không | `1` | Vị trí ký tự bắt đầu tìm kiếm (không được nhỏ hơn `1`) |

**Trả về:** Vị trí bắt đầu của `substr` trong `str` (tính từ `1`).

**Ví dụ**

```cms
$search = "mind"
$r = STRPOS("where is my mind", $search)
PRINT($r) // kết quả 13 (chuỗi con bắt đầu từ ký tự thứ 13)

$var = "abcabc"
$r = STRPOS($var, "a", 3)
PRINT($r) // kết quả 4, vì bắt đầu tìm từ vị trí 3 nên bỏ qua chữ "a" đầu tiên
HALT
```

**Lưu ý**

- Mặc định `offset` bằng `1`. Giá trị của `offset` không được nhỏ hơn `1`.

---

## STRCONCAT

Nối nhiều chuỗi lại với nhau thành một chuỗi duy nhất.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRCONCAT (str1, str2, ...)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str1, str2, ...` | chuỗi | có | | Các chuỗi đầu vào (số lượng tham số không giới hạn) |

**Trả về:** Chuỗi tổng hợp sau khi nối tất cả các đối số.

**Ví dụ**

```cms
PRINT(STRCONCAT("hello", "2000", "!!!")) // kết quả "hello2000!!!"
HALT
```

---

## STRREPLACE

Tìm và thay thế chuỗi con trong chuỗi đầu vào bằng một chuỗi mới.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRREPLACE (str, find, replace)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi gốc ban đầu |
| `find` | chuỗi | có | | Chuỗi con cần tìm để thay thế |
| `replace` | chuỗi | có | | Chuỗi mới dùng để thay vào chỗ `find` |

**Trả về:** Chuỗi mới sau khi đã thay thế.

**Ví dụ**

```cms
$s = STRREPLACE("Xin chao, %username%!!!", "%username%", "An")
PRINT($s) // kết quả "Xin chao, An!!!"
HALT
```

---

## STRREADLN

Đọc một dòng bất kỳ từ tệp văn bản theo số thứ tự dòng.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRREADLN (file, str_n)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên (hoặc đường dẫn) tệp văn bản cần đọc |
| `str_n` | số | có | | Số thứ tự của dòng cần đọc trong tệp |

**Trả về:** Nội dung chuỗi văn bản tại dòng `str_n`.

**Ví dụ**

```cms
PRINT(STRREADLN("input.txt", 5)) // in ra dòng thứ 5 của tệp input.txt
HALT
```

---

## STRWRITELN

Ghi một dòng văn bản vào cuối tệp.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRWRITELN (file, str, [rewrite])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản cần ghi |
| `str` | chuỗi | có | | Chuỗi nội dung cần ghi thành một dòng |
| `rewrite` | số | không | Help không nói rõ | Cờ ghi đè (`1` — xóa hết nội dung cũ trước khi ghi) |

**Ví dụ**

```cms
// Ghi vào tệp "out.txt" dòng chữ dạng "NgauNhien:N" với N từ 1 đến 9
STRWRITELN("out.txt", STRCONCAT("NgauNhien:", RND(1, 9)))
HALT
```

**Lưu ý**

- Nếu tệp có tên `file` chưa tồn tại, chương trình sẽ tự tạo tệp mới.
- Nếu truyền `rewrite = 1`, toàn bộ nội dung cũ trong tệp sẽ bị xóa sạch trước khi ghi dòng mới.
- Help nói có thể đạt hành vi tương tự bằng các lệnh mới hơn [`TFREAD`](#tfread) và [`TFCLEAR`](#tfclear). Suy luận: để ghi tệp có lẽ cần [`TFWRITE`](#tfwrite), help không nhắc lệnh này.

---

## STRMD5

Tính mã băm (hash) MD5 của một chuỗi đầu vào.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRMD5 (str)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi cần tính mã MD5 |

**Trả về:** Mã băm MD5 của chuỗi đầu vào. Ví dụ của help cho kết quả dạng `202CB962AC59075B964B07152D234B70`.

**Ví dụ**

```cms
PRINT(STRMD5("123")) // 202CB962AC59075B964B07152D234B70
HALT
```

---

## STRSEPARATE

Tách một chuỗi thành nhiều chuỗi con dựa theo ký tự/chuỗi phân cách và đưa kết quả vào mảng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
STRSEPARATE (str, substr, $arr)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi đầu vào cần tách |
| `substr` | chuỗi | có | | Chuỗi dấu phân cách |
| `$arr` | mảng | có | | Mảng nhận các chuỗi con sau khi tách |

**Ví dụ**

```cms
$str = "mot,hai,ba"
STRSEPARATE($str, ",", $arr)
PRINT($arr[1]) // "hai"
HALT
```

---

## FROMCLIP

Lấy chuỗi văn bản hiện đang lưu trong bộ nhớ tạm (Clipboard) của Windows.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
FROMCLIP ()
```

**Trả về:** Chuỗi văn bản hiện có trong Clipboard.

**Ví dụ**

```cms
// Lưu ý vẫn phải viết cặp ngoặc tròn rỗng ()
LOGWRITE(FROMCLIP())
HALT
```

---

## TOCLIP

Chép một chuỗi văn bản vào bộ nhớ tạm (Clipboard) của Windows.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TOCLIP (str)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str` | chuỗi | có | | Chuỗi văn bản muốn đưa vào Clipboard |

**Ví dụ**

```cms
TOCLIP("Noi dung sao chep")
HALT
```

---

## HTTPGET

Gửi truy vấn HTTP GET tới một địa chỉ web và trả về nội dung phản hồi.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HTTPGET (url, [headers, ...])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `url` | chuỗi | có | | Địa chỉ URL cần gửi truy vấn |
| `headers, ...` | chuỗi | không | | Các dòng tiêu đề HTTP (headers) bổ sung |

**Trả về:** Chuỗi nội dung phản hồi từ máy chủ web.

**Ví dụ**

```cms
// Lấy nội dung từ trang web
$str = HTTPGET("http://example.com")

// Cùng truy vấn trên nhưng kèm theo tiêu đề Referrer
$str = HTTPGET("http://example.com", "Referrer: http://example.com")
PRINT($str)
HALT
```

**Lưu ý**

- Hàm gửi yêu cầu qua giao thức HTTP nên script sẽ đứng chờ cho đến khi máy chủ từ xa trả lời xong (hoặc hết thời gian chờ - timeout) rồi mới chạy tiếp.
- Có thể dùng `HTTPGET` để gửi các tham số điều khiển trên URL. Ngay cả khi bạn không cần dùng tới chuỗi kết quả trả về, vẫn bắt buộc phải gọi `HTTPGET` như một hàm (gán vào biến như ở ví dụ trên).

---

## TFREAD

Đọc một dòng bất kỳ từ tệp văn bản theo số thứ tự dòng.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFREAD (file, str_n)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản cần đọc |
| `str_n` | số | có | | Số thứ tự dòng trong tệp (tính từ `1` — Tham khảo: sách của Chô tô, tr. 54) |

**Trả về:** Chuỗi nội dung tại dòng `str_n`.

**Ví dụ**

```cms
PRINT(TFREAD("input.txt", 5))
HALT
```

---

## TFREADARR

Đọc toàn bộ tệp văn bản vào mảng, mỗi dòng trong tệp trở thành một phần tử của mảng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFREADARR (file, $arr)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên (hoặc đường dẫn) tệp văn bản cần đọc |
| `$arr` | mảng | có | | Mảng nhận các dòng đọc được từ tệp |

**Ví dụ**

```cms
TFREADARR("C:\out.txt", $arr)
PRINT($arr[0])
PRINT($arr[1])
HALT
```

---

## TFWRITE

Ghi một dòng vào cuối tệp văn bản hoặc chèn vào vị trí dòng chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFWRITE (file, str, [str_n])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản cần ghi |
| `str` | chuỗi | có | | Chuỗi nội dung cần ghi |
| `str_n` | số | không | cuối tệp | Vị trí số thứ tự dòng muốn chèn vào |

**Ví dụ**

```cms
TFWRITE("input.txt", "Xin chao")
HALT
```

**Lưu ý**

- Nếu truyền `str_n`, dòng mới sẽ được chèn vào đúng vị trí dòng `str_n`, còn dòng cũ đang ở vị trí đó cùng các dòng bên dưới sẽ được đẩy lùi xuống.
- Nếu không truyền `str_n`, dòng mới được nối vào cuối tệp.

---

## TFWRITEARR

Ghi toàn bộ một mảng ra tệp văn bản, mỗi phần tử mảng nằm trên một dòng riêng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFWRITEARR (file, $arr)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản cần ghi |
| `$arr` | mảng | có | | Mảng chứa các dòng dữ liệu cần xuất ra tệp |

**Ví dụ**

```cms
$arr[0] = "mot"
$arr[1] = "hai"
TFWRITEARR("out.txt", $arr)
HALT
```

---

## TFDELETE

Xóa một dòng khỏi tệp văn bản theo số thứ tự dòng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFDELETE (file, str_n)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản |
| `str_n` | số | có | | Số thứ tự dòng cần xóa |

**Ví dụ**

```cms
TFDELETE("input.txt", 2)
HALT
```

**Lưu ý**

- Sau khi xóa dòng `str_n`, tất cả các dòng nằm bên dưới nó sẽ được dồn lên trên.

---

## TFCLEAR

Làm rỗng nội dung tệp văn bản hoặc xóa hẳn tệp khỏi ổ cứng.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFCLEAR (file, [delete])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản |
| `delete` | số | không | `0` | Cờ xóa tệp (`1` — xóa hẳn tệp khỏi ổ đĩa; `0` — chỉ xóa trắng nội dung bên trong) |

**Ví dụ**

```cms
TFCLEAR("input.txt")
HALT
```

**Lưu ý**

- Nếu truyền tham số thứ hai bằng `1`, tệp tin sẽ bị xóa khỏi ổ đĩa cứng; nếu bỏ trống (hoặc bằng `0`), tệp tin vẫn còn nhưng nội dung bên trong được làm rỗng.

---

## TFCOUNT

Đếm tổng số dòng hiện có trong một tệp văn bản.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
TFCOUNT (file)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Tên tệp văn bản cần đếm dòng |

**Trả về:** Tổng số dòng trong tệp `file`.

**Ví dụ**

```cms
PRINT(TFCOUNT("input.txt"))
HALT
```

---

## CHAR

Trả về ký tự tương ứng với mã số Unicode truyền vào.

**Loại:** hàm · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
CHAR (code)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `code` | số | có | | Mã số Unicode của ký tự |

**Trả về:** Chuỗi gồm 1 ký tự ứng với mã `code`.

**Ví dụ**

```cms
// Tạo một chuỗi ngẫu nhiên gồm 10 chữ cái thường từ a đến z
$str = ""
FOR($i=0, $i < 10)
   $chr = CHAR(RND(97, 122))
   $str = STRCONCAT($str, $chr)
END_CYC
PRINT($str)
HALT
```

**Lưu ý**

- Hàm sử dụng mã từ bảng mã Unicode. Không nhầm với ASCII. Bảng mã có thể tra cứu tại <http://unicode-table.com/ru/>.
