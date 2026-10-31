# Cẩm nang: Đọc và ghi tệp văn bản (.txt) và cấu hình (.ini)

Trang này hướng dẫn từng bước cách lưu trữ và đọc lại dữ liệu từ tệp cấu hình `.ini` và tệp văn bản `.txt` bằng các hàm xử lý tệp và chuỗi trong Clickermann.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Kịch bản 1: Lưu và đọc thông số cấu hình bằng tệp `.ini`

Khi viết một script cần nhớ các thông số giữa nhiều lần chạy (như tọa độ nút bấm, thời gian chờ hay số lượt đã hoàn thành), cách gọn nhất là dùng cặp lệnh [`INIWRITE`](/lenh/chuoi-file#iniwrite) và [`INIREAD`](/lenh/chuoi-file#iniread).

### Giải thích từng bước

1. Dùng `INIWRITE(filename, parname, value, [section])` để ghi từng cặp khóa - giá trị vào tệp `.ini`.
2. Dùng `INIREAD(filename, parname, [section])` để đọc giá trị ra biến khi bắt đầu chạy script.
3. Nếu cần đưa giá trị đọc được vào tính toán số học, bạn có thể bọc qua hàm [`INT`](/lenh/so#int) để ép chuỗi thành số.

```cms
LOGCLEAR
LOGSHOW(1)

// 1. Ghi các thiết lập vào tệp "cau_hinh.ini" trong phân mục "CHUNG"
INIWRITE("cau_hinh.ini", "ToaDoX", "250", "CHUNG")
INIWRITE("cau_hinh.ini", "ToaDoY", "180", "CHUNG")
INIWRITE("cau_hinh.ini", "SoLanLap", "5", "CHUNG")

// 2. Đọc lại các thiết lập từ tệp "cau_hinh.ini"
$x = INT(INIREAD("cau_hinh.ini", "ToaDoX", "CHUNG"))
$y = INT(INIREAD("cau_hinh.ini", "ToaDoY", "CHUNG"))
$so_lan = INT(INIREAD("cau_hinh.ini", "SoLanLap", "CHUNG"))

LOGWRITE("Doc tu INI -> X=", $x, ", Y=", $y, ", SoLanLap=", $so_lan)
HALT
```

---

## Kịch bản 2: Đọc từng dòng trong tệp `.txt` và tách dữ liệu

Giả sử bạn có một tệp văn bản `danh_sach.txt` chứa nhiều dòng dữ liệu có dạng `TenMuc:GiaTri`. Bạn có thể đếm tổng số dòng bằng [`TFCOUNT`](/lenh/chuoi-file#tfcount), đọc từng dòng bằng [`TFREAD`](/lenh/chuoi-file#tfread) và tách hai phần trước/sau dấu `:` bằng [`STRPOS`](/lenh/chuoi-file#strpos) và [`STRCUT2`](/lenh/chuoi-file#strcut2).

### Giải thích từng bước

1. Tạo dữ liệu mẫu vào tệp `danh_sach.txt` bằng [`TFCLEAR`](/lenh/chuoi-file#tfclear) và [`TFWRITE`](/lenh/chuoi-file#tfwrite).
2. Dùng vòng lặp `FOR($i=1, $i <= TFCOUNT("danh_sach.txt"))` để duyệt từ dòng `1` đến dòng cuối cùng (số dòng tính từ `1` — theo tệp mẫu đi kèm Clickermann và sách của Chô tô, tr. 54).
3. Ở mỗi dòng, tìm vị trí dấu `:` bằng `STRPOS($dong, ":")` rồi cắt phần tên ở bên trái và phần giá trị ở bên phải.

```cms
LOGCLEAR
LOGSHOW(1)

// Chuẩn bị tệp dữ liệu mẫu "danh_sach.txt"
IF(TFCOUNT("danh_sach.txt") > 0)
   TFCLEAR("danh_sach.txt", 1)
END_IF

TFWRITE("danh_sach.txt", "HoTen:Nguyen Van A")
TFWRITE("danh_sach.txt", "PhongBan:Ke Toan")
TFWRITE("danh_sach.txt", "MaHoSo:HS001")

// Đọc và tách từng dòng trong tệp
$tong_dong = TFCOUNT("danh_sach.txt")
FOR($i=1, $i <= $tong_dong)
   $str = TFREAD("danh_sach.txt", $i)
   $vi_tri = STRPOS($str, ":")
   $ten_truong = STRCUT2($str, 1, $vi_tri - 1)
   $gia_tri = STRCUT2($str, $vi_tri + 1, STRLEN($str))
   LOGWRITE("Dong ", $i, " -> Truong: ", $ten_truong, " | Gia tri: ", $gia_tri)
END_CYC

HALT
```

---

## Kịch bản 3: Đọc toàn bộ tệp vào mảng và dùng `STRSEPARATE`

Nếu tệp không quá lớn, bạn có thể nạp toàn bộ các dòng của tệp vào mảng chỉ bằng một lệnh [`TFREADARR`](/lenh/chuoi-file#tfreadarr), và tách các cột phân cách bằng dấu hai chấm `:` qua thủ tục [`STRSEPARATE`](/lenh/chuoi-file#strseparate) *(lưu ý: kịch bản 3 này đọc tệp `danh_sach.txt` đã được tạo sẵn từ Kịch bản 2 ở trên)*:

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
   LOGWRITE("Cot 1: ", $cot[0], " — Cot 2: ", $cot[1])
END_CYC

HALT
```
