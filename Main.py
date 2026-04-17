import json
import os, shutil, re, logging
from functions import get_unique_path
from datetime import datetime


with open("config.json", "r") as f:
    config = json.load(f)

# --- Config --- Takes from config.json and converts to variables
INPUT = config["input"]
PROCESSED = config["processed"]
QUARANTINE = config["quarantine"]
ARCHIVE = config["archive"]
LOG_DIR = config["log_dir"]

FOLDERS = config["folders"]

# --- Setup --- Create necessary folders if they don't exist.
os.makedirs(PROCESSED, exist_ok=True)
os.makedirs(QUARANTINE, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(ARCHIVE, exist_ok=True)

for folder in set(FOLDERS.values()):
    os.makedirs(folder, exist_ok=True)

# --- Logging --- Time, folder, info and file name in log file.
log_file = os.path.join(LOG_DIR, f"fileflow_{datetime.now():%Y%m%d_%H%M%S}.log")
logging.basicConfig(
        filename=log_file,
            level=logging.INFO,
                format="%(asctime)s | %(levelname)s | %(message)s"
                )




# file format with ddmmyyyy, name, and the extension.
VALID_PATTERN = re.compile(r"^\d{8}_[a-z0-9\-]+\.(pdf|csv|png|jpg|docx|txt)$")

# quick check for file format, and used in process function.
def validate(filename):
    return bool(VALID_PATTERN.match(filename))


# main processing function that checks files, moves them, and logs actions. Returns counts for report generation.
def process():
    files = [f for f in os.listdir(INPUT) if os.path.isfile(os.path.join(INPUT, f))]
    processed, quarantined, archived = 0, 0, 0

    for f in files:
        src = os.path.join(INPUT, f)

        if validate(f): # if file is valid, check year and move accordingly.
            date_part = f.split("_")[0]
            year = int(date_part[4:])

            if year < 2000: # if year is less than 2000, move to archive.
                #shutil.move(src, os.path.join(ARCHIVE, f))
                dest_path = get_unique_path(os.path.join(ARCHIVE, f))
                shutil.move(src, dest_path)
                logging.info(f"ARCHIVE (<2000) → archive: {f}")
                archived += 1
                continue # skip further processing for archived files.

            ext = f.split(".")[-1].lower() # get file extension and determine destination folder.
            dest_folder = FOLDERS.get(ext, PROCESSED)

            dest_path = get_unique_path(os.path.join(dest_folder, f))
            shutil.move(src, dest_path)
            logging.info(f"{ext.upper()} → {dest_folder}: {f}")
            processed += 1

        else: # if file is invalid, move to quarantine.
            dest_path = get_unique_path(os.path.join(QUARANTINE, f))
            shutil.move(src, dest_path)
            logging.warning(f"INVALID → quarantine: {f}")
            quarantined += 1

    return processed, quarantined, archived

# generates a summary report with counts of processed, quarantined, and archived files.
def generate_report(processed, quarantined, archived): 
    report_file = os.path.join(LOG_DIR, f"summary_{datetime.now():%Y%m%d_%H%M%S}.txt")

    total = processed + quarantined + archived
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(report_file, "w") as r:
        r.write("FILE PROCESSING SUMMARY\n")
        r.write("========================\n\n")
        r.write(f"Generated at     : {now}\n\n")
        r.write(f"Processed files   : {processed}\n")
        r.write(f"Archived files    : {archived}\n")
        r.write(f"Quarantined files : {quarantined}\n")
        r.write(f"Total files       : {total}\n\n")
        r.write(f"Log file          : {log_file}\n")

    print("\n📊 SUMMARY REPORT")
    print("========================")
    print(f"Generated at : {now}")
    print(f"Processed   : {processed}")
    print(f"Archived    : {archived}")
    print(f"Quarantined : {quarantined}")
    print(f"Total       : {total}")
    print(f"📄 Report: {report_file}")

# --- Main execution ---
if __name__ == "__main__":
    processed, quarantined, archived = process() #
    generate_report(processed, quarantined, archived)


# Testing function to clear all folders before running the main process.
def clear_folders():
    folders_to_clear = set(FOLDERS.values())

    for folder in folders_to_clear:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                file_path = os.path.join(folder, f)

                if os.path.isfile(file_path):
                    os.remove(file_path)

#clear_folders()
