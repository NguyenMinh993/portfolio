# Railway Deployment - Step by Step

## Your Repository
https://github.com/NguyenMinh993/portfolio

## Step 1: Sign Up for Railway

1. Go to: **https://railway.app**
2. Click **"Login"** or **"Start a New Project"**
3. Click **"Login With GitHub"**
4. Authorize Railway to access your GitHub account

## Step 2: Create New Project

1. Click **"New Project"** (purple button)
2. Select **"Deploy from GitHub repo"**
3. You'll see a list of your repositories
4. Find and click **"NguyenMinh993/portfolio"**
5. Railway will start deploying automatically

## Step 3: Wait for Build (2-3 minutes)

Railway will:
- ✓ Clone your repository
- ✓ Detect Dockerfile
- ✓ Build Docker image
- ✓ Deploy container
- ✓ Assign a public URL

Watch the build logs in real-time on the Railway dashboard.

## Step 4: Add Environment Variables

1. Click on your deployed service (the card showing your app)
2. Go to the **"Variables"** tab
3. Click **"+ New Variable"** and add these one by one:

```
DEBUG=False
SECRET_KEY=django-insecure-6n+$^sa+%qex3ye#35^1zjb11s$l(+^i9w7&-r84c28r_tk*7s
EMAIL_HOST_USER=nguyenminh090903@gmail.com
EMAIL_HOST_PASSWORD=vtgmfkpwmuthqinn
```

4. Railway will automatically redeploy after adding variables

## Step 5: Get Your Public URL

1. Go to the **"Settings"** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"**
4. You'll get a URL like: `portfolio-production-xxxx.up.railway.app`

## Step 6: Update ALLOWED_HOSTS

After getting your Railway URL, you need to update the environment variable:

1. Go back to **"Variables"** tab
2. Add a new variable:
```
ALLOWED_HOSTS=portfolio-production-xxxx.up.railway.app,127.0.0.1,localhost
```
(Replace `portfolio-production-xxxx.up.railway.app` with your actual Railway domain)

3. Railway will redeploy automatically

## Step 7: Verify Deployment

1. Click on your Railway domain URL
2. Your portfolio website should load!

## Troubleshooting

### Build Failed
- Check the build logs in Railway dashboard
- Make sure all files are pushed to GitHub

### App Crashes
- Check the deployment logs
- Verify all environment variables are set correctly
- Make sure `ALLOWED_HOSTS` includes your Railway domain

### Static Files Not Loading
- Railway automatically runs `collectstatic` during build
- Check that `STATIC_ROOT` is set in settings.py

## Updating Your Site

Whenever you make changes:
```bash
git add .
git commit -m "Your update message"
git push
```

Railway will automatically detect the push and redeploy!

## Cost
- Railway offers $5 free credit per month
- After that, it's pay-as-you-go (typically $5-10/month for small apps)

## Need Help?
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
