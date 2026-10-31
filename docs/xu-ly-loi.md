# Xử lý lỗi và câu hỏi thường gặp (FAQ)

Trang này tổng hợp cách khắc phục các sự cố thường gặp khi dùng Clickermann v4.13 dựa theo help, phần FAQ. *(Lưu ý: các tên tiếng Anh như Settings, Record, Open, "Record mouse movements" trong bài là tên minh họa để dễ hình dung, vì tài liệu help gốc viết bằng tiếng Nga).*

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Làm sao để vừa chạy Clickermann vừa dùng máy tính làm việc khác?

Trong một số trường hợp (theo help, phần FAQ), bạn có thể dùng **[Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so)** (`Alt + W` hoặc lệnh [`HSET`](/lenh/winapi#hset)). Ở chế độ này, Clickermann không chiếm chuột và bàn phím thật mà hoạt động ngay cả trong cửa sổ không kích hoạt hoặc đang bị cửa sổ khác che khuất, giúp bạn thoải mái làm việc riêng.

Trong một số trường hợp (theo help, phần FAQ), bạn thậm chí có thể dùng các lệnh phân tích hình ảnh (`GETSCREEN`, `IF_PIXEL_IN`...) ngay cả khi cửa sổ đó đang bị cửa sổ khác đè lên (miễn là **không thu nhỏ** cửa sổ xuống thanh Taskbar). Tuy nhiên, không phải mọi ứng dụng đều cho phép làm như vậy; khả năng hoạt động của chế độ này phụ thuộc vào ứng dụng đích (theo help, phần FAQ).

## Không bấm được chuột / bàn phím ở chế độ khóa cửa sổ

Khi bạn dùng chế độ khóa cửa sổ (`Alt + W`), có thể phát sinh những trục trặc đặc thù **tùy cách ứng dụng được viết** (theo help, phần FAQ; ví dụ trong help: "trên Firefox chạy được, trên Google Chrome thì không").

**Cách xử lý:**

- Suy luận (từ help, bài Khóa cửa sổ): kiểm tra lại xem lúc nhấn `Alt + W` bạn đã trỏ chuột đúng vào **phần tử con** cần thao tác bên trong cửa sổ chưa (thay vì khóa nhầm vào phần khung/thanh tiêu đề ngoài cùng).
- Nếu ứng dụng đích không hoạt động với chế độ khóa cửa sổ, hãy từ bỏ chế độ khóa cửa sổ để chuyển sang chế độ thường nếu chấp nhận được (theo help, phần FAQ), hoặc chạy Clickermann ở chế độ thường bên trong một máy ảo (theo help, bài Khóa cửa sổ).
- Lưu ý: Clickermann có chỉ thị `#ps2_mouse`, `#ps2_keyboard` (chế độ PS/2). Tài liệu này không hướng dẫn phần đó.

## Các lệnh đọc màu / tìm ảnh không hoạt động

Nếu các lệnh [`PXL`](/lenh/man-hinh#pxl), [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if) hay [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if) không hoạt động như mong đợi (theo help, phần FAQ và bài Khóa cửa sổ):

1. **Quên gọi `GETSCREEN` (theo help, phần FAQ):** Đây là lỗi rất thường gặp ở người mới học ("trong trình soạn thảo thì chạy mà vào script lại không chạy"). Hãy nhớ đặt lệnh [`GETSCREEN`](/lenh/man-hinh#getscreen) trước các lệnh phân tích màn hình để cập nhật **bộ đệm ảnh**.
2. **Lớp phủ (Overlay) và cửa sổ phân lớp / trong suốt (theo help, phần FAQ):**
   - Các **lớp phủ (overlay)** và các **cửa sổ phân lớp (trong suốt)** đều không được chụp vào bộ đệm ảnh.
   - Riêng với **cửa sổ trong suốt**, công cụ **[Quản lý cửa sổ](/bat-dau/quan-ly-cua-so)** có thể xử lý được: nếu bạn đặt độ hiển thị của cửa sổ đó lên **100%** (theo ảnh trong help của bản cũ: chọn **Alpha 100%** rồi bấm nút áp dụng), cờ cửa sổ phân lớp sẽ được gỡ bỏ và Clickermann bắt đầu nhìn thấy cửa sổ đó.
3. **Con trỏ chuột đồ họa riêng (theo help, phần FAQ):** Nếu ứng dụng sử dụng con trỏ chuột đồ họa riêng, trình soạn thảo có thể lúc nào cũng chỉ nhìn thấy điểm ảnh mang màu của chính con trỏ đồ họa đó. Cách khắc phục: tắt con trỏ đồ họa trong phần cài đặt của ứng dụng (nếu có), hoặc trước khi phân tích hãy dùng [`MOVE`](/lenh/chuot#move) đưa con trỏ chuột ra góc xa rồi mới chụp màn hình và xử lý.
4. **Cửa sổ đang bị thu nhỏ (theo help, bài Khóa cửa sổ):** Ở chế độ khóa cửa sổ, nếu cửa sổ bị thu nhỏ xuống thanh tác vụ thì Windows ngừng vẽ cửa sổ đó nên các hàm phân tích đồ họa không hoạt động (màu trong kính lúp luôn là màu đen).

## Chương trình có hỗ trợ nhiều màn hình (Multi-monitor) không?

**Có.** Clickermann hỗ trợ đầy đủ màn hình mở rộng (Extended Desktop / nhiều màn hình) cho cả các lệnh phân tích màn hình lẫn các lệnh bấm chuột, bất kể tọa độ mang giá trị dương hay giá trị âm (theo help, phần FAQ).

## Làm sao để tự động chạy script ngay khi mở tệp `.cms`?

Thực hiện 2 bước sau (theo help, phần FAQ):

1. Thêm chỉ thị `#autorun` vào script `.cms`.
2. Mở phần cài đặt (Settings) của Clickermann và tạo liên kết định dạng tệp `*.cms` (File Association) với Clickermann.

Từ lúc đó, khi bạn mở tệp `.cms` (giống như mở tệp `.txt` bằng Notepad), Clickermann sẽ khởi động và bắt đầu chạy ngay script đó. Lưu ý: tự động chạy không áp dụng khi bạn mở script từ bên trong cửa sổ chương trình ngay cả khi có chỉ thị `#autorun`.

## Phím tắt (`Alt + A`, `Alt + S`...) không hoạt động

Có thể sau khi mở Clickermann, một chương trình khác đã gán đè tổ hợp phím tắt đó cho riêng nó (theo help, phần FAQ).

- Hãy vào phần cài đặt của Clickermann, đặt lại các phím tắt cần thiết, bấm áp dụng và khởi động lại chương trình. Nếu vẫn còn xung đột, hãy thử các tổ hợp phím khác (theo help, phần FAQ).
- Nếu bạn dùng cùng lúc nhiều bản Clickermann nhân bản, bạn cần đặt cho mỗi bản một bộ phím tắt riêng (theo help, phần FAQ).

## Script ghi tự động (Record) quá dài vì toàn lệnh `MOVE`

Khi bạn ghi lại thao tác (Record), script tạo ra có thể rất dài và toàn là lệnh [`MOVE`](/lenh/chuot#move) gây bất tiện khi chỉnh sửa (theo help, phần FAQ).

**Cách xử lý:** Trước khi ghi, hãy vào phần cài đặt (Settings) và **bỏ dấu chọn ở mục "ghi lại chuyển động chuột"** (minh họa tiếng Anh: *Record mouse movements*).

## Chương trình kết nối mạng khi vừa khởi động

Khi vừa mở lên, Clickermann tự động kiểm tra bản cập nhật mới trên máy chủ chính thức (theo help, phần FAQ). Bạn có thể tắt chức năng này trong phần cài đặt. Ngoài ra, tường lửa cũng có thể cảnh báo nếu bản thân script đang chạy có **sử dụng các hàm mạng** (theo help, phần FAQ).

## Phần mềm diệt virus cảnh báo

Theo help, phần FAQ, trình diệt virus (thường là các trình diệt virus ít tên tuổi, không phổ biến) có thể không thích khả năng theo dõi chuột, bàn phím và các chức năng tương tự của chương trình. Nếu bạn tải đúng bản chính thức từ `http://crapware.aidf.org`, hãy thêm Clickermann vào danh sách loại trừ (exclusion) của trình diệt virus.
