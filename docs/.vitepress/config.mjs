import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vitepress'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const cmsGrammar = JSON.parse(
  fs.readFileSync(path.resolve(__dirname, './cms.tmLanguage.json'), 'utf-8')
)

export default defineConfig({
  // Bản GitHub Pages nằm dưới /clickermann-guide-vi/, xem tools/deploy.sh
  base: process.env.VITEPRESS_BASE || '/',
  lang: 'vi-VN',
  title: 'Clickermann v4.13 Tiếng Việt',
  description: 'Tài liệu hướng dẫn Clickermann v4.13 bằng tiếng Việt cho người mới học',
  markdown: {
    anchor: {
      slugify: (str) =>
        str
          .normalize('NFKD')
          .replace(/[\u0300-\u036f]/g, '')
          .replace(/[đĐ]/g, 'd')
          .toLowerCase()
          .replace(/[^a-z0-9]+/g, '-')
          .replace(/^-+|-+$/g, '')
    },
    languages: [
      {
        ...cmsGrammar,
        name: 'cms',
        scopeName: 'source.cms',
        aliases: ['clickermann']
      }
    ]
  },
  themeConfig: {
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Tìm kiếm',
            buttonAriaLabel: 'Tìm kiếm'
          },
          modal: {
            displayDetails: 'Hiện chi tiết',
            resetButtonTitle: 'Xóa tìm kiếm',
            backButtonTitle: 'Đóng tìm kiếm',
            noResultsText: 'Không tìm thấy kết quả cho',
            footer: {
              selectText: 'để chọn',
              selectKeyAriaLabel: 'Enter',
              navigateText: 'để di chuyển',
              navigateUpKeyAriaLabel: 'Mũi tên lên',
              navigateDownKeyAriaLabel: 'Mũi tên xuống',
              closeText: 'để đóng',
              closeKeyAriaLabel: 'Escape'
            }
          }
        }
      }
    },
    nav: [
      { text: 'Bắt đầu', link: '/bat-dau/cai-dat' },
      { text: 'Khái niệm cơ bản', link: '/khai-niem/ngon-ngu' },
      { text: 'Cẩm nang', link: '/cam-nang/click-theo-lich' },
      { text: 'Xử lý lỗi', link: '/xu-ly-loi' },
      { text: 'Tra cứu lệnh', link: '/lenh/' },
      { text: 'Nâng cao', link: '/bat-dau/quan-ly-cua-so' },
      { text: 'Phụ lục', link: '/phu-luc/ma-phim' }
    ],
    sidebar: [
      {
        text: 'Giới thiệu',
        items: [
          { text: 'Tổng quan Clickermann', link: '/' }
        ]
      },
      {
        text: 'Bắt đầu',
        items: [
          { text: 'Cài đặt và chạy lần đầu', link: '/bat-dau/cai-dat' },
          { text: 'Màn hình chính', link: '/bat-dau/man-hinh-chinh' },
          { text: 'Trình soạn thảo và kính lúp', link: '/bat-dau/trinh-soan-thao' },
          { text: 'Viết script đầu tiên', link: '/bat-dau/script-dau-tien' }
        ]
      },
      {
        text: 'Khái niệm cơ bản',
        items: [
          { text: 'Ngôn ngữ script', link: '/khai-niem/ngon-ngu' },
          { text: 'Bộ đệm ảnh', link: '/khai-niem/bo-dem-anh' },
          { text: 'Hệ tọa độ', link: '/khai-niem/toa-do' },
          { text: 'Màu sắc và giảm màu', link: '/khai-niem/mau-sac' },
          { text: 'Chế độ khóa cửa sổ', link: '/khai-niem/khoa-cua-so' }
        ]
      },
      {
        text: 'Cẩm nang',
        items: [
          { text: 'Bấm chuột theo lịch', link: '/cam-nang/click-theo-lich' },
          { text: 'Tìm màu trên màn hình', link: '/cam-nang/tim-mau' },
          { text: 'Tìm hình ảnh mẫu', link: '/cam-nang/tim-anh' },
          { text: 'Đọc và ghi tệp tin', link: '/cam-nang/doc-ghi-file' },
          { text: 'Tự động vẽ trong Paint', link: '/cam-nang/tu-ve' }
        ]
      },
      {
        text: 'Xử lý lỗi',
        items: [
          { text: 'Xử lý lỗi thường gặp (FAQ)', link: '/xu-ly-loi' }
        ]
      },
      {
        text: 'Tra cứu lệnh',
        items: [
          { text: 'Tra cứu theo việc cần làm', link: '/lenh/' },
          { text: 'Số, biến và mảng', link: '/lenh/so' },
          { text: 'Chuỗi, tệp tin và HTTP', link: '/lenh/chuoi-file' },
          { text: 'Chuột', link: '/lenh/chuot' },
          { text: 'Bàn phím', link: '/lenh/ban-phim' },
          { text: 'Điều kiện, vòng lặp, chương trình con', link: '/lenh/cau-truc' },
          { text: 'Màn hình và màu sắc', link: '/lenh/man-hinh' },
          { text: 'Nhật ký và âm báo', link: '/lenh/nhat-ky' },
          { text: 'Điều khiển script và hệ thống', link: '/lenh/kich-ban' },
          { text: 'Cửa sổ và WinAPI', link: '/lenh/winapi' }
        ]
      },
      {
        text: 'Nâng cao',
        items: [
          { text: 'Quản lý cửa sổ', link: '/bat-dau/quan-ly-cua-so' },
          { text: 'Luồng (THREAD)', link: '/khai-niem/luong' },
          { text: 'Plugin mở rộng (DLL)', link: '/khai-niem/plugin' }
        ]
      },
      {
        text: 'Phụ lục',
        items: [
          { text: 'Bảng mã phím và hằng số', link: '/phu-luc/ma-phim' },
          { text: 'Lịch sử phiên bản', link: '/phu-luc/lich-su' },
          { text: 'Bảng thuật ngữ', link: '/phu-luc/thuat-ngu' },
          { text: 'Lệnh ẩn và chưa có tài liệu', link: '/phu-luc/lenh-an' },
          { text: 'Cần kiểm tra trên Windows', link: '/phu-luc/can-kiem-tra-tren-windows' },
          { text: 'Nguồn tài liệu và ghi công', link: '/phu-luc/nguon' }
        ]
      }
    ],
    outline: {
      label: 'Mục lục trang',
      level: [2, 3]
    },
    docFooter: {
      prev: 'Trang trước',
      next: 'Trang tiếp'
    },
    darkModeSwitchLabel: 'Giao diện',
    lightModeSwitchTitle: 'Chuyển sang giao diện sáng',
    darkModeSwitchTitle: 'Chuyển sang giao diện tối',
    sidebarMenuLabel: 'Danh mục',
    returnToTopLabel: 'Lên đầu trang'
  }
})
