@echo off
echo Clearing processed folders...

rmdir /s /q processed 2>nul
rmdir /s /q quarantine 2>nul
rmdir /s /q archive 2>nul
@REM rmdir /s /q logs 2>nul

mkdir processed
mkdir quarantine
mkdir archive
@REM mkdir logs

echo Done.