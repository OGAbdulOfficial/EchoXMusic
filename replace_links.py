import os

directory = r"d:\AntigravityProjects\EchoXMusic"

for root, _, files in os.walk(directory):
    if ".git" in root or "__pycache__" in root:
        continue
    for file in files:
        if file.endswith((".py", ".yml", ".md", ".txt")):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    content = f.read()
                except UnicodeDecodeError:
                    continue
            
            new_content = content.replace("https://t.me/AbdulSupportBot", "https://t.me/AbdulSupportBot")
            new_content = new_content.replace("https://t.me/AbdulBotzOfficial", "https://t.me/AbdulBotzOfficial")
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

print("Replacement complete!")
