# Bảng mã phím và hằng số

Trang này liệt kê bảng mã phím ảo (Virtual-Key Codes) của bàn phím tiêu chuẩn và các hằng số dựng sẵn trong file hằng trong thư mục `data` của tool (theo help, phần Mã phím và file hằng trong thư mục `data` của tool; cột **Mã hệ 16** được tài liệu tự quy đổi thêm từ mã thập phân trong help, phần Mã phím để tiện tra cứu).

Khi dùng các lệnh bàn phím như [`KEYPRESS`](/lenh/ban-phim#keypress), [`KEYDOWN`](/lenh/ban-phim#keydown), [`KEYUP`](/lenh/ban-phim#keyup) hoặc [`ISKEYDOWN`](/lenh/ban-phim#iskeydown), bạn có thể truyền **mã số thập phân**, **mã thập lục phân (`0x...`)** hoặc **tên hằng số (`#...`)**.

## Các hằng số đặc biệt

| Hằng số | Giá trị | Ý nghĩa |
|---|---|---|
| `#TRUE` | `1` | Giá trị logic Đúng |
| `#FALSE` | `0` | Giá trị logic Sai |
| `#NULL` | `-1` | Suy luận: giá trị rỗng / bỏ qua (file hằng trong thư mục `data` của tool định nghĩa `#NULL -1`, help, Lịch sử phiên bản ghi nhận thêm hằng số `#null`) |
| `#NIL` | `-1` | Suy luận: tương đương `#NULL` (file hằng trong thư mục `data` của tool định nghĩa `#NIL -1`) |

---

## Bảng mã phím chuột và phím điều khiển

| Phím / Nút bấm | Hằng số (file hằng trong `data`) | Mã hệ 10 | Mã hệ 16 |
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
| PrintScreen | `#PRINTSCREEN` | `154` | `0x9A` |
| Meta | | `157` | `0x9D` |

---

## Bảng mã phím chữ số (`0..9`) và chữ cái (`A..Z`)

| Phím | Hằng số (file hằng trong `data`) | Mã hệ 10 | Mã hệ 16 |
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

| Phím | Hằng số (file hằng trong `data`) | Mã hệ 10 | Mã hệ 16 |
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
