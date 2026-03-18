import os

# Define the root of the project
root_dir = r"D:\AntigravityProjects\EchoXMusic"

# Replacement Map
# (Old String, New String)
replacements = [
    ("EchoXMusic", "EchoXMusic"),
    ("EchoXMusic", "EchoXMusic"),
    ("EchoXMusic", "EchoXMusic"),
    ("abdulbotz.site", "abdulbotz.site"), # Example fallback
    ("OGAbdulOfficial", "OGAbdulOfficial"),
    ("EchoXMusic", "EchoXMusic"),
    ("EchoXMusicBot", "EchoXMusicBot"),
    ("OGAbdulOfficial", "OGAbdulOfficial"),
    ("AbdulSupportBot", "AbdulSupportBot")
]

# Files to exclude from scrubbing (e.g., git history, binaries, sessions)
exclude_dirs = {".git", "__pycache__", "venv", "cache"}
exclude_extensions = {".png", ".jpg", ".jpeg", ".session", ".pyc", ".ttf", ".svg"}

def perform_global_rebrand():
    count = 0
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip excluded extensions
            if any(file_path.endswith(ext) for ext in exclude_extensions):
                continue

            try:
                # Read with utf-8, fallback to latin-1 if fails
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(file_path, "r", encoding="latin-1") as f:
                        content = f.read()
                
                original_content = content
                for old, new in replacements:
                    content = content.replace(old, new)
                
                if content != original_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Patched: {file_path}")
                    count += 1
            except Exception as e:
                print(f"Error patching {file_path}: {e}")
    
    # Special Handling for the SVG because I actually WANT to patch its XML text
    svg_path = os.path.join(root_dir, "EchoXMusic", "assets", "equalizer.svg")
    if os.path.exists(svg_path):
        try:
            with open(svg_path, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace("EchoXMusic", "EchoXMusic")
            with open(svg_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Patched SVG: {svg_path}")
            count += 1
        except Exception:
            pass

    print(f"Rebranding complete. Total files modified: {count}")

if __name__ == "__main__":
    perform_global_rebrand()
