# MOV to MP4 Converter

A simple GUI application to convert MOV files to MP4 format using FFmpeg.

## Features

- 🎬 Convert MOV files to MP4 format
- 🖥️ Cross-platform support (Linux, macOS, Windows)
- 🎨 Simple and intuitive GUI
- ⚡ Fast conversion using FFmpeg
- 📁 Automatic output file naming

## Requirements

- Python 3.8 or higher
- FFmpeg (included in the `bin` directory)

## Installation

### Option 1: Run from source

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

## Building from Source

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

For building on Linux for other platforms, use the GitHub Actions workflow:

1. Push your code to GitHub
2. The GitHub Actions workflow will automatically build for all platforms
3. Download the artifacts from the Actions tab

## Project Structure

```
mov2mp4/
├── main.py              # Main application
├── build.py             # Build script
├── setup_macos.py       # Setup script for cross-platform builds
├── requirements.txt     # Python dependencies
├── bin/                 # FFmpeg binaries
│   ├── ffmpeg-linux/    # Linux FFmpeg
│   ├── ffmpeg-mac/      # macOS FFmpeg
│   └── ffmpeg-windows/  # Windows FFmpeg
├── .github/workflows/   # GitHub Actions workflows
└── dist/                # Build outputs
```

## Usage

1. Launch the application
2. Click "Selecionar" to choose a MOV file
3. Click "Converter" to start the conversion
4. The converted MP4 file will be saved in the same directory as the original file

## Building for Different Platforms

### Linux Build
```bash
pyinstaller --onefile --windowed --add-data "bin:bin" --name mov2mp4-linux main.py
```

### macOS Build
```bash
pyinstaller --onefile --windowed --add-data "bin:bin" --name mov2mp4-macos main.py
```

### Windows Build
```bash
pyinstaller --onefile --windowed --add-data "bin;bin" --name mov2mp4-windows main.py
```

## Troubleshooting

### Permission Denied Error
If you get a permission denied error when running the executable:
```bash
chmod +x dist/mov2mp4-linux
```

### FFmpeg Not Found
Make sure the FFmpeg binaries are in the correct location:
- Linux: `bin/ffmpeg-linux/ffmpeg`
- macOS: `bin/ffmpeg-mac/ffmpeg`
- Windows: `bin/ffmpeg-windows/ffmpeg.exe`

### Cross-platform Build Issues
- Cross-platform builds from Linux to macOS/Windows require the target platform's FFmpeg binaries
- Use the `setup_macos.py` script to download the required binaries
- For automated builds, use the GitHub Actions workflow

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on your target platform
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FFmpeg for the video conversion capabilities
- PyInstaller for the packaging system
- Tkinter for the GUI framework
