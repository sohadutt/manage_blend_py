import bpy
import os
import sys

def get_main_parent(obj):
    """Recursively get top-most parent."""
    while obj.parent:
        obj = obj.parent
    return obj

def find_primary_parent_name():
    """Find main parent object name in the scene."""
    mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    if not mesh_objects:
        return None
    top_parents = list({get_main_parent(obj) for obj in mesh_objects})
    if not top_parents:
        return None
    return bpy.path.clean_name(top_parents[0].name)

def main():
    # First command-line argument passed from driver script: original file path
    original_filepath = sys.argv[-1]  # last argument
    directory = os.path.dirname(original_filepath)

    # Load file
    bpy.ops.wm.open_mainfile(filepath=original_filepath)

    new_name = find_primary_parent_name()
    if not new_name:
        print(f"❌ No parent object found in: {original_filepath}")
        return

    new_filename = f"{new_name}.blend"
    new_filepath = os.path.join(directory, new_filename)

    if new_filepath != original_filepath:
        # Save the file with the new name
        bpy.ops.wm.save_as_mainfile(filepath=new_filepath)
        os.remove(original_filepath)
        print(f"✅ Renamed: {os.path.basename(original_filepath)} → {new_filename}")
    else:
        print(f"✔️ Already correctly named: {new_filename}")

if __name__ == "__main__":
    main()
