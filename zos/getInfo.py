from zoautil_py import opercmd, datasets
import textwrap

# Nome do dataset
dataset_name = 'Z14306.OUTPUT.IPLINFO'

# Verifica se o dataset existe; se nao, cria um novo
if not datasets.exists(dataset_name):
    datasets.create(
        name=dataset_name,
        type='SEQ',
        record_format='FB',
        record_length=80,
        block_size=8000
    )

# Funcao para processar e escrever a saida no dataset
def process_and_write(command_output):
    lines = command_output.stdout_response.splitlines()
    for line in lines:
        wrapped_lines = textwrap.wrap(line, width=80)
        for wrapped_line in wrapped_lines:
            datasets.write(dataset_name, wrapped_line, append=True)

# Executa os comandos e processa as saidas
commands = ['D IPLINFO', 'D R,L,TN', 'D SMF', 'D TCPIP,TCPIP,NETSTAT']
for cmd in commands:
    output = opercmd.execute(cmd)
    process_and_write(output)
