import json
import re
import subprocess # Importe o modulo subprocess
import sys
from datetime import datetime, timedelta

def converter_data_mainframe(julian_date_str: str, time_str: str) -> str:
    """
    Converte uma data juliana (YYYYDDD) e hora do mainframe para o formato ISO 8601 (YYYY-MM-DDTHH:MM:SS).
    """
    try:
        year = int(julian_date_str[:4])
        day_of_year = int(julian_date_str[4:])
        # Remove os milissegundos para a conversao
        time_str_clean = time_str.split('.')[0]
        
        # Cria a data baseada no ano e dia do ano
        date_obj = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)
        # Cria o objeto de tempo
        time_obj = datetime.strptime(time_str_clean, '%H:%M:%S').time()
        
        # Combina data e hora e formata
        full_datetime = datetime.combine(date_obj, time_obj)
        return full_datetime.isoformat()
    except (ValueError, TypeError):
        # Retorna None se houver erro na conversao
        return None

def converter_data_mainframe(julian_date_str: str, time_str: str) -> str:
    try:
        year = int(julian_date_str[:4])
        day_of_year = int(julian_date_str[4:])
        time_str_clean = time_str.split('.')[0]
        date_obj = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)
        time_obj = datetime.strptime(time_str_clean, '%H:%M:%S').time()
        full_datetime = datetime.combine(date_obj, time_obj)
        return full_datetime.isoformat()
    except (ValueError, TypeError):
        return None

# --- CORRECAO APLICADA NESTA FUNCAO ---
def extrair_informacoes_log(log_data: str) -> dict:
    """
    Processa o log do mainframe, extrai informacoes e retorna um dicionario estruturado.
    """
    dados_extraidos = {}
    regex_cabecalho = re.compile(r'^(\S+)\s+(\d{7})\s+([\d:.]+)\s+.*')
    regex_ipl_display = re.compile(r'IPLINFO DISPLAY')
    regex_ipl_data = re.compile(r'SYSTEM IPLED AT ([\d.]+)\s+ON\s+([\d/]+)')
    regex_release_zos = re.compile(r'RELEASE\s+(z/OS\s+[\d.]+)')
    regex_vm_info = re.compile(r'VM CPID = (z/VM\s+[\d.]+)')
    regex_vm_name = re.compile(r'VM NAME = (\S+)')
    regex_smf_display = re.compile(r'SMF DATA SETS') # Nome correto da variavel
    regex_smf_active = re.compile(r'^\s+S-([^\s]+)\s+[^\s]+\s+[^\s]+\s+(\d+)\s+ACTIVE')
    regex_rl_display = re.compile(r'PENDING REQUESTS')
    regex_rl_request = re.compile(r'^\s+\d+\s+R\s+[\d.]+\s+\S+\s+\S+\s+(\*\d+\s+.*)')
    regex_error = re.compile(r'(EZZ\d{4}I\s+SYNTAX ERROR.*)')
    contexto_atual = None
    lpar_atual = None
    timestamp_atual = None

    for linha in log_data.splitlines():
        match_cabecalho = regex_cabecalho.match(linha)
        if match_cabecalho:
            lpar_atual, data_juliana, hora = match_cabecalho.groups()
            timestamp_atual = converter_data_mainframe(data_juliana, hora)
            dados_extraidos.setdefault(lpar_atual, {'infoLpar': {}, 'historico': [], 'alertas': []})
            contexto_atual = None

        if regex_ipl_display.search(linha):
            contexto_atual = 'IPLINFO'
            continue
        # --- LINHA CORRIGIDA ---
        if regex_smf_display.search(linha):
            contexto_atual = 'SMF'
            continue
        if regex_rl_display.search(linha):
            contexto_atual = 'RLTN'
            continue
        
        # O resto da funcao permanece igual...
        if contexto_atual == 'IPLINFO':
            match_data_ipl = regex_ipl_data.search(linha)
            if match_data_ipl:
                hora_ipl, data_ipl = match_data_ipl.groups()
                data_ipl_obj = datetime.strptime(data_ipl, '%m/%d/%Y').date()
                hora_ipl_obj = datetime.strptime(hora_ipl, '%H.%M.%S').time()
                dados_extraidos[lpar_atual]['infoLpar']['ultimoIpl'] = datetime.combine(data_ipl_obj, hora_ipl_obj).isoformat()
            match_release = regex_release_zos.search(linha)
            if match_release:
                dados_extraidos[lpar_atual]['infoLpar']['releaseOs'] = match_release.group(1)
            match_vm_info = regex_vm_info.search(linha)
            if match_vm_info:
                dados_extraidos[lpar_atual]['infoLpar']['versaoVm'] = match_vm_info.group(1)
            match_vm_name = regex_vm_name.search(linha)
            if match_vm_name:
                dados_extraidos[lpar_atual]['infoLpar']['nomeVm'] = match_vm_name.group(1)
                dados_extraidos[lpar_atual]['infoLpar']['nomeLpar'] = lpar_atual
        elif contexto_atual == 'SMF':
            match_smf = regex_smf_active.search(linha)
            if match_smf:
                dataset, percentual_full = match_smf.groups()
                registro_historico = {'timestamp': timestamp_atual, 'tipo': 'USO_SMF', 'datasetAtivo': f"SYS1.{lpar_atual}.{dataset}", 'percentualUso': int(percentual_full)}
                dados_extraidos[lpar_atual]['historico'].append(registro_historico)
        elif contexto_atual == 'RLTN':
            match_req = regex_rl_request.search(linha)
            if match_req:
                mensagem = " ".join(match_req.group(1).split())
                alerta = {'timestamp': timestamp_atual, 'nivel': 'AVISO' if 'DFS996I' not in mensagem else 'INFO', 'idMensagem': mensagem.split()[1], 'mensagemCompleta': mensagem}
                dados_extraidos[lpar_atual]['alertas'].append(alerta)
        match_erro = regex_error.search(linha)
        if match_erro:
            mensagem_erro = match_erro.group(1).strip()
            alerta_erro = {'timestamp': timestamp_atual, 'nivel': 'ERRO', 'idMensagem': mensagem_erro.split()[0], 'mensagemCompleta': mensagem_erro}
            dados_extraidos[lpar_atual]['alertas'].append(alerta_erro)
    return dados_extraidos

