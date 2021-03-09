import os
import subprocess

myenv = os.environ.copy()
myenv['PATH'] = os.pathsep.join(['/opt/myapp', myenv['PATH']])

result = subprocess.run(['export'])
