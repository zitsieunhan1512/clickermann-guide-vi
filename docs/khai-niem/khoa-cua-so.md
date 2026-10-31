# Chế độ khóa cửa sổ

Trang này giải thích bản chất của **chế độ khóa cửa sổ** trong Clickermann, khái niệm cửa sổ và phần tử con trong Windows, cách bật khóa cửa sổ bằng phím tắt `Alt + W` và các điều kiện để đọc được màu sắc.

**Trạng thái:** 🟡 Theo help, chưa chạy thử

## Chế độ khóa cửa sổ là gì?

Ở chế độ thường, Clickermann điều khiển trực tiếp con trỏ chuột và bàn phím của máy tính nên trong lúc script đang chạy, bạn không thể dùng chuột hay gõ phím để làm việc khác.

Khi bật **chế độ khóa cửa sổ** (help, bài Khóa cửa sổ), Clickermann sẽ khóa mục tiêu vào một phần tử cửa sổ cụ thể và chỉ gửi các thông điệp thao tác thẳng tới phần tử đó. Nhờ vậy, **cả Clickermann và bạn có thể làm việc đồng thời trên cùng một máy tính mà không hề làm phiền nhau**.

![So sánh chế độ thường và chế độ khóa cửa sổ](/so-do/hai-che-do.svg)

## Bản chất "cửa sổ" và "phần tử con" trong Windows

Theo giải thích trong help, bài Khóa cửa sổ, khái niệm "cửa sổ" của người dùng thông thường và của hệ điều hành Windows có điểm khác nhau:

