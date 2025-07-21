import subprocess
import os

# Define each path and the command to run there
tasks = [
    {
        "path": r"C:\Users\lenovo\Desktop\Backend\my-django\mydjango",
        "command": 'python manage.py runserver'
    }
]

# Launch each command in its own terminal window
for task in tasks:
    path = task["path"]
    cmd = task["command"]
    if os.path.exists(path):
        subprocess.Popen(f'start cmd /K "cd /d {path} && {cmd}"', shell=True)
    else:
        print(f"Directory does not exist: {path}")
