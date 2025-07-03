# -*- coding: utf-8 -*-
import subprocess
import json
import textwrap

# Caminho do arquivo temporario de saida
output_file_path = "/u/z14306/iplinfo_output.txt"  # Ajuste para seu diretorio se necessario

# Lista de comandos MVS a serem executados
commands = ['D IPLINFO', 'D R,L,TN', 'D SMF', 'D TCPIP,TCPIP,NETSTAT']

# Dicionario para armazenar os resultados
results = {}

# Funcao para executar comando via tsocmd
def run_tsocmd(command):
    try:
        result = subprocess.run(
            ['tsocmd', command],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar '{command}': {e.stderr or str(e)}"

# Executa os comandos e armazena os resultados
for cmd in commands:
    print(f"Executando comando: {cmd}")
    results[cmd] = run_tsocmd(cmd)

# Converte para JSON formatado
json_output = json.dumps(results, indent=4)

# Escreve no arquivo com quebra de linha para 80 colunas
with open(output_file_path, 'w') as file:
    for line in json_output.splitlines():
        wrapped = textwrap.wrap(line, width=80)
        for wrapped_line in wrapped:
            file.write(wrapped_line + '\n')

print(f"\n Saida gravada em: {output_file_path}")
