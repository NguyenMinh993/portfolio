# Hướng Dẫn Deploy Portfolio (Không Dùng Docker)

## ✅ Đã Chuẩn Bị
- Bỏ Docker, dùng Python thuần
- Thêm WhiteNoise để serve static files
- Cấu hình Railway và Render

## 🚀 Cách 1: Deploy Trên Railway (Khuyên Dùng)

### Bước 1: Đăng Ký Railway
1. Vào: https://railway.app
2. Nhấn "Login" → Chọn "Login with GitHub"
3. Cho phép Railway truy cập GitHub

### Bước 2: Tạo Project Mới
1. Nhấn "New Project"
2. Chọn "Deploy from GitHub repo"
3. Chọn repository: **NguyenMinh993/portfolio**
4. Railway sẽ tự động build và deploy (2-3 phút)

### Bước 3: Thêm Biến Môi Trường
1. Nhấn vào service vừa tạo
2. Vào tab "Variables"
3. Thêm các biến sau:

```
DEBUG=False
SECRET_KEY=django-insecure-6n+$^sa+%qex3ye#35^1zjb11s$l(+^i9w7&-r84c28r_tk*7s
EMAIL_HOST_USER=nguyenminh090903@gmail.com
EMAIL_HOST_PASSWORD=vtgmfkpwmuthqinn
```

### Bước 4: Tạo Domain
1. Vào tab "Settings"
2. Tìm phần "Networking"
3. Nhấn "Generate Domain"
4. Copy URL (ví dụ: `portfolio-production-xxxx.up.railway.app`)

### Bước 5: Cập Nhật ALLOWED_HOSTS
1. Quay lại tab "Variables"
2. Thêm biến:
```
ALLOWED_HOSTS=portfolio-production-xxxx.up.railway.app
```
(Thay `portfolio-production-xxxx.up.railway.app` bằng domain thực của bạn)

### ✅ Xong! Website đã live!

---

## 🚀 Cách 2: Deploy Trên Render

### Bước 1: Đăng Ký Render
1. Vào: https://render.com
2. Nhấn "Get Started" → Đăng nhập bằng GitHub

### Bước 2: Tạo Web Service
1. Nhấn "New +" → Chọn "Web Service"
2. Chọn repository: **NguyenMinh993/portfolio**
3. Điền thông tin:
   - **Name**: portfolio
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python manage.py migrate && gunicorn --bind 0.0.0.0:$PORT --workers 3 DjangoProject.wsgi:application`

### Bước 3: Thêm Environment Variables
Trong phần "Environment Variables", thêm:
```
DEBUG=False
SECRET_KEY=django-insecure-6n+$^sa+%qex3ye#35^1zjb11s$l(+^i9w7&-r84c28r_tk*7s
EMAIL_HOST_USER=nguyenminh090903@gmail.com
EMAIL_HOST_PASSWORD=vtgmfkpwmuthqinn
ALLOWED_HOSTS=your-app-name.onrender.com
```

### Bước 4: Deploy
1. Nhấn "Create Web Service"
2. Đợi 5-10 phút để build
3. Website sẽ có URL: `your-app-name.onrender.com`

---

## 📝 Cập Nhật Website

Mỗi khi thay đổi code:
```bash
git add .
git commit -m "Mô tả thay đổi"
git push
```

Railway/Render sẽ tự động deploy lại!

---

## ❌ Khắc Phục Lỗi

### Lỗi: DisallowedHost
- Kiểm tra biến `ALLOWED_HOSTS` có đúng domain không
- Thêm domain của Railway/Render vào `ALLOWED_HOSTS`

### Lỗi: Static files không load
- WhiteNoise đã được cài đặt, sẽ tự động serve static files
- Chạy: `python manage.py collectstatic --noinput`

### Lỗi: Database
- Railway/Render dùng SQLite mặc định
- Nếu cần PostgreSQL, thêm database trong dashboard

---

## 💰 Chi Phí

### Railway
- $5 credit miễn phí mỗi tháng
- Sau đó: ~$5-10/tháng

### Render
- Free tier: 750 giờ/tháng (đủ cho 1 app)
- Paid: $7/tháng

---

## 🎯 Lưu Ý Quan Trọng

1. ✅ Đã bỏ Docker - dùng Python thuần
2. ✅ Đã thêm WhiteNoise - serve static files
3. ✅ Đã cấu hình Procfile và runtime.txt
4. ✅ Đã cập nhật settings.py cho production
5. ✅ Không cần cài Docker Desktop nữa!

---

## 📞 Cần Trợ Giúp?
- Railway Docs: https://docs.railway.app
- Render Docs: https://render.com/docs
