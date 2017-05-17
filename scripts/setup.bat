@echo off&setlocal
SET current_path=%~dp0
for %%i in ("%~dp0..") do set "project_path=%%~fi"

cd %project_path%
python setup.py install
cd %current_path%
