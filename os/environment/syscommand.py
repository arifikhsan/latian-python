import subprocess

subprocess.run(['date'])
subprocess.run(['sleep', '2'])

result = subprocess.run(['ls', 'notexists'])
print(result.returncode)
