# MOV → MP4 Converter - Animation

Simple GUI application to convert MOV files to MP4 using FFmpeg, with specific naming system for animation workflows.

## ✨ Features

- 🎬 Convert MOV files to MP4 format
- 🎯 Animation naming system (Scene/Shot)
- 🖥️ Cross-platform support (Linux, macOS, Windows)
- 🎨 Simple and intuitive interface
- ⚡ Fast conversion using FFmpeg
- 🔄 Automatic file replacement
- 📝 Real-time filename preview

## 📋 Requirements

- Python 3.8 or higher
- FFmpeg (included in the `bin` directory)

## 🚀 Installation

### Option 1: Run from source code

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

### Option 2: Use pre-built executable

Download the appropriate executable for your platform from the releases page.

## 🎬 How to Use

### Application Interface

1. **Select MOV File**
   - Click "Select" to choose your .mov file

2. **Set Scene and Shot**
   - **Scene**: Enter a number from 0 to 99 (e.g., `5` becomes `05`)
   - **Shot**: Enter a number from 0 to 9999 (e.g., `123` becomes `0123`)

3. **Filename Preview**
   - See how the filename will look: `Anim_sc05_sh0123.mp4`

4. **Convert**
   - Click "🎬 Convert to MP4"
   - The file will be saved in the same folder as the original file

### Naming Examples

| Scene | Shot | Final Filename |
|-------|------|---------------|
| 1 | 10 | `Anim_sc01_sh0010.mp4` |
| 5 | 123 | `Anim_sc05_sh0123.mp4` |
| 12 | 2 | `Anim_sc12_sh0002.mp4` |

## 🔧 Building

### Prerequisites

- Python 3.8+
- PyInstaller (installed automatically by the build script)

### Local Build

1. Set up the project:
   ```bash
   python setup_macos.py  # Downloads FFmpeg for different platforms
   ```

2. Build for your current platform:
   ```bash
   python build.py
   ```

3. The executable will be created in the `dist` directory.

### Cross-platform Builds

To build on Linux for other platforms, use GitHub Actions:

1. Push the code to GitHub
2. The GitHub Actions workflow will automatically build for all platforms
3. Download the artifacts from the Actions tab

## 📁 Project Structure

```
mov2mp4/
├── main.py                    # Main application
├── build.py                   # Build script
├── setup_macos.py             # Cross-platform setup script
├── requirements.txt           # Python dependencies
├── macos_unlock_instructions.txt  # macOS instructions
├── bin/                       # FFmpeg binaries
│   ├── ffmpeg-linux/          # FFmpeg for Linux
│   └── ffmpeg-mac/            # FFmpeg for macOS
├── .github/workflows/         # GitHub Actions workflows
└── dist/                      # Build outputs
```

## 🔨 Build Commands

### Linux Build
```bash
pyinstaller --onefile --windowed --add-data "bin:bin" --name mov2mp4-linux main.py
```

### macOS Build
```bash
pyinstaller --onefile --windowed --add-data "bin:bin" --name mov2mp4-macos --target-architecture universal2 main.py
```

## 🔧 Troubleshooting

### macOS Permission Error
If the application is blocked on macOS, check the `macos_unlock_instructions.txt` file for detailed instructions on how to unlock the application.

Quick method via Terminal:
```bash
sudo xattr -rd com.apple.quarantine mov2mp4-macos
chmod +x mov2mp4-macos
```

### Linux Permission Error
If you get a permission error when running:
```bash
chmod +x dist/mov2mp4-linux
```

### FFmpeg Not Found
Make sure the FFmpeg binaries are in the correct location:
- Linux: `bin/ffmpeg-linux/ffmpeg`
- macOS: `bin/ffmpeg-mac/ffmpeg`

### Cross-platform Build Issues
- Cross-platform builds from Linux to macOS require the target platform's FFmpeg binaries
- Use the `setup_macos.py` script to download the required binaries
- For automated builds, use the GitHub Actions workflow

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on your target platform
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FFmpeg for video conversion capabilities
- PyInstaller for the packaging system
- Tkinter for the GUI framework

---

**Built for animation workflows** 🎬✨
