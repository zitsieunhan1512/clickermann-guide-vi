# Xử lý lỗi và câu hỏi thường gặp (FAQ)

Trang này tổng hợp cách khắc phục nhanh các sự cố thường gặp khi mới làm quen với Clickermann v4.13 cũng như các câu hỏi thường gặp trong tài liệu trợ giúp. *(Lưu ý: một số tên nút tiếng Anh như Settings, Record, Open trong bài là tên minh họa để dễ hình dung, vì tài liệu trợ giúp gốc viết bằng tiếng Nga).*

## Script không dừng được (con trỏ chuột tự chạy liên tục)

Khi script có lệnh điều khiển chuột (như `LCLICK`, `MOVE`, `LDOWN`) đang chạy lặp liên tục, bạn rất khó dùng chuột để bấm vào nút **Dừng** trên cửa sổ Clickermann.

- **Cách xử lý ngay:** Nhấn tổ hợp phím tắt toàn cục **`Alt + S`** trên bàn phím để ngắt script ngay lập tức mà không cần chạm vào chuột.
- Nếu vừa dừng giữa chừng một script có lệnh giữ chuột `LDOWN` và thấy nút chuột trái vẫn đang bị giữ, hãy bấm chuột trái một cái trên vùng trống để nhả ra.
- Nếu nhấn `Alt + S` không có tác dụng do xung đột phím tắt, hãy xem mục [Phím tắt không hoạt động](#phim-tat-alt-a-alt-s-khong-hoat-dong) bên dưới.

## Bấm chạy nhưng không thấy chuyện gì xảy ra

Nếu bạn vừa gõ hoặc sửa code xong, bấm Chạy (`Alt + A`) mà không thấy Clickermann thực hiện lệnh mới:

1. **Quên bấm nút Áp dụng:** Trong [Trình soạn thảo](/bat-dau/trinh-soan-thao), sau khi gõ hoặc sửa code, bạn **bắt buộc phải bấm nút Áp dụng** (ở cột bên trái) trước khi bấm Chạy. Nếu chưa bấm Áp dụng, chương trình vẫn chạy kịch bản cũ (hoặc kịch bản trống ban đầu).
2. **Chưa mở cửa sổ Nhật ký:** Nếu script của bạn chỉ in kết quả bằng lệnh [`PRINT`](/lenh/nhat-ky#logwrite-print) / `LOGWRITE` mà không di chuyển chuột, hãy bấm nút **Nhật ký** ở cột bên trái của Trình soạn thảo (hoặc gọi `LOGSHOW(1)` trong script) để mở cửa sổ nhật ký xem kết quả.

## Không tìm thấy tệp `.txt`, `.ini`, `.bmp` do script tạo ra (hoặc script không đọc được tệp)

- **Nguyên nhân:** Từ bản v4.6.000, mọi đường dẫn tệp tương đối (chỉ viết tên tệp như `"cau_hinh.ini"`, `"nut_bam.bmp"`) đều được tính từ **thư mục dự án** — tức là thư mục chứa tệp script `.cms` đang nạp.
- **Cách xử lý:**
  - Trước khi chạy script có đọc/ghi tệp, hãy nhấn `Ctrl + S` trong Trình soạn thảo để lưu tệp `.cms` vào một thư mục riêng (thư mục dự án), và đặt các tệp `.bmp`, `.txt`, `.ini` cần dùng vào **cùng thư mục với tệp `.cms` đó**.
  - Riêng với lệnh chụp màn hình [`SCREENSHOT`](/lenh/man-hinh#screenshot) và [`SCREENSHOTEX`](/lenh/man-hinh#screenshotex), ảnh chụp thường được đặt trong thư mục con `screens\` nằm bên trong thư mục dự án.

## Làm sao để vừa chạy Clickermann vừa dùng máy tính làm việc khác?

Trong một số trường hợp, bạn có thể dùng **[Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so)** (`Alt + W` hoặc lệnh [`HSET`](/lenh/winapi#hset)). Ở chế độ này, Clickermann không chiếm chuột và bàn phím thật mà hoạt động ngay cả trong cửa sổ không kích hoạt hoặc đang bị cửa sổ khác che khuất, giúp bạn thoải mái làm việc riêng.

Trong một số trường hợp, bạn thậm chí có thể dùng các lệnh phân tích hình ảnh (`GETSCREEN`, `IF_PIXEL_IN`...) ngay cả khi cửa sổ đó đang bị cửa sổ khác đè lên (miễn là **không thu nhỏ** cửa sổ xuống thanh tác vụ). Tuy nhiên, không phải mọi ứng dụng đều cho phép làm như vậy; khả năng hoạt động của chế độ này phụ thuộc vào ứng dụng đích.

## Không bấm được chuột / bàn phím ở chế độ khóa cửa sổ

Khi bạn dùng chế độ khóa cửa sổ (`Alt + W`), có thể phát sinh những trục trặc đặc thù **tùy cách ứng dụng được viết** (ví dụ: trên Firefox chạy được, trên Google Chrome thì không).

**Cách xử lý:**

- **Suy luận:** Kiểm tra lại xem lúc nhấn `Alt + W` bạn đã trỏ chuột đúng vào **phần tử con** cần thao tác bên trong cửa sổ chưa (thay vì khóa nhầm vào phần khung/thanh tiêu đề ngoài cùng).
- Nếu ứng dụng đích không hoạt động với chế độ khóa cửa sổ, hãy từ bỏ chế độ khóa cửa sổ để chuyển sang chế độ thường nếu chấp nhận được, hoặc chạy Clickermann ở chế độ thường bên trong một máy ảo (xem [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so#gioi-han-va-giai-phap-dung-may-ao)).
- Lưu ý: Clickermann có chỉ thị `#ps2_mouse`, `#ps2_keyboard` (chế độ PS/2). Tài liệu này không hướng dẫn phần đó.

## Các lệnh đọc màu / tìm ảnh không hoạt động

Nếu các lệnh [`PXL`](/lenh/man-hinh#pxl), [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if) hay [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if) không hoạt động như mong đợi:

1. **Quên gọi `GETSCREEN`:** Đây là lỗi rất thường gặp ở người mới học ("trong trình soạn thảo thì thấy màu mà vào script lại không chạy"). Hãy nhớ đặt lệnh [`GETSCREEN`](/lenh/man-hinh#getscreen) trước các lệnh phân tích màn hình để cập nhật [bộ đệm ảnh](/khai-niem/bo-dem-anh).
2. **Lớp phủ (Overlay) và cửa sổ phân lớp / trong suốt:**
   - Các **lớp phủ (overlay)** và các **cửa sổ phân lớp (trong suốt)** đều không được chụp vào bộ đệm ảnh.
   - Riêng với **cửa sổ trong suốt**, công cụ **[Quản lý cửa sổ](/bat-dau/quan-ly-cua-so)** có thể xử lý được: nếu bạn đặt độ hiển thị của cửa sổ đó lên **100%** (theo ảnh trong help của bản cũ: chọn **Alpha 100%** rồi bấm nút áp dụng), cờ cửa sổ phân lớp sẽ được gỡ bỏ và Clickermann bắt đầu nhìn thấy cửa sổ đó.
3. **Con trỏ chuột đồ họa riêng:** Nếu ứng dụng sử dụng con trỏ chuột đồ họa riêng, trình soạn thảo có thể lúc nào cũng chỉ nhìn thấy điểm ảnh mang màu của chính con trỏ đồ họa đó. Cách khắc phục: tắt con trỏ đồ họa trong phần cài đặt của ứng dụng (nếu có), hoặc trước khi phân tích hãy dùng [`MOVE`](/lenh/chuot#move) đưa con trỏ chuột ra góc xa rồi mới chụp màn hình và xử lý.
4. **Cửa sổ đang bị thu nhỏ:** Ở chế độ khóa cửa sổ, nếu cửa sổ bị thu nhỏ xuống thanh tác vụ thì Windows ngừng vẽ cửa sổ đó nên các hàm phân tích đồ họa không hoạt động (màu trong kính lúp luôn là màu đen).

## Chương trình có hỗ trợ nhiều màn hình (Multi-monitor) không?

**Có.** Clickermann hỗ trợ đầy đủ màn hình mở rộng (Extended Desktop / nhiều màn hình) cho cả các lệnh phân tích màn hình lẫn các lệnh bấm chuột, bất kể tọa độ mang giá trị dương hay giá trị âm.

## Làm sao để tự động chạy script ngay khi mở tệp `.cms`?

Thực hiện 2 bước sau:

1. Thêm chỉ thị `#autorun` vào script `.cms`.
2. Mở phần cài đặt (Settings) của Clickermann và tạo liên kết định dạng tệp `*.cms` (File Association) với Clickermann.

Từ lúc đó, khi bạn mở tệp `.cms` (giống như mở tệp `.txt` bằng Notepad), Clickermann sẽ khởi động và bắt đầu chạy ngay script đó. Lưu ý: tự động chạy không áp dụng khi bạn mở script từ bên trong cửa sổ chương trình ngay cả khi có chỉ thị `#autorun`.

## Phím tắt (`Alt + A`, `Alt + S`...) không hoạt động

Có thể sau khi mở Clickermann, một chương trình khác đã gán đè tổ hợp phím tắt đó cho riêng nó.

- Hãy vào phần cài đặt của Clickermann, đặt lại các phím tắt cần thiết, bấm áp dụng và khởi động lại chương trình. Nếu vẫn còn xung đột, hãy thử các tổ hợp phím khác.
- Nếu bạn dùng cùng lúc nhiều bản Clickermann nhân bản, bạn cần đặt cho mỗi bản một bộ phím tắt riêng.

## Script ghi tự động (Record) quá dài vì toàn lệnh `MOVE`

Khi bạn ghi lại thao tác (Record), script tạo ra có thể rất dài và toàn là lệnh [`MOVE`](/lenh/chuot#move) gây bất tiện khi chỉnh sửa.

**Cách xử lý:** Trước khi ghi, hãy vào phần cài đặt (Settings) và **bỏ dấu chọn ở mục "ghi lại chuyển động chuột"** (minh họa tiếng Anh: *Record mouse movements*).

## Chương trình kết nối mạng khi vừa khởi động

Khi vừa mở lên, Clickermann tự động kiểm tra bản cập nhật mới trên máy chủ chính thức. Bạn có thể tắt chức năng này trong phần cài đặt. Ngoài ra, tường lửa cũng có thể cảnh báo nếu bản thân script đang chạy có **sử dụng các hàm mạng**.

## Phần mềm diệt virus cảnh báo

Trình diệt virus (thường là các trình diệt virus ít tên tuổi, không phổ biến) có thể không thích khả năng theo dõi chuột, bàn phím và các chức năng tương tự của chương trình. Nếu bạn tải đúng bản chính thức từ `http://crapware.aidf.org`, hãy thêm Clickermann vào danh sách loại trừ (exclusion) của trình diệt virus.

---

*Nguồn: Tài liệu trợ giúp `help.chm` (phần FAQ, bài Khóa cửa sổ, bài Trình soạn thảo và Lịch sử phiên bản).*
