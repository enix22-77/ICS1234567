    f.write("\n".join(whl_files))

with open("zip.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(zip_files))

print("Імена файлів успішно записано у py.txt, whl.txt та zip.txt")
