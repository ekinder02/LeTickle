from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation
import random

class TestWidget(BoxLayout):
    def __init__(self, **args):
        super(TestWidget, self).__init__(**args)
        aimg = AsyncImage(
            source='https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png'
        )
        self.add_widget(aimg)
        animation = Animation(pos=(random.randint(-500,500),random.randint(-500,500)), t='in_out_back')
        animation += Animation(pos=(random.randint(-500,500),random.randint(-500,500)), t='in_out_back')
        animation += Animation(pos=(random.randint(-500,500), random.randint(-500,500)), t='in_out_back')
        animation.repeat = True
        animation.start(self)


class TestApp(App):
    def build(self):
        return TestWidget()
    
TestApp().run()