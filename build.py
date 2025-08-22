#!/usr/bin/env python3
"""
Build script for mov2mp4 converter
Supports building for Linux, Windows, and macOS
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return None

def build_for_platform(target_platform):
    """Build the application for a specific platform"""
    print(f"\n🚀 Building for {target_platform}...")
    
    # Create output directory
    output_dir = f"dist/mov2mp4-{target_platform}"
    os.makedirs(output_dir, exist_ok=True)
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",  # No console window
        f"--name=mov2mp4-{target_platform}",
        "--add-data=bin:bin",  # Include the bin directory
        "main.py"
    ]
    
    # Platform-specific options
    if target_platform == "macos":
        cmd.extend([
            "--target-architecture=universal2",  # Universal binary for Intel + Apple Silicon
            "--osx-bundle-identifier=com.mov2mp4.converter"
        ])
    elif target_platform == "windows":
        cmd.extend([
            "--target-architecture=x86_64"
        ])
    
    result = run_command(" ".join(cmd), f"Building {target_platform} executable")
    
    if result:
        print(f"✅ Build completed for {target_platform}")
        print(f"📁 Output: {output_dir}")
        return True
    return False

def create_macos_bundle():
    """Create a proper macOS .app bundle"""
    print("\n🍎 Creating macOS bundle...")
    
    # Create .app structure
    app_name = "mov2mp4.app"
    app_path = f"dist/{app_name}"
    
    if os.path.exists(app_path):
        shutil.rmtree(app_path)
    
    # Create bundle structure
    os.makedirs(f"{app_path}/Contents/MacOS", exist_ok=True)
    os.makedirs(f"{app_path}/Contents/Resources", exist_ok=True)
    
    # Copy executable
    shutil.copy("dist/mov2mp4-macos", f"{app_path}/Contents/MacOS/mov2mp4")
    os.chmod(f"{app_path}/Contents/MacOS/mov2mp4", 0o755)
    
    # Create Info.plist
    info_plist = f"""{app_path}/Contents/Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>mov2mp4</string>
    <key>CFBundleIdentifier</key>
    <string>com.mov2mp4.converter</string>
    <key>CFBundleName</key>
    <string>MOV to MP4 Converter</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>"""
    
    with open(f"{app_path}/Contents/Info.plist", "w") as f:
        f.write(info_plist)
    
    print(f"✅ macOS bundle created: {app_path}")

def main():
    """Main build function"""
    print("🔨 MOV to MP4 Converter Build Script")
    print("=" * 40)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Not running in a virtual environment")
        print("Continuing anyway...")
    
    # Clean previous builds
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("*.spec"):
        for spec_file in Path(".").glob("*.spec"):
            spec_file.unlink()
    
    # Build for current platform first
    current_platform = platform.system().lower()
    if current_platform == "darwin":
        current_platform = "macos"
    elif current_platform == "windows":
        current_platform = "windows"
    else:
        current_platform = "linux"
    
    print(f"🖥️  Current platform: {current_platform}")
    
    # Build for current platform
    if build_for_platform(current_platform):
        print(f"✅ Successfully built for {current_platform}")
        
        # Create macOS bundle if building for macOS
        if current_platform == "macos":
            create_macos_bundle()
    else:
        print(f"❌ Failed to build for {current_platform}")
        return
    
    # Ask if user wants to build for other platforms
    print("\n" + "=" * 40)
    print("🎯 Cross-platform builds")
    print("Note: Cross-platform builds may require additional setup")
    
    platforms = ["linux", "macos", "windows"]
    platforms.remove(current_platform)
    
    for platform_name in platforms:
        response = input(f"Build for {platform_name}? (y/N): ")
        if response.lower() == 'y':
            build_for_platform(platform_name)
    
    print("\n🎉 Build process completed!")
    print("📁 Check the 'dist' directory for your builds")

if __name__ == "__main__":
    main()
