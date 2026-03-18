import os

file_path = r"EchoXMusic\core\call.py"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace deprecated PyTgCalls methods
code = code.replace(".join_group_call(", ".play(")
code = code.replace(".leave_group_call(", ".leave_call(")
code = code.replace(".pause_stream(", ".pause(")
code = code.replace(".resume_stream(", ".resume(")
code = code.replace(".change_stream(", ".play(")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Replaced all PyTgCalls legacy methods!")
