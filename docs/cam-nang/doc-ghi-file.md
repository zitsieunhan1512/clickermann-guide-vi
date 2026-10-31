# Cẩm nang: Đọc và ghi tệp văn bản (.txt) và cấu hình (.ini)

Trang này hướng dẫn từng bước cách lưu trữ và đọc lại dữ liệu từ tệp cấu hình `.ini` và tệp văn bản `.txt` bằng các hàm xử lý tệp và chuỗi trong Clickermann.

::: important Chuẩn bị thư mục dự án trước khi bắt đầu
Hãy **tạo một thư mục riêng (thư mục dự án) và lưu tệp script `.cms` vào đó trước khi chạy**. Mọi tệp `.ini` và `.txt` viết đường dẫn tương đối sẽ được tạo và đọc ngay trong thư mục dự án này.
:::

## Tình huống 1: Lưu và đọc thông số cấu hình bằng tệp `.ini`

Khi viết một script cần nhớ các thông số giữa nhiều lần chạy (như tọa độ nút bấm, thời gian chờ hay số lượt đã hoàn thành), cách gọn nhất là dùng cặp lệnh [`INIWRITE`](/lenh/chuoi-file#iniwrite) và [`INIREAD`](/lenh/chuoi-file#iniread).

### Phần A: Ghi thông số vào tệp `.ini`

Dùng `INIWRITE(filename, parname, value, [section])` để ghi từng cặp khóa - giá trị vào tệp `cau_hinh.ini`:

```cms
LOGCLEAR
LOGSHOW(1)

// Ghi các thiết lập vào tệp "cau_hinh.ini" trong phân mục "CHUNG"
INIWRITE("cau_hinh.ini", "ToaDoX", "250", "CHUNG")
INIWRITE("cau_hinh.ini", "ToaDoY", "180", "CHUNG")
INIWRITE("cau_hinh.ini", "SoLanLap", "5", "CHUNG")

PRINT("Da ghi xong tep cau_hinh.ini trong thu muc du an.")
HALT
```

Sau khi chạy đoạn script trên, bạn có thể mở thư mục dự án và mở tệp `cau_hinh.ini` bằng **Notepad** để xem hoặc chỉnh sửa trực tiếp các con số bên trong.

### Phần B: Đọc thông số từ tệp `.ini`

Trong script chính, bạn dùng `INIREAD(filename, parname, [section])` để đọc giá trị ra biến. Nếu cần đưa giá trị đọc được vào tính toán số học, bạn có thể bọc qua hàm [`INT`](/lenh/so#int) để đổi chuỗi thành số:

```cms
LOGCLEAR
LOGSHOW(1)

// Đọc lại các thiết lập từ tệp "cau_hinh.ini"
$x = INT(INIREAD("cau_hinh.ini", "ToaDoX", "CHUNG"))
$y = INT(INIREAD("cau_hinh.ini", "ToaDoY", "CHUNG"))
$so_lan = INT(INIREAD("cau_hinh.ini", "SoLanLap", "CHUNG"))

PRINT("Doc tu INI -> X=", $x, ", Y=", $y, ", SoLanLap=", $so_lan)
HALT
```

---

## Tình huống 2: Đọc từng dòng trong tệp `.txt` và tách dữ liệu

Giả sử bạn có một tệp văn bản `danh_sach.txt` chứa nhiều dòng dữ liệu có dạng `TenMuc:GiaTri`. Bạn có thể đếm tổng số dòng bằng [`TFCOUNT`](/lenh/chuoi-file#tfcount), đọc từng dòng bằng [`TFREAD`](/lenh/chuoi-file#tfread) và tách hai phần trước/sau dấu `:` bằng [`STRPOS`](/lenh/chuoi-file#strpos) và [`STRCUT2`](/lenh/chuoi-file#strcut2).

### Phần A: Tạo dữ liệu mẫu (chạy một lần, sẽ ghi đè tệp)

Nếu bạn chưa có sẵn tệp `danh_sach.txt`, hãy chạy đoạn script ngắn dưới đây một lần để tạo tệp mẫu (dòng đầu tiên dùng [`STRWRITELN`](/lenh/chuoi-file#strwriteln) với cờ `rewrite = 1` để ghi mới từ đầu, hai dòng tiếp theo nối thêm vào cuối tệp):

```cms
// Ghi mới dòng đầu tiên (rewrite = 1 sẽ xóa nội dung cũ của danh_sach.txt nếu có)
STRWRITELN("danh_sach.txt", "HoTen:Nguyen Van A", 1)

// Ghi nối tiếp dòng thứ 2 và thứ 3 vào cuối tệp
TFWRITE("danh_sach.txt", "PhongBan:Ke Toan")
TFWRITE("danh_sach.txt", "MaHoSo:HS001")

PRINT("Da tao xong tep mau danh_sach.txt")
HALT
```

### Phần B: Đọc từng dòng dữ liệu

Sau khi đã có tệp `danh_sach.txt` trong thư mục dự án, bạn chạy script dưới đây để duyệt từ dòng `1` đến dòng cuối cùng (số thứ tự dòng trong `TFREAD` tính từ `1` — theo tệp mẫu đi kèm Clickermann và sách của Chô tô, tr. 54):

```cms
LOGCLEAR
LOGSHOW(1)

// Đọc và tách từng dòng trong tệp "danh_sach.txt"
$tong_dong = TFCOUNT("danh_sach.txt")
FOR($i=1, $i <= $tong_dong)
   $str = TFREAD("danh_sach.txt", $i)
   $vi_tri = STRPOS($str, ":")
   $ten_truong = STRCUT2($str, 1, $vi_tri - 1)
   $gia_tri = STRCUT2($str, $vi_tri + 1, STRLEN($str))
   PRINT("Dong ", $i, " -> Truong: ", $ten_truong, " | Gia tri: ", $gia_tri)
END_CYC

HALT
```

---

## Tình huống 3: Đọc toàn bộ tệp vào mảng và dùng `STRSEPARATE`

Nếu tệp không quá lớn, bạn có thể nạp toàn bộ các dòng của tệp vào mảng chỉ bằng một lệnh [`TFREADARR`](/lenh/chuoi-file#tfreadarr), và tách các cột phân cách bằng dấu hai chấm `:` qua thủ tục [`STRSEPARATE`](/lenh/chuoi-file#strseparate) *(tình huống 3 này đọc tệp `danh_sach.txt` đã tạo ở Tình huống 2)*:

```cms
LOGCLEAR
LOGSHOW(1)

// Nạp toàn bộ các dòng của tệp vào mảng $cac_dong
TFREADARR("danh_sach.txt", $cac_dong)

// Duyệt mảng từ chỉ số 0 đến ARRSIZE - 1
FOR($i=0, $i < ARRSIZE($cac_dong))
   // Tách dòng hiện tại theo dấu ":" vào mảng $cot
   UNDEFINE($cot)
   STRSEPARATE($cac_dong[$i], ":", $cot)
   PRINT("Cot 1: ", $cot[0], " — Cot 2: ", $cot[1])
END_CYC

HALT
```

---

*Nguồn: Tài liệu trợ giúp `help.chm` (mục Chuỗi và tệp, mục Làm việc với số); tham khảo đối chiếu sách của Chô tô (tr. 54).*
