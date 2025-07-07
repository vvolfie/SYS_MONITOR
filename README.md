# SYS_MONITOR

Ferramenta simples em Python para monitorização de hardware do sistema, incluindo CPU, disco e GPU, em tempo real, via linha de comandos.

## 📌 Funcionalidades

- 📊 Monitorização em tempo real da utilização da CPU por core
- 💾 Informações sobre partições e uso de disco
- 🎮 Deteção e listagem de GPUs disponíveis no sistema
- Interface simples baseada em menus (CLI)
- Suporte para interrupção com `Ctrl + C`

## ⚙️ Requisitos

- Python 3.6+
- Sistema operativo compatível com os módulos `psutil` e `GPUtil` (Linux e Windows testados)

### 📦 Dependências

Instala as bibliotecas necessárias com:

```bash
pip install psutil cpuinfo GPUtil
