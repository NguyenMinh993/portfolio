# Fix Azure Login Error

## Lỗi Gặp Phải
```
Selected user account does not exist in tenant 'Microsoft Services' 
and cannot access the application...
```

## Nguyên Nhân
- Tài khoản Microsoft cá nhân chưa có Azure subscription
- Hoặc đang dùng tài khoản work/school không có quyền

## 🔧 Giải Pháp

### Option 1: Tạo Azure Free Account Mới ⭐ (Khuyến nghị nếu muốn dùng Azure)

1. **Đăng xuất** tất cả tài khoản Microsoft
2. Mở **Incognito/Private window**
3. Truy cập: https://azure.microsoft.com/free/
4. Click **"Start free"**
5. Chọn **"Create a new Microsoft account"**
6. Dùng email mới (Gmail, Yahoo, v.v.)
7. Điền thông tin:
   - Số điện thoại (verify)
   - Thẻ tín dụng/debit (không charge, chỉ verify)
8. Complete setup
9. Vào Azure Portal: https://portal.azure.com

### Option 2: Dùng Cloudinary ⭐⭐ (Khuyến nghị nhất - Dễ hơn)

**Tại sao nên dùng Cloudinary?**
- ✅ Không cần thẻ tín dụng
- ✅ Setup 5 phút
- ✅ Free tier tốt hơn (25GB vs 5GB)
- ✅ Tự động optimize ảnh
- ✅ CDN built-in

**Setup Cloudinary:**

1. **Đăng ký**: https://cloudinary.com/users/register/free
   - Email
   - Password
   - Cloud name: `portfolio-minh` (hoặc tên bạn thích)

2. **Lấy credentials**:
   - Dashboard → Settings
   - Copy: Cloud Name, API Key, API Secret

3. **Update code** (đã có sẵn):
   ```python
   # Trong forms.py, thay đổi import:
   from .cloudinary_storage import get_cloudinary_storage
   
   # Thay vì:
   # from .azure_storage import get_azure_storage
   ```

4. **Set environment variables**:
   ```env
   CLOUDINARY_CLOUD_NAME=portfolio-minh
   CLOUDINARY_API_KEY=123456789012345
   CLOUDINARY_API_SECRET=your-secret
   ```

5. **Deploy**:
   ```bash
   git add .
   git commit -m "Use Cloudinary instead of Azure"
   git push origin main
   ```

### Option 3: Dùng Tài Khoản Azure Hiện Tại

Nếu đã có tài khoản Azure:

1. Đăng nhập: https://portal.azure.com
2. Nếu lỗi, click **"Use another account"**
3. Chọn tài khoản có Azure subscription
4. Hoặc tạo subscription mới trong account hiện tại

## 📊 So Sánh

| Feature | Azure Blob | Cloudinary |
|---------|-----------|------------|
| **Free Storage** | 5GB | 25GB |
| **Free Bandwidth** | 20K ops | 25GB/month |
| **Setup Time** | 15-30 phút | 5 phút |
| **Credit Card** | ✅ Cần | ❌ Không cần |
| **Auto Optimize** | ❌ | ✅ |
| **CDN** | Cần setup | Built-in |
| **Difficulty** | 🔴 Khó | 🟢 Dễ |

## 💡 Khuyến Nghị

**Dùng Cloudinary** vì:
1. Không cần thẻ tín dụng
2. Setup nhanh hơn
3. Free tier tốt hơn
4. Tự động optimize ảnh
5. Phù hợp cho portfolio

**Dùng Azure** nếu:
1. Đã có tài khoản Azure
2. Muốn học Azure services
3. Có kế hoạch scale lớn

## 🚀 Quick Start với Cloudinary

```bash
# 1. Đăng ký Cloudinary (5 phút)
https://cloudinary.com/users/register/free

# 2. Update forms.py
# Thay đổi dòng import từ azure_storage sang cloudinary_storage

# 3. Set env variables trên Railway
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# 4. Deploy
git add .
git commit -m "Switch to Cloudinary"
git push origin main
```

## ❓ Cần Giúp?

Nếu vẫn gặp vấn đề:
1. Check file `CLOUDINARY_SETUP.md` để setup chi tiết
2. Check file `AZURE_SETUP.md` nếu muốn dùng Azure
3. Hoặc hỏi tôi!
