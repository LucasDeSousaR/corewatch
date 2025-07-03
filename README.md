# 🖥️ CoreWatch

**CoreWatch** é uma plataforma web desenvolvida em **Django** que realiza o **monitoramento de LPARs** (Logical Partitions) em ambientes z/OS. Ele permite consultar visualmente informações operacionais, histórico de uso de CPU/MSU/SMF e executar comandos no mainframe para fins de auditoria e análise.

---

## 📌 Funcionalidades

- 📊 Visualização gráfica diária de uso de recursos (CPU, MSU, SMF)
- 🔍 Detalhamento de cada LPAR
- 🗂️ Armazenamento de dados históricos no MongoDB
- 🧾 Exportação de comandos z/OS para datasets ou arquivos via Python no USS
- 🌐 Interface responsiva com sidebar e layout fixo (header/footer)
- 🔧 Preparado para integração com Zowe e automações

---

## 📷 Capturas de Tela

### Tela Inicial
> Exibe introdução ao projeto e instituição

### Página de LPARs
> Lista de LPARs disponíveis com links para detalhes

### Detalhes da LPAR
> Exibe cards com última leitura e gráfico de histórico

### Gráfico Diário
> Gráfico interativo com agrupamento por data

---

## 🧰 Tecnologias Utilizadas

### Backend
- Python 3.12
- Django 5.2
- MongoDB (MongoEngine)
- Zowe CLI ou Python USS scripts para coleta de dados

### Frontend
- HTML + CSS + JS
- Bootstrap (custom)
- Chart.js

### Outros
- Docker (opcional)
- JCL / OCOPY (para envio de arquivos ao MVS)

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.12
- MongoDB
- Virtualenv (opcional)

### Instalação

```bash
git clone https://github.com/seunome/corewatch.git
cd corewatch
python -m venv .venv
source .venv/bin/activate  # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
