import sys
import os

print("Folder creat local")
foldername = str(sys.argv[1])
mode=""
if foldername.__contains__("_"):
    mode=foldername[-2:]
    foldername=foldername[0:-3]

subfolder=""
if mode == 'py':
    subfolder='Python'
if mode == 'ja':
    subfolder='Java'
path ='C:\\Users\\Vlad\\Desktop\\gitprojects'  #os.environ.get('C:\Users\Vlad\Desktop\gitprojects')
_dir = path  +'\\'+subfolder+'\\' + foldername
try:
    os.mkdir(_dir)
    os.chdir(_dir)
    os.system('git init')
    os.system(f'echo "# {foldername}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')
    if mode=='py' :
     os.system(f'pycharm.bat {_dir} ')
    if mode=='ja' :
     os.system(f'idea.bat ')

    print(f'{foldername} created locally')
    


except:
    print("create <project_name> l")
