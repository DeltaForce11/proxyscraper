from kivy.app import App
import requests
from bs4 import BeautifulSoup as bs
from kivy.core.audio import SoundLoader
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random
class ProxyScraper(App):
	def build(self):
		self.bl = RelativeLayout()
		Window.clearcolor = (1,1,1,1)
		self.logo = Image(source='hawk.png',size=(100,100),pos=(10,280))
		self.countrys = ["DE","US","FR","FI"]
		self.location = "US"
		self.country =  Label(text="[color=000000][b]Country:[/b] [u]{}[/u][/color]".format(self.location),markup=True,pos=(10,-400))
		
		self.text = Label(text="[b][color=#3b4044]Proxy Scraper v.1[/color][/b]",font_size=60,pos=(10,130),markup=True)
		self.alttext = Label(text="[u][color=000000]Coded By DeltaF0rceX[/color][/u]",font_size=30,pos=(10,80),markup=True)
		self.btn1 = Button(text="[b]HTTP[/b]",size_hint=(0.6,None),height=80,pos=(150,600),markup=True,background_color=(0,0,0,1))
		self.btn2 = Button(text="[b]HTTPS[/b]",size_hint=(0.6,None),height=80,pos=(150,500),markup=True,background_color=(0,0,0,1))
		self.btn3 = Button(text="[b]Socks4[/b]",size_hint=(0.6,None),height=80,pos=(150,400),markup=True,background_color=(0,0,0,1))
		self.btn4 = Button(text="[b]Socks5[/b]",size_hint=(0.6,None),height=80,pos=(150,300),markup=True,background_color=(0,0,0,1))
		self.backbtn = Button(text="[b]Back[/b]",size_hint=(0.6,None),height=80,pos=(150,200),markup=True,background_color=(0,0,0,1))
		self.btn1.bind(on_press=self.httpclicked)
		self.btn2.bind(on_press=self.httpsclicked)
		self.btn3.bind(on_press=self.socks4clicked)
		self.btn4.bind(on_press=self.socks5clicked)
		
		self.backbtn.bind(on_press=self.returnback)
		self.bl.add_widget(self.logo)
		self.bl.add_widget(self.text)
		self.bl.add_widget(self.alttext)
		self.bl.add_widget(self.country)
		self.bl.add_widget(self.btn1)
		self.bl.add_widget(self.btn2)
		self.bl.add_widget(self.btn3)
		self.bl.add_widget(self.btn4)
	

		return self.bl
	

	
	def removeitems(self):
		 self.bl.remove_widget(self.btn1)
		 self.bl.remove_widget(self.btn2)
		 self.bl.remove_widget(self.btn3)
		 self.bl.remove_widget(self.btn4)

				 
	def httpclicked(self,instance):
		 self.results = TextInput(text="",multiline=True,size_hint=(0.6,0.3),pos=(150,300))
		 self.clicksound = SoundLoader.load('click.wav')
		 self.clicksound.play()
		 self.response = requests.get("https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country={}".format(self.location))
		 self.bl.add_widget(self.results)
		 self.bl.add_widget(self.backbtn)
		 self.results.text = self.response.content
		
		 	
		 
		 
	def httpsclicked(self,instance):
		 self.results = TextInput(text="",multiline=True,size_hint=(0.6,0.3),pos=(150,300))
		 self.clicksound = SoundLoader.load('click.wav')
		 self.clicksound.play()
		 self.response = requests.get("https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country={}".format(self.location))
		 self.removeitems()
		 self.bl.add_widget(self.results)
		 self.bl.add_widget(self.backbtn)
		 self.results.text = self.response.content
		 
	def socks4clicked(self,instance):
		 self.results = TextInput(text="",multiline=True,size_hint=(0.6,0.3),pos=(150,300))
		 self.clicksound = SoundLoader.load('click.wav')
		 self.clicksound.play()
		 self.response = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite&country={}".format(self.location))
		 self.removeitems()
		 self.bl.add_widget(self.results)
		 self.bl.add_widget(self.backbtn)
		 self.results.text = self.response.content
		 
	def socks5clicked(self,instance):
		 self.results = TextInput(text="",multiline=True,size_hint=(0.6,0.3),pos=(150,300))
		 self.clicksound = SoundLoader.load('click.wav')
		 self.clicksound.play()
		 self.response = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite&country={}".format(self.location))
		 self.removeitems()
		 self.bl.add_widget(self.results)
		 self.bl.add_widget(self.backbtn)
		 self.results.text = self.response.content
	
	def returnback(self,instance):
		self.removeitems()
		self.bl.add_widget(self.btn1)
		self.bl.add_widget(self.btn2)
		self.bl.add_widget(self.btn3)
		self.bl.add_widget(self.btn4)
		self.bl.remove_widget(self.results)
		self.bl.remove_widget(self.backbtn)
		


		

if __name__ == "__main__":
	ProxyScraper().run()