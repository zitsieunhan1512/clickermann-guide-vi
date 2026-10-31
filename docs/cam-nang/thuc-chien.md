# Thực chiến: kỹ thuật viết script

Trang này tổng hợp 8 kỹ thuật tổ chức và viết script thực tế trong Clickermann, giúp kịch bản chạy nhanh, tự xử lý khi màn hình thay đổi bất ngờ, dễ gỡ lỗi và quản lý được nhiều cửa sổ ứng dụng cùng lúc.

::: info Nguồn gốc kỹ thuật và trạng thái kiểm chứng
- Các kỹ thuật lấy từ script thực tế do người biên soạn tự viết và báo là chạy tốt. Ví dụ ở đây được viết lại cho Notepad và Paint, chưa chạy thử.
- **Trạng thái chung của toàn bộ ví dụ trên trang:** `🟡 Chưa chạy thử` (riêng những chỗ có điểm chưa thống nhất giữa các nguồn tài liệu được gắn nhãn `🟠 Chưa thống nhất` kèm liên kết tới mục kiểm tra).
:::

---

## Kiểm tra một điểm ảnh bằng `IF_PIXEL_IN(x, y, x, y, mau)`

### Khi nào dùng

Khi bạn đã biết **tọa độ cố định `(x, y)`** của một nút bấm hoặc một biểu tượng trạng thái và chỉ muốn kiểm tra xem đúng điểm ảnh đó có đang mang màu `mau` (hoặc một trong vài mã màu cho trước) hay không, bạn truyền vùng tìm kiếm có điểm đầu trùng với điểm cuối: `IF_PIXEL_IN(x, y, x, y, mau)`.

