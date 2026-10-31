# Quy tắc viết Clickermann Guide tiếng Việt

Tài liệu dành cho người Việt mới học Clickermann v4.13. Đây là tài liệu cộng đồng, không phải tài liệu chính thức.

## Thứ tự nguồn

1. **Chính:** `sources/help-text/*.txt` (help chính thức, tiếng Nga). Khi text lạ hoặc thiếu, đọc trang gốc trong `sources/help-html/` (mã hóa cp1251).
2. **Chỉ để làm rõ chỗ help không rõ:** `sources/choto-guidebook.txt` (sách của Chô tô, công khai cho cộng đồng tham khảo). Không chép câu chữ hay ví dụ của sách, phải tự viết lại. Khi dùng một ý từ sách, ghi nguồn: `Tham khảo: sách của Chô tô, tr. N`.
3. **Mâu thuẫn đã biết:** `sources/doi-chieu.html`, bảng 1. Mỗi điểm trong bảng phải được ghi rõ trong trang của lệnh đó.
4. **Mẫu:** `sources/samples/*.cms`, `sources/const.txt`, `sources/keywords.txt`.

Không thêm cơ chế, nguyên nhân, giá trị mặc định, đuôi file hay giới hạn mà help không nói. Nếu cần suy luận, ghi rõ "Suy luận:" và nêu cơ sở. Một ví dụ trong help không phải là quy tắc chung: viết "Ví dụ của help cho kết quả...", không khái quát thành luật. Mỗi ý trích nguồn chỉ gán cho đúng nguồn có ý đó.

Thứ gì help không nói thì viết "Help không nói rõ", không đoán. Không dùng kiến thức bên ngoài để khẳng định hành vi của Clickermann. Riêng kiến thức Windows chung (HWND, mã thông điệp) được phép dùng nếu ghi rõ đó là kiến thức Windows.

## Không được đưa vào

- **PS/2:** không dịch `ps2.txt`. Chỉ ghi: "Clickermann có chỉ thị `#ps2_mouse`, `#ps2_keyboard` (chế độ PS/2). Tài liệu này không hướng dẫn phần đó."
- **FAQ:** bỏ các đoạn về GameGuard, Frost, diễn đàn cheat, đổi tên hoặc giấu tool để tránh bị phát hiện.
- **`READMEM`, `WRITEMEM`:** chỉ ghi cú pháp, tham số và ý nghĩa. Không có ví dụ đọc/ghi bộ nhớ của game hay chương trình khác.
- **Game:** không có ví dụ về Gunny hay game online. Không dùng nội dung mục 12.4–12.6 của sách Chô tô. Ví dụ dùng Notepad, Paint hoặc việc văn phòng.
- **File `.exe`:** không đính kèm. Chỉ dẫn link site chính thức `http://crapware.aidf.org`.
- **Comment HTML trong help:** `NUM`, `STR`, `ADDR`, `FROMADDR`, `TOADDR`, `LOAD` đang bị ẩn trong help. Không viết trang riêng, chỉ liệt kê ở `phu-luc/lenh-an.md` với ghi chú "bị ẩn trong help, chưa rõ còn chạy không".

## Trạng thái kiểm chứng

Mỗi lệnh và mỗi ví dụ dài có đúng một nhãn. **Chưa có máy Windows nên không được dùng nhãn xanh.**

- `🟡 Theo help, chưa chạy thử` (mặc định)
- `🟠 Chưa thống nhất` khi help tự mâu thuẫn, help khác sách Chô tô hoặc help không nói rõ. Phải nêu cả hai cách hiểu.
- `🟢 Đã chạy thử` chỉ dùng sau này.

Mọi điểm 🟠 và mọi ví dụ cần chạy thử được ghi thêm vào `docs/phu-luc/can-kiem-tra-tren-windows.md`, kèm đoạn script để kiểm tra.

## Khuôn trang lệnh

Mỗi lệnh là một mục `##` trong trang nhóm lệnh, theo đúng thứ tự:

````markdown
## SETTHREAD

Đổi trạng thái của một luồng. <!-- một câu: nó làm gì -->

**Loại:** thủ tục · **Trạng thái:** 🟡 Theo help, chưa chạy thử

```cms
SETTHREAD (thread_name, state)
```

| Tham số | Kiểu | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|---|
| `thread_name` | tên | có | | Tên luồng |

**Trả về:** ... <!-- bỏ dòng này nếu là thủ tục -->

**Ví dụ**

```cms
// comment tiếng Việt
```

**Lưu ý** <!-- chỉ khi có điều cần nói -->

- ...
````

