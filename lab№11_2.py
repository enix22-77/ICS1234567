import json
import shutil

drives_info = []

path = "/"
total, used, free = shutil.disk_usage(path)

drives_info.append({
    "drive": "System Disk",
    "total_gb": round(total / (1024**3), 2),
    "used_gb": round(used / (1024**3), 2),
    "free_gb": round(free / (1024**3), 2)
})

with open("disks.json", "w", encoding="utf-8") as f:
    json.dump(drives_info, f, ensure_ascii=False, indent=4)

print("Відомості про диски записано в disks.json")
