import difflib
import os
import subprocess

os.makedirs('.venv',exist_ok=True)  # pysidedeploy.spec:python_path ← https://stackoverflow.com/questions/57919110/how-to-set-pipenv-venv-in-project-on-per-project-basis
os.system('pipenv -q update')
with open('pysidedeploy.template','r') as f: template = f.read()
spec = template.format(
    pythonpath = subprocess.run(args='pipenv -q --py', capture_output=True).stdout.decode('utf-8').strip(),
    venv =  subprocess.run(args='pipenv -q --venv', capture_output=True).stdout.decode('utf-8').strip(),
)
with open('pysidedeploy.spec','w') as f: f.write(spec)
# with open('pysidedeploy.test','w') as f: f.write(spec)
os.makedirs('build',exist_ok=True)  # pysidedeploy.spec:exec_directory
os.system('pipenv -q run pyside6-deploy --config-file pysidedeploy.spec')# --extra-ignore-dirs .venv')
with open('pysidedeploy.spec','r') as f: readback = f.read()
assert readback == spec, '`pyside6-deploy` unexpectedly changed `pysidedeploy.spec`. Here are the differences:\n'+'\n'.join(difflib.unified_diff(spec.splitlines(),readback.splitlines()))
