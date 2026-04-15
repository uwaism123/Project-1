import os, shutil, re, logging
from datetime import datetime

# --- Config ---
INPUT = "input"
PROCESSED = "processed/other"
QUARANTINE = "quarantine"
LOG_DIR = "logs"

os.makedirs(PROCESSED, exist_ok=True)
os.makedirs(QUARANTINE, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# --- Logging ---
log_file = os.path.join(LOG_DIR, f"fileflow_{datetime.now():%Y%m%d_%H%M%S}.log")
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

VALID_PATTERN = re.compile(r"^\d{8}_[a-z]+_[a-z0-9\-]+\.(pdf|csv|png|jpg|docx|txt)$")

def validate(filename):
    return bool(VALID_PATTERN.match(filename))

def process():
    files = [f for f in os.listdir(INPUT) if os.path.isfile(os.path.join(INPUT, f))]
    valid, invalid = 0, 0
    for f in files:
        src = os.path.join(INPUT, f)
        if validate(f):
            shutil.move(src, os.path.join(PROCESSED, f))
            logging.info(f"VALID → processed: {f}")
            valid += 1
        else:
            shutil.move(src, os.path.join(QUARANTINE, f))
            logging.warning(f"INVALID → quarantine: {f}")
            invalid += 1
    print(f"\n✅ Processed: {valid} | ❌ Quarantined: {invalid}")
    print(f"📄 Log: {log_file}")

if __name__ == "__main__":
    process()