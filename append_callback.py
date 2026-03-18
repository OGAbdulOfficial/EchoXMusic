filepath = r"d:\AntigravityProjects\EchoXMusic\EchoXMusic\plugins\admins\callback.py"
with open(filepath, "a", encoding="utf-8") as f:
    f.write("\n\n@app.on_callback_query(filters.regex('ahh_soon'))\n")
    f.write("async def ahh_soon_cb(client, CallbackQuery):\n")
    f.write("    await CallbackQuery.answer('ahh soon ~', show_alert=True)\n")
print("Callback appended.")
