import pyttsx3
import os
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr

def wish():
	hour = int(datetime.datetime.now().hour) 		#it will give the hour value from the current time
	if(hour>=0 and hour<12):
		pyttsx3.speak("Hi!Good Morning Boss..")
	elif(hour>=12 and hour<18):
		pyttsx3.speak("Hi!Good Afternoon Boss..")
	else:
		pyttsx3.speak("Hi!Good Evening Boss..")

def time():
	strTime = datetime.datetime.now().strftime("%H:%M:%S") #it will tell the current time and strftime formats the time in H:M:S
	pyttsx3.speak(f"Boss,The Time is {strTime}")
	print(f"{strTime}")

def takeCommand():
		r = sr.Recognizer()
		sr.Microphone()
		with sr.Microphone() as source:
			pyttsx3.speak('I am listening boss... please wait till i recognize your voice boss...')
			print("listening..")
			r.pause_threshold = 1
			audio = r.listen(source)
		try:
			pyttsx3.speak('recognizing ...')
			print("recognizing..")
			p = r.recognize_google(audio, language="en-in")
			print(f"User said:{p}\n")
		except Exception as e:
			print("say that again please..")
			return "None"
		return p
	
def songs():
	print("Here is your Playlist:")
	print("1.Jatta Jatti da Crush - Kay Vee Singh\n2.Death bed - Powfu\n3.Moscow-mashuka - Honey Singh")
	print("4.Lover - Taylor Swift\n5.Lal Bindi-Akull")
	print("Which song you want to play:")
	pyttsx3.speak("Which song you want to play:")

	ch = input().lower()

	pyttsx3.speak("Playing your song..")

	if("death bed" in ch or "death" in ch or "bed" in ch):
		webbrowser.open("https://youtu.be/FkuZ2mOs1sA")
	elif("lal bindi" in ch or "bindi" in ch or "lal" in ch):
		webbrowser.open("https://youtu.be/PAW_Gd3QVww")
	elif("suka" in ch or "moscow" in ch or "mashuka" in ch):
		webbrowser.open("https://youtu.be/oCwh2H_qcdY")
	elif("jatta" in ch or "jatti" in ch or "crush" in ch):
		webbrowser.open("https://youtu.be/qckMuki39xI")
	elif("lover" in ch):
		webbrowser.open("https://youtu.be/sIsXIJ9k8aA")
	else: 
		print("Try again Boss!!")
		pyttsx3.speak("Try again Boss!!")

