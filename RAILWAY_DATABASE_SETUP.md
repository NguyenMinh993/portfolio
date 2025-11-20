# 🚂 Hướng Dẫn Setup Database & Cloudinary trên Railway

## 📋 Tổng Quan

Bạn cần setup:
1. ✅ PostgreSQL Database
2. ✅ Cloudinary Credentials
3. ✅ Environment Variables
4. ✅ Run Migrations
5. ✅ Create Superuser

---

## 🗄️ BƯỚC 1: Setup PostgreSQL Database

### 1.1. Vào Railway Dashboard
- Truy cập: https://railway.app
- Login và chọn project portfolio của bạn

### 1.2. Thêm PostgreSQL Database
1. Click nút **"+ New"** (góc trên phải)
2. Chọn **"Database"**
3. Chọn **"Add PostgreSQL"**
4. Railway sẽ tự động:
   - Tạo PostgreSQL instance
   - Generate `DATABASE_URL`
   - Link với Django service của bạn

### 1.3. Verify Database
- Click vào PostgreSQL service
- Tab "Variables" → Xem `DATABASE_URL` đã có
- Tab "Data" → Có thể xem tables sau khi migrate

---

## ☁️ BƯỚC 2: Setup Cloudinary Credentials

### 2.1. Lấy Thông Tin Cloudinary
1. Truy cập: https://cloudinary.com
2. Login vào account của bạn
3. Dashboard → Settings → Account
4. Copy: Cloud Name, API Key, API Secret

### 2.2. Add Variables vào Railway

1. **Click vào Django Service** (không phải PostgreSQL)
2. **Click tab "Variables"**
3. **Click "+ New Variable"** và thêm từng biến:

```
CLOUDINARY_CLOUD_NAME
```
Value: `your-cloud-name`

```
CLOUDINARY_API_KEY
```
Value: `your-api-key`

```
CLOUDINARY_API_SECRET
```
Value: `your-api-secret`

4. **Railway sẽ tự động redeploy** sau khi add variables

---

## 🔧 BƯỚC 3: Verify Environment Variables

Trong Railway → Django Service → Tab "Variables", bạn phải có:

### Variables Tự Động (Railway tạo):
- ✅ `DATABASE_URL` - từ PostgreSQL service
- ✅ `PORT` - Railway tự set

### Variables Bạn Cần Thêm:
- ✅ `CLOUDINARY_CLOUD_NAME` = your-cloud-name
- ✅ `CLOUDINARY_API_KEY` = your-api-key
- ✅ `CLOUDINARY_API_SECRET` = your-api-secret
- ✅ `SECRET_KEY` = (nếu chưa có, thêm random string)
- ✅ `DEBUG` = False
- ✅ `SENDGRID_API_KEY` = (nếu có)
- ✅ `FROM_EMAIL` = nguyenminh090903@gmail.com

---

## 🚀 BƯỚC 4: Deploy & Run Migrations

### 4.1. Đợi Deploy Hoàn Tất
- Railway → Deployments tab
- Đợi status = "Success" (màu xanh)
- Nếu failed, check Logs để xem lỗi

### 4.2. Run Migrations
1. **Click vào Django Service**
2. **Click tab "Settings"**
3. Scroll xuống **"Service"** section
4. Click **"Open Terminal"** hoặc **"Shell"**

Trong terminal, chạy:

```bash
# Run migrations
python manage.py migrate

# Verify migrations
python manage.py showmigrations
```

Kết quả phải thấy:
```
portfolio
 [X] 0001_initial
 [X] 0002_...
```

---

## 👤 BƯỚC 5: Create Superuser (Admin Account)

### 5.1. Trong Railway Terminal
```bash
python manage.py createsuperuser
```

### 5.2. Nhập Thông Tin
```
Username: admin
Email: nguyenminh090903@gmail.com
Password: ********** (tạo password mạnh)
Password (again): **********
```

### 5.3. Verify
```
Superuser created successfully.
```

---

## ✅ BƯỚC 6: Test Admin Panel

### 6.1. Lấy URL của App
- Railway → Django Service → Settings
- Copy **"Public Domain"**
- Ví dụ: `https://portfolio-production-xxxx.up.railway.app`

### 6.2. Truy Cập Admin
```
https://your-app.railway.app/admin
```

### 6.3. Login
- Username: `admin`
- Password: (password bạn vừa tạo)

### 6.4. Test Upload Ảnh
1. Click **"Projects"** → **"Add Project"**
2. Điền thông tin:
   - Title: "Test Project"
   - Description: "Testing image upload"
   - Tech Stack: "Django, Cloudinary"
