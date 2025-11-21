# SendGrid Anti-Spam Configuration Guide

## Các thay đổi đã thực hiện trong code:

### 1. ✅ Thêm Plain Text Version
- Email có cả HTML và plain text version
- Giúp email clients không hỗ trợ HTML vẫn đọc được
- Tăng deliverability score

### 2. ✅ Cải thiện From Email
- Sử dụng domain của website: `noreply@nguyenminh993.up.railway.app`
- Thêm display name: "Portfolio Contact Form"
- Tránh sử dụng Gmail làm sender

### 3. ✅ Thêm Reply-To Header
- Set reply-to = email của người gửi
- Khi reply, email sẽ gửi trực tiếp cho người liên hệ

### 4. ✅ Thêm Categories và Custom Args
- Giúp tracking và phân loại email
- SendGrid sử dụng để cải thiện reputation

## Các bước cấu hình trên SendGrid Dashboard:

### Bước 1: Domain Authentication (QUAN TRỌNG NHẤT)
1. Đăng nhập SendGrid: https://app.sendgrid.com
2. Vào **Settings** → **Sender Authentication**
3. Click **Authenticate Your Domain**
4. Chọn DNS host của bạn (Railway/Cloudflare/etc.)
5. Thêm các DNS records vào domain:
   - CNAME records cho DKIM
   - TXT record cho SPF
   - CNAME cho domain verification

**Lưu ý:** Nếu không có custom domain, có thể dùng subdomain của Railway

### Bước 2: Single Sender Verification
1. Vào **Settings** → **Sender Authentication**
2. Click **Verify a Single Sender**
3. Nhập email: `nguyenminh090903@gmail.com`
4. Điền thông tin:
   - From Name: Nguyen Van Minh
   - From Email: nguyenminh090903@gmail.com
   - Reply To: nguyenminh090903@gmail.com
   - Company: Portfolio
5. Xác nhận email verification

### Bước 3: Enable Link Branding
1. Vào **Settings** → **Sender Authentication**
2. Click **Brand Links**
3. Setup link branding để tránh suspicious links

### Bước 4: Cấu hình Suppression Management
1. Vào **Suppressions** → **Global Suppressions**
2. Đảm bảo không có email của bạn trong danh sách
3. Check **Bounces**, **Spam Reports**, **Invalid Emails**

### Bước 5: Warm Up IP (Nếu dùng Dedicated IP)
- Với Free plan, SendGrid dùng shared IP đã warm
- Nếu upgrade, cần warm up IP từ từ

## Best Practices để tránh Spam:

### 1. Email Content
- ✅ Có cả HTML và plain text
- ✅ Tránh từ ngữ spam: "FREE", "CLICK HERE", "ACT NOW"
- ✅ Tỷ lệ text/image cân đối
- ✅ Không dùng quá nhiều link
- ✅ Không dùng ALL CAPS trong subject

### 2. Technical Setup
- ✅ SPF record configured
- ✅ DKIM signature enabled
- ✅ DMARC policy set
- ✅ Valid reverse DNS
- ✅ Consistent From address

### 3. Sending Behavior
- ✅ Không gửi quá nhiều email cùng lúc
- ✅ Monitor bounce rate (< 5%)
- ✅ Monitor spam complaint rate (< 0.1%)
- ✅ Có unsubscribe link (nếu là marketing email)

### 4. Reputation Management
- ✅ Maintain good sender reputation
- ✅ Monitor SendGrid statistics
- ✅ Handle bounces properly
- ✅ Remove invalid emails

## Kiểm tra Email Deliverability:

### Tools để test:
1. **Mail-Tester**: https://www.mail-tester.com
   - Gửi test email đến địa chỉ họ cung cấp
   - Nhận điểm từ 0-10 (cần > 8)

2. **GlockApps**: https://glockapps.com
   - Test inbox placement
   - Check spam score

3. **SendGrid Email Activity**
   - Vào **Activity** → **Email Activity**
   - Monitor delivery status

## Troubleshooting:

### Nếu email vẫn vào spam:

1. **Check SendGrid Statistics**
   ```
   Settings → Statistics → Overview
   - Delivery rate should be > 95%
   - Bounce rate should be < 5%
   - Spam report rate should be < 0.1%
   ```

2. **Verify Domain Authentication**
   ```
   Settings → Sender Authentication
   - Domain should show "Verified" with green checkmark
   ```

3. **Check Email Content**
   - Remove suspicious links
   - Reduce image size
   - Add more text content
   - Remove spam trigger words

4. **Whitelist Email**
   - Tạm thời: Add sender to Gmail contacts
   - Mark as "Not Spam" trong Gmail
   - Create filter to never send to spam

## Environment Variables cần thiết:

```bash
SENDGRID_API_KEY=SG.xxxxxxxxxxxxx
FROM_EMAIL=noreply@nguyenminh993.up.railway.app
```

## Monitoring:

### Daily checks:
- SendGrid dashboard statistics
- Bounce rate
- Spam complaint rate
- Delivery rate

### Weekly checks:
- Sender reputation score
- Domain authentication status
- Suppression list

## Notes:

- Domain authentication là yếu tố QUAN TRỌNG NHẤT
- Nếu không có custom domain, sender reputation sẽ thấp hơn
- Free SendGrid plan có giới hạn 100 emails/day
- Cần thời gian để build sender reputation (1-2 tuần)

## Contact SendGrid Support:

Nếu vẫn gặp vấn đề:
- Email: support@sendgrid.com
- Docs: https://docs.sendgrid.com
- Community: https://community.sendgrid.com
