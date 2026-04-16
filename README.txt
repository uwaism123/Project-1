# FileFlow - Dockerised File Processing Pipeline

## 📌 Overview
FileFlow is a Python-based file processing system that automatically organises files based on rules defined in a configuration file. It validates filenames, routes files into appropriate folders, quarantines invalid files, archives old files, and generates summary reports.

The project is fully containerised using Docker for portability and consistent execution across environments.

---

## 🚀 Features
- File validation using regex rules
- Automatic routing by file type:
  - Images → processed/images
  - PDFs → processed/invoice
  - Text/Docs → processed/meeting_notes
  - CSV → processed/exports
- Quarantine system for invalid filenames- Archive system for files older than year 2000
- Summary report generation (processed, quarantined, archived)
- Logging system for traceability
- Dockerised execution
- Host folder mounting for persistence

        ---

        ## 📁 Project Structure

        Project 1/
        │
        ├── main.py
        ├── functions.py
        ├── config.json
        ├── Dockerfile
        │
        ├── input/
        ├── processed/
        ├── quarantine/
        ├── archive/
        ├── logs/
        │
        ├── run_file.bat
        ├── reset_demo_data.bat
        ├── backup_reports.bat├──│
        └── README.md



To run in git bash 
- have docker desktop open and download repo 
- in git bash cd "folder path"
- docker build -t project_1 .
- MSYS_NO_PATHCONV=1 docker run -v "${PWD}:/app" project_1
- should run and work.

To run the Docker in terminal enter: 
- .\run_file.bat