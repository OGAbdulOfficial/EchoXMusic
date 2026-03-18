import os

repo_dir = r"d:\AntigravityProjects\ShrutiMusic"

for root, _, files in os.walk(repo_dir):
    if ".git" in root or "__pycache__" in root or "venv" in root:
        continue
    for file in files:
        if file.endswith((".py", ".md", ".yml", ".txt", ".env", ".json")):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue
            
            new_content = content.replace("EchoXMusicBot", "EchoXMusicBot")
            new_content = new_content.replace("EchoXMusic", "EchoXMusic")
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

print("EchoXMusicBot references removed globally.")
