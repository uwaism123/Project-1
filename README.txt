# Project 1 - Dockerised File Processing Pipeline

## 📌 Overview
Project 1 is a Python-based file processing system that organises files using configurable rules. 
It validates filenames, routes files by type, quarantines invalid files, archives old files, and generates summary reports.

The project is containerised using Docker for consistent execution across environments.
---

## 🚀 Features
- Filename validation using regex  
- File routing by type:
  - Images → `processed/images`
  - PDFs → `processed/invoice`
  - Text/Docs → `processed/meeting_notes`
  - CSV → `processed/exports`
- Quarantine for invalid files  
- Archive for files before year 2000  
- Summary report generation  
- Docker support with persistent storage  

---

## 📁 Project Structure

Project 1/
|
├── main.py
├── functions.py
├── config.json
├── Dockerfile
|
├── input/
├── processed/
├── quarantine/
├── archive/
├── logs/
|
├── run_file.bat
├── reset_demo_data.bat
├── backup_reports.bat
└── README.md

---

## To run in git bash 
- Have docker desktop open and download repo 
- in git bash cd "folder path"
- docker build -t project_1 .
- MSYS_NO_PATHCONV=1 docker run -v "${PWD}:/app" project_1
- should run and work.

## To run the Docker in terminal enter: 
- .\run_file.bat

---

## File Format Rules
Format: DDMMYYYY_filename.extension

Example: 25032024_testing.pdf

Rules:
- Date: 8 digits (DDMMYYYY)
- Filename: lowercase, numbers
- Extensions: pdf, csv, png, jpg, docx, txt

---

## Processing Rules

### Quarantine
Files are moved to `quarantine/` if:
- Invalid format
- Unsupported extension
- Incorrect naming

### Archive
Files with year < 2000 are moved to `archive/`

---

## Output
After processing:
- Images → `processed/images`
- Documents → `processed/meeting_notes`
- PDFs → `processed/invoice`
- CSV → `processed/exports`
- Invalid files → `quarantine`
- Old files → `archive`

Summary reports and logs are saved in `logs/` with timestamps.

---

## Testing
Tested with 100+ files including:
- Valid files across all supported formats  
- Invalid filenames and extensions  
- Pre-2000 files for archive validation  

All files were processed correctly with no runtime errors.