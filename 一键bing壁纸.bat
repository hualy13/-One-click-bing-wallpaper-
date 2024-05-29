@echo off
rem 查找 Python 可执行文件的路径，并根据路径包含特定驱动器来选择 Python 环境
for /f "delims=" %%i in ('where python ^| findstr /i "C:"') do (
    set "python_path=%%i"
)

rem 如果 C: 盘中没有找到 Python 环境，则尝试在 D: 盘中寻找
if not defined python_path (
    for /f "delims=" %%i in ('where python ^| findstr /i "D:"') do (
        set "python_path=%%i"
    )
)

rem 如果任何驱动器中都没有找到 Python 环境，则给出提示
if not defined python_path (
    echo No Python executable found in C: or D: drive.
    pause
    exit /b
)
rem 自己添加python
::set python_path=your python path
set script_path=%~dp0bizhiisbing.py 

REM 添加到任务计划程序之系统启动触发器
schtasks /create /tn "Bing Wallpaper Update" /tr "%python_path% %script_path%" /sc onstart /delay 0001:00
