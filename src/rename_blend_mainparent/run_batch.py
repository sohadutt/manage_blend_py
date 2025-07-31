import os
import subprocess

blender_path = "C:/Program Files/Blender Foundation/Blender 4.5/blender.exe" 
blend_folder = "C:/Users/pc/Desktop/trimlight/8733 Series"
script_path = "C:/Users/pc/Desktop/trimlight/batch_rename_blends_by_parent.py"

for filename in os.listdir(blend_folder):
    if filename.lower().endswith(".blend"):
        filepath = os.path.join(blend_folder, filename)
        subprocess.run([
            blender_path,
            "--background",
            "--python", script_path,
            "--", filepath
        ])
