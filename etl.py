import pandas as pd
import pycountry
import os

# Configurações
ARQUIVO_ENTRADA = "dados-imersao-final.csv"
ARQUIVO_SAIDA = "dados_tratados.csv"
URL_BACKUP = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"

def processar_dados():
    print("Iniciando processamento de dados...")
    
    # 1. Carregar dados (Local ou URL)
    if os.path.exists(ARQUIVO_ENTRADA):
        print(f"Lendo arquivo local: {ARQUIVO_ENTRADA}")
        try:
            df = pd.read_csv(ARQUIVO_ENTRADA)
            if len(df.columns) <= 1:
                df = pd.read_csv(ARQUIVO_ENTRADA, sep=";")
        except Exception as e:
            print(f"Erro ao ler localmente: {e}. Tentando URL...")
            df = pd.read_csv(URL_BACKUP)
    else:
        print(f"Arquivo local não encontrado. Baixando de: {URL_BACKUP}")
        df = pd.read_csv(URL_BACKUP)

    # 2. Renomear colunas
    rename_map = {
        'work_year': 'ano', 'ano_trabalho': 'ano',
        'experience_level': 'senioridade', 'nivel_experiencia': 'senioridade',
        'employment_type': 'contrato', 'tipo_emprego': 'contrato',
        'salary_in_usd': 'usd', 'salario_em_usd': 'usd',
        'remote_ratio': 'remoto', 'taxa_remoto': 'remoto',
        'employee_residence': 'residencia_iso3', 'residencia_funcionario': 'residencia_iso3',
        'company_size': 'tamanho_empresa', 'tamanho_empresa': 'tamanho_empresa',
        'job_title': 'cargo', 'cargo': 'cargo'
    }
    df = df.rename(columns=rename_map)

    # 3. Traduzir siglas para nomes completos
    print("Traduzindo siglas...")
    mapa_senioridade = {
        'EN': 'Júnior', 'MI': 'Pleno', 'SE': 'Sênior', 'EX': 'Executivo'
    }
    mapa_contrato = {
        'PT': 'Meio período', 'FT': 'Tempo integral', 'CT': 'Contrato', 'FL': 'Freelance'
    }
    mapa_tamanho = {
        'S': 'Pequena', 'M': 'Média', 'L': 'Grande'
    }
    mapa_remoto = {
        0: 'Presencial', 50: 'Híbrido', 100: 'Remoto'
    }

    if 'senioridade' in df.columns:
        df['senioridade'] = df['senioridade'].replace(mapa_senioridade)
    if 'contrato' in df.columns:
        df['contrato'] = df['contrato'].replace(mapa_contrato)
    if 'tamanho_empresa' in df.columns:
        df['tamanho_empresa'] = df['tamanho_empresa'].replace(mapa_tamanho)
    if 'remoto' in df.columns:
        df['remoto'] = df['remoto'].replace(mapa_remoto)

    # 4. Converter países (ISO2 -> ISO3)
    print("Convertendo códigos de países...")
    def converter_pais(codigo):
        try:
            return pycountry.countries.get(alpha_2=codigo).alpha_3
        except:
            return codigo
            
    if 'residencia_iso3' in df.columns:
        df['residencia_iso3'] = df['residencia_iso3'].apply(converter_pais)

    # 5. Salvar
    df.to_csv(ARQUIVO_SAIDA, index=False)
    print(f"Sucesso! Arquivo '{ARQUIVO_SAIDA}' gerado.")

if __name__ == "__main__":
    processar_dados()