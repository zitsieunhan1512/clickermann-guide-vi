# Clickermann v4.13 Tiếng Việt

Trang này giới thiệu tổng quan về Clickermann v4.13 chạy trên hệ điều hành **Windows**, cách chương trình hoạt động và danh mục toàn bộ các trang hướng dẫn trong bộ tài liệu. Đây là tài liệu cộng đồng dành cho người Việt mới học, không phải tài liệu chính thức của tác giả.

::: tip Lộ trình cho người mới
Mới bắt đầu? Đọc lần lượt [Cài đặt](/bat-dau/cai-dat) → [Màn hình chính](/bat-dau/man-hinh-chinh) → [Trình soạn thảo](/bat-dau/trinh-soan-thao) → [Viết script đầu tiên](/bat-dau/script-dau-tien), rồi chọn một trang trong mục Cẩm nang.
:::

::: warning Lưu ý kiểm chứng thực tế
Toàn bộ tài liệu chưa chạy thử trên Windows; nếu màn hình của bạn khác, hãy tin màn hình.
:::

## Clickermann là gì?

Clickermann là chương trình chạy trên **Windows**, giúp mô phỏng thao tác chuột và bàn phím của người dùng trên máy tính, đồng thời hỗ trợ nhiều tính năng xử lý khác. Chương trình hoạt động dựa trên các **script** (còn gọi là kịch bản hay macro) do người dùng tự gõ vào hoặc ghi lại trực tiếp trong lúc thao tác. Các script hoàn toàn mở để chỉnh sửa bằng bất kỳ trình soạn thảo văn bản nào, hoặc bằng chính trình soạn thảo được tối ưu riêng đi kèm trong Clickermann.

Chương trình được tạo ra để tự động hóa các thao tác lặp đi lặp lại đơn giản trên máy tính. Trong thực tế, chương trình có thể dùng cho nhiều công việc khác nhau, chẳng hạn như tự động sao chép dữ liệu từ các phần mềm chưa hỗ trợ sẵn tính năng xuất dữ liệu.

