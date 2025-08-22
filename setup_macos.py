#!/usr/bin/env python3
"""
Setup script to prepare the project for macOS builds
This script helps download the macOS version of ffmpeg
"""

import os
import sys
import urllib.request
import zipfile
import tarfile
import shutil
from pathlib import Path

def download_file(url, filename):
    """Download a file with progress indicator"""
    print(f"📥 Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"✅ Downloaded {filename}")
        return True
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return False

def extract_archive(archive_path, extract_to):
    """Extract an archive file"""
    print(f"📦 Extracting {archive_path}...")
    try:
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        elif archive_path.endswith('.tar.bz2'):
            with tarfile.open(archive_path, 'r:bz2') as tar_ref:
                tar_ref.extractall(extract_to)
        print(f"✅ Extracted to {extract_to}")
        return True
    except Exception as e:
        print(f"❌ Failed to extract {archive_path}: {e}")
        return False

def setup_macos_ffmpeg():
    """Download and set up ffmpeg for macOS"""
    print("🍎 Setting up ffmpeg for macOS...")
    
    # Create bin directory if it doesn't exist
    bin_dir = Path("bin")
    bin_dir.mkdir(exist_ok=True)
    
    # Check if ffmpeg-mac already exists
    ffmpeg_mac_dir = bin_dir / "ffmpeg-mac"
    if ffmpeg_mac_dir.exists():
        print("✅ ffmpeg-mac directory already exists")
        return True
    
    # Download ffmpeg for macOS
    # Using the official ffmpeg builds
    ffmpeg_url = "https://evermeet.cx/ffmpeg/getrelease/zip"
    ffmpeg_zip = "ffmpeg-mac.zip"
    
    if not download_file(ffmpeg_url, ffmpeg_zip):
        print("❌ Failed to download ffmpeg for macOS")
        return False
    
    # Extract the archive
    if not extract_archive(ffmpeg_zip, "temp_extract"):
        print("❌ Failed to extract ffmpeg")
        return False
    
    # Move the extracted files to the correct location
    try:
        # Find the ffmpeg executable in the extracted files
        extracted_files = list(Path("temp_extract").rglob("ffmpeg"))
        if not extracted_files:
            print("❌ Could not find ffmpeg executable in extracted files")
            return False
        
        ffmpeg_executable = extracted_files[0]
        
        # Create the ffmpeg-mac directory structure
        ffmpeg_mac_dir.mkdir(exist_ok=True)
        
        # Copy the ffmpeg executable
        shutil.copy2(ffmpeg_executable, ffmpeg_mac_dir / "ffmpeg")
        os.chmod(ffmpeg_mac_dir / "ffmpeg", 0o755)
        
        # Also copy ffprobe if it exists
        ffprobe_files = list(Path("temp_extract").rglob("ffprobe"))
        if ffprobe_files:
            shutil.copy2(ffprobe_files[0], ffmpeg_mac_dir / "ffprobe")
            os.chmod(ffmpeg_mac_dir / "ffprobe", 0o755)
        
        print("✅ Successfully set up ffmpeg for macOS")
        
        # Clean up
        shutil.rmtree("temp_extract")
        os.remove(ffmpeg_zip)
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up ffmpeg: {e}")
        return False

def setup_windows_ffmpeg():
    """Download and set up ffmpeg for Windows"""
    print("🪟 Setting up ffmpeg for Windows...")
    
    # Create bin directory if it doesn't exist
    bin_dir = Path("bin")
    bin_dir.mkdir(exist_ok=True)
    
    # Check if ffmpeg-windows already exists
    ffmpeg_windows_dir = bin_dir / "ffmpeg-windows"
    if ffmpeg_windows_dir.exists():
        print("✅ ffmpeg-windows directory already exists")
        return True
    
    # Download ffmpeg for Windows
    ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    ffmpeg_zip = "ffmpeg-windows.zip"
    
    if not download_file(ffmpeg_url, ffmpeg_zip):
        print("❌ Failed to download ffmpeg for Windows")
        return False
    
    # Extract the archive
    if not extract_archive(ffmpeg_zip, "temp_extract"):
        print("❌ Failed to extract ffmpeg")
        return False
    
    # Move the extracted files to the correct location
    try:
        # Find the ffmpeg executable in the extracted files
        extracted_files = list(Path("temp_extract").rglob("ffmpeg.exe"))
        if not extracted_files:
            print("❌ Could not find ffmpeg.exe in extracted files")
            return False
        
        ffmpeg_executable = extracted_files[0]
        
        # Create the ffmpeg-windows directory structure
        ffmpeg_windows_dir.mkdir(exist_ok=True)
        
        # Copy the ffmpeg executable
        shutil.copy2(ffmpeg_executable, ffmpeg_windows_dir / "ffmpeg.exe")
        
        # Also copy ffprobe if it exists
        ffprobe_files = list(Path("temp_extract").rglob("ffprobe.exe"))
        if ffprobe_files:
            shutil.copy2(ffprobe_files[0], ffmpeg_windows_dir / "ffprobe.exe")
        
        print("✅ Successfully set up ffmpeg for Windows")
        
        # Clean up
        shutil.rmtree("temp_extract")
        os.remove(ffmpeg_zip)
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up ffmpeg: {e}")
        return False

def main():
    """Main setup function"""
    print("🔧 MOV to MP4 Converter - Cross-platform Setup")
    print("=" * 50)
    
    # Check current platform
    import platform
    current_platform = platform.system().lower()
    print(f"🖥️  Current platform: {current_platform}")
    
    # Set up ffmpeg for different platforms
    if current_platform == "darwin":
        print("🍎 You're on macOS - setting up local ffmpeg...")
        setup_macos_ffmpeg()
    elif current_platform == "windows":
        print("🪟 You're on Windows - setting up local ffmpeg...")
        setup_windows_ffmpeg()
    else:
        print("🐧 You're on Linux - setting up ffmpeg for other platforms...")
        
        # Ask which platforms to set up
        print("\nWhich platforms would you like to set up ffmpeg for?")
        print("1. macOS")
        print("2. Windows")
        print("3. Both")
        print("4. Skip")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice in ["1", "3"]:
            setup_macos_ffmpeg()
        
        if choice in ["2", "3"]:
            setup_windows_ffmpeg()
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. For local builds: Use the build.py script")
    print("2. For automated builds: Push to GitHub and use GitHub Actions")
    print("3. For macOS builds from Linux: Use the GitHub Actions workflow")

if __name__ == "__main__":
    main()
