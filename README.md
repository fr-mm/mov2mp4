# Conversor MOV → MP4 - Animação

Aplicativo GUI simples para converter arquivos MOV para MP4 usando FFmpeg, com sistema de nomenclatura específico para animação.

## ✨ Funcionalidades

- 🎬 Converte arquivos MOV para formato MP4
- 🎯 Sistema de nomenclatura para animação (Scene/Shot)
- 🖥️ Suporte multiplataforma (Linux, macOS, Windows)
- 🎨 Interface simples e intuitiva
- ⚡ Conversão rápida usando FFmpeg
- 🔄 Substituição automática de arquivos existentes
- 📝 Preview do nome do arquivo em tempo real

## 📋 Requisitos

- Python 3.8 ou superior
- FFmpeg (incluído no diretório `bin`)

## 🚀 Instalação

### Opção 1: Executar a partir do código fonte

1. Clone ou baixe este repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o aplicativo:
   ```bash
   python main.py
   ```

### Opção 2: Usar executável pré-compilado

Baixe o executável apropriado para sua plataforma na página de releases.

## 🎬 Como Usar

### Interface do Aplicativo

1. **Selecionar Arquivo MOV**
   - Clique em "Selecionar" para escolher seu arquivo .mov

2. **Definir Scene e Shot**
   - **Scene (Cena)**: Digite um número de 0 a 99 (ex: `5` vira `05`)
   - **Shot (Plano)**: Digite um número de 0 a 9999 (ex: `123` vira `0123`)

3. **Preview do Nome**
   - Veja como ficará o nome do arquivo: `Anim_sc05_sh0123.mp4`

4. **Converter**
   - Clique em "🎬 Converter para MP4"
   - O arquivo será salvo na mesma pasta do arquivo original

### Exemplos de Nomenclatura

| Scene | Shot | Arquivo Final |
|-------|------|---------------|
| 1 | 10 | `Anim_sc01_sh0010.mp4` |
| 5 | 123 | `Anim_sc05_sh0123.mp4` |
| 12 | 2 | `Anim_sc12_sh0002.mp4` |

## 🔧 Compilação

### Pré-requisitos

- Python 3.8+
- PyInstaller (instalado automaticamente pelo script de build)

### Build Local

1. Configure o projeto:
   ```bash
   python setup_macos.py  # Baixa FFmpeg para diferentes plataformas
   ```

2. Compile para sua plataforma atual:
   ```bash
   python build.py
   ```

3. O executável será criado no diretório `dist`.

### Builds Multiplataforma

Para compilar no Linux para outras plataformas, use o GitHub Actions:

1. Faça push do código para o GitHub
2. O workflow do GitHub Actions compilará automaticamente para todas as plataformas
3. Baixe os artefatos da aba Actions

## 📁 Estrutura do Projeto

```
mov2mp4/
├── main.py                    # Aplicativo principal
├── build.py                   # Script de compilação
├── setup_macos.py             # Script de configuração multiplataforma
├── requirements.txt           # Dependências Python
├── instrucoes de desbloqueio.txt  # Instruções para macOS
├── bin/                       # Binários do FFmpeg
│   ├── ffmpeg-linux/          # FFmpeg para Linux
│   └── ffmpeg-mac/            # FFmpeg para macOS
├── .github/workflows/         # Workflows do GitHub Actions
└── dist/                      # Saídas da compilação
```

## 🔨 Comandos de Compilação

### Build para Linux
```bash
pyinstaller --onefile --windowed --add-data "bin:bin" --name mov2mp4-linux main.py
```

### Build para macOS
```bash
pyinstaller --onefile --windowed --add-data "bin:bin" --name mov2mp4-macos --target-architecture universal2 main.py
```

## 🔧 Solução de Problemas

### Erro de Permissão no macOS
Se o aplicativo for bloqueado no macOS, consulte o arquivo `instrucoes de desbloqueio.txt` para instruções detalhadas sobre como desbloquear o aplicativo.

Método rápido via Terminal:
```bash
sudo xattr -rd com.apple.quarantine mov2mp4-macos
chmod +x mov2mp4-macos
```

### Erro de Permissão no Linux
Se receber um erro de permissão ao executar:
```bash
chmod +x dist/mov2mp4-linux
```

### FFmpeg Não Encontrado
Certifique-se de que os binários do FFmpeg estão na localização correta:
- Linux: `bin/ffmpeg-linux/ffmpeg`
- macOS: `bin/ffmpeg-mac/ffmpeg`

### Problemas de Build Multiplataforma
- Builds multiplataforma do Linux para macOS requerem os binários do FFmpeg da plataforma de destino
- Use o script `setup_macos.py` para baixar os binários necessários
- Para builds automatizados, use o workflow do GitHub Actions

## 🤝 Contribuindo

1. Faça fork do repositório
2. Crie uma branch para sua funcionalidade
3. Faça suas alterações
4. Teste na plataforma de destino
5. Submeta um pull request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- FFmpeg pelas capacidades de conversão de vídeo
- PyInstaller pelo sistema de empacotamento
- Tkinter pelo framework de interface gráfica

---

**Desenvolvido para workflows de animação** 🎬✨