# --- Bloco Principal de Execucao ---
if __name__ == "__main__":
    # 1. DEFINA AQUI O NOME DO SEU DATASET E PERFIL ZOWE
    # Exemplo: "IBMUSER.SYSLOG.OUTPUT" ou "CUST.PROD.LOG(0)"
    NOME_DO_DATASET = "Z14306.OUTPUT.IPLINFO" # Substitua pelo seu dataset
    NOME_DO_PERFIL_ZOWE = "Z14306" # Opcional, se nao for o default
    
    # 2. MONTAGEM DO COMANDO ZOWE
    comando_zowe = [
        "zowe", "files", "download", "ds", NOME_DO_DATASET,
        "--encoding", "1047" # Use o encoding correto (ex: 1047 para EBCDIC Latin-1)
    ]
    # Se voce usa um perfil especifico, adicione-o ao comando
    if NOME_DO_PERFIL_ZOWE:
        comando_zowe.extend(["--zosmf-profile", NOME_DO_PERFIL_ZOWE])

    try:
        print(f"Acessando o dataset '{NOME_DO_DATASET}' no mainframe via Zowe...")
        
        # 3. EXECUCAO DO COMANDO ZOWE E CAPTURA DA SAIDA
        resultado = subprocess.run(
            comando_zowe,
            capture_output=True, # Captura a saida (stdout) e erros (stderr)
            text=True,           # Decodifica a saida como texto
            check=True           # Lanca uma excecao se o comando falhar (retornar codigo != 0)
        )
        
        # O conteudo do dataset esta em 'resultado.stdout'
        dataset_mainframe = resultado.stdout
        print("Conteudo do dataset recebido com sucesso.")

        # 4. PARSING E GERACAO DO JSON (sem alteracoes aqui)
        dados_processados = extrair_informacoes_log(dataset_mainframe)
        nome_arquivo_saida = "dados_mainframe.json"
        
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(dados_processados, f, indent=4, ensure_ascii=False)

        print(f"Script finalizado! As informacoes foram salvas em '{nome_arquivo_saida}'.")

    except FileNotFoundError:
        print("ERRO: O comando 'zowe' nao foi encontrado.")
        print("   Verifique se a Zowe CLI esta instalada e no PATH do seu sistema.")
    except subprocess.CalledProcessError as e:
        print(f"ERRO ao executar o comando Zowe:")
        print(f"Comando: {' '.join(e.cmd)}")
        print(f"Codigo de Retorno: {e.returncode}")
        print(f"Mensagem de Erro (stderr):\n{e.stderr}")
    # Extrai os dados
    dados_processados = extrair_informacoes_log(dataset_mainframe)

    # Define o nome do arquivo de saida
    nome_arquivo_saida = "dados_mainframe.json"

    # Salva o dicionario em um arquivo JSON
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
        json.dump(dados_processados, f, indent=4, ensure_ascii=False)

    print(f"Script finalizado! As informacoes foram extraidas e salvas no arquivo '{nome_arquivo_saida}'.")