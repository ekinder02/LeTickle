from kivy.app import App
from kivy.animation import Animation
from kivy.uix.button import Button
import random
from kivy.core.audio import SoundLoader
from kivy.config import Config
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.uix.image import Image

# Set window size
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')

# Set window to not be resizable
Config.set('graphics', 'resizable', False)
Config.write()

# Set global variables
tickles = 0
canClick = True
lastClick = 0

# Create the App class
class LeTickleApp(App): 
    def build(self): 
        return(LebronLayout())

#Create the SoundPlayer class
class SoundPlayer(BoxLayout):
    #plays the giggle sound
    def play_sound(self):
        sound = SoundLoader.load('Cartoon Human Male Giggle - QuickSounds.com.mp3')
        if sound:
            sound.play()
    #plays the explosion sound
    def play_sound2(self):
        sound = SoundLoader.load('Explosion+3.mp3')
        if sound:
            sound.play()

#game functionality
class LebronLayout(Widget):
    def __init__(self, **args):
        super(LebronLayout, self).__init__(**args)

        # Create the progress bar widget
        pb = ProgressBar(max=100,
                        center = (480,400),
                        size = (500, 500))
        pb.value = tickles
        self.add_widget(pb)
        
        # Create the button widget
        btn = Button(text ="",
                        color =(1, 0, .65, 1),
                        background_normal = 'lebron.png',
                        background_down ='lebronBlush4.png',
                        size = (250, 250),
                        pos = (0,0),
                    ) 
        #makes the button do stuff when clicked
        btn.bind(on_press = lambda x: self.callback(btn,pb,end))
        self.add_widget(btn)
        
        # Create the background widget
        background = Button(background_normal='LeBackground.png',
                            background_down ='LeBackground.png',
                           size = (1200,750),
                           pos = (0,-25)
                           )
        #makes the background do stuff when clicked
        background.bind(on_press = lambda x: self.start(background))
        self.add_widget(background)
        
        # Create the end screen widget
        end = Button(background_normal='click.jpg',
                            background_down ='click.jpg',
                           size = (0,0),
                           pos = (0,-25)
                           )
        #makes the end screen do stuff when clicked
        end.bind(on_press = lambda x: self.restart(end,pb,btn))
        self.add_widget(end)
        
    #makes the background shrink when clicked
    def start(self,back):
        animation= Animation(size=(0,0), t='in_out_back',d = 2)
        animation.start(back)
        
    #makes the end screen shrink when clicked and restarts the game
    def restart(self,back,pb,btn):
        animation= Animation(size=(0,0), t='in_out_back',d = 2)
        animation&= Animation(pos=(0,-25),d = 0)
        animation.start(back)
        pb.value = 0
        btn.background_normal = 'lebron.png'
        
    #what happens when the lebron is clicked
    def callback(self,btn,pb,end):
        #plays the giggle sound
        SoundPlayer.play_sound(self)
        
        #global variables
        global canClick
        global lastClick
        
        #makes it so you can't click the button too fast
        currentTime = time.time()
        if currentTime - lastClick > 0.5:
            canClick = True
        
        #if you can click the button, it moves the button and increases the progress bar
        if canClick == True and pb.value < 100:
            #moves the button
            animation = Animation(pos=(random.randint(0,960),random.randint(0,400)), t='in_out_back',d = 0.5)
            animation.start(btn)
            
            #increases the progress bar
            pb.value += 50
            
            #changes the lebron's face based on the progress bar
            if pb.value > 25 and pb.value <= 50:
                btn.background_normal = 'lebronBlush1.png'
            elif pb.value > 50 and pb.value <= 75:
                btn.background_normal = 'lebronBlush2.png'
            elif pb.value > 75 and pb.value <= 99:
                btn.background_normal = 'lebronBlush3.png'
            #when the progress bar is full, it changes the lebron's face and plays the explosion sound
            elif pb.value >= 100:
                btn.background_normal = 'lebronBlush4.png'
                SoundPlayer.play_sound2(self)
                grow = Animation(size=(1200,700), t='in_out_back',d = 2)
                grow&= Animation(pos=(0,0),d = 0)
                grow.start(end)
            lastClick = time.time()
            canClick = False

# Run the App
root = LeTickleApp() 

root.run()