import pyttsx3
import os
import webbrowser
import wikipedia
import pytube
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

def songs():
	print("1.jatta jatti da crush - kay vee singh\n2.death bed - powfu\n3.Moskow-suka - Honey Singh")
	print("4.Lover - Taylor Swift\n5.ghgh")
	print("which song you want to play:")

	ch = input().lower()

	if("death bed" in ch):webbrowser.open("https://youtu.be/FkuZ2mOs1sA")
	elif("lal bindi" in ch):webbrowser.open("https://youtu.be/PAW_Gd3QVww")
	elif("suka" in ch):webbrowser.open("https://youtu.be/oCwh2H_qcdY")
	elif("jatta" in ch):webbrowser.open("https://youtu.be/qckMuki39xI")
	elif("lover" in ch):webbrowser.open("https://youtu.be/sIsXIJ9k8aA")
	else: print("not supported")

def fun():
	while True:
		p=input("Type anything you want to run/open:").lower()

		if( "donot" in p or "not" in p or "dont" in p or "don't" in p or "no" in p or "never" in p or "do nothing" in p):pyttsx3.speak("Ok Boss... Not running!!")
		
		elif("lara" in p or "hey" in p or "assistance" in p):
			pyttsx3.speak("I am here to listen to you!!") 

		elif( "time" in p):
			time()
	
		elif ("google chrome" in p or "chrome" in p):
			pyttsx3.speak("Launching your chrome"),os.system("chrome")

		elif( "editor" in p or "notepad" in p or "texteditor" in p):
			pyttsx3.speak("Launching your notepad"), os.system("notepad")

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

		elif( "sublime text" in p or "sublime editor" in p or "sublime text editor" in p or "sublime" in p  ):
			pyttsx3.speak("Launching your sublime text editor"),os.system("subl")

		elif("song" in p or "playlist" in p):
			songs()
				
		elif("exit" in p) or ("quit" in p ) or ("close" in p) or ("break" in p) or ("shut down" in p ):
			pyttsx3.speak("Exiting!!See you again Boss.. Good bye...")
			break

		elif( "wikipedia" in p or "search" in p) :
			pyttsx3.speak("searching..")
			p= p.replace("wikipedia", " ")
			p= p.replace("search", " ")
			results = wikipedia.summary(p, sentences= 2)
			print(results)
			pyttsx3.speak("According to wiki" +results)
			
		else:
			pyttsx3.speak("Not supported!! please try again Boss")

if __name__ == "__main__":
	wish()
	print("```````````````---------------------------------------------------``````````````")
	print("```````````````------------------->>LARA<<------------------------``````````````")
	print("```````````````---------------------------------------------------``````````````")
	pyttsx3.speak("Welcome here!!I am your personal assistance Laara!!! How can i help you Boss?? ")
	print()
	print("Here are the things i can launch for you ")
	pyttsx3.speak("here are the things i can launch for you-")
	print("Time\nWikipedia search\nChrome\nYoutube\nPlaylist\nGoogle\nFacebook\nNotepad\nVLC Media Player\nMicrosoft Edge\nControl Panel\nSublime Text Editor\nCommand Prompt\nExit")
	print()
	pyttsx3.speak("would you like to type or speak Boss?")
	print("would you like to type or speak Boss?")
	print("Choose (1 or 2)\n 1.Typing\n 2.Microphone\n")
	a = int(input())

	if a == 1:
		fun()
	else:
		pyttsx3.speak('what can i do for you boss??')
		print('what can i do for you boss??')
		r = sr.Recognizer()
		sr.Microphone()
		with sr.Microphone() as source:
			audio = r.listen(source)
			pyttsx3.speak('I am listening boss... please wait till i recognize your voice boss...')
			print(audio)
			pyttsx3.speak('recognizing done ..')
			print('recognizing done ..')
		p = r.recognize_google(audio)
		fun()

		