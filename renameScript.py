import os

def rename_files_with_custom_name(folder_path, custom_name):
    files = sorted(os.listdir(folder_path))
    count = 1

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1]
            new_name = f"{custom_name}_{count}{ext}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(file_path, new_path)
            print(f"Renamed: {file} → {new_name}")
            count += 1

# Example Usage:
folder = "~/Sample"
custom_name = "Salathai"  
rename_files_with_custom_name(folder, custom_name)
