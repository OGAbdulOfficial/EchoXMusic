import os

replacements = {
    r"d:\AntigravityProjects\ShrutiMusic\config.py": [
        ("ShrutixMusicBot", "EchoXMusicBot"),
        ("WTF_WhyMeeh", "OGAbdulOfficial")
    ],
    r"d:\AntigravityProjects\ShrutiMusic\EchoXMusic\__main__.py": [
        ("Shruti Music Bot", "EchoXMusic")
    ],
    r"d:\AntigravityProjects\ShrutiMusic\EchoXMusic\plugins\tools\downloader.py": [
        ("ShrutixMusic", "EchoXMusic")
    ],
    r"d:\AntigravityProjects\ShrutiMusic\EchoXMusic\plugins\bot\privacy.py": [
        ("ShrutiBotSupport", "AbdulSupportBot")
    ]
}

for filepath, reps in replacements.items():
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        for old, new in reps:
            content = content.replace(old, new)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Leftovers patched successfully.")
