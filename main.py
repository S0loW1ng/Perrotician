from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
import random


class GameW(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down = self.on_key_down)
        self._keyboard.bind(on_key_up = self.on_key_up)
        self.arr = []

        with self.canvas:
          self.player=   Rectangle(pos=(0,0), size=(50,60))
          self.obs = Rectangle(pos = (50,50 ), size = (70,70))
          
          self.arr.append(Rectangle(pos = (200,100),size = (40,40)))
        
        self._keyPressed = set()
        Clock.schedule_interval(self.move_sept,0)
        Clock.schedule_interval(self.move_obs,0)
        Clock.schedule_interval(self.move_obs_arr,0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.on_key_down)
        self._keyboard.unbind(on_key_up = self.on_key_up)
        self._keyboard = None

    def on_key_down(self,keyboard,keycode,text,modifiers):
        print(keycode)
        self._keyPressed.add(text)
        
    def on_key_up(self,keyboard,keycode):
        text = keycode[1]
        if text in self._keyPressed:
            self._keyPressed.remove(text)
    def move_sept(self,dt):
        cx = self.player.pos[0]
        cy = self.player.pos[1]
        nx = cx
        ny = cy
        stepsz = 100*dt
        if 'w'in self._keyPressed:
           ny = cy +stepsz
        if 's'in self._keyPressed:
            ny = cy - stepsz
        if 'a'in self._keyPressed:
            nx = cx - stepsz
        if 'd'in self._keyPressed:
            nx = cx +stepsz
        self.player.pos =(nx,ny)
    def move_obs(self,dt):
        cx = self.obs.pos[0]
        cy = self.obs.pos[1]
        nx = cx
        ny = cy

        stepx = random.randint(-100,100) * dt
        stepy = random.randint(-100,100) * dt

        nx += stepx
        ny += stepy
        self.obs.pos = (nx,ny)

    def move_obs_arr(self,dt):
        for i in self.arr:
             cx = i.pos[0]
             cy = i.pos[1]
             nx = cx
             ny = cy

             stepx = random.randint(-100,100) * dt
             stepy = random.randint(-100,100) * dt

             nx += stepx
             ny += stepy
             i.pos = (nx,ny)


class MyApp(App):
    def build(self):
        return GameW()


if __name__=="__main__":
    app = MyApp()
    app.run()

     