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

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
Config.set('graphics', 'resizable', False)
Config.write()

tickles = 0
canClick = True
lastClick = 0
        
class LeTickleApp(App): 
    def build(self): 
        return(LebronLayout())
    
class SoundPlayer(BoxLayout):
    def play_sound(self):
        sound = SoundLoader.load('Cartoon Human Male Giggle - QuickSounds.com.mp3')
        if sound:
            sound.play()
    def play_sound2(self):
        sound = SoundLoader.load('Explosion+3.mp3')
        if sound:
            sound.play()
    


class LebronLayout(Widget):
    def __init__(self, **args):
        super(LebronLayout, self).__init__(**args)
    
        pb = ProgressBar(max=100,
                        center = (480,400),
                        size = (500, 500))
        pb.value = tickles
        self.add_widget(pb)
        
    
        btn = Button(text ="",
                        color =(1, 0, .65, 1),
                        background_normal = 'lebron.png',
                        background_down ='lebronBlush4.png',
                        size = (250, 250),
                        pos = (0,0),
                    ) 
        btn.bind(on_press = lambda x: self.callback(btn,pb))
        self.add_widget(btn)
        
        background = Button(background_normal='LeBackground.png',
                            background_down ='LeBackground.png',
                           size = (1200,825),
                           pos = (0,-75)
                           )
        background.bind(on_press = lambda x: self.start(background))
        self.add_widget(background)
        
    def start(self,back):
        animation= Animation(size=(0,0), t='in_out_back',d = 2)
        animation.start(back)
    def callback(self,btn,pb):
        SoundPlayer.play_sound(self)
        global canClick
        global lastClick
        currentTime = time.time()
        if currentTime - lastClick > 0.5:
            canClick = True
        if canClick == True and pb.value < 100:
            animation = Animation(pos=(random.randint(0,960),random.randint(0,400)), t='in_out_back',d = 0.5)
            animation.start(btn)
            pb.value += 5
            if pb.value > 25 and pb.value <= 50:
                btn.background_normal = 'lebronBlush1.png'
            elif pb.value > 50 and pb.value <= 75:
                btn.background_normal = 'lebronBlush2.png'
            elif pb.value > 75 and pb.value <= 99:
                btn.background_normal = 'lebronBlush3.png'
            elif pb.value >= 100:
                btn.background_normal = 'lebronBlush4.png'
                SoundPlayer.play_sound2(self)
            lastClick = time.time()
            canClick = False

root = LeTickleApp() 
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()