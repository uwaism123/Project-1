@echo off
echo Backing up logs...

mkdir backup 2>nul
xcopy logs backup\logs /E /I /Y

echo Backup complete.