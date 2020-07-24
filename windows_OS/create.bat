@echo off

cd
cd C:\Users\Vlad\Desktop\ProjectInitializationAutomation\windows_OS
pause
set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="" (
        C:\Users\Vlad\AppData\Local\Programs\Python\Python37\python.exe "C:\Users\Vlad\Desktop\ProjectInitializationAutomation\windows_OS\remote.py" %fn% %flag%
        ) else (
            if "%2"=="l" (
                C:\Users\Vlad\AppData\Local\Programs\Python\Python37\python.exe "C:\Users\Vlad\Desktop\ProjectInitializationAutomation\windows_OS\local.py" %fn%
            )
        )
    )
