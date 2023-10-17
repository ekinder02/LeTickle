from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import random
from kivy.config import Config
import time

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
Config.write()

tickles = 0

class SoundPlayer(BoxLayout):
    def play_sound(self):
        sound = SoundLoader.load('Machine-Gun-Automatic-Fire-A-www.fesliyanstudios.com (1).mp3')
        if sound:
            sound.play()
           
        
class LeTickleApp(App):
    def build(self): 
        btn = Button(text ="",
                     color =(1, 0, .65, 1),
                     background_normal = 'lebron.png',
                     background_down ='lebronBlush4.png',
                     size_hint = (.3, .3),
                     pos = (0,0),
                   ) 
        btn.bind(on_press = lambda x: self.callback(btn))
        return btn 
    #code to delay on click animatio
    
    def callback(self,btn, ):
        SoundPlayer.play_sound(self)
        animation = Animation(pos=(random.randint(0,960),random.randint(0,540)), t='in_out_back')
        animation.start(btn)
        global tickles
        tickles += 1
        if tickles > 5 and tickles <= 10:
            btn.background_normal = 'lebronBlush1.png'
        elif tickles > 10 and tickles <= 15:
            btn.background_normal = 'lebronBlush2.png'
        elif tickles > 15 and tickles <= 20:
            btn.background_normal = 'lebronBlush3.png'
        elif tickles > 20:
            btn.background_normal = 'lebronBlush4.png'

    
 
    
root = LeTickleApp() 
    
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()