- Giữ nguyên tên lệnh, tham số và cú pháp theo help, không sửa theo sách Chô tô.
- Loại lệnh ghi đúng theo help: `Функция` là hàm; còn lại là thủ tục hoặc cấu trúc lệnh.
- Tiêu đề mục bằng chữ HOA đúng tên lệnh. Lệnh gộp theo help thì giữ gộp, ví dụ `## RCLICK, RDOWN, RUP`.

## Tiêu đề và link

- Tiêu đề không bắt đầu bằng số (VitePress đổi slug, làm hỏng link neo). Viết `## Trạng thái mặc định của THREAD`, không viết `## 1. Trạng thái...`.
- Sau mỗi đợt phải chạy, và cả ba đều phải qua:
  - `npm run build`
  - `python3 -I tools/check_docs.py .`
  - `python3 -I tools/check_anchors.py docs/.vitepress/dist`
- Không sửa hai file kiểm tra trong `tools/`. Nếu tin kiểm tra sai, ghi vào báo cáo và để nguyên.

## Văn phong

- Viết tiếng Việt tự nhiên, câu ngắn, cho người chưa biết lập trình. Dịch theo ý, không dịch từng chữ; giữ hết thông tin kỹ thuật trong help.
- Bỏ câu đùa và lời chửi thề trong help.
- Mỗi trang bắt đầu bằng 1–2 câu nói trang này giúp làm được gì.
- Không có chữ Nga trong `docs/`. Comment và chuỗi trong code đều bằng tiếng Việt không dấu hoặc có dấu UTF-8.

## Thuật ngữ cố định

| Gốc | Dùng |
|---|---|
| сценарий / script | script |
| буфер анализа | bộ đệm ảnh |
| привязка к окну, оконный режим | khóa cửa sổ, chế độ khóa cửa sổ |
| рабочий элемент | phần tử đang khóa |
| окно-элемент, дочернее окно | phần tử con |
| поток | luồng |
| процедура / функция | thủ tục / hàm |
| подпрограмма | chương trình con (`SUB`) |
| массив | mảng |
| директива | chỉ thị |
| цветокоррекция | giảm màu |
| лупа | kính lúp |
| горячая клавиша | phím tắt |
| file | tệp |
| лог | nhật ký |
| кликер | Clickermann (không viết "tool") |
| панель задач | thanh tác vụ |
| đỏ, xanh lá, xanh dương | không viết "lục", "lam" |

## Code ví dụ

- Dùng fence ` ```cms `. Chỉ dùng lệnh có trong help đang hiển thị.
- Không tự chế tham số. Ví dụ trong help thì giữ logic, đổi tên và thông báo sang tiếng Việt.
- Ví dụ phải đóng đủ `END_IF`, `END_CYC`, `END_SUB`, `END_THREAD`, `END_SWITCH`.
- Script tự lặp lại từ đầu sau dòng cuối (theo help). Ví dụ chỉ chạy một lần phải kết thúc bằng `HALT`.

## Ảnh và sơ đồ

- Sơ đồ là file SVG tự viết trong `docs/public/so-do/`, chữ tiếng Việt, có nền trắng riêng để đọc được ở cả giao diện sáng và tối. Không lấy ảnh ngoài.
- Sơ đồ phải vẽ đúng điều help nói. Không vẽ cơ chế bên trong mà help không mô tả.
- Chỗ cần ảnh chụp giao diện, dùng đúng khối này:

```markdown
::: info Ảnh sẽ bổ sung
Ảnh chụp: <mô tả cần chụp>. Cần máy Windows.
:::
```

## Cấu trúc thư mục `docs/`

```text
index.md
bat-dau/        cai-dat.md, script-dau-tien.md, man-hinh-chinh.md, trinh-soan-thao.md, quan-ly-cua-so.md
khai-niem/      ngon-ngu.md, bo-dem-anh.md, toa-do.md, mau-sac.md, khoa-cua-so.md, luong.md, plugin.md
lenh/           index.md, so.md, chuoi-file.md, chuot.md, ban-phim.md, cau-truc.md, man-hinh.md, nhat-ky.md, kich-ban.md, winapi.md
cam-nang/       click-theo-lich.md, tim-mau.md, tim-anh.md, doc-ghi-file.md, tu-ve.md
xu-ly-loi.md
phu-luc/        ma-phim.md, lich-su.md, thuat-ngu.md, lenh-an.md, can-kiem-tra-tren-windows.md, nguon.md
public/so-do/
```

`phu-luc/nguon.md` ghi: tài liệu dựa trên help chính thức của Clickermann (tác giả J.Challenger), tham khảo sách của Chô tô, kèm link; đây là tài liệu cộng đồng, miễn phí, không bán.
