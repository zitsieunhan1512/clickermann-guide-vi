# Nhật ký và âm báo

Trang này hướng dẫn các thủ tục dùng để ghi thông tin ra cửa sổ nhật ký (log), phát âm thanh cảnh báo và hiển thị thông báo nổi ở khay hệ thống giúp theo dõi quá trình chạy script.

## LOGWRITE (PRINT)

Ghi một dòng thông báo ra cửa sổ nhật ký (log) của chương trình.

**Loại:** thủ tục · **Trạng thái:** 🟠 Chưa thống nhất

```cms
LOGWRITE (str, ...)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `str, ...` | chuỗi / số | có | | Chuỗi thông báo (số lượng tham số không giới hạn) |

**Ví dụ**

```cms
$var = 5
// In thông báo ghép từ chuỗi chú thích và giá trị biến
LOGWRITE("Bien $var = ", $var)
HALT
```

**Lưu ý**

- Lệnh này có bí danh là `PRINT`, cú pháp giống nhau.
- Số lượng tham số của lệnh này không giới hạn.
- Khi có khai báo chỉ thị `#logfile`, ngoài cửa sổ nhật ký, thông báo còn được ghi thêm vào tệp nhật ký trong thư mục dự án.
- 🟠 **Điểm chưa thống nhất về tên tệp của chỉ thị `#logfile`:**
  - **Nên làm:** Khi dùng `#logfile`, hãy viết rõ tên tệp như `#logfile "debug.txt"` ở đầu script để biết chắc tên tệp nhật ký được tạo ra trong thư mục dự án.
  ::: details Vì sao chưa chắc
  - Ở mục Xuất thông tin (lệnh `LOGWRITE`), help ghi khi có chỉ thị `#logfile` thì thông báo được ghi thêm vào tệp `%thu_muc_du_an%/log.txt` (không nhắc tham số tên tệp).
  - Còn ở phần Giới thiệu ngôn ngữ (bảng chỉ thị tiền xử lý) và Lịch sử phiên bản (v4.13.014: nâng cấp `#logfile`, nay có thể đặt tên tệp nhật ký tùy ý), help viết ví dụ `#logfile "debug.txt"` (có truyền tên tệp riêng). Câu hỏi cần kiểm tra là khi viết `#logfile` không kèm tên tệp thì chương trình có ghi ra `log.txt` như mục `LOGWRITE` nêu hay không.
  - Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#ten-tep-nhat-ky-cua-logwrite-va-chi-thi-logfile).
  :::

---

## LOGCLEAR

Xóa toàn bộ nội dung đang hiển thị trong cửa sổ nhật ký của chương trình.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
LOGCLEAR ()
```

**Ví dụ**

```cms
LOGWRITE("Dong tam thoi")
WAIT(1)
LOGCLEAR()
HALT
```

---

## LOGSHOW

Hiện hoặc ẩn cửa sổ nhật ký của chương trình trên màn hình.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
LOGSHOW (show, [x, y])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `show` | số | có | | Cờ hiển thị: `1` — hiện cửa sổ nhật ký; `0` — ẩn cửa sổ nhật ký |
| `x, y` | số | không | | Tọa độ vị trí đặt cửa sổ nhật ký trên màn hình |

**Ví dụ**

```cms
LOGSHOW(1, 100, 100)
LOGWRITE("Cua so nhat ky da hien tai 100:100")
HALT
```

---

## SOUND

Phát một tệp âm thanh định dạng `*.wav`.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SOUND (file)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `file` | chuỗi | có | | Đường dẫn tới tệp âm thanh `.wav` cần phát |

**Ví dụ**

```cms
SOUND("thongbao.wav")
HALT
```

---

## BEEP

Phát tiếng bíp qua loa hệ thống với tần số và thời lượng chỉ định.

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
BEEP (freq, [time])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `freq` | số | có | | Tần số (độ cao) của âm thanh phát ra |
| `time` | số | không | `333` | Thời lượng phát âm thanh tính bằng mili-giây |

**Ví dụ**

```cms
// Phát một chuỗi giai điệu mẫu bằng tiếng bíp
BEEP(110, 170)
WAITMS(10)
BEEP(100, 140)
WAITMS(190)

FOR($i, $i < 2)
   BEEP(90, 200)
   WAITMS(300)
   BEEP(90, 200)
   WAITMS(300)
   BEEP(90, 200)
   WAITMS(500)
   BEEP(90, 140)
   WAITMS(60)
   BEEP(90, 140)
   WAITMS(60)
   BEEP(95, 120)
   WAITMS(75)
   BEEP(90, 120)
   WAITMS(60)
   BEEP(95, 140)
   WAITMS(105)
   BEEP(90, 170)
   WAITMS(10)
   BEEP(110, 150)
   WAITMS(500)
END_CYC

HALT
```

**Lưu ý**

- Thủ tục này làm script tạm dừng chờ trong suốt thời gian tiếng bíp đang phát.
- Nếu bỏ qua tham số `time`, thời lượng mặc định là `333` mili-giây (một phần ba giây).

---

## HINTPOPUP

Hiển thị một khung thông báo nhỏ (balloon tip) bật lên ở khay hệ thống (system tray).

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
HINTPOPUP (message, [title])
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `message` | chuỗi | có | | Nội dung chuỗi thông báo |
| `title` | chuỗi | không | | Tiêu đề của khung thông báo |

**Ví dụ**

```cms
HINTPOPUP("Da hoan thanh cong viec!", "Thong bao")
HALT
```
