import os, shutil, re, logging
from datetime import datetime

# --- Config ---
INPUT = "input"
PROCESSED = "processed"
QUARANTINE = "quarantine"
ARCHIVE = "archive"

LOG_DIR = "logs"

FOLDERS = {
    "png": "processed/images",
    "jpg": "processed/images",
    "txt": "processed/meeting_notes",
    "docx": "processed/meeting_notes",
    "pdf": "processed/invoice",
    "csv": "processed/exports",
}

os.makedirs(PROCESSED, exist_ok=True)
os.makedirs(QUARANTINE, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(ARCHIVE, exist_ok=True)

for folder in set(FOLDERS.values()):
    os.makedirs(folder, exist_ok=True)

# --- Logging ---
log_file = os.path.join(LOG_DIR, f"fileflow_{datetime.now():%Y%m%d_%H%M%S}.log")
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")



# New version with filename pattern
VALID_PATTERN = re.compile(r"^\d{8}_[a-z0-9\-]+\.(pdf|csv|png|jpg|docx|txt)$")

def validate(filename):
    return bool(VALID_PATTERN.match(filename))



def process():
    files = [f for f in os.listdir(INPUT) if os.path.isfile(os.path.join(INPUT, f))]
    processed, quarantined, archived = 0, 0, 0

    for f in files:
        src = os.path.join(INPUT, f)

        if validate(f):
            date_part = f.split("_")[0]
            year = int(date_part[4:])

            if year < 2000:
                shutil.move(src, os.path.join(ARCHIVE, f))
                logging.info(f"ARCHIVE (<2000) → archive: {f}")
                archived += 1
                continue

            ext = f.split(".")[-1].lower()
            dest_folder = FOLDERS.get(ext, PROCESSED)

            shutil.move(src, os.path.join(dest_folder, f))
            logging.info(f"{ext.upper()} → {dest_folder}: {f}")
            processed += 1

        else:
            shutil.move(src, os.path.join(QUARANTINE, f))
            logging.warning(f"INVALID → quarantine: {f}")
            quarantined += 1

    return processed, quarantined, archived


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

if __name__ == "__main__":
    #process()
    processed, quarantined, archived = process()
    generate_report(processed, quarantined, archived)



def clear_folders():
    folders_to_clear = set(FOLDERS.values())

    for folder in folders_to_clear:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                file_path = os.path.join(folder, f)

                if os.path.isfile(file_path):
                    os.remove(file_path)