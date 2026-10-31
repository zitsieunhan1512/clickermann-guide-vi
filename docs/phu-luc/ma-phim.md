# Bảng mã phím và hằng số

Trang này liệt kê bảng mã phím ảo (Virtual-Key Codes) của bàn phím tiêu chuẩn và các hằng số dựng sẵn trong tệp `data/const.txt` (theo help, phần Mã phím và tệp `data/const.txt`; cột **Mã hệ 16** được tài liệu tự quy đổi thêm từ mã thập phân trong help để tiện tra cứu).

Khi dùng các lệnh bàn phím như [`KEYPRESS`](/lenh/ban-phim#keypress), [`KEYDOWN`](/lenh/ban-phim#keydown), [`KEYUP`](/lenh/ban-phim#keyup) hoặc [`ISKEYDOWN`](/lenh/ban-phim#iskeydown), bạn có thể truyền **mã số thập phân**, **mã thập lục phân (`0x...`)** hoặc **tên hằng số (`#...`)**.

## Các hằng số đặc biệt

| Hằng số | Giá trị | Ý nghĩa |
|---|---|---|
| `#TRUE` | `1` | Giá trị logic Đúng |
| `#FALSE` | `0` | Giá trị logic Sai |
| `#NULL` | `-1` | Suy luận: giá trị rỗng / bỏ qua (tệp `data/const.txt` định nghĩa `#NULL -1`, Lịch sử phiên bản ghi nhận thêm hằng số `#null`) |
| `#NIL` | `-1` | Suy luận: tương đương `#NULL` (tệp `data/const.txt` định nghĩa `#NIL -1`) |

---

## Bảng mã phím chuột và phím điều khiển

| Phím / Nút bấm | Hằng số (`data/const.txt`) | Mã hệ 10 | Mã hệ 16 |
|---|---|---|---|
| Nút chuột trái | | `1` | `0x01` |
| Nút chuột phải | | `2` | `0x02` |
| Nút chuột giữa | | `4` | `0x04` |
| Backspace | `#BACKSPACE` | `8` | `0x08` |
| Tab | `#TAB` | `9` | `0x09` |
| Enter | `#ENTER` | `13` | `0x0D` |
| Shift | `#SHIFT` | `16` | `0x10` |
| Ctrl | `#CTRL` | `17` | `0x11` |
| Alt | `#ALT` | `18` | `0x12` |
| Pause | `#PAUSE` | `19` | `0x13` |
| CapsLock | `#CAPSLOCK` | `20` | `0x14` |
| Esc | `#ESC` | `27` | `0x1B` |
| Phím cách (Space) | `#SPACE` | `32` | `0x20` |
| PageUp | `#PAGEUP` | `33` | `0x21` |
| PageDown | `#PAGEDOWN` | `34` | `0x22` |
| End | `#END` | `35` | `0x23` |
| Home | `#HOME` | `36` | `0x24` |
| Mũi tên trái | `#LEFT` | `37` | `0x25` |
| Mũi tên lên | `#UP` | `38` | `0x26` |
| Mũi tên phải | `#RIGHT` | `39` | `0x27` |
| Mũi tên xuống | `#DOWN` | `40` | `0x28` |
| Insert | `#INSERT` | `45` | `0x2D` |
| Delete | `#DELETE` | `46` | `0x2E` |
| Phím Windows trái | `#WIN`, `#LWIN` | `91` | `0x5B` |
| Phím Windows phải | `#RWIN` | `92` | `0x5C` |
| Phím Applications (Menu) | | `93` | `0x5D` |
| NumLock | `#NUMLOCK` | `144` | `0x90` |
| ScrollLock | `#SCROLLLOCK` | `145` | `0x91` |
| PrintScreen | `#PRINTSCREEN` | 🟠 `154` | `0x9A` |
| Meta | | `157` | `0x9D` |

- 🟠 **Lưu ý về mã phím `PrintScreen` (`154`):**
  - **Nên làm:** Nếu dùng `#PRINTSCREEN` (`154`) mà không bắt được phím PrintScreen trên máy bạn, hãy thử truyền mã số **`44`** (`0x2C`).
  ::: details Vì sao chưa chắc
  Cả bảng phụ lục mã phím trong help lẫn tệp `data/const.txt` đều ghi `#PRINTSCREEN` là `154` (`0x9A`). Tuy nhiên, **Suy luận:** theo kiến thức Windows, mã phím ảo chuẩn (`VK_SNAPSHOT`) của phím PrintScreen trên Windows thường là `44` (`0x2C`). Bảng tự dò cũng ghi `44`, cột `KEYDOWN` ghi `90`, khớp quy luật (xem mục [Khi `KEYDOWN` cần mã khác](#khi-keydown-can-ma-khac)). Xem script kiểm chứng tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#ma-phim-printscreen-154-va-44).
  :::

---

## Khi `KEYDOWN` cần mã khác

**Trạng thái:** 🟠 Chưa thống nhất (xem kịch bản kiểm tra tại [Cần kiểm tra trên Windows](/phu-luc/can-kiem-tra-tren-windows#quy-luat-ma-keydown))

1. **Hiện tượng:** Theo bảng tự dò của Mai Bảo Long, có trường hợp [`KEYDOWN`](/lenh/ban-phim#keydown), [`KEYUP`](/lenh/ban-phim#keyup) phải dùng mã khác [`KEYPRESS`](/lenh/ban-phim#keypress) thì mới ra đúng phím. Ví dụ mũi tên trái: `KEYPRESS(37)` nhưng `KEYDOWN(75)`.
2. **Quy luật:**
   - **Suy luận:** Muốn ứng dụng nhận phím có mã `V`, gửi phím có **mã quét bằng `V`**.
   - **Kiến thức Windows:** Mỗi phím trên bàn phím có mã phím ảo (Virtual-Key Code) và mã quét (Scan Code) riêng; mã quét của phím `K` là `37`, nên `KEYDOWN(75)` ra phím mũi tên trái có mã `37`.
   - Ba ví dụ khác:
     - Mũi tên lên dùng mã `76` (vì mã quét của phím `L` là `38`, bằng mã thường của mũi tên lên).
     - Enter dùng mã `187` (vì mã quét của phím `=` là `13`, bằng mã thường của Enter).
     - Space dùng mã `68` (vì mã quét của phím `D` là `32`, bằng mã thường của Space).
3. **Mức bằng chứng:**
   - Trong bảng đo, `67/67` giá trị đối chiếu được đều khớp quy luật, không lệch giá trị nào. `18` giá trị khác không đối chiếu được vì nằm ngoài bảng mã quét đã dùng.
   - `35/38` phím bị bỏ trống đúng là các phím không có mã nào tạo ra theo quy luật. Ba phím trống còn lại là `Shift`, `Ctrl`, `Alt`.
   - Chưa rõ quy luật do Clickermann hay do ứng dụng đã đo, và xảy ra ở chế độ nào. Bảng mã quét dùng để đối chiếu dựa trên bàn phím US, không phải đo trong Clickermann.
4. **Nên làm:** Thử `KEYDOWN` với mã thường trước. Nếu ra sai phím, chạy [script dò mã phím](/cam-nang/thuc-chien#do-ma-phim) ở phần Cẩm nang, hoặc tra hai bảng dưới đây.

::: details Bảng đo được (Tự dò bởi Mai Bảo Long)
Nguồn: Tự dò bởi Mai Bảo Long tại [Tài liệu Clickermann by Mai Bảo Long](https://maibaolongne.blogspot.com/2024/09/tai-lieu-clickermann-by-mai-bao-long.html) (tác giả không ghi đo trên ứng dụng và chế độ nào).

| Phím | Mã thường (`KEYPRESS`) | `KEYDOWN`/`KEYUP` đo được | Mã khác đo được |
|---|---|---|---|
| A | `65` | `118` |  |
| B | `66` | `119` |  |
| C | `67` | `120` |  |
| D | `68` | `121` |  |
| E | `69` | `144` |  |
| F | `70` | `3` | `145` |
| G | `71` | `36` | `103` |
| H | `72` | `38` | `104` |
| I | `73` | `33` | `105` |
| J | `74` | `109` |  |
| K | `75` | `37` | `100` |
| L | `76` | `12` | `101` |
| M | `77` | `39` | `102` |
| N | `78` | `107` |  |
| O | `79` | `35` | `97` |
| P | `80` | `40` | `98` |
| Q | `81` | `34` | `99` |
| R | `82` | `45` | `96` |
| S | `83` | `46` | `110` |
| T | `84` | `44` |  |
| V | `86` | `226` |  |
| W | `87` | `122` |  |
| X | `88` | `123` |  |
| Z | `90` | `238` |  |
| 1 | `49` | `78` |  |
| 2 | `50` | `77` | `172` |
| 3 | `51` | `188` |  |
| 4 | `52` | `190` |  |
| 5 | `53` | `111` | `191` |
| 6 | `54` | `161` |  |
| 7 | `55` | `106` |  |
| 8 | `56` | `18` | `164` |
| 9 | `57` | `32` |  |
| 0 | `48` | `66` | `175` |
| Tab | `9` | `56` |  |
| Space | `32` | `68` | `173` |
| Enter | `13` | `187` |  |
| Backspace | `8` | `55` |  |
| Caps Lock | `20` | `84` |  |
| Escape | `27` | `221` |  |
| F2 | `113` | `233` |  |
| F4 | `115` | `193` |  |
| F7 | `118` | `135` |  |
| F12 | `123` | `235` |  |
| Insert | `45` | `88` |  |
| Delete | `46` | `67` | `174` |
| Home | `36` | `74` | `178` |
| End | `35` | `72` |  |
| Page Up | `33` | `70` | `183` |
| Page Down | `34` | `71` | `179` |
| Arrow Up | `38` | `76` |  |
| Arrow Down | `40` | `222` |  |
| Arrow Left | `37` | `75` |  |
| Arrow Right | `39` | `186` |  |
| Pause break | `19` | `82` |  |
| PrtScr | `44` | `90` |  |
| ; : | `59` | `112` |  |
| =+ | `61` | `114` |  |
| menu | `93` | `93` | `249` |
| Numpad . | `110` | `134` |  |

**Ghi chú về bảng tự dò trên blog:**
- Bảng trên không đưa vào 3 dòng click chuột của blog vì blog ghi nút chuột trái, giữa, phải lần lượt là `0`, `1`, `2`, trong khi help chính thức ghi là `1`, `4`, `2`.
- Ở cột mã thường (`KEYPRESS`) trên blog, 3 phím `; :`, `=+` và `-_` được ghi thêm các mã `59`, `61`, `173` (khác với mã Windows trong help là `186`, `187`, `189`; chưa rõ nguyên nhân của sự khác biệt này).
:::

**Bảng tính theo quy luật, chưa đo (`Shift`, `Ctrl`, `Alt`):**

| Phím | Mã thường | Mã tính theo quy luật |
|---|---|---|
| Shift | `16` | `81` |
| Ctrl | `17` | `87` |
| Alt | `18` | `69` |

::: warning Cảnh báo khi thử mã của Shift, Ctrl, Alt
Dùng `KEYDOWN` với các mã `81`, `87`, `69` trên có thể làm hệ thống giữ phím `Shift`, `Ctrl`, `Alt` nếu quy luật đúng, nên luôn phải gọi lệnh `KEYUP` tương ứng ngay sau đó.
:::

---

## Bảng mã phím chữ số (`0..9`) và chữ cái (`A..Z`)

| Phím | Hằng số (`data/const.txt`) | Mã hệ 10 | Mã hệ 16 |
|---|---|---|---|
| `0` | `#0` | `48` | `0x30` |
| `1` | `#1` | `49` | `0x31` |
| `2` | `#2` | `50` | `0x32` |
| `3` | `#3` | `51` | `0x33` |
| `4` | `#4` | `52` | `0x34` |
| `5` | `#5` | `53` | `0x35` |
| `6` | `#6` | `54` | `0x36` |
| `7` | `#7` | `55` | `0x37` |
| `8` | `#8` | `56` | `0x38` |
| `9` | `#9` | `57` | `0x39` |
| `A` | `#A` | `65` | `0x41` |
| `B` | `#B` | `66` | `0x42` |
| `C` | `#C` | `67` | `0x43` |
| `D` | `#D` | `68` | `0x44` |
| `E` | `#E` | `69` | `0x45` |
| `F` | `#F` | `70` | `0x46` |
| `G` | `#G` | `71` | `0x47` |
| `H` | `#H` | `72` | `0x48` |
| `I` | `#I` | `73` | `0x49` |
| `J` | `#J` | `74` | `0x4A` |
| `K` | `#K` | `75` | `0x4B` |
| `L` | `#L` | `76` | `0x4C` |
| `M` | `#M` | `77` | `0x4D` |
| `N` | `#N` | `78` | `0x4E` |
| `O` | `#O` | `79` | `0x4F` |
| `P` | `#P` | `80` | `0x50` |
| `Q` | `#Q` | `81` | `0x51` |
| `R` | `#R` | `82` | `0x52` |
| `S` | `#S` | `83` | `0x53` |
| `T` | `#T` | `84` | `0x54` |
| `U` | `#U` | `85` | `0x55` |
| `V` | `#V` | `86` | `0x56` |
| `W` | `#W` | `87` | `0x57` |
| `X` | `#X` | `88` | `0x58` |
| `Y` | `#Y` | `89` | `0x59` |
| `Z` | `#Z` | `90` | `0x5A` |

---

## Bảng mã cụm phím số (NumPad), phím chức năng (`F1..F12`) và dấu câu

| Phím | Hằng số (`data/const.txt`) | Mã hệ 10 | Mã hệ 16 |
|---|---|---|---|
| NumPad `0` | | `96` | `0x60` |
| NumPad `1` | | `97` | `0x61` |
| NumPad `2` | | `98` | `0x62` |
| NumPad `3` | | `99` | `0x63` |
| NumPad `4` | | `100` | `0x64` |
| NumPad `5` | | `101` | `0x65` |
| NumPad `6` | | `102` | `0x66` |
| NumPad `7` | | `103` | `0x67` |
| NumPad `8` | | `104` | `0x68` |
| NumPad `9` | | `105` | `0x69` |
| NumPad `*` | | `106` | `0x6A` |
| NumPad `+` | | `107` | `0x6B` |
| NumPad `-` | | `109` | `0x6D` |
| NumPad `.` | | `110` | `0x6E` |
| NumPad `/` | | `111` | `0x6F` |
| `F1` | `#F1` | `112` | `0x70` |
| `F2` | `#F2` | `113` | `0x71` |
| `F3` | `#F3` | `114` | `0x72` |
| `F4` | `#F4` | `115` | `0x73` |
| `F5` | `#F5` | `116` | `0x74` |
| `F6` | `#F6` | `117` | `0x75` |
| `F7` | `#F7` | `118` | `0x76` |
| `F8` | `#F8` | `119` | `0x77` |
| `F9` | `#F9` | `120` | `0x78` |
| `F10` | `#F10` | `121` | `0x79` |
| `F11` | `#F11` | `122` | `0x7A` |
| `F12` | `#F12` | `123` | `0x7B` |
| `;` | | `186` | `0xBA` |
| `=` | | `187` | `0xBB` |
| `,` | | `188` | `0xBC` |
| `-` | | `189` | `0xBD` |
| `.` | | `190` | `0xBE` |
| `/` | | `191` | `0xBF` |
| `~` | | `192` | `0xC0` |
| `[` | | `219` | `0xDB` |
| `\` | | `220` | `0xDC` |
| `]` | | `221` | `0xDD` |
| `'` | | `222` | `0xDE` |
