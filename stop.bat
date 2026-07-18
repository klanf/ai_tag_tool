@echo off
cd /d "%~dp0"
echo 正在停止 AI 绘图标签分类工具服务器...
netstat -ano | findstr :8080 > nul
if %errorlevel% equ 0 (
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8080') do (
        taskkill /F /PID %%a > nul
        echo 已终止进程 PID: %%a
    )
) else (
    echo 未找到运行中的服务器进程
)
echo 完成！
timeout /t 2 /nobreak > nul
