import os

import requests
from W2HBOT.utils import admin_cmd, sudo_cmd


@bot.on(admin_cmd(pattern="picgen"))
@bot.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return

    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
        with open("W2HBOT.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By W2HBOT."
    fole = "W2HBOT.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/W2HBOT.jpg ")
