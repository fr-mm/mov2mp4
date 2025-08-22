import tkinter as tk
from tkinter import filedialog, messagebox, ttk
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
    
    # Validar scene e shot
    try:
        scene = int(scene_entry.get())
        shot = int(shot_entry.get())
        
        if scene < 0 or scene > 99:
            messagebox.showerror("Erro", "Scene deve ser um número entre 0 e 99")
            return
            
        if shot < 0 or shot > 9999:
            messagebox.showerror("Erro", "Shot deve ser um número entre 0 e 9999")
            return
            
    except ValueError:
        messagebox.showerror("Erro", "Scene e Shot devem ser números válidos")
        return

    # Criar nome do arquivo com formato específico
    scene_formatted = f"{scene:02d}"  # 2 dígitos com zero à esquerda
    shot_formatted = f"{shot:04d}"   # 4 dígitos com zero à esquerda
    
    # Obter diretório do arquivo original
    input_dir = os.path.dirname(input_path)
    output_filename = f"Anim_sc{scene_formatted}_sh{shot_formatted}.mp4"
    output_path = os.path.join(input_dir, output_filename)
    
    ffmpeg = get_ffmpeg_path()

    try:
        subprocess.run([ffmpeg, "-y", "-i", input_path,
                        "-c:v", "libx264", "-c:a", "aac", output_path],
                       check=True)
        messagebox.showinfo("Sucesso", f"Convertido: {output_filename}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Conversor MOV → MP4 - Animation")
root.geometry("520x320")
root.minsize(500, 300)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Arquivo MOV
tk.Label(frame, text="Arquivo MOV:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
input_frame = tk.Frame(frame)
input_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 15))

input_entry = tk.Entry(input_frame, width=50, font=("Arial", 9))
input_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

browse_btn = tk.Button(input_frame, text="Selecionar", command=select_file, bg="#4CAF50", fg="white", font=("Arial", 9))
browse_btn.pack(side="right")

# Scene e Shot
numbers_frame = tk.Frame(frame)
numbers_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))

# Scene
scene_frame = tk.Frame(numbers_frame)
scene_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
tk.Label(scene_frame, text="Scene (00-99):", font=("Arial", 10, "bold")).pack(anchor="w")
scene_entry = tk.Entry(scene_frame, width=10, font=("Arial", 12), justify="center")
scene_entry.pack(fill="x", pady=(5, 0))

# Shot
shot_frame = tk.Frame(numbers_frame)
shot_frame.pack(side="right", fill="x", expand=True)
tk.Label(shot_frame, text="Shot (0000-9999):", font=("Arial", 10, "bold")).pack(anchor="w")
shot_entry = tk.Entry(shot_frame, width=10, font=("Arial", 12), justify="center")
shot_entry.pack(fill="x", pady=(5, 0))

# Preview do nome
preview_frame = tk.Frame(frame)
preview_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 15))
tk.Label(preview_frame, text="Nome do arquivo:", font=("Arial", 10, "bold")).pack(anchor="w")
preview_label = tk.Label(preview_frame, text="Anim_sc00_sh0000.mp4", font=("Arial", 11), fg="#666", bg="#f0f0f0", relief="sunken", padx=10, pady=5)
preview_label.pack(fill="x", pady=(5, 0))

# Função para atualizar preview
def update_preview(*args):
    try:
        scene = int(scene_entry.get() or 0)
        shot = int(shot_entry.get() or 0)
        scene_formatted = f"{scene:02d}"
        shot_formatted = f"{shot:04d}"
        preview_text = f"Anim_sc{scene_formatted}_sh{shot_formatted}.mp4"
        preview_label.config(text=preview_text)
    except ValueError:
        preview_label.config(text="Anim_sc00_sh0000.mp4")

# Bind para atualizar preview quando os valores mudarem
scene_entry.bind('<KeyRelease>', update_preview)
shot_entry.bind('<KeyRelease>', update_preview)

# Botão converter
convert_btn = tk.Button(frame, text="🎬 Converter para MP4", command=convert, 
                       bg="#2196F3", fg="white", font=("Arial", 12, "bold"), 
                       pady=10)
convert_btn.grid(row=4, column=0, columnspan=2, sticky="ew")

# Configurar grid weights para responsividade
frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
