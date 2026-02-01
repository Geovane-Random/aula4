## 🚀 Guia de Configuração e Execução

>Siga os passos abaixo para preparar seu ambiente e colocar a aplicação para rodar.

### 1. Criar o Ambiente Virtual
O primeiro passo é isolar as bibliotecas do projeto para evitar conflitos com outras versões do Python no seu sistema.

```bash
python3 -m venv venv
```

### 2. Ativar o Ambiente Virtual
Dependendo do seu sistema operacional, o comando de ativação muda:

**No Windows:**
```powershell
venv\Scripts\activate
```

**No Linux/macOS:**
```bash
source venv/bin/activate
```

> 💡 **Dica:** Você saberá que deu certo quando ver o prefixo `(venv)` aparecer no terminal.

### 3. Instalar Dependências
Com o ambiente ativo, instale todos os pacotes necessários (como o Streamlit e as bibliotecas de IA dos seus modelos de negócio):

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
Agora é só dar o comando de partida e abrir o link que aparecerá no seu terminal (geralmente http://localhost:8501):

```bash
streamlit run app.py
```