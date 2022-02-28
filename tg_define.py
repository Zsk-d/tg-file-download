from pyrogram import Client

SEARCH_CHAT_ID = 0

API_ID = 0
API_HASH = "0"

PROXY = dict(hostname="127.0.0.1", port=10809)

app = Client("my_account", API_ID, API_HASH,proxy=PROXY)
app.start()