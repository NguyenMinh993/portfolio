# Deployment Guide - DigitalOcean App Platform

## Prerequisites
- DigitalOcean account
- GitHub account with this repository pushed

## Step-by-Step Deployment

### 1. Push Your Code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Deploy on DigitalOcean

#### Option A: Using App Spec File (Recommended)
1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Select "GitHub" as source
4. Authorize DigitalOcean to access your GitHub
5. Select your repository and branch (main)
6. Click "Next"
7. DigitalOcean will detect the Dockerfile automatically
8. Click "Edit Plan" and select the $5/month Basic plan (or Free tier if available)
9. Click "Next" through the remaining steps
10. Click "Create Resources"

#### Option B: Using doctl CLI
```bash
# Install doctl
# Windows: Download from https://github.com/digitalocean/doctl/releases

# Authenticate
doctl auth init

# Create app from spec
doctl apps create --spec .do/app.yaml
```

### 3. Configure Environment Variables (In DigitalOcean Dashboard)
After app creation, go to Settings → Environment Variables and verify:
- `DEBUG=False`
- `SECRET_KEY` (use a strong secret key)
- `ALLOWED_HOSTS` (will be auto-set to your app domain)
- `EMAIL_HOST_USER=nguyenminh090903@gmail.com`
- `EMAIL_HOST_PASSWORD` (your email app password)

### 4. Add Database (Optional)
If you need PostgreSQL instead of SQLite:
1. In your app dashboard, go to "Database"
2. Click "Add Database"
3. Select PostgreSQL
4. DigitalOcean will automatically set `DATABASE_URL` environment variable

### 5. Update ALLOWED_HOSTS
After deployment, your app will have a URL like: `portfolio-xxxxx.ondigitalocean.app`

Update the `ALLOWED_HOSTS` environment variable to include this domain.

## Post-Deployment

### Run Migrations
Migrations run automatically on each deployment via the Dockerfile CMD.

### Collect Static Files
Static files are collected during the Docker build process.

### Monitor Logs
```bash
doctl apps logs YOUR_APP_ID --type run
```

Or view in the DigitalOcean dashboard under "Runtime Logs"

## Updating Your App
Simply push changes to your GitHub repository:
```bash
git add .
git commit -m "Update description"
git push
```

DigitalOcean will automatically rebuild and redeploy.

## Troubleshooting

### App won't start
- Check Runtime Logs in the dashboard
- Verify all environment variables are set correctly
- Ensure `ALLOWED_HOSTS` includes your app domain

### Static files not loading
- Check that `collectstatic` ran successfully in build logs
- Verify `STATIC_ROOT` and `STATIC_URL` in settings.py

### Database errors
- If using PostgreSQL, ensure `DATABASE_URL` is set
- Check that migrations ran successfully

## Cost
- Basic plan: $5/month
- Includes 512MB RAM, 1 vCPU
- Free tier may be available for new accounts

## Alternative: Deploy with Docker Hub
If you prefer using Docker Hub:
1. Build and push image:
```bash
docker build -t your-username/portfolio .
docker push your-username/portfolio
```
2. In DigitalOcean, select "Docker Hub" as source instead of GitHub
