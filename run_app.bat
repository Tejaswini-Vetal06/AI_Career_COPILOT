@echo off
title Career Copilot AI - Launcher
cd /d "%~dp0"

echo =======================================================
echo          Starting Career Copilot AI...
echo =======================================================
echo Working Directory: %CD%

:: Check if .venv python exists, otherwise fallback to system python
if exist ".venv\Scripts\python.exe" (
    echo Using Virtual Environment Python (.venv)...
    ".venv\Scripts\python.exe" -m streamlit run app.py
) else (
    echo Using System Python...
    python -m streamlit run app.py
)

pause

