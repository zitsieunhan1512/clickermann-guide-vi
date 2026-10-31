# Plugin mở rộng (DLL)

Trang này giải thích cơ chế hoạt động của plugin trong Clickermann, giao diện hàm C++ để tự viết một plugin DLL, cách gọi plugin bằng lệnh `CALL` và cảnh báo an toàn.

## Plugin trong Clickermann là gì?

**Plugin** là các mô-đun phần mềm độc lập bên ngoài nhưng có thể giao tiếp với Clickermann để mở rộng khả năng của chương trình.

Mỗi plugin là một tệp thư viện liên kết động chuẩn của Windows (**DLL**) xuất ra (export) một hàm duy nhất. Bên trong tệp DLL này, ngôn ngữ lập trình và môi trường phát triển dùng để viết DLL đều không quan trọng.

## Khuôn mẫu hàm xuất (Export Function) khi viết DLL

Bất kể bạn dùng trình biên dịch hay môi trường phát triển nào, tệp DLL của plugin chỉ cần xuất đúng một hàm theo chuẩn C++ như sau:

```cpp
int execute(int* _arr, int _size)
```

Trong đó:

- Tên hàm bắt buộc là `execute`, kiểu trả về là số nguyên `int`.
- Tham số thứ nhất `_arr`: con trỏ trỏ tới mảng các số nguyên được truyền từ Clickermann sang plugin.
- Tham số thứ hai `_size`: số lượng phần tử của mảng `_arr` (giúp code trong DLL biết giới hạn để không đọc tràn bộ nhớ).

Cách truyền qua mảng con trỏ này cho phép truyền số lượng tham số số nguyên gần như không giới hạn vào plugin.

## Cách gọi plugin từ script trong Clickermann

Trong script `.cms`, bạn gọi plugin thông qua thủ tục [`CALL`](/lenh/kich-ban#call):

```cms
CALL("plugin.dll", 1, 2, 3)
PRINT("Ket qua: ", $_return1)
HALT
```

Cơ chế thực thi khi gọi `CALL`:

1. Tham số đầu tiên bắt buộc là chuỗi tên tệp DLL của plugin (ví dụ `"plugin.dll"`), theo sau là danh sách các tham số số nguyên (`1, 2, 3`).
2. Trong lúc hàm `execute` bên trong plugin đang chạy, script của Clickermann sẽ **đứng chờ** cho đến khi hàm `execute` hoàn tất rồi mới chạy sang dòng lệnh tiếp theo.
3. Giá trị `int` mà hàm `execute` trả về sẽ được Clickermann ghi vào biến hệ thống **`$_return1`**.

## Điểm chưa thống nhất về thư mục đặt tệp DLL

- 🟠 **Vị trí đặt tệp DLL của plugin:**
  - **Nên làm:** Khi dùng lệnh `CALL("plugin.dll", ...)`, hãy đặt bản sao tệp `.dll` ở cả thư mục dự án (cùng chỗ với tệp `.cms`) và thư mục `%Clickermann%/plugins/`, hoặc kiểm tra xem vị trí nào trả về `$_return1` đúng trên máy bạn.
  ::: details Vì sao chưa chắc
  - **Theo help, bài Plugin:** Tệp DLL của plugin phải nằm trong **thư mục dự án**, đặt cạnh tệp script đang chạy hoặc trong thư mục con. Nếu không tìm thấy tệp DLL theo tên đã truyền ở đó, lệnh `CALL` sẽ âm thầm kết thúc.
  - **Theo sách của Chô tô (tr. 104):** Chỉ ghi rằng tệp DLL đặt cùng thư mục với tệp script.
  - **Theo help, mục Script và plugin (lệnh `CALL`):** Lại ghi rằng `filename` là đường dẫn tương đối tính từ thư mục **`%Clickermann%/plugins`**.
  - Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#thu-muc-nap-plugin-dll-cua-call).
  :::

## Cảnh báo an toàn khi dùng plugin

::: warning Cảnh báo từ tác giả Clickermann
Các tệp plugin `.dll` là những "hộp đen" chứa mã thực thi máy tính mà người dùng thông thường rất khó kiểm tra bên trong làm gì. Nếu bạn không phải là chuyên gia, **tuyệt đối không sử dụng các tệp plugin `.dll` tải từ những nguồn không đáng tin cậy**, vì chúng hoàn toàn có thể chứa mã độc gây hại cho máy tính của bạn.
:::

---

*Nguồn: Tài liệu trợ giúp `help.chm` (bài Plugin và mục Script và plugin); tham khảo đối chiếu sách của Chô tô (tr. 104).*