if __name__ == "__main__":
	wish()
	print("```````````````---------------------------------------------------``````````````")
	print("```````````````------------------->>LARA<<------------------------``````````````")
	print("```````````````---------------------------------------------------``````````````")
	pyttsx3.speak("Welcome here!!I am your personal assistance Laara!!! How can i help you Boss?? ")
	print()
	print("Here are the things i can launch for you ")
	pyttsx3.speak("here are the things i can launch for you-")
	print("Time\nDate\nWikipedia search\nChrome\nYoutube\nPlaylist\nGoogle\nFacebook\nEditor\nVLC Media Player\nMicrosoft Edge\nControl Panel\nSublime Text Editor\nCommand Prompt\nExit")
	print()
	pyttsx3.speak("would you like to type or speak Boss?")
	print("How would you like to Communicate boss???")
	print("Choose (1 or 2)\n 1.Typing\n 2.Microphone\n")
	a = int(input())

	if a == 1:
		while True:
			p=input("Type anything you want to run/open:").lower()

			if( "donot" in p or "not" in p or "dont" in p or "don't" in p or "no" in p or "never" in p or "do nothing" in p):
				pyttsx3.speak("Ok Boss... Not running!!")
				
			elif("lara" in p or "hey" in p or "assistance" in p):
				pyttsx3.speak("I am here to listen to you!!") 

			elif( "time" in p):
				time()

			elif("date" in p):
				pyttsx3.speak("Boss the date is")
				pyttsx3.speak(f"{datetime.datetime.now():%Y-%m-%d}")
				print(f"{datetime.datetime.now():%Y-%m-%d}")
			
			elif ("google chrome" in p or "chrome" in p):
				pyttsx3.speak("Launching your chrome"),os.system("chrome")

			elif( "editor" in p or "texteditor" in p):
					pyttsx3.speak("Launching your notepad"),os.system("notepad")

			elif( "vlc" in p or "media player" in p or "music player" in p ):
					pyttsx3.speak("Launching your vlc media player"),os.system("vlc")

			elif("microsoft edge" in p or "edge" in p or "browser" in p ):
					pyttsx3.speak("Launching your microsoft edge browser"), os.system("microsoftedge")

			elif( "cmd" in p or "command prompt" in p or "prompt" in p ):
					pyttsx3.speak("Launching your command prompt"),os.system("cmd")

			elif( "yt" in p or "youtube.com" in p or "youtube" in p ):
					pyttsx3.speak("Launching your youtube"),os.system('start chrome "www.youtube.com"')

			elif( "fb" in p or "facebook.com" in p or "facebook" in p ):
					pyttsx3.speak("Launching your facebook"),webbrowser.open("www.facebook.com")
					
			elif( "control panel" in p or "panel" in p or "control" in p or "settings" in p  ):
					pyttsx3.speak("Launching your control pannel"),os.system("control panel")

			elif( "google" in p or "google.com" in p or "www.google.com" in p ):
					pyttsx3.speak("Launching your google.com"),os.system('start chrome "www.google.com"')

			elif( "sublime text" in p or "sublime editor" in p or "sublime text editor" in p or "sublime" in p or "subl" in p  ):
					pyttsx3.speak("Launching your sublime text editor"),os.system("subl")

			elif("song" in p or "playlist" in p):
					songs()

			elif( "wikipedia" in p or "search" in p or "wiki" in p) :
					pyttsx3.speak("searching..")
					p= p.replace("wikipedia", " ")
					p= p.replace("search", " ")
					results = wikipedia.summary(p, sentences= 2)
					print(results)
					pyttsx3.speak("According to wiki" +results)	
				
			elif("exit" in p) or ("quit" in p ) or ("close" in p) or ("break" in p) or ("shut down" in p ):
				pyttsx3.speak("Exiting!!See you again Boss.. Good bye...")
				break

			else:
				pyttsx3.speak("Not supported!! please try again Boss")
			
	else:
		while True:
			pyttsx3.speak('what can i do for you boss??')
			print('what can i do for you boss??')

			p = takeCommand().lower()

			if( "donot" in p or "not" in p or "dont" in p or "don't" in p or "no" in p or "never" in p or "do nothing" in p):
				pyttsx3.speak("Ok Boss... Not running!!")
			
			elif("lara" in p or "hey" in p or "assistance" in p):
				pyttsx3.speak("I am here to listen to you!!") 

			elif( "time" in p):
				time()

			elif("date" in p):
				pyttsx3.speak("Boss the date is")
				pyttsx3.speak(f"{datetime.datetime.now():%Y-%m-%d}")
				print(f"{datetime.datetime.now():%Y-%m-%d}")
			
			elif ("google chrome" in p or "chrome" in p):
				pyttsx3.speak("Launching your chrome"),os.system("chrome")

			elif( "editor" in p or "texteditor" in p):
				pyttsx3.speak("Launching your notepad"),os.system("notepad")

			elif( "vlc" in p or "media player" in p or "music player" in p ):
				pyttsx3.speak("Launching your vlc media player"),os.system("vlc")

			elif("microsoft edge" in p or "edge" in p or "browser" in p ):
				pyttsx3.speak("Launching your microsoft edge browser"), os.system("microsoftedge")

			elif( "cmd" in p or "command prompt" in p or "prompt" in p ):
				pyttsx3.speak("Launching your command prompt"),os.system("cmd")

			elif( "yt" in p or "youtube.com" in p or "youtube" in p ):
				pyttsx3.speak("Launching your youtube"),os.system('start chrome "www.youtube.com"')

			elif( "fb" in p or "facebook.com" in p or "facebook" in p ):
				pyttsx3.speak("Launching your facebook"),webbrowser.open("www.facebook.com")
					
			elif( "control panel" in p or "panel" in p or "control" in p or "settings" in p  ):
				pyttsx3.speak("Launching your control pannel"),os.system("control panel")

			elif( "google" in p or "google.com" in p or "www.google.com" in p ):
				pyttsx3.speak("Launching your google.com"),os.system('start chrome "www.google.com"')

			elif( "sublime text" in p or "sublime editor" in p or "sublime text editor" in p or "sublime" in p or "subl" in p  ):
				pyttsx3.speak("Launching your sublime text editor"),os.system("subl")

			elif("song" in p or "playlist" in p):
				songs()

			elif( "wikipedia" in p or "search" in p or "wiki" in p) :
				pyttsx3.speak("searching..")
				p= p.replace("wikipedia", " ")
				p= p.replace("search", " ")
				results = wikipedia.summary(p, sentences= 2)
				print(results)
				pyttsx3.speak("According to wiki" +results)	
				
			elif("exit" in p) or ("quit" in p ) or ("close" in p) or ("break" in p) or ("shut down" in p ):
				pyttsx3.speak("Exiting!!See you again Boss.. Good bye...")
				break

			else:
				pyttsx3.speak("Not supported!! please try again Boss")
					

			