@echo off

REM 1. Get the root directory of the repo
for /f "tokens=*" %%i in ('git rev-parse --show-toplevel') do set REPO_ROOT=%%i

REM 2. Check if it's the first commit
for /f %%i in ('git rev-list --count HEAD') do set COMMIT_COUNT=%%i
if %COMMIT_COUNT% LSS 1 (
    exit /b 0
)

REM 3. Trigger Quill
echo --- Quill is starting up ---
python "%REPO_ROOT%\main.py" run