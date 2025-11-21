# Hướng dẫn Setup SendGrid API Key

## Bước 1: Tạo SendGrid API Key

1. Đăng nhập vào SendGrid: https://app.sendgrid.com
2. Vào **Settings** → **API Keys**
3. Click **Create API Key**
4. Chọn tên: `Portfolio Contact Form`
5. Chọn **Full Access** hoặc **Restricted Access** với quyền:
   - Mail Send: Full Access
6. Click **Create & View**
7. **QUAN TRỌNG**: Copy API key ngay (chỉ hiển thị 1 lần)
   - Format: `SG.xxxxxxxxxxxxxxxxxx.yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy`

## Bước 2: Thêm vào Railway Environment Variables

1. Vào Railway Dashboard: https://railway.app
2. Chọn project `portfolio`
3. Vào tab **Variables**
4. Click **New Variable**
5. Thêm:
   ```
   Key: SENDGRID_API_KEY
   Value: SG.xxxxxxxxxxxxxxxxxx.yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
   ```
6. Click **Add**
7. Railway sẽ tự động redeploy

## Bước 3: Test Email

Sau khi Railway redeploy xong:
1. Vào trang contact form
2. Điền email và message
3. Click Send
4. Kiểm tra email `nguyenminh090903@gmail.com`

## Troubleshooting

### Nếu vẫn lỗi "Email Error":

1. **Check Railway logs**:
   - Vào Railway Dashboard → Deployments → View Logs
   - Tìm error message

2. **Verify SendGrid API Key**:
   - Vào SendGrid → Settings → API Keys
   - Đảm bảo key có status "Active"
   - Đảm bảo có quyền "Mail Send"

3. **Check SendGrid Activity**:
   - Vào SendGrid → Activity
   - Xem có request nào không

### Nếu email vào Spam:

Xem file `SENDGRID_ANTI_SPAM_SETUP.md` để cấu hình:
- Domain Authentication
- Single Sender Verification
- Link Branding

## Lưu ý

- SendGrid Free plan: 100 emails/day
- API key chỉ hiển thị 1 lần khi tạo
- Nếu mất key, phải tạo key mới
- Không commit API key vào Git (đã có trong .gitignore)

## Alternative: Dùng Gmail SMTP

Nếu không muốn dùng SendGrid, có thể dùng Gmail SMTP:
1. Xóa dòng `SENDGRID_API_KEY` trong Railway Variables
2. Code sẽ tự động fallback về Gmail
3. Nhưng Gmail có giới hạn 500 emails/day và dễ bị spam filter hơn
