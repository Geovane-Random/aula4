# Criar o ambiente virtual
```bash
python3 -m venv venv
```

# Ativar o ambiente virtual

## No Windows:
```bash
venv\Scripts\activate
```

## No Linux/macOS:
```bash
source venv/bin/activate
```

### 6. Instalar Dependências Python
Com o ambiente virtual ativo, instale os pacotes listados no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 7. Executar a Aplicação
Para iniciar o projeto, execute o comando:
```bash
streamlit run app.py
