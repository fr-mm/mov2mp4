import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess, os, sys, platform

def get_ffmpeg_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    system = platform.system().lower()
    if system == "windows":
        # Check for Windows ffmpeg in different possible locations
        windows_paths = [
            os.path.join(base_dir, "bin", "ffmpeg-windows", "ffmpeg.exe"),
            os.path.join(base_dir, "bin", "ffmpeg.exe"),
            "ffmpeg.exe"  # System PATH fallback
        ]
        for path in windows_paths:
            if os.path.exists(path):
                return path
        return windows_paths[0]  # Return the first path as default
    elif system == "darwin":
        # Check for macOS ffmpeg in different possible locations
        mac_paths = [
            os.path.join(base_dir, "bin", "ffmpeg-mac", "ffmpeg"),
            os.path.join(base_dir, "bin", "ffmpeg-mac"),
            "ffmpeg"  # System PATH fallback
        ]
        for path in mac_paths:
            if os.path.exists(path):
                return path
        return mac_paths[0]  # Return the first path as default
    else:
        # Linux - check for Linux ffmpeg in different possible locations
        linux_paths = [
            os.path.join(base_dir, "bin", "ffmpeg-linux", "ffmpeg"),
            os.path.join(base_dir, "bin", "ffmpeg-linux"),
            "ffmpeg"  # System PATH fallback
        ]
        for path in linux_paths:
            if os.path.exists(path):
                return path
        return linux_paths[0]  # Return the first path as default

def select_file():
    path = filedialog.askopenfilename(
        title="Selecione um arquivo .mov",
        filetypes=[("MOV files", "*.mov")]
    )
    if path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, path)

def convert():
    input_path = input_entry.get()
    if not input_path.lower().endswith(".mov"):
        messagebox.showerror("Erro", "Selecione um arquivo .mov válido")
        return

    output_path = os.path.splitext(input_path)[0] + ".mp4"
    ffmpeg = get_ffmpeg_path()

    try:
        subprocess.run([ffmpeg, "-i", input_path,
                        "-c:v", "libx264", "-c:a", "aac", output_path],
                       check=True)
        messagebox.showinfo("Sucesso", f"Convertido: {output_path}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Conversor MOV → MP4")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

input_entry = tk.Entry(frame, width=50)
input_entry.grid(row=0, column=0, padx=5, pady=5)

browse_btn = tk.Button(frame, text="Selecionar", command=select_file)
browse_btn.grid(row=0, column=1, padx=5, pady=5)

convert_btn = tk.Button(frame, text="Converter", command=convert)
convert_btn.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
