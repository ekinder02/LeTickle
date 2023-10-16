from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation
from kivy.uix.button import Button
import random
        
class ButtonApp(App): 
        
    def build(self): 
        btn = Button(text ="",
                     color =(1, 0, .65, 1),
                     background_normal = 'lebron.png',
                     background_down ='lebron2.jpg',
                     size_hint = (.3, .3),
                     pos_hint = {"x":0.35, "y":0.3}
                   ) 
     
        return btn 
            
    
root = ButtonApp() 
    
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()