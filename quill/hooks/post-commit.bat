@echo off
REM --- Quill Git Hook (Windows) ---

REM Check if this is the first commit
for /f %%i in ('git rev-list --count HEAD') do set COMMIT_COUNT=%%i
if %COMMIT_COUNT% LSS 1 exit /b 0

REM Run Quill via installed CLI
echo --- Quill is starting up ---
quill run