- Với người dùng, một "cửa sổ" là cả khung chương trình lớn có nút đóng `[X]` ở góc phải trên.
- Nhưng đối với hệ điều hành Windows, mỗi nút bấm, nhãn chữ, thanh công cụ hay ô nhập văn bản bên trong khung chương trình đó đều là một **phần tử con** (cửa sổ con) độc lập. Một cửa sổ ứng dụng quen thuộc có thể chứa khoảng mười phần tử con như vậy (theo help, bài Khóa cửa sổ).
- Mỗi phần tử đều có một mã số định danh duy nhất gọi là **`HWND`**. Khi đưa trỏ chuột lên bất kỳ vị trí nào, Clickermann sẽ hiển thị mã `HWND` của phần tử nằm ngay dưới mũi chuột tại mục "Khóa cửa sổ" trên màn hình chính (kèm theo mã tiến trình `PID` và tên tệp `.exe`). Ngoài ra, ngôn ngữ script còn có một số lệnh cho phép lấy mã `HWND` trong lúc script đang chạy (theo help, bài Khóa cửa sổ, như [`WNDFIND`](/lenh/winapi#wndfind), [`HGET`](/lenh/winapi#hget)).

![Một cửa sổ ứng dụng chứa nhiều phần tử con, mỗi phần tử có HWND riêng](/so-do/cua-so-phan-tu.svg)

## Cách bật khóa cửa sổ và hệ tọa độ

Chế độ khóa cửa sổ được bật bằng tổ hợp phím tắt vì tại thời điểm khóa, mũi trỏ chuột của bạn cần phải đang trỏ đúng vào phần tử mục tiêu:

1. Đưa con trỏ chuột trỏ vào **phần tử mục tiêu** cần tự động hóa (ví dụ khung nội dung bên trong cửa sổ ứng dụng hoặc khung Flash trong trình duyệt — bản thân khung đó cũng là một phần tử có `HWND` riêng).
2. Nhấn tổ hợp phím **`Alt + W`** (mặc định).
3. Chương trình sẽ bắt lấy phần tử dưới trỏ chuột làm **phần tử đang khóa**. Từ lúc này, số `HWND` trên màn hình chính sẽ đứng yên ở mã của phần tử đang khóa.

Ngoài ra, bạn cũng có thể bật hoặc đổi phần tử đang khóa ngay trong code bằng lệnh [`HSET(hwnd, 1)`](/lenh/winapi#hset).

**Thay đổi về hệ tọa độ:**

- Cú pháp các lệnh trong script giữ nguyên giữa chế độ thường và chế độ khóa cửa sổ.
- Điểm khác biệt duy nhất là hệ tọa độ: mỗi phần tử con có **hệ tọa độ tương đối riêng** với điểm `(0, 0)` nằm ở góc trái trên của chính phần tử đó. Dù bạn di chuyển cửa sổ ứng dụng sang vị trí khác trên màn hình, hệ tọa độ bên trong phần tử đang khóa vẫn không thay đổi.

## Khi nào đọc được màu ở chế độ khóa cửa sổ?

Các lệnh phân tích màn hình (như [`GETSCREEN`](/lenh/man-hinh#getscreen), [`IF_PIXEL_IN`](/lenh/man-hinh#if-pixel-in-end-if), [`IF_PICTURE_IN`](/lenh/man-hinh#if-picture-in-end-if)) ở chế độ khóa cửa sổ tuân theo quy tắc sau (theo help, bài Khóa cửa sổ và phần FAQ):

- **Cửa sổ bị che khuất bởi cửa sổ khác:** **Có thể đọc được màu, tùy ứng dụng; hãy kiểm tra bằng kính lúp** (theo help, phần FAQ và bài Khóa cửa sổ). Trong một số trường hợp, bạn có thể mở cửa sổ Word hoặc xem phim đè lên trên cửa sổ đang khóa mà script vẫn phân tích được đồ họa.
- **Cửa sổ bị thu nhỏ xuống thanh tác vụ (Minimize):** **Không đọc được màu**. Lý do là khi cửa sổ bị thu nhỏ xuống Taskbar, Windows ngừng vẽ đồ họa của cửa sổ đó để tiết kiệm tài nguyên hệ thống (theo help, bài Khóa cửa sổ).

![So sánh cửa sổ bị che khuất và cửa sổ bị thu nhỏ](/so-do/che-va-thu-nho.svg)

**Cách kiểm tra nhanh (theo help, bài Khóa cửa sổ):** Sau khi bật khóa cửa sổ, hãy mở [Trình soạn thảo](/bat-dau/trinh-soan-thao) và bật **kính lúp**. Nếu màu sắc/hình ảnh trong kính lúp vẫn thay đổi ngay cả khi có cửa sổ khác đè lên thì mọi thứ hoạt động tốt; ngược lại nếu kính lúp luôn chỉ có màu đen thì không phân tích hình ảnh ở chế độ khóa cửa sổ được.

## Giới hạn và giải pháp dùng máy ảo

- Không phải ứng dụng nào cũng cho phép hoạt động ở chế độ khóa cửa sổ; khả năng hoạt động phụ thuộc vào cách ứng dụng đích được viết (theo help, phần FAQ). Lệnh [`MOVER`](/lenh/chuot#mover) cũng không hoạt động ở chế độ khóa cửa sổ (theo help, mục Chuột).
- 🟠 **Điểm khác nhau khi so sánh giữa help và sách của Chô tô về trình duyệt và máy ảo:**
  - **Theo sách của Chô tô (tr. 19):** Xếp chung trình duyệt và máy ảo vào nhóm cửa sổ không nhận tool ở chế độ khóa cửa sổ.
  - **Theo help (bài Khóa cửa sổ và phần FAQ):** Giải thích rằng khả năng hoạt động ở chế độ khóa cửa sổ **tùy cách ứng dụng được viết** (ví dụ khung Flash trong trình duyệt là một phần tử con riêng, hoặc có trường hợp chạy được trên Firefox nhưng không chạy trên Google Chrome — theo help, phần FAQ).
  - **Giải pháp dùng máy ảo (theo help, bài Khóa cửa sổ):** Với máy ảo (như MS Virtual PC, VMware), help gợi ý đây là **giải pháp thay thế** khi chế độ khóa cửa sổ không dùng được: bạn cài hệ điều hành, ứng dụng và Clickermann **vào bên trong máy ảo**, cho chạy ở chế độ thường bên trong máy ảo rồi thu nhỏ cửa sổ máy ảo xuống để làm việc khác trên máy thật. Tuy nhiên, help lưu ý cách này đòi hỏi máy tính đủ mạnh để gánh hai hệ điều hành cùng ứng dụng, và một số ứng dụng chạy khá kém hoặc từ chối chạy trên máy ảo. Xem thêm tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#che-do-khoa-cua-so-voi-trinh-duyet-va-may-ao).