Trang chủ chính thức của tác giả J.Challenger: [http://crapware.aidf.org](http://crapware.aidf.org) (tài liệu này không đính kèm tệp `.exe`).

## Cách làm việc với chương trình

Chương trình thực hiện các thao tác dựa trên tập hợp lệnh trong script. Có hai cách để tạo một script:

1. **Tự viết script bằng tay:** Dựa vào tài liệu hướng dẫn và trình soạn thảo tích hợp. Cách này giúp tạo ra các script linh hoạt, tự kiểm tra điều kiện để xử lý từng tình huống, nhưng đòi hỏi người dùng nắm kiến thức cơ bản và tư duy logic.
2. **Dùng hệ thống ghi thao tác (Record):** Để chương trình tự viết script bằng cách ghi lại các hành động bạn vừa làm. Cách này giúp người dùng không phải gõ lệnh thủ công, nhưng kém linh hoạt hơn vì chỉ lặp lại đúng các thao tác đã ghi.

Tác giả khuyến nghị bạn nên tìm hiểu cách tự viết script bằng tay vì đây là chế độ làm việc chính của chương trình, còn chức năng ghi tự động là phần bổ trợ thêm.

## Ngôn ngữ script

Ngôn ngữ script của Clickermann được thiết kế đơn giản, chạy lần lượt từng dòng lệnh từ trên xuống dưới nên người mới chưa từng lập trình vẫn có thể làm quen nhanh chóng.

Dưới đây là ví dụ một script đơn giản bấm chuột trái một lần vào tọa độ `(100, 200)`, chờ 1 giây rồi dừng hẳn; nếu bỏ dòng `HALT` ở cuối thì sau khi chạy xong dòng cuối, script sẽ tự động quay lại dòng đầu tiên và lặp lại:

```cms
// Bấm chuột trái tại tọa độ X = 100, Y = 200
LCLICK(100, 200)

// Chờ 1 giây
WAIT(1)

// Dừng hẳn script (nếu bỏ dòng này thì script sẽ tự lặp lại từ đầu)
HALT
```

## Quy ước nhãn kiểm chứng

Mỗi lệnh và mục có điểm cần lưu ý trong tài liệu này được gắn nhãn hoặc tiền tố để bạn biết rõ nguồn gốc thông tin:

- `🟡 Theo help, chưa chạy thử` — Nội dung dịch và biên soạn sát theo tài liệu `help.chm` chính thức (v4.13.014), chưa chạy kiểm chứng thực tế trên máy Windows.
- `🟠 Chưa thống nhất` — Có điểm mâu thuẫn giữa các phần trong help, giữa help với tài liệu cộng đồng (sách của Chô tô), hoặc help không nêu rõ. Mỗi mục đều có dòng gợi ý **"Nên làm"** ngay đầu, phần so sánh chi tiết nằm trong khung thu gọn và có hướng dẫn kiểm tra tại trang [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows).
- **Suy luận:** — Nhận định suy ra từ ví dụ hoặc thông tin gián tiếp trong help khi lời giải thích của help không ghi thẳng.
- **Tham khảo:** — Ý bổ sung từ tài liệu cộng đồng tiếng Việt (sách của Chô tô) tại những chỗ help chính thức không nói rõ.

## Danh mục toàn bộ tài liệu

- **Bắt đầu:**
  - [Cài đặt và chạy lần đầu](/bat-dau/cai-dat)
  - [Màn hình chính](/bat-dau/man-hinh-chinh)
  - [Trình soạn thảo và kính lúp](/bat-dau/trinh-soan-thao)
  - [Viết script đầu tiên](/bat-dau/script-dau-tien)
- **Khái niệm cơ bản:**
  - [Ngôn ngữ script](/khai-niem/ngon-ngu)
  - [Bộ đệm ảnh](/khai-niem/bo-dem-anh)
  - [Hệ tọa độ màn hình và phần tử](/khai-niem/toa-do)
  - [Màu sắc và giảm màu (`COLORMODE`)](/khai-niem/mau-sac)
  - [Chế độ khóa cửa sổ](/khai-niem/khoa-cua-so)
- **Cẩm nang:**
  - [Bấm chuột theo lịch và chu kỳ](/cam-nang/click-theo-lich)
  - [Tìm màu trên màn hình rồi bấm chuột](/cam-nang/tim-mau)
  - [Tìm hình ảnh mẫu trên màn hình](/cam-nang/tim-anh)
  - [Đọc và ghi tệp `.txt` và `.ini`](/cam-nang/doc-ghi-file)
  - [Tự động vẽ hình trong Paint](/cam-nang/tu-ve)
- **Xử lý lỗi:**
  - [Xử lý lỗi và câu hỏi thường gặp (FAQ)](/xu-ly-loi)
- **Tra cứu lệnh:**
  - [Tổng quan tra cứu lệnh theo việc cần làm](/lenh/)
  - [Số, biến và mảng](/lenh/so)
  - [Chuỗi, tệp tin, bộ nhớ tạm và HTTP](/lenh/chuoi-file)
  - [Chuột](/lenh/chuot)
  - [Bàn phím](/lenh/ban-phim)
  - [Điều kiện, vòng lặp, chương trình con](/lenh/cau-truc)
  - [Màn hình và màu sắc](/lenh/man-hinh)
  - [Nhật ký và âm báo](/lenh/nhat-ky)
  - [Điều khiển script và hệ thống](/lenh/kich-ban)
  - [Cửa sổ và WinAPI](/lenh/winapi)
- **Nâng cao:**
  - [Quản lý cửa sổ](/bat-dau/quan-ly-cua-so)
  - [Luồng (`THREAD`)](/khai-niem/luong)
  - [Plugin mở rộng (DLL)](/khai-niem/plugin)
- **Phụ lục:**
  - [Bảng mã phím và hằng số](/phu-luc/ma-phim)
  - [Lịch sử phát triển phiên bản](/phu-luc/lich-su)
  - [Bảng thuật ngữ đối chiếu](/phu-luc/thuat-ngu)
  - [Lệnh ẩn và lệnh không có tài liệu](/phu-luc/lenh-an)
  - [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows)
  - [Nguồn tài liệu và ghi công](/phu-luc/nguon)
