import subprocess

def run_mvs_command(cmd):
    full_cmd = f"opercmd '{cmd}'"
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return result.stdout

output = run_mvs_command('D IPLINFO')
print(output)