3. **Upload Image**: Click "Choose File" → Chọn ảnh
4. Click **"Save"**
5. Nếu thành công:
   - ✅ Ảnh upload lên Cloudinary
   - ✅ URL tự động điền vào "Image url"
   - ✅ Preview hiển thị ảnh

---

## 🎯 BƯỚC 7: Verify Cloudinary

### 7.1. Check Cloudinary Dashboard
- Truy cập: https://cloudinary.com
- Login
- Dashboard → **"Media Library"**
- Phải thấy ảnh vừa upload trong folder `projects/`

### 7.2. Check Image URL
- URL format: `https://res.cloudinary.com/your-cloud-name/image/upload/...`
- Click vào URL → Ảnh phải hiển thị

---

## 🔍 Troubleshooting

### Lỗi: "Cloudinary credentials not set"
**Fix:**
1. Railway → Django Service → Variables
2. Verify 3 biến Cloudinary đã có
3. Redeploy: Settings → Redeploy

### Lỗi: "No such table: portfolio_project"
**Fix:**
```bash
# Trong Railway Terminal
python manage.py migrate
```

### Lỗi: "Permission denied" trong admin
**Fix:**
```bash
# Tạo lại superuser
python manage.py createsuperuser
```

### Lỗi: Upload ảnh failed
**Fix:**
1. Check Cloudinary credentials đúng
2. Check file size < 10MB
3. Check logs: Railway → Deployments → Logs

### Không vào được Terminal
**Alternative:**
1. Railway → Service → Settings
2. Scroll xuống "One-off Commands"
3. Chạy command:
```bash
python manage.py migrate && python manage.py createsuperuser
```

---

## 📊 Database Schema

Sau khi migrate, bạn sẽ có các tables:

```
✅ portfolio_project      - Dự án
✅ portfolio_experience   - Kinh nghiệm
✅ portfolio_photo        - Ảnh photography
✅ portfolio_skill        - Kỹ năng
✅ auth_user             - Users (Django default)
✅ django_session        - Sessions
```

---

## 🎨 Sử Dụng Admin Panel

### Thêm Project Mới
1. Admin → Projects → Add Project
2. Điền:
   - Title: "E-Commerce Platform"
   - Description: "Full stack e-commerce..."
   - Tech Stack: "Django, PostgreSQL, React"
   - GitHub URL: https://github.com/...
   - **Upload Image** (tự động lên Cloudinary)
   - Order: 1
   - Featured: ✓
3. Save

### Thêm Experience
1. Admin → Experiences → Add Experience
2. Điền thông tin công việc
3. Save

### Thêm Photo
1. Admin → Photos → Add Photo
2. Upload ảnh (tự động tạo thumbnail)
3. Chọn category: Digital/Film
4. Save

### Thêm Skill
1. Admin → Skills → Add Skill
2. Điền tên skill, category, proficiency (0-100)
3. Save

---

## 📝 Checklist Hoàn Thành

- [ ] PostgreSQL database đã tạo
- [ ] Cloudinary credentials đã add
- [ ] Environment variables đã set
- [ ] Deploy thành công (status = Success)
- [ ] Migrations đã chạy
- [ ] Superuser đã tạo
- [ ] Login admin thành công
- [ ] Upload ảnh test thành công
- [ ] Ảnh hiển thị trên Cloudinary

---

## 🎉 Hoàn Tất!

Bây giờ bạn có:
- ✅ PostgreSQL database hoạt động
- ✅ Cloudinary lưu ảnh (25GB free)
- ✅ Admin panel CRUD đầy đủ
- ✅ Authentication bảo mật
- ✅ Auto deploy khi push code

### Next Steps:
1. Thêm data vào admin panel
2. Update views.py để hiển thị data từ database
3. Update templates để render dynamic content
4. Customize admin panel (optional)

---

## 📞 Support

Nếu gặp vấn đề:
1. **Check Logs**: Railway → Deployments → View Logs
2. **Check Variables**: Railway → Service → Variables
3. **Check Database**: Railway → PostgreSQL → Data
4. **Check Cloudinary**: https://cloudinary.com → Media Library

## 🔗 Useful Links

- Railway Dashboard: https://railway.app
- Cloudinary Dashboard: https://cloudinary.com
- Admin Panel: https://your-app.railway.app/admin
- Database Guide: `DATABASE_CRUD_GUIDE.md`
- Cloudinary Guide: `CLOUDINARY_SETUP.md`
