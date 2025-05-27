@echo off
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

call .venv\Scripts\activate.bat

if "%~1"=="" (
    python main.py
) else (
    python main.py "%~1"
)

echo 処理が完了しました。Enterキーを押して終了してください...
pause > nul