So với việc quét cả một vùng hình chữ nhật rộng lớn, việc chỉ kiểm tra đúng 1 điểm ảnh `(x, y, x, y)` giúp giảm tối đa diện tích phải phân tích. Trong help (mục Màn hình, lệnh [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if)) cũng lưu ý rằng với danh sách màu truyền vào, **cứ thêm mỗi một mã màu vào danh sách tìm kiếm thì thời gian phân tích sẽ tăng thêm 100%** (và với [`GETSCREEN(x1, y1, x2, y2)`](/lenh/man-hinh#getscreen), chỉ định vùng nhỏ cũng giúp lệnh cập nhật bộ đệm ảnh nhanh hơn trên một số hệ thống).

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

Đoạn script dưới đây chỉ cập nhật và kiểm tra đúng 1 điểm ảnh tại tọa độ `(250, 180)` xem có mang màu trắng (`16777215`) hay màu xám (`15790320`) của nút bấm trong hộp thoại hay không:

```cms
// Chỉ chụp vùng 1 điểm ảnh (250, 180) vào bộ đệm ảnh
GETSCREEN(250, 180, 250, 180)

// Kiểm tra đúng điểm ảnh (250, 180) có màu 16777215 hoặc 15790320 không
IF_PIXEL_IN(250, 180, 250, 180, 16777215, 15790320)
   PRINT("Diem (250, 180) khop mau, bam chuot!")
   LCLICK(250, 180)
   WAITMS(300)
END_IF

HALT
```

*(Lưu ý: nếu chỉ cần so sánh với đúng 1 mã màu duy nhất, bạn cũng có thể dùng `IF(PXL(250, 180) = 16777215)`; còn `IF_PIXEL_IN(x, y, x, y, mau1, mau2)` tiện hơn khi điểm đó có thể nhận một trong vài mã màu khác nhau).*

### Lỗi dễ gặp

- **Quên gọi `GETSCREEN` trước `IF_PIXEL_IN`:** Nếu không gọi `GETSCREEN`, `IF_PIXEL_IN` chỉ đọc dữ liệu cũ trong bộ đệm ảnh nên không nhận ra điểm `(x, y)` trên màn hình đã đổi màu.
- **Cửa sổ bị xê dịch vài điểm ảnh:** Vì vùng quét chỉ rộng đúng 1 pixel `(x, y, x, y)`, nếu cửa sổ ứng dụng bị lệch vị trí dù chỉ 1–2 pixel thì điểm kiểm tra sẽ trượt ra ngoài nút bấm. Hãy cố định vị trí cửa sổ bằng [`WNDPOS`](/lenh/winapi#wndpos) / [`WNDSETINFO`](/lenh/winapi#wndsetinfo) trước khi dùng kỹ thuật này.

---

## Vòng lặp theo trạng thái màn hình

### Khi nào dùng

Nếu bạn viết một chuỗi lệnh cứng nhắc từ bước 1 đến bước 10 nối tiếp nhau bằng `WAIT`, chỉ cần một bước tải chậm hoặc có một hộp thoại thông báo bất ngờ hiện lên chắn ngang là toàn bộ các bước phía sau sẽ bấm trượt.

Thay vì viết theo thứ tự bước cố định, kỹ thuật **vòng lặp theo trạng thái màn hình** hoạt động như sau:
- Ở mỗi lượt lặp của script, gọi `GETSCREEN` một lần để chụp trạng thái màn hình hiện tại.
- Dùng các khối `IF_PIXEL_IN` kiểm tra lần lượt các điểm màu đặc trưng đại diện cho từng màn hình hoặc từng hộp thoại.
- Gặp trạng thái nào đang xuất hiện trên màn hình thì thực hiện thao tác tương ứng với trạng thái đó.
- Ở cuối lượt lặp, luôn có một lệnh nghỉ ngắn `WAITMS(100)`.

**Suy luận:** Lý do cách viết này ổn định là vì script không cần nhớ mình đang ở bước thứ mấy trong quy trình; ở mỗi vòng lặp, nó nhìn màn hình thực tế để quyết định việc cần làm tiếp theo, nên khi có hộp thoại bất ngờ hiện ra hoặc một bước bị chậm, script sẽ tự động xử lý hộp thoại đó rồi tự phục hồi về luồng công việc chính.

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

Ví dụ dưới đây kiểm tra hai trạng thái trong một vòng lặp: nếu thấy hộp thoại xác nhận của Notepad hiện lên (nhận diện qua màu đặc trưng tại `(420, 310)`) thì bấm nút đóng hộp thoại; nếu đang ở màn hình soạn thảo bình thường (màu trắng `16777215` tại `(300, 250)`) thì bấm vào vùng soạn thảo:

```cms
// Mỗi lượt lặp chụp lại màn hình hiện tại
GETSCREEN

// Trạng thái 1: Nếu xuất hiện hộp thoại thông báo (điểm 420, 310 có màu 15790320)
IF_PIXEL_IN(420, 310, 420, 310, 15790320)
   PRINT("Phat hien hop thoai -> Bam nut tren hop thoai")
   LCLICK(420, 310)
   WAITMS(500)
END_IF

// Trạng thái 2: Nếu vùng soạn thảo Notepad tại (300, 250) đang hiển thị màu trắng (16777215)
IF_PIXEL_IN(300, 250, 300, 250, 16777215)
   PRINT("Man hinh soan thao san sang -> Click vao khung soan thao")
   LCLICK(300, 250)
   WAITMS(500)
END_IF

// Nghỉ ngắn ở cuối mỗi lượt lặp để không làm nặng CPU
WAITMS(100)
```

### Lỗi dễ gặp

- **Thiếu `WAITMS` ở cuối vòng lặp:** Nếu không có trạng thái nào khớp mà cuối script cũng không có `WAITMS(100)`, vòng lặp sẽ gọi `GETSCREEN` liên tục, có thể gây tốn tài nguyên máy tính.
- **Hai trạng thái cùng khớp trong một lượt chụp:** Khi nhánh `IF_PIXEL_IN` đầu tiên vừa bấm chuột làm giao diện trên màn hình thay đổi, bức ảnh lưu trong **bộ đệm ảnh** vẫn là ảnh cũ chụp từ đầu lượt. Nếu nhánh `IF_PIXEL_IN` thứ hai ở ngay bên dưới cũng thỏa mãn trên bức ảnh cũ đó, script sẽ bấm tiếp vào giao diện đã đổi. Bạn có thể gọi lại `GETSCREEN` sau khi bấm chuột, hoặc dùng `ELSE` để mỗi lượt chỉ xử lý một trạng thái ưu tiên nhất.

---

## Khởi tạo một lần ở đầu vòng lặp bằng `DEFINE($init, 0)`

### Khi nào dùng

Vì script Clickermann tự động quay lại dòng đầu tiên sau khi chạy hết dòng cuối cùng, những công việc chỉ cần làm **đúng một lần lúc mới bắt đầu** (như tìm cửa sổ bằng `WNDFIND`, đặt vị trí cửa sổ bằng `WNDPOS`, lấy mã `hwnd` phần tử con bằng `HGET`...) cần được đặt bên trong một khối điều kiện bảo vệ bằng biến cờ `$init`:

1. Khai báo `DEFINE($init, 0)` ở đầu script. Theo help (mục Làm việc với số, lệnh [`DEFINE`](/lenh/so#define)), nếu biến `$init` đã tồn tại từ lượt chạy trước thì `DEFINE` sẽ bỏ qua không gán lại.
2. Kiểm tra `IF($init == 0)`: thực hiện các bước khởi tạo rồi gán `$init = 1` ở cuối khối `IF`.
3. Ở các lượt lặp tiếp theo, vì `$init` đã bằng `1`, khối khởi tạo sẽ được bỏ qua.
4. Khi nào phát hiện cửa sổ bị đóng hoặc cần thiết lập lại từ đầu, script chỉ cần gán lại **`$init = 0`** để lượt lặp kế tiếp tự động chạy lại khối khởi tạo.

::: warning Giả định về biến giữ giá trị qua các lượt lặp
**Trạng thái:** 🟡 Chưa chạy thử (cần kiểm tra thêm hành vi khi bấm Dừng / Áp dụng).

Kỹ thuật này dựa trên quy tắc trong help (phần Giới thiệu ngôn ngữ) rằng biến giữ nguyên giá trị khi script tự lặp lại sang lượt mới. Tuy nhiên, việc biến `$init` có giữ giá trị cũ sau khi người dùng bấm nút **Dừng** rồi bấm **Chạy** lại hay không cần được kiểm tra thực tế tại trang [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#gia-tri-bien-sau-khi-bam-dung-bam-ap-dung-hoac-doi-script).
:::

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

```cms
// Chỉ tạo biến $init = 0 nếu biến này chưa tồn tại
DEFINE($init, 0)

IF($init == 0)
   PRINT("Dang khoi tao cua so Notepad...")
   $hwnd_np = WNDFIND("Notepad")
   IF($hwnd_np > 0)
      WNDPOS($hwnd_np, 50, 50)
      WNDSIZE($hwnd_np, 500, 400)
      WAITMS(300)
      $init = 1
      PRINT("Da khoi tao xong, HWND = ", $hwnd_np)
   ELSE
      PRINT("Chua mo Notepad, cho 1 giay roi thu lai...")
      WAIT(1)
   END_IF
END_IF

// Phần công việc chính lặp lại ở mỗi lượt sau khi đã khởi tạo thành công
IF($init == 1)
   PRINT("Dang chay cong viec chinh tren cua so HWND = ", $hwnd_np)
   // Nếu phát hiện cửa sổ không còn tồn tại thì đặt $init = 0 để khởi tạo lại:
   IF(WNDFIND("Notepad") == 0)
      PRINT("Cua so Notepad da dong! Dat lai $init = 0 de tim lai.")
      $init = 0
   END_IF
   WAIT(2)
END_IF
```

### Lỗi dễ gặp

- **Viết `$init = 0` thay vì `DEFINE($init, 0)`:** Nếu viết phép gán thường `$init = 0` ở đầu script, mỗi khi script quay lại dòng đầu tiên thì `$init` luôn bị xóa về `0` và khối khởi tạo sẽ chạy lại ở mọi vòng lặp.
- **Gán `$init = 1` ngay cả khi chưa tìm thấy cửa sổ:** Chỉ nên gán `$init = 1` bên trong nhánh xác nhận đã tìm thấy cửa sổ (`IF($hwnd_np > 0)`) để nếu chưa mở ứng dụng thì vòng sau vẫn tiếp tục tìm.

---

## Xếp nhiều cửa sổ không chồng lên nhau và lấy phần tử con bằng `HGET`

### Khi nào dùng

Khi cần điều khiển hai hoặc nhiều cửa sổ ứng dụng cùng lúc (ví dụ hai cửa sổ Notepad đang mở hai tệp văn bản khác tên là `ghi-chu-1.txt` và `ghi-chu-2.txt`), bạn nên:

1. Dùng [`WNDFIND`](/lenh/winapi#wndfind) theo tên riêng trên thanh tiêu đề để tìm mã `hwnd` của từng cửa sổ cha.
2. Đặt vị trí và kích thước cho từng cửa sổ (bằng [`WNDPOS`](/lenh/winapi#wndpos) + [`WNDSIZE`](/lenh/winapi#wndsize) hoặc [`WNDSETINFO`](/lenh/winapi#wndsetinfo)) sao cho **hai cửa sổ nằm cạnh nhau, không chồng đè lên nhau**.
3. Sau khi các cửa sổ đã cố định vị trí trên màn hình, gọi [`HGET(x, y)`](/lenh/winapi#hget) tại một điểm tọa độ màn hình nằm bên trong vùng làm việc (khung soạn thảo) của từng cửa sổ để lấy mã `hwnd` của **phần tử con** bên trong.

**Vì sao phải lấy `hwnd` của phần tử con bằng `HGET` mà không dùng luôn `hwnd` từ `WNDFIND`?**
Theo help (bài [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so) và mục [`WNDFIND`](/lenh/winapi#wndfind)):
- Một cửa sổ ứng dụng gồm khung cửa sổ cha bên ngoài và nhiều **phần tử con** bên trong (như nút bấm, thanh công cụ, khung soạn thảo văn bản), mỗi phần tử con có mã `HWND` riêng và hệ tọa độ tương đối riêng.
- Hàm `WNDFIND` chỉ tìm được cửa sổ cha theo tiêu đề chứ **không tìm được các phần tử con** bên trong. Trong khi đó, các thao tác gõ phím hoặc bấm chuột ở chế độ cửa sổ (hoặc qua `POSTMESSAGE` / `alt_winmode`) cần gửi tới đúng mã `hwnd` của phần tử con trực tiếp nhận thao tác. Vì vậy, sau khi cố định vị trí cửa sổ cha, ta dùng `HGET(x, y)` tại tọa độ điểm nằm trên khung soạn thảo để lấy đúng `hwnd` của phần tử con đó.

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

Chuẩn bị: mở hai cửa sổ Notepad đang mở hai tệp có tên `ghi-chu-1` và `ghi-chu-2` trên thanh tiêu đề:

```cms
DEFINE($init, 0)

IF($init == 0)
   // 1. Tìm 2 cửa sổ cha theo tên tệp trên thanh tiêu đề
   $w1 = WNDFIND("ghi-chu-1")
   $w2 = WNDFIND("ghi-chu-2")

   IF(($w1 > 0) & ($w2 > 0))
      // 2. Xếp 2 cửa sổ nằm cạnh nhau, không chồng lấn:
      // Cửa sổ 1 ở bên trái: X = 0, Y = 0, Rộng = 450, Cao = 400
      WNDPOS($w1, 0, 0)
      WNDSIZE($w1, 450, 400)

      // Cửa sổ 2 ở bên phải: X = 460, Y = 0, Rộng = 450, Cao = 400
      WNDPOS($w2, 460, 0)
      WNDSIZE($w2, 450, 400)
      WAITMS(500)

      // 3. Lấy HWND của phần tử con (khung soạn thảo) bên trong mỗi cửa sổ
      // Điểm (200, 200) nằm trong khung soạn thảo của Cửa sổ 1 (0..450)
      $h_soan_1 = HGET(200, 200)
      // Điểm (660, 200) nằm trong khung soạn thảo của Cửa sổ 2 (460..910)
      $h_soan_2 = HGET(660, 200)

      PRINT("Cua so 1 -> Cha: ", $w1, " | Khung soan thao: ", $h_soan_1)
      PRINT("Cua so 2 -> Cha: ", $w2, " | Khung soan thao: ", $h_soan_2)
      $init = 1
   ELSE
      PRINT("Hay mo du 2 cua so Notepad co tieu de ghi-chu-1 va ghi-chu-2!")
   END_IF
END_IF

HALT
```

*(Lưu ý: với lệnh [`WNDSETINFO`](/lenh/winapi#wndsetinfo) dùng để gộp đặt vị trí và kích thước, có điểm `🟠 Chưa thống nhất` về việc truyền số trực tiếp hay truyền biến — xem chi tiết tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#truyen-so-truc-tiep-vao-wndsetinfo)).*

### Lỗi dễ gặp

- **Gọi `HGET` khi cửa sổ đang bị cửa sổ khác che đè lên:** `HGET(x, y)` lấy phần tử đang hiển thị tại tọa độ màn hình `(x, y)` ngay lúc gọi. Nếu có một cửa sổ khác (kể cả cửa sổ Clickermann) đang nằm đè lên điểm `(200, 200)` hoặc `(660, 200)`, `HGET` sẽ trả về nhầm `hwnd` của cửa sổ đang nằm đè ở phía trên. Bạn có thể gọi thêm [`WNDBUMP($w1)`](/lenh/winapi#wndbump), [`WNDBUMP($w2)`](/lenh/winapi#wndbump) trước khi gọi `HGET`.
- **Hai cửa sổ có cùng tiêu đề giống hệt nhau:** Nếu cả hai cửa sổ đều chỉ có tiêu đề `"Untitled - Notepad"`, hai lệnh `WNDFIND("Notepad")` sẽ trả về cùng một cửa sổ. Hãy mở hai tệp có tên khác nhau hoặc dùng [`HSETTEXT($w1, "Cua so 1")`](/lenh/winapi#hsettext) để đổi tiêu đề cửa sổ thứ nhất trước khi tìm cửa sổ thứ hai.

---

## Luồng giám sát (`THREAD`) phát hiện script chính bị kẹt

### Khi nào dùng

Khi script chính chạy trong thời gian dài, đôi khi script chính có thể bị kẹt ở một vòng lặp chờ màu hoặc không còn tiến triển qua các bước dự kiến. Bạn có thể tạo thêm một **luồng giám sát** chạy song song bằng [`THREAD(giam_sat, 1)`](/lenh/cau-truc#thread-end-thread) hoạt động theo nguyên tắc "nhịp tim":

- Mỗi khi script chính hoàn thành được một chu kỳ công việc quan trọng, script chính gán biến cờ **`$nhip = 1`**.
- Luồng `giam_sat` cứ mỗi `60` giây kiểm tra biến `$nhip` một lần:
  - Nếu thấy `$nhip == 0` (tức suốt 60 giây vừa qua script chính không hề đặt lại `$nhip = 1`), luồng giám sát sẽ in thông báo cảnh báo ra cửa sổ nhật ký.
  - Nếu thấy `$nhip == 1` (script chính vẫn đang hoạt động bình thường), luồng giám sát đặt lại **`$nhip = 0`** để bắt đầu theo dõi chu kỳ 60 giây tiếp theo.

**Nhắc lại hai quy tắc quan trọng của [`THREAD`](/khai-niem/luong) trong help:**
1. **Biến dùng chung:** Mọi luồng và script chính dùng chung tất cả các biến (như biến `$nhip`) và dùng chung bộ đệm ảnh.
2. **`SUB` và `#include` phải đặt trong thân luồng:** Nếu bên trong thân `THREAD` có gọi chương trình con (`SUB`) hoặc nạp thư viện qua `#include`, bạn bắt buộc phải đặt khối `SUB ... END_SUB` hoặc dòng `#include` đó ngay bên trong thân của chính luồng đó (xem thêm mục kiểm tra `🟠` tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#dat-sub-trong-tep-include)).

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

```cms
// Luồng giám sát chạy song song (truyền rõ init_state = 1)
THREAD(giam_sat, 1)
   // Chờ 60 giây mỗi nhịp kiểm tra
   WAIT(60)
   IF($nhip == 0)
      PRINT("CANH BAO: Script chinh khong cap nhat $nhip trong 60 giay qua!")
   ELSE
      PRINT("Giam sat: Script chinh van dang hoat dong binh thuong.")
      // Đặt lại $nhip = 0 để theo dõi chu kỳ 60 giây tiếp theo
      $nhip = 0
   END_IF
END_THREAD

// --- Script chính ---
GETSCREEN(200, 200, 300, 300)
IF_PIXEL_IN(200, 200, 300, 300, 16777215)
   // Báo cho luồng giám sát biết script chính vừa xử lý xong một nhịp
   $nhip = 1
   PRINT("Script chinh: Da xu ly xong mot luot, dat $nhip = 1")
END_IF

WAIT(5)
```

### Lỗi dễ gặp

- **Đặt `WAIT(60)` ở sau câu lệnh kiểm tra `IF($nhip == 0)`:** Nếu vừa bắt đầu chạy script mà luồng giám sát kiểm tra `IF($nhip == 0)` ngay ở dòng đầu tiên trước khi `WAIT(60)`, luồng giám sát sẽ báo cảnh báo giả ngay lập tức vì script chính chưa kịp chạy lượt đầu tiên. Hãy đặt `WAIT(60)` ở đầu thân luồng trước khi kiểm tra `$nhip`.
- **Gọi `SUB` khai báo ở ngoài từ trong thân `THREAD`:** Theo help, mỗi luồng chỉ gọi được `SUB` khai báo bên trong chính luồng đó.

---

## Tách script thành ba tệp bằng `#include`

### Khi nào dùng

Khi kịch bản của bạn dài hàng trăm dòng, việc để tất cả các chương trình con thư viện, các hàm xử lý nghiệp vụ và vòng lặp chính trong cùng một tệp duy nhất sẽ rất khó cuộn tìm và chỉnh sửa.

Bạn có thể tách dự án thành **3 tệp `.cms`** đặt trong cùng một thư mục dự án:

1. **`alt_winmode.cms` (Tệp thư viện dùng chung):** Chứa các chương trình con nền tảng (`A_LCLICK`, `A_KEYPRESS`, `A_GETSCREEN`... của [Thư viện alt_winmode](/nang-cao/alt-winmode)).
2. **`ham_xu_ly.cms` (Tệp chương trình con của dự án):** Chứa các khối `SUB ... END_SUB` do bạn tự viết riêng cho công việc hiện tại (như `SUB(khoi_tao_cua_so)`, `SUB(kiem_tra_hop_thoai)`).
3. **`chinh.cms` (Tệp script chính để mở và bấm Chạy):** Ở đầu tệp đặt hai dòng `#include` nạp tệp thư viện và tệp hàm theo đúng thứ tự, phía dưới chỉ viết vòng lặp điều khiển chính ngắn gọn.

::: warning Lưu ý thứ tự khai báo SUB và điểm chưa thống nhất về #include
**Trạng thái:** 🟠 Chưa thống nhất

- **Quy tắc thứ tự khai báo:** Theo help (mục Cấu trúc lệnh, lệnh [`SUB`](/lenh/cau-truc#sub-end-sub)), phần định nghĩa `SUB ... END_SUB` bắt buộc phải nằm **trước (phía trên)** mọi lời gọi tới nó. Vì chỉ thị `#include` chèn nội dung tệp vào đúng vị trí đặt chỉ thị, bạn phải đặt `#include "alt_winmode.cms"` ở trên cùng, tiếp theo là `#include "ham_xu_ly.cms"`, rồi mới tới phần code gọi các `SUB` đó ở bên dưới.
- **Điểm chưa thống nhất giữa các nguồn:** Help chính thức khuyến khích tách các `SUB` ra tệp riêng rồi nạp bằng `#include` và coi đó là thói quen tốt; ngược lại, sách của Chô tô (tr. 81) khuyên hạn chế để `SUB` ở tệp ngoài vì đôi lúc bị lỗi. Script thực tế có dùng cách tách tệp `#include` này và báo chạy tốt, chưa kiểm chứng lại trên máy Windows — xem hướng dẫn kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#dat-sub-trong-tep-include).
:::

### Ví dụ

**Trạng thái:** 🟠 Chưa thống nhất (do sử dụng `SUB` trong tệp `#include`, chưa chạy thử)

- **Tệp 1 — `alt_winmode.cms`:** Lưu mã nguồn 26 `SUB` từ trang [Thư viện alt_winmode](/nang-cao/alt-winmode#ma-nguon-thu-vien-alt-winmode-cms-26-chuong-trinh-con).
- **Tệp 2 — `ham_xu_ly.cms`:**
  ```cms
  // Các chương trình con phục vụ riêng cho dự án Notepad
  SUB(go_chu_ab, $hwnd_muc_tieu)
     A_KEYPRESS(#A, $hwnd_muc_tieu)
     WAITMS(100)
     A_KEYPRESS(#B, $hwnd_muc_tieu)
     WAITMS(100)
  END_SUB
  ```
- **Tệp 3 — `chinh.cms` (tệp mở trong Clickermann):**
  *(Minh họa cấu trúc nạp `#include` ở đầu tệp rồi gọi chương trình con bên dưới):*
  ```text
  // 1. Nạp thư viện nền trước
  #include "alt_winmode.cms"
  // 2. Nạp tệp chứa các SUB của dự án (có gọi tới A_KEYPRESS của alt_winmode)
  #include "ham_xu_ly.cms"

  // 3. Kịch bản chính ngắn gọn
  $w = WNDFIND("Notepad")
  IF($w > 0)
     WNDPOS($w, 100, 100)
     WNDSIZE($w, 500, 400)
     WAITMS(300)
     $h_edit = HGET(250, 250)
     go_chu_ab($h_edit)
  END_IF

  HALT
  ```

### Lỗi dễ gặp

- **Đặt ngược thứ tự `#include`:** Nếu trong `ham_xu_ly.cms` có gọi `A_LCLICK` nhưng bạn lại đặt `#include "ham_xu_ly.cms"` ở phía trên `#include "alt_winmode.cms"` (hoặc đặt `#include` ở cuối tệp `chinh.cms`), lời gọi `SUB` sẽ nằm trước định nghĩa `SUB` và gây lỗi.
- **Chưa lưu các tệp vào cùng một thư mục dự án:** Chỉ thị `#include "ten_tep.cms"` tìm tệp tương đối trong thư mục dự án hiện tại; nếu để lệch thư mục, Clickermann sẽ không nạp được tệp.

---

## Công cụ dò tọa độ và màu nhanh kèm mẹo ghi chú mã màu

### Khi nào dùng

Khi chuẩn bị viết script cho một cửa sổ mới, bạn cần lấy hàng loạt cặp tọa độ `(X, Y)` và mã màu tại các nút bấm. Ngoài việc nhìn khung thông tin bên trái [Trình soạn thảo](/bat-dau/trinh-soan-thao) hoặc nhấn phím tắt `Alt + Q`, bạn có thể dùng một script ngắn tự in tọa độ và mã màu tại mũi chuột ra cửa sổ nhật ký mỗi giây:

- **Ở chế độ màn hình thường:** Gọi `GETSCREEN` rồi dùng `PRINT($_xmouse, ", ", $_ymouse, " // ", PXL($_xmouse, $_ymouse))`.
- **Khi cần tọa độ tương đối theo một cửa sổ `$hwnd`:** Gọi chương trình con **`A_CHECK_PXL($hwnd)`** có sẵn trong [Thư viện alt_winmode](/nang-cao/alt-winmode) — hàm này tự trừ tọa độ góc cửa sổ `$A_x0, $A_y0` và in ra cửa sổ nhật ký theo định dạng `(x,y) // mã_màu`.

**Mẹo ghi chú mã màu ngay sau lệnh bấm chuột:**
Khi viết lệnh `LCLICK` hoặc `A_LCLICK`, hãy tập thói quen ghi chú lại **mã màu của điểm đó** ngay sau dấu `//` trên cùng dòng lệnh, ví dụ:

```cms
LCLICK(180, 240)  // 16777215
```

Cách ghi chú này rất hữu ích: về sau khi đọc lại code hoặc khi muốn chuyển dòng `LCLICK(180, 240)` thành câu lệnh kiểm tra `IF_PIXEL_IN(180, 240, 180, 240, 16777215)` trước khi bấm, bạn đã có sẵn mã màu ngay bên cạnh tọa độ mà không phải mở lại ứng dụng để đo lại. *(Suy luận: định dạng `LCLICK(x, y)  // màu` cũng có thể chính là mẫu dòng lệnh do phím tắt `Alt + Q` trong Trình soạn thảo tự động chèn — xem mục kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#noi-dung-chen-nhanh-cua-phim-tat-alt-q)).*

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

```cms
// Công cụ dò tọa độ màn hình và mã màu dưới trỏ chuột mỗi 500ms
// Nhấn Alt + S để dừng khi đã lấy đủ tọa độ
LOGSHOW(1)
GETSCREEN
PRINT("Toa do (", $_xmouse, ", ", $_ymouse, ") // ", PXL($_xmouse, $_ymouse))
WAITMS(500)
```

Khi áp dụng tọa độ và mã màu vừa dò được vào script:

```cms
// Ghi chú mã màu ngay sau tọa độ bấm chuột để dễ tra cứu và bảo trì sau này
GETSCREEN(180, 240, 180, 240)
IF_PIXEL_IN(180, 240, 180, 240, 16777215)
   LCLICK(180, 240)  // 16777215
   WAITMS(300)
END_IF

HALT
```

### Lỗi dễ gặp

- **Cửa sổ cần đo bị che khuất lúc chạy `A_CHECK_PXL` hoặc `GETSCREEN`:** Vì `PXL($_xmouse, $_ymouse)` lấy màu trên ảnh chụp màn hình tại vị trí mũi chuột, bạn cần để điểm cần đo hiển thị rõ trên màn hình.
- **Bật kính lúp liên tục trong lúc chạy script chính:** Theo help (bài Trình soạn thảo), việc bật kính lúp trong Trình soạn thảo có thể làm con trỏ chuột di chuyển chậm. Sau khi đã dò xong tọa độ và mã màu, hãy tắt kính lúp trước khi cho script chạy thật.

---

## Thêm khoảng chờ `WAITMS` sau thao tác và in nhật ký `PRINT` ở từng nhánh

### Khi nào dùng

Hai thói quen nhỏ nhưng quyết định việc bạn có dễ dàng chỉnh sửa script hay không:

1. **Luôn thêm `WAITMS` sau mỗi lệnh click chuột hoặc gõ phím:** Khi script gọi `LCLICK` hay `A_LCLICK`, ứng dụng đích cần một khoảng thời gian ngắn để vẽ lại giao diện, mở hộp thoại hoặc đổi màu nút bấm. Nếu bạn gọi `GETSCREEN` kiểm tra bước tiếp theo ngay lập tức mà không có `WAITMS`, giao diện chưa kịp đổi nên script sẽ đọc lại hình ảnh cũ và tưởng rằng cú click vừa rồi chưa ăn.
2. **Đặt `PRINT` ở đầu mỗi nhánh `IF` / `IF_PIXEL_IN`:** Trong một vòng lặp có 5–10 nhánh điều kiện khác nhau, việc thêm một dòng `PRINT("Nhanh A: ...")` ngắn gọn ở mỗi nhánh giúp bạn nhìn vào cửa sổ Nhật ký là biết ngay script đang đi vào nhánh nào, đang chờ màu nào hoặc bị lặp kẹt ở nhánh nào.

### Ví dụ

**Trạng thái:** 🟡 Chưa chạy thử

```cms
LOGSHOW(1)
GETSCREEN

// Nhánh 1: Kiểm tra nút mở bảng màu trong Paint tại (320, 90)
IF_PIXEL_IN(320, 90, 320, 90, 15790320)
   PRINT("[Nhanh 1] Thay nut bang mau tai (320, 90) -> Bam mo bang mau")
   LCLICK(320, 90)  // 15790320
   // Chờ 300ms để bảng màu kịp hiện ra trên giao diện trước khi sang lượt sau
   WAITMS(300)
ELSE
   PRINT("[Cho] Chua thay nut bang mau tai (320, 90), tiep tuc doi...")
   WAITMS(200)
END_IF

HALT
```

### Lỗi dễ gặp

- **Đặt `PRINT` bên ngoài mọi nhánh điều kiện trong vòng lặp cực nhanh:** Nếu bạn đặt `PRINT` ở mỗi vòng lặp `WAITMS(50)` mà không nằm trong nhánh sự kiện, cửa sổ nhật ký sẽ bị trôi hàng chục dòng mỗi giây khiến bạn không kịp đọc các thông báo quan trọng. Chỉ nên `PRINT` khi một nhánh hành động thực sự được kích hoạt hoặc khi trạng thái thay đổi.
- **Dùng `WAIT` (đơn vị giây) thay vì `WAITMS` (mili-giây) do nhầm lẫn:** Viết nhầm `WAIT(300)` sẽ làm script đứng chờ tới `300` giây (5 phút) thay vì `300` mili-giây (`0,3` giây). Hãy kiểm tra kỹ tên lệnh `WAIT` và `WAITMS`.

---

*Nguồn: Kỹ thuật tổng hợp từ script thực tế của người biên soạn (đã viết lại ví dụ cho Notepad và Paint) và tài liệu trợ giúp `help.chm` (phần Giới thiệu ngôn ngữ, bài Khóa cửa sổ, mục Cấu trúc lệnh, mục Màn hình và mục WinAPI); tham khảo đối chiếu sách của Chô tô (tr. 81).*
