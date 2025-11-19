# Fix WSL Update Issue

## Fix "Class not registered" Error (REGDB_E_CLASSNOTREG)

This error means Windows registry entries for WSL are corrupted or missing.

### Solution 1: Re-register WSL Components (Quick Fix)

Open PowerShell as Administrator and run these commands one by one:

```powershell
# Re-register Windows Store
Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

# Re-register WSL
wsl --unregister Ubuntu
wsl --install
```

### Solution 2: Enable Required Windows Features

```powershell
# Enable WSL feature
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Enable Virtual Machine Platform
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart computer
shutdown /r /t 0
```

After restart, run:
```powershell
wsl --set-default-version 2
wsl --update
```

### Solution 3: Manual WSL Installation

1. Download WSL update package directly:
   https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

2. Run the MSI installer

3. Restart computer

4. Open PowerShell as Admin:
```powershell
wsl --install -d Ubuntu
```

## Method 1: Update WSL (Recommended)

1. Open PowerShell as Administrator:
   - Press Windows key
   - Type "PowerShell"
   - Right-click "Windows PowerShell"
   - Select "Run as administrator"

2. Run the update command:
```powershell
wsl --update
```

3. After update completes, restart Docker Desktop by clicking the "Restart" button

## Method 2: Manual WSL Update

If the above doesn't work:

1. Download the latest WSL update package:
   https://aka.ms/wsl2kernel

2. Run the downloaded installer

3. Restart your computer

4. Open Docker Desktop

## Method 3: Check WSL Version

Check your current WSL version:
```powershell
wsl --version
```

If WSL is not installed, install it:
```powershell
wsl --install
```

## Method 4: Update Windows

Sometimes WSL updates come through Windows Update:

1. Open Settings → Windows Update
2. Click "Check for updates"
3. Install all available updates
4. Restart your computer

## Verify Docker Works

After fixing WSL, verify Docker is working:
```powershell
docker --version
docker ps
```

## Alternative: Deploy Without Docker

If you want to deploy without fixing Docker, you can use:
- Railway (uses cloud builders)
- Render (uses cloud builders)
- Heroku (uses cloud builders)

These platforms build your Docker image in the cloud, so you don't need Docker Desktop running locally.
