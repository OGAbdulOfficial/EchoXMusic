import os
import shutil

repo_dir = r"d:\AntigravityProjects\EchoXMusic"

# 1. Global Text Replacement
def replace_in_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        return
    
    new_content = content.replace("EchoXMusic", "EchoXMusic")
    new_content = new_content.replace("EchoXMusic", "EchoXMusic") # catch any remaining
    new_content = new_content.replace("https://github.com/OGAbdulOfficial/EchoXMusic", "https://github.com/OGAbdulOfficial/EchoXMusic")
    new_content = new_content.replace("OGAbdulOfficial", "OGAbdulOfficial")
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

for root, dirs, files in os.walk(repo_dir):
    if ".git" in root or "__pycache__" in root or "venv" in root:
        continue
    for file in files:
        if file.endswith((".py", ".md", ".yml", ".txt", ".env", "Dockerfile", "Procfile", ".json")):
            replace_in_file(os.path.join(root, file))

# 2. Rename the package directory
old_pack_dir = os.path.join(repo_dir, "EchoXMusic")
new_pack_dir = os.path.join(repo_dir, "EchoXMusic")

if os.path.exists(old_pack_dir):
    os.rename(old_pack_dir, new_pack_dir)
    print("Renamed directory EchoXMusic -> EchoXMusic")

print("Rebranding text replacements completed successfully.")
