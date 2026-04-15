import os

def get_unique_path(path):
    base, ext = os.path.splitext(path)
    counter = 1

    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}_{counter}{ext}"
        counter += 1

    return new_path


# def generate_report(processed, quarantined, archived):
#     report_file = os.path.join(LOG_DIR, f"summary_{datetime.now():%Y%m%d_%H%M%S}.txt")

#     total = processed + quarantined + archived
#     now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#     with open(report_file, "w") as r:
#         r.write("FILE PROCESSING SUMMARY\n")
#         r.write("========================\n\n")
#         r.write(f"Generated at     : {now}\n\n")
#         r.write(f"Processed files   : {processed}\n")
#         r.write(f"Archived files    : {archived}\n")
#         r.write(f"Quarantined files : {quarantined}\n")
#         r.write(f"Total files       : {total}\n\n")
#         r.write(f"Log file          : {log_file}\n")

#     print("\n📊 SUMMARY REPORT")
#     print("========================")
#     print(f"Generated at : {now}")
#     print(f"Processed   : {processed}")
#     print(f"Archived    : {archived}")
#     print(f"Quarantined : {quarantined}")
#     print(f"Total       : {total}")
#     print(f"📄 Report: {report_file}")
