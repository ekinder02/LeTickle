from kivy.app import App
from kivy.animation import Animation
from kivy.uix.button import Button
import random
from kivy.config import Config
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
import time

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
Config.write()

tickles = 0
canClick = True
lastClick = 0
        
class LeTickleApp(App): 
    def build(self): 
        return(LebronLayout())

          
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
    
    def callback(self,btn,pb):
        global canClick
        global lastClick
        currentTime = time.time()
        if currentTime - lastClick > 5:
            canClick = True
        if canClick == True:
            animation = Animation(pos=(random.randint(0,960),random.randint(0,400)), t='in_out_back',d = 0.5)
            animation.start(btn)
            pb.value += 5
            if pb.value > 25 and pb.value <= 50:
                btn.background_normal = 'lebronBlush1.png'
            elif pb.value > 50 and pb.value <= 75:
                btn.background_normal = 'lebronBlush2.png'
            elif pb.value > 75 and pb.value <= 100:
                btn.background_normal = 'lebronBlush3.png'
            elif pb.value > 100:
                btn.background_normal = 'lebronBlush4.png'
            lastClick = time.time()
            canClick = False

root = LeTickleApp() 
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()