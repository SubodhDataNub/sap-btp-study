@echo off
title BTP Study Site
rem Starts the local study site and opens it in your browser. Close this window (or press Ctrl+C) to stop it.
where python >nul 2>nul
if %errorlevel%==0 (
  python "%~dp0site\serve.py" %*
) else (
  py "%~dp0site\serve.py" %*
)
pause
