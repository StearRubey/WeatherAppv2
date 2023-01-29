from ParseData import parse_data
import tkinter as tk
from kivy.properties import NumericProperty

county_data = parse_data()

import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App



from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp

from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarker
from kivy_garden.mapview import MapSource



from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


def show_home(hwid, mwid):
  hide_widget(mwid)
  hide_widget(hwid, dohide=False)

def show_map(hwid, mwid, map):
  hide_widget(hwid)
  hide_widget(mwid, dohide=False)
  longitude = NumericProperty(-105.7821)
  latitude = NumericProperty(39.5501)
  map.root.center_on(latitude, longitude)
  

def hide_widget(wid, dohide=True):
    if hasattr(wid, 'saved_attrs'):
        if not dohide:
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
            wid.size_hint_y = 20
            del wid.saved_attrs
    elif dohide:
        wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
        wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True


class MyApp(App):
    def build(self):
      Window.size = (900 , 700)
      root = GridLayout(cols = 2)
      Scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
      layout = GridLayout(cols = 2)
      mapLayout = GridLayout(cols = 1)
      map = MapView(zoom=7, lat= 39.5501, lon= -105.7821, map_source = MapSource(max_zoom = 10, min_zoom = 7))
      marker = MapMarker(lat= 39.5501, lon= -105.7821, source = "Checkmark.png")
      map.add_marker(marker)


      mapLayout.add_widget(map)
      layout.size_hint_y= None
      layout.padding = 40
      layout.spacing = 30
      homeButton = Button(text = "home", size_hint_y = 20)
      mapButton = Button(text = "map", size_hint_y = 20)
      layout.bind(minimum_height=layout.setter('height'))#checks when window maximized
      nav = GridLayout(cols = 1, size_hint_x=None, width=100)
      content = GridLayout(cols = 1)
      content.add_widget(Scroll)
      content.add_widget(mapLayout)
      nav.add_widget(homeButton)
      nav.add_widget(mapButton)
      root.add_widget(nav)
      root.add_widget(content)

      hide_widget(Scroll)
      hide_widget(mapLayout)
      homeButton.bind(on_press = lambda x: show_home(Scroll, mapLayout))
      mapButton.bind(on_press = lambda x: show_map(Scroll, mapLayout, map))




      for county in county_data:
        #print(f"county: {county['name']}\t\trestriction: {county['restriction']}")
        layout.add_widget(Label(text = county["name"]))

        if(county["restriction"] == True):
          layout.add_widget(Label(text = "fire restriction active"))
        else:
          layout.add_widget(Label(text = "no fire restriction"))
      Scroll.add_widget(layout)
      root.pos_hint = {'center_x':0.5,'top': 1}
      return root


if __name__ == '__main__':
    MyApp().run()

