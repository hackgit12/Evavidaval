class script(object):
    START_TXT = """π·π΄π»πΎ {},πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>
Ιͺα΄'κ± α΄ α΄Κy α΄α΄κ±y α΄α΄κ±α΄ α΄α΄α΄ α΄α΄ ΙͺΙ΄ yα΄α΄Κ Ι’Κα΄α΄α΄© α΄Ι΄α΄ α΄α΄α΄α΄ α΄α΄ α΄α΄α΄ΙͺΙ΄,
α΄Κα΄α΄κ± α΄ΚΚ Ιͺ'ΚΚ α΄©Κα΄α΄ Ιͺα΄α΄ α΄α΄α΄ Ιͺα΄κ± α΄Κα΄Κα΄ π
"""
    HELP_TXT = """β’"""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: {}
β― π²ππ΄π°ππΎπ: <a href=https://t.me/The_user_death>α΄©Κα΄κ°α΄κ±α΄Κ</a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [ π±π΄ππ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This bot is not a open source project. 

<b>DEVS:</b>
- <a href=https://t.me/The_user_death>α΄©Κα΄κ°α΄κ±α΄Κ</a>"""
    MANUELFILTER_TXT = """κ°ΙͺΚα΄α΄Κκ±

- Filter is the feature were users can set automated replies for a particular keyword and <a href=https://t.me/{}>{}</a> will respond whenever a keyword is found the message

<b>NOTE:</b>
- α΄ΚΙͺκ± Κα΄α΄ should have admin privillage.
- only admins can add filters in a chat.
- alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Buttons

- α΄ΚΙͺκ± Κα΄α΄  Supports both url and alert inline buttons.

<b>NOTE:</b>
- Telegram will not allows you to send buttons without any content, so content is mandatory.
- α΄ΚΙͺκ± Κα΄α΄  supports buttons with any telegram media type.
- Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/FILIMPIRATESGROUP)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Auto Filter

<b>NOTE:</b>
- Make me the admin of your channel if it's private.
- make sure that your channel does not contains camrips, porn and fake files.
- Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    BATCH_TXT = """
π΅πΈπ»π΄ πππΎππ΄ πΌπΎπ³ππ»π΄../


π±π πππΈπ½πΆ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎπ π²π°π½ πππΎππ΄ π΅πΈπ»π΄π πΈπ½ πΌπ π³π°ππ°π±π°ππ΄ π°π½π³ πΈ ππΈπ»π» πΆπΈππ΄ ππΎπ π° πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ ππΎ π°π²π²π΄ππ ππ·π΄ ππ°ππ΄π³ π΅πΈπ»π΄π.πΈπ΅ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ π° πΏππ±π»πΈπ² π²π·π°π½π½π΄π» ππ΄π½π³ ππ·π΄ π΅πΈπ»π΄ π»πΈπ½πΊ πΎπ½π»π πΎπ ππΎπ ππ°π½π ππΎ π°π³π³ π΅πΈπ»π΄π π΅ππΎπΌ πΏππΈππ°ππ΄ π²π·π°π½π½π΄π» ππΎπ πΌπππ πΌπ°πΊπ΄ πΌπ΄ ππ·π΄ π°π³πΌπΈπ½ πΈπ½ ππ·π΄πΈπ π²π·π°π½π½π΄π» ππΎ π°π²π²π΄ππ ππ·π΄ π΅πΈπ»π΄π..../

βͺΌ π²πΎπΌπΌπ°π½π³π π°π½π³ πππ°πΆπ΄ βΊ

β― /plink βΊβΊ ππ΄πΏπ»π ππΎ π°π½π πΌπ΄π³πΈπ° ππΎ πΆπ΄π π»πΈπ½πΊ.
β― /pbatch βΊβΊ πππ΄ ππΎππ πΌπ΄π³πΈπ° π»πΈπ½πΊ ππΈππ· ππ·πΈπ π²πΎπΌπΌπ°π½π³.
β― /batch βΊβΊ ππΎ π²ππ΄π°ππ΄ π»πΈπ½πΊ π΅πΎπ πΌππ»ππΈπΏπ»π΄ πΏπΎππ.

β ππ±ππ¦π©π₯π βΊ

/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336"""
    ALIVE_TXT = """
ALIVE MODULE
β’ /alive - check me alive or deadπ€§
Just for a rasamπ"""
    INFO_TXT = """
Information

Get information about something!

Commands and Usage:
β’ /id - get id of a specifed user.
β’ /info  - get information about a user.

NOTE:
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    CONNECTION_TXT = """α΄α΄Ι΄Ι΄α΄α΄α΄Ιͺα΄Ι΄

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """ΙͺΙ΄κ°α΄

<b>NOTE:</b>
these are the extra features of <a href=https://t.me/{}>{}</a>

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Admin α΄α΄α΄

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
* ππΎππ°π» πππ΄ππ: <code>{}</code>
* ππΎππ°π» π²π·π°ππ: <code>{}</code>
* πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
* π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
