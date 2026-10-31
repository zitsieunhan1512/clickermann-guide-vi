# Cẩm nang: Bấm chuột theo lịch và chu kỳ thời gian

Trang này hướng dẫn từng bước cách viết script bấm chuột tự động lặp theo chu kỳ giây/mili-giây, bấm đủ số lần rồi dừng hoặc chờ tới đúng mốc giờ/phút trong ngày mới thực hiện thao tác.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Kịch bản 1: Bấm chuột lặp lại theo chu kỳ cố định

Khi cần bấm vào một nút trên phần mềm văn phòng cách đều mỗi 5 giây một lần, bạn kết hợp [`LCLICK`](/lenh/chuot#lclick) và [`WAIT`](/lenh/kich-ban#wait).

### Giải thích từng bước

1. Xác định tọa độ điểm cần bấm bằng cách mở [Trình soạn thảo](/bat-dau/trinh-soan-thao), đưa trỏ chuột vào nút và xem tọa độ `X, Y` (hoặc nhấn `Alt + Q`).
2. Gọi `LCLICK(x, y)` để bấm chuột trái.
3. Gọi `WAIT(5)` để nghỉ 5 giây (hoặc thêm độ trễ ngẫu nhiên bằng [`RND`](/lenh/so#rnd)).
4. Không đặt `HALT` ở cuối để script tự quay lại dòng đầu tiên sau mỗi lượt (khi muốn dừng hẳn, bạn nhấn tổ hợp phím tắt `Alt + S` theo help, bài Màn hình chính).

```cms
// Bấm chuột trái vào nút ở tọa độ (250, 180)
LCLICK(250, 180)

// Tăng bộ đếm và ghi nhật ký để tiện theo dõi
INC($dem)
LOGWRITE("Da bam lan thu: ", $dem, " luc ", $_time_str)

// Chờ 5 giây trước khi tự động lặp lại lượt tiếp theo
WAIT(5)
```

---

## Kịch bản 2: Bấm đúng N lần theo chu kỳ rồi tự dừng

Nếu bạn chỉ muốn bấm làm mới dữ liệu đúng 20 lần (mỗi lần cách nhau 2 giây) rồi dừng hẳn, hãy dùng vòng lặp [`FOR ... END_CYC`](/lenh/cau-truc#for-end-cyc) và kết thúc bằng [`HALT`](/lenh/kich-ban#halt).

### Giải thích từng bước

1. Mở vòng lặp `FOR($i=1, $i <= 20)` để đếm từ lần 1 đến lần 20.
2. Bên trong vòng lặp, thực hiện thao tác bấm chuột và chờ `WAIT(2)`.
3. Sau `END_CYC`, phát tiếng bíp báo hiệu bằng [`BEEP`](/lenh/nhat-ky#beep) và gọi `HALT` để dừng hẳn script.

```cms
LOGCLEAR
LOGSHOW(1)

FOR($i=1, $i <= 20)
   LCLICK(250, 180)
   LOGWRITE("Hoan thanh luot bam: ", $i, "/20")
   WAIT(2)
END_CYC

BEEP(800, 300)
LOGWRITE("Da bam du 20 lan. Dung script.")
HALT
```

---

## Kịch bản 3: Chờ tới đúng giờ và phút trong ngày mới bấm

Clickermann cung cấp sẵn các biến hệ thống thời gian thực là `$_time_h` (giờ hiện tại, dải `0..23`), `$_time_m` (phút hiện tại, dải `0..59`) và `$_time_s` (giây hiện tại, dải `0..59`) *(Tham khảo dải giá trị: sách của Chô tô, tr. 26)*. Bạn có thể dùng vòng lặp [`WHILE ... END_CYC`](/lenh/cau-truc#while-end-cyc) để chờ tới đúng mốc giờ mong muốn (nhấn `Alt + S` nếu muốn hủy chờ giữa chừng).

### Giải thích từng bước

1. Đặt giờ và phút mục tiêu vào biến (ví dụ `17` giờ `30` phút).
2. Dùng vòng lặp `WHILE` kiểm tra: chừng nào giờ hiện tại chưa bằng `17` **hoặc** phút hiện tại chưa bằng `30` thì nghỉ `WAIT(1)` rồi kiểm tra lại.
3. Khi đồng hồ vừa điểm `17:30`, vòng lặp `WHILE` kết thúc, script chạy tiếp xuống lệnh bấm chuột bên dưới rồi dừng hẳn bằng `HALT`.

```cms
// Cài đặt mốc thời gian cần thực hiện: 17 giờ 30 phút
$gio_hen = 17
$phut_hen = 30

LOGWRITE("Dang cho toi ", $gio_hen, ":", $phut_hen, "...")

// Lặp chờ chừng nào chưa tới đúng giờ và phút đã hẹn
WHILE(($_time_h != $gio_hen) | ($_time_m != $phut_hen))
   WAIT(1)
END_CYC

// Đã tới đúng giờ hẹn -> thực hiện thao tác
LOGWRITE("Da toi gio hen! Thuc hien thao tac luc: ", $_time_str)
LCLICK(300, 220)
HINTPOPUP("Da bam theo lich hen!", "Clickermann")

HALT
```
