# https://t.me/PythonAI_Bikovskiy_bot



from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import random


memes = [
    '''     /\_/\  
   =( °w° )=  
     )   (  //
    (__ __)//''',

    '''   /\___/\
  ( - _ - )
   (   -   )
   /       \
  ( /     \ )''',

    '''     /\_/\      ⚔️      /\_/\
    ( o.o )    ⚔️    ( o.o )
     > ^ <             > ^ <''',

    '''          /\_____/\ 
         /  o   o  \
        ( ==  ^  == )
         )         (
        (           )
       ( (  )   (  ) )
      (__(__)___(__)__)''',

    '''     /\_/\  
   =( °w° )=  
     )   (  //
    (__ __)//''',

    ''' ／l、
(° o ° )
じしf_,)ノ'''
]





snake_position = [5, 5]
board_size = 10

def draw_board():
    board = ""
    for y in range(board_size):
        for x in range(board_size):
            if [x, y] == snake_position:
                board += "🟩"
            else:
                board += "⬜"
        board += "\n"
    return board

async def snake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🐍 Гра почалась! Напиши /up, /down, /left або /right щоб рухатись.")
    await update.message.reply_text(draw_board())

async def move_up(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    snake_position[1] = (snake_position[1] - 1) % board_size
    await update.message.reply_text(draw_board())

async def move_down(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    snake_position[1] = (snake_position[1] + 1) % board_size
    await update.message.reply_text(draw_board())

async def move_left(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    snake_position[0] = (snake_position[0] - 1) % board_size
    await update.message.reply_text(draw_board())

async def move_right(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    snake_position[0] = (snake_position[0] + 1) % board_size
    await update.message.reply_text(draw_board())



def choice():
    return random.choice(memes)



url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")


soup_list_href = soup.find_all("a", {'class': "short-img img-fit"})
links_list = [href['href'] for href in soup_list_href]


list_name = []
list_desc = []

for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text, features="html.parser")
    soup_list_name_film = soup1.find_all('span', {"class": "oname_ua"})
    if soup_list_name_film:
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul', {"class": "short-list fx-1"})
    for item in soup_list_ul:
        list_desc.append(item.text)


command = """/help - список всіх команд бота
/hello - привітання
/film - список найновіших фільмів
/snake - змійка 
/time - час у даний момент
/meme - рандомний котячий мем ASCII art
/track - трек тижня
/random - випадкова функція
"""



async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f'{list_name[i]}\n{list_desc[i]}\n{links_list[i]}'
        await update.message.reply_text(text)
    await update.message.reply_text("Приємного перегляду 🍿")


async def song(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tracks = [
        "Imagine Dragons - Believer",
        "The Weeknd - Blinding Lights",
        "Ed Sheeran - Shape of You",
        "C152- Broken memories",
        "Linkin Park - In the end",
        "Billie Eilish - bad guy",
        "Crystal Castles - Kerosene",
    ]
    track = random.choice(tracks)
    await update.message.reply_text(f"🎶 Трек тижня:\n{track}")




async def random_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    actions = [hello, memchick, time_now, song, film, snake]
    random_action = random.choice(actions)
    await random_action(update, context)


async def time_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.now()
    await update.message.reply_text(now.strftime("%H:%M:%S"))


async def memchick(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_meme = choice()
    await update.message.reply_text(random_meme)




app = ApplicationBuilder().token("8142640011:AAH2wazr4fhROKdVUZte_QD1XRFGuZDGW9w").build()


app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))

app.add_handler(CommandHandler("time", time_now))
app.add_handler(CommandHandler("meme", memchick))
app.add_handler(CommandHandler("track", song))
app.add_handler(CommandHandler("random", random_func))
app.add_handler(CommandHandler("snake", snake))
app.add_handler(CommandHandler("up", move_up))
app.add_handler(CommandHandler("down", move_down))
app.add_handler(CommandHandler("left", move_left))
app.add_handler(CommandHandler("right", move_right))

app.run_polling()
