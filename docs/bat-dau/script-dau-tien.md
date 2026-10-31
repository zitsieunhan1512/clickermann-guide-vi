# Viết script đầu tiên

Trang này hướng dẫn từng bước cách viết một script Clickermann từ cơ bản nhất: bắt đầu bằng thao tác bấm chuột lặp lại, thêm biến đếm, thêm câu lệnh điều kiện và kết hợp chụp màn hình với `GETSCREEN`.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Cơ chế chạy lặp tự động của script

Trong Clickermann, một script gồm các dòng lệnh được thực thi lần lượt **từ trên xuống dưới**. Khi chạy xong dòng cuối cùng, chương trình sẽ **tự động quay lại dòng đầu tiên** và lặp lại quy trình đó cho tới khi bạn bấm nút dừng hoặc gặp lệnh [`HALT`](/lenh/kich-ban#halt).

![Thứ tự chạy tự động từ trên xuống dưới của script và lệnh HALT](/so-do/vong-lap-script.svg)

## Bước 1: Script bấm chuột mỗi giây một lần

Hãy bắt đầu bằng ví dụ đầu tiên trong help (phần Giới thiệu ngôn ngữ): bấm chuột trái vào tọa độ `(100, 200)` rồi chờ 1 giây.

```cms
// Bấm chuột trái vào tọa độ X=100, Y=200
LCLICK(100, 200)

// Tạm dừng chờ 1 giây
WAIT(1)
```

Giải thích từng dòng:

- Dòng bắt đầu bằng `//` là **chú thích (comment)**, chỉ dùng để ghi chú cho người đọc, chương trình sẽ bỏ qua không chạy.
- [`LCLICK(100, 200)`](/lenh/chuot#lclick) là lời gọi thủ tục bấm chuột trái tại tọa độ màn hình `X = 100`, `Y = 200`. Mỗi dòng chỉ được viết một lệnh.
- [`WAIT(1)`](/lenh/kich-ban#wait) làm script tạm dừng `1` giây trước khi chuyển sang bước tiếp theo.
- Sau khi hết lệnh `WAIT(1)`, script tự quay lại dòng 1 và tiếp tục bấm chuột mỗi giây một lần (bạn có thể dừng bằng phím tắt `Alt + S` theo help, bài Màn hình chính). Nếu bạn chỉ muốn bấm đúng một lần rồi dừng hẳn, hãy thêm dòng `HALT` ở cuối script.

## Bước 2: Thêm biến để đếm số lần đã bấm

Biến là một ô nhớ có tên bắt đầu bằng dấu `$` (ví dụ `$count`). Mọi biến chưa được gán giá trị ban đầu sẽ tự động mang giá trị `0` ở lần đọc đầu tiên.

Ta nâng cấp script ở Bước 1 để đếm tổng số lần đã bấm chuột và in ra cửa sổ nhật ký bằng lệnh [`PRINT`](/lenh/nhat-ky#logwrite-print) (nhấn `Alt + S` khi muốn dừng script):

```cms
// Bấm chuột trái
LCLICK(100, 200)

// Chờ 1 giây
WAIT(1)

// Tăng biến đếm thêm 1 đơn vị
$count = $count + 1

// In thông báo ra cửa sổ nhật ký
PRINT("So lan bam: ", $count)
```

Nếu muốn bấm vào vị trí ngẫu nhiên trong vùng từ `100` đến `150` và chờ ngẫu nhiên từ `3` đến `5` giây, bạn có thể kết hợp hàm [`RND`](/lenh/so#rnd) ngay trong tham số (nhấn `Alt + S` khi muốn dừng):

```cms
// Bấm chuột vào tọa độ ngẫu nhiên từ 100 đến 150
LCLICK(RND(50, 100) + 50, RND(50, 100) + 50)

// Chờ ngẫu nhiên từ 3 đến 5 giây
WAIT(RND(3, 5))

// Tăng biến đếm
$count = $count + 1

// In thông báo
PRINT("So lan bam: ", $count)
```

## Bước 3: Thêm câu lệnh điều kiện `IF`

Để script tự đưa ra quyết định tùy theo tình huống, ta dùng cấu trúc [`IF ... END_IF`](/lenh/cau-truc#if-end-if). Ví dụ dưới đây kiểm tra nếu số ngẫu nhiên lớn hơn `5` thì mới in thông báo, và dừng lại sau khi chạy đủ 5 lượt:

```cms
// Sinh một số ngẫu nhiên từ 1 đến 10
$var = RND(1, 10)

// Kiểm tra điều kiện: nếu $var lớn hơn 5 thì in ra nhật ký
IF($var > 5)
   PRINT($var, " > 5")
END_IF

// Đếm số lượt chạy và dừng hẳn sau 5 lượt
$count = $count + 1
IF($count >= 5)
   PRINT("Da chay du 5 luot, dung script.")
   HALT
END_IF

WAIT(1)
```

## Bước 4: Đọc màu màn hình với `GETSCREEN`

Khi muốn script nhìn thấy màu sắc hoặc hình ảnh trên màn hình, bạn **bắt buộc phải gọi [`GETSCREEN`](/lenh/man-hinh#getscreen)** trước để chương trình chụp màn hình vào **bộ đệm ảnh**, sau đó mới dùng các lệnh kiểm tra màu như [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if):

```cms
// 1. Chụp màn hình hiện tại vào bộ đệm ảnh
GETSCREEN

// 2. Tìm điểm ảnh màu đỏ (255) trong vùng từ (10, 20) đến (100, 40)
IF_PIXEL_IN(10, 20, 100, 40, 255)
   // Nếu tìm thấy, tọa độ nằm sẵn trong $_return1 (X) và $_return2 (Y)
   PRINT("Tim thay mau do tai: ", $_return1, ", ", $_return2)
   LCLICK($_return1, $_return2)
ELSE
   PRINT("Khong tim thay mau do trong vung quet")
END_IF

HALT
```
