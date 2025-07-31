import os
from collections import defaultdict

def find_blend_files_grouped_by_prefix(root_folder):
    groups = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".blend"):
                name_without_ext = os.path.splitext(filename)[0]
                parts = name_without_ext.split("_", 1)
                if parts[0].isdigit() and len(parts[0]) == 4:
                    prefix = parts[0]
                else:
                    prefix = "Unknown"
                groups[prefix].append(name_without_ext)

    # Sort each group
    for key in groups:
        groups[key].sort()

    return dict(sorted(groups.items()))  # Sort groups by prefix

# 📂 Target folder
target_folder = r"C:\Users\pc\Desktop\trimlight"

# 📄 Output file
output_file = os.path.join(target_folder, "list_blend_files.txt")

# 🔍 Collect grouped data
grouped_files = find_blend_files_grouped_by_prefix(target_folder)

# 📝 Write to .txt
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"Target folder: {target_folder}\n")
    f.write("🗂️ Categorized .blend file names:\n\n")

    total = 0
    for prefix, names in grouped_files.items():
        f.write(f"[{prefix}] ({len(names)} files):\n")
        for name in names:
            f.write(f" - {name}\n")
        f.write("\n")
        total += len(names)

    f.write(f"📦 Total .blend files: {total}\n")

print(f"✅ Done. Categorized list saved to:\n{output_file}")
