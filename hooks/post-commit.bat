@echo off

REM Get commit count
for /f %%i in ('git rev-list --count HEAD') do set COMMIT_COUNT=%%i

if %COMMIT_COUNT% LSS 2 (
    exit /b 0
)

REM Current commit
for /f %%i in ('git rev-parse HEAD') do set CURRENT_COMMIT=%%i

REM Previous commit
for /f %%i in ('git rev-parse HEAD~1') do set PREVIOUS_COMMIT=%%i

echo current_commit=%CURRENT_COMMIT%
echo previous_commit=%PREVIOUS_COMMIT%

echo changed_files:
git diff --name-only HEAD~1 HEAD
