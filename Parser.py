# https://t.me/PythonAI_Bikovskiy_bot
from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import random



a = '''     /\_/\  
   =( °w° )=  
     )   (  //
    (__ __)//
'''

b = '''   /\___/\
  ( - _ - )
   (   -   )
   /       \
  ( /     \ )
'''

c = '''     /\_/\      ⚔️      /\_/\
    ( o.o )    ⚔️    ( o.o )
     > ^ <             > ^ <
'''

d = '''          /\_____/\
         /  o   o  \
        ( ==  ^  == )
         )         (
        (           )
       ( (  )   (  ) )
      (__(__)___(__)__)
'''


e = '''     /\_/\  
   =( °w° )=  
     )   (  //
    (__ __)//
'''

f =''' ／l、
(° o ° )
 じしf_,)ノ
'''

def choice():
    meme_list = [a, b, c, d, e, f]  # no curly braces, just variables
    random_meme = random.choice(meme_list)  # random.choice should work now
    return random_meme







url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
f = open("Link.txt", "w", encoding="utf-8")
soup_list_href = soup.find_all("a", {'class':"short-img img-fit"})
for href in soup_list_href:
    # print(href['href'])
    f.write(f"{href['href']}\n")


f.close()
links_list = []
with open("link.txt", "r") as file:
    links_list = file.readlines()
# print(links_list)
f = open("info.txt", 'w', encoding = "utf8")
list_name = []
list_desc = []



for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text, features="html.parser")
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    # print(soup_list_name_film)
    if len(soup_list_name_film)>0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)


f.close()

command = """/help - список всіх команд бота
/hello - привітання
/film - список найновіших фільмів
/calculato місті зараз
/track - трек тижня
/time - час у данний момент
/meme - рандомний котячий мем ASCII art
/random - випадкова функція
"""









async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f'{list_name[i]}\n{list_desc[i]}\n{links_list[i]}'
        await update.message.reply_text(text)
    await update.message.reply_text("Приємного перегляду🍿")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("1")

# async def song(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     for p in range(len(links_list2)):
#         text = f'{list_name2[p]}\n{list_desc2[p]}\n{links_list2[p]}'
#         await update.message.reply_text(text)
#     await update.message.reply_text("2")

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.now()
    await update.message.reply_text(now.strftime("%H:%M:%S"))

async def memchick(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_meme = choice()
    await update.message.reply_text(random_meme)


# async def random(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("5")

app = ApplicationBuilder().token("8142640011:AAH2wazr4fhROKdVUZte_QD1XRFGuZDGW9w").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("weather", weather))
# app.add_handler(CommandHandler("track", song))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("meme", memchick))
# app.add_handler(CommandHandler("random", random))


app.run_polling()






