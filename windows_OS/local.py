import sys
import os

print("Folder creat local")
foldername = str(sys.argv[1])
path ='C:\\Users\\Vlad\\Desktop\\gitprojects'  #os.environ.get('C:\Users\Vlad\Desktop\gitprojects')
_dir = path + '/' + foldername

try:
    os.mkdir(_dir)
    os.chdir(_dir)
    os.system('git init')
    os.system(f'echo "# {foldername}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')

    print(f'{foldername} created locally')
    os.system('code .')


except:
    print("create <project_name> l")
