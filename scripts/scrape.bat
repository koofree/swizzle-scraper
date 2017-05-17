@echo off&setlocal

set PYTHONPATH=%1

SET current_path=%~dp0
for %%i in ("%~dp0..") do set "project_path=%%~fi"

cd %project_path%\python
python scraper.py %*
cd %current_path%