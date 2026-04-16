@echo off
set "DIR=%cd%"
docker run -v "%DIR%:/app" project_1