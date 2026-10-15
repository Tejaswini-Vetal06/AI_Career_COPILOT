@echo off
title Career Copilot AI - FastAPI Backend
cd /d "%~dp0"

echo =======================================================
echo     Starting Career Copilot AI Backend (Port 8008)...
echo =======================================================
echo Swagger UI will be available at: http://localhost:8008/docs

:: Check if .venv python exists, otherwise fallback to system python
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" -m uvicorn api:app --port 8008 --reload
) else (
    python -m uvicorn api:app --port 8008 --reload
)

pause

