from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen #not needed directly
from kivy.uix.spinner import Spinner #not needed directly in python code
from kivy.core.window import Window
from kivy.lang.builder import Builder
import webbrowser

#RGBA = Red, Green, Blue, Opacity
Window.clearcolor = (66/255, 105/255, 245/255,1)

class Erste(Screen):
   
    def aendern(self):
        if self.ids.eb.text == "Starten":
            self.manager.current = "second"
            self.ids.eb.text = "Willkommen"
        elif self.ids.eb.text == "Beenden":
            hauptgui().stop()
        else:
            pass

class Zweite(Screen):
    
    def oeffnen(self, link):
        webbrowser.open(link)
    
class Wmanager(ScreenManager):
    pass

kv = Builder.load_file("guicode.kv")

class hauptgui(App):
    def build(self):
        return kv

if __name__ == "__main__":
    hauptgui().run()
