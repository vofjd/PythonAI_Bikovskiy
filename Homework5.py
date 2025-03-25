class Computer:
    def work(self, tasks):
        print(f"Working with programs: {tasks}")

print("---------------------------------------")
class PC(Computer):
    def internet(self):
        print("Downloading images from the net")
        print('''      .----------------.  
     |  (^_^)/ 💖      |  
     |  [  💾  ] [🖱️]  |  
     '----------------'  
        ||        ||  
      [____]    [____] '''
)
        print('''   ✨(◕ᴗ◕)✨ 📡  
  /[ 💙🤖💙 ]\ ~📶  
    |     |  
    U     U  '''
)
        print('''  (\_/)   📡  
  (o w o) ~📶  
  /[ 🤖 ]\  
   |  ||  |  
   U     U '''
)
        print("Success!")

print("---------------------------------------")
class GamingPC(PC):
    def ultra_graphics_games(self):
        print(f"Playing games at 200 FPS : {games}")
        print("""
              _______       _______       _______
             /       \\     /       \\     /       \\
            |  O   X  |   |  ◄  ▲  ► |   |  ▼   □  |
             \\_______/     \\_______/     \\_______/
                | |           | |           | |
               [===]         [===]         [===]
             /       \\     /       \\     /       \\
            |  START  |   |  SELECT |   |  PAUSE  |
             \\_______/     \\_______/     \\_______/
        """)


programs = 'Browser, Downloader, File Manager, Office'
games = 'Shooter, Building, Strategy, Team'

user = GamingPC()
user.work(programs)
user.internet()
user.ultra_graphics_games()
