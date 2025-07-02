import webbrowser as wb
import time
import pyfiglet as pfg
import random
import emoji
#welcome message
heading = pfg.figlet_format("Web Archive")
print(heading)
print("_" * 60)
time.sleep(1)
print("Archive for all the essential websites you'd need.")
print("This tool is meant to help you find the exact websites you'll need to get your work done!")
print("-" * 60)
print("Choose the websites provided below and enter their code to launch them.")
print("")
#website dicription and code
print("[1] FMHY(Free Media Heck Yeah)")
print("-" * 30)
print("# Collection of many websites in itself including torrenting, downloading, streaming etc.")
print()
print("[2] Virus Total")
print("-" * 30)
print("# Scan for virus in any file under 650MB. Simple drag and drop interface.")
print()
print("[3] Wallheaven")
print("-" * 30)
print("# Download high quality wallpapers for desktop.")
print()
print("[4] Preplexity AI")
print("-" * 30)
print("# Google on steriods. A powerful search engine for research and brainstorming.")
print()
time.sleep(2)
print("[5] Deviant Art")
print("-" * 30)
print("# Discover art, themes, skins, icons and wallpaper for desktop.")
print()
print("[6] Steam Underground")
print("-" * 30)
print("# Download steam games(free/paid)")
print()
print("[7] Internet Archive")
print("-" * 30)
print("# Another website for downloading anything.")
print() 
print("[8] Flash Museum")
print("-" * 30)
print("# Website for playing many old school and retero games online.")
print()
time.sleep(3)
print("[9] Riddlewot")
print("-" * 30)
print("# Solve riddles created by thousands of people.")
print()
print("[10] Neal.fun")
print("-" * 30)
print("# A very random website containing cool and interesting games.")
print()
print("[11] Read something interesting")
print("-" * 30)
print("# Randomly directs you to an interesting article on the internet.")
print("[12] Line Rider")
print("-" * 30)
print("# Draw and ride on own path.")
print()
print("[r] Surpirise me!")
print("-" * 30)
print("Randomly opens a website mentioned above.")
print()
#website choices
try:
	print("Type 'r' if you want to randomly open a website.")
	print()
	code = int(input("Enter the website code written before the name.: "))
	print("-" * 60)
except ValueError: #random website code generation
	code = random.randint(1 , 13)
if code == 1:
	print("Opening FMHY...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://fmhy.net/")
elif code == 2:
	print("Opening Virus Total...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://www.virustotal.com/gui/home/upload")
elif code == 3:
	print("Opening Wallheaven...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("wallhaven.cc")
elif code == 4:
	print("Opening Preplexity AI...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://www.perplexity.ai/")
elif code == 5:
	print("Opening Deviant Art...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("www.deviantart.com")
elif code == 6:
	print("Opening Steam Underground...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://steamunderground.net")
elif code == 7:
	print("Opening Internet Archive...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://archive.org/")
elif code == 8:
	print("Opening Flash Museum...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb,open("https://flashmuseum.org/")	
elif code == 9:
	print("Opening Riddlewot...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://www.riddlewot.com/")
elif code == 10:
	print("Opening Neal fun...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://neal.fun/")
elif code == 11:
	print("Opening Read something interesting...")
	print("Press esc to cancel.")
	time.sleep(3)
	wb.open("https://readsomethinginteresting.com/")
elif code == 12:
	print("Opening Line rider...")
	print("Press esc to cancel.")
	time.sleep(2)
	wb.open("https://www.linerider.com/")
elif code > 12:
	print("You know, maybe try putting a vaid website code next time smartypants.")
print()
#closing message
if code <=12 and code >= 1:
	thanksmsg = pfg.figlet_format("Thanks!" , font = "doom")
	print("")
	messages = [
	    "Done. May your downloads be fast and your distractions few.",
	    "Mission accomplished, Captain! Websites deployed.",
	    "All done! Stay curious and keep exploring.",
	    "Everything's launched. You deserve a cookie.",
	    "One click at a time, you're getting smarter.",
	    "Nothing left to launch. Except maybe your career.",
	    "Website launched. Now go waste your time like a champ!",
	    "Spoon feeding done! Time to go get some work done.",

	]

	print(random.choice(messages))
	print(thanksmsg)
else:
	duh = pfg.figlet_format("Nice Try Diddy!")
	print(duh)
	print("With love, from the dev.")
print("Made with hardwork, stress and questionalble sleep cycles.")
print(emoji.emojize(":smiling_face_with_hearts:"))