import sys
import os
from github import Github

print("folder creat remote")

foldername = str(sys.argv[1])
mode=""
if foldername.__contains__("_"):
    mode=foldername[-2:]
    foldername=foldername[0:-3]

subfolder = ""
if mode == 'py':
    subfolder = 'Python'
if mode == 'ja':
    subfolder = 'Java'

path = "C:\\Users\\Vlad\\Desktop\\gitprojects"   #os.environ.get('C:\Users\Vlad\Desktop\gitprojects')         # add projects dirctory to the env vars
token ="d02e35e3bdeab22f3e56e3e5bdce42cf987e4300"       #os.environ.get('gt')        # add github token to the env vars
_dir = path  +'\\'+subfolder+'\\' + foldername

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']
if mode == 'py':
    commands.append(f'pycharm.bat {_dir} ')
if mode == 'ja':
    commands.append(f'idea.bat  ')

os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
   os.system(c)


print(f'{foldername} created locally')



