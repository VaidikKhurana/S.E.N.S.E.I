import pyttsx3
import speech_recognition as sr  
from colorama import Fore
import os
import datetime
import subprocess
from time import sleep
import time
import wikipedia
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame 
import requests 
from bs4 import BeautifulSoup
import pyautogui
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import socket
import colorama
from colorama import Fore, Back, Style
import serial
from time import sleep
def print_chars(text):
    for char in text:
        print(char, end='', flush=True)  # Print each character without newline
        time.sleep(0.1)  # Adjust the sleep duration to change the speed
    print()  # Print newline after the text

def print_chars_byspeed(text, speed):
    for char in text:
        print(char, end='', flush=True)  # Print each character without newline
        time.sleep(speed)  # Adjust the sleep duration to change the speed
    print()  # Print newline after the text


def play_wav(file_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    try:
        # Load the WAV file
        sound = pygame.mixer.Sound(file_path)

        # Play the sound
        sound.play()

        # Wait for the sound to finish (optional)
        pygame.time.wait(int(sound.get_length() * 1000))

    except pygame.error as e:
        print("Error playing sound:", e)
    finally:
        pygame.mixer.quit()

bootfile = "Sounds\Booting_Progress.mp3"
os.system('cls')
print_chars("starting...")


try:
    port = 'COM8'  # Replace 'COM8' with your actual port
    baud_rate = 9600  # Replace 9600 with your actual baud rate
    ser = serial.Serial(port, baud_rate)
    def rotate(angle):
        ser.write(str(angle).encode())
        sleep(0.015)
    def reset_servo():
        rotate(0) 
    os.system('cls')

   
except serial.SerialException as e:
    print("ARDUINO not detected.\n", e)
    os.system('cls')
    # Add any additional handling code here, such as logging the exception or notifying the user

 
def rotate(angle):
        ser.write(str(angle).encode())
        sleep(0.015)
    


# Initialize Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
chrome_options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
website = r"https://ttsmp3.com/text-to-speech/British2English/"
driver.get(website)
Buttonselection = Select(driver.find_element(by=By.ID, value='sprachwahl'))
Buttonselection.select_by_visible_text("British English / Brian")

# Define the speak function
def speak(*args):
    Text=""
    for i in args:
        Text+=i
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        print(Fore.RED, f"S.E.N.S.E.I : {Text}")
        print("")
        Data = str(Text)
        driver.find_element(By.ID, "voicetext").send_keys(Data)
        driver.find_element(By.ID, value="vorlesenbutton").click()
        driver.find_element(By.ID, "voicetext").clear()
        if lengthoftext >= 30:
            sleep(7)
        elif lengthoftext >= 40:
            sleep(8)
        elif lengthoftext >= 55:
            sleep(12)
        elif lengthoftext >= 70:
            sleep(14)
        elif lengthoftext >= 108:
            sleep(16)
        elif lengthoftext >= 120:
            sleep(18)
        else:
            sleep(2)

# Continue with the rest of your code...


#print letter by letter

#listen function - sr
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.YELLOW, "Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source,0,8)

    try:
        print(" Recognizing...")
        print("")
        query = r.recognize_google(audio, language="en")
        print(Fore.BLUE, f"Vaidik : {str(query).lower()}")
        return query.lower()
        
    
    except:
         return ""

def boot1():
    try:
      rotate(0)
    
    
    except NameError as ne:
        print("buffered servo: failure")
        print_chars("ignoring and proceeding.")
        os.system('cls')
        pass

    bn = """      
                                            / ____||  ____| | \ | |  / ____||  ____| |_   _|
                                            | (___  | |__    |  \| | | (___  | |__      | |  
                                            \___ \ |  __|   | . ` |  \___ \ |  __|     | |  
                                            ____) || |____ _| |\  |_ ____) || |____ _ _| |_ 
                                            |_____(_)______(_)_| \_(_)_____(_)______(_)_____|"""
    print(Fore.RED, bn)
    print(Fore.BLUE, "\n                                   Synthetic Entity Navigating Solutions and Engagements Intuitively")
    print(Fore.LIGHTRED_EX, "")
    print_chars(f"\n TIME : {datetime.datetime.now()}")
    print(Fore.YELLOW, "")
    print_chars(text=" USER : Vaidik Khurana")
    print(Fore.WHITE, "")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    sleep(3)
    
def boot2():
    bn = """      
                                            / ____||  ____| | \ | |  / ____||  ____| |_   _|
                                            | (___  | |__    |  \| | | (___  | |__      | |  
                                            \___ \ |  __|   | . ` |  \___ \ |  __|     | |  
                                            ____) || |____ _| |\  |_ ____) || |____ _ _| |_ 
                                            |_____(_)______(_)_| \_(_)_____(_)______(_)_____|"""
    print(Fore.RED, bn)
    print(Fore.BLUE, "\n                                   Synthetic Entity Navigating Solutions and Engagements Intuitively")
    print(Fore.LIGHTRED_EX, "")
    print_chars(f"\n TIME : {datetime.datetime.now()}")
    print(Fore.LIGHTMAGENTA_EX, "")
    print_chars(text=" USER : Incognito - :/")
    print(Fore.WHITE, "")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    sleep(3)


def MainExecution(query):
    Query = str(query).lower()

    # Greetings and casual conversation
    if "hello" in Query or "hi" in Query or "hey" in Query or "howdy" in Query:
        random_greetings = [
            'Greetings! How can I assist you today?',
            'Hello there! Ready to help!',
            'Hello Sir! What can I do for you?',
            'Hi Sir! How may I assist you today?',
            'Good Day Sir! How can I help?'
        ]
        speak(random.choice(random_greetings))

    elif "how are you" in Query or "how are you feeling" in Query or "are you okay" in Query or "what's up" in Query:
        random_how_are_you = [
            "I'm doing well, thank you! How can I assist you?",
            "I'm here and ready to assist you! How can I be of service?",
            "I'm feeling great! How about you? What can I help you with?",
            "I'm good, thanks for asking! What can I do for you?",
            "I'm doing fine, thank you! What can I assist you with?"
        ]
        speak(random.choice(random_how_are_you))

    # ... (incorporating other expanded functionalities)

    # Search-related queries
    if "search about" in Query or "google about" in Query or "google search about" in Query or "do a google search on" in Query or "can you search about" in Query or "can you search for" in Query:
        search_query = Query.replace("search about", "").replace("google about", "").replace("google search about", "").replace("do a google search on", "").replace("can you search for", "")
        search_responses = [
            f"Searching about {search_query} for you.",
            f"Let me find information about {search_query}.",
            f"I'll look up details about {search_query} for you.",
            f"Searching the web for information about {search_query}.",
            f"Let me find some information about {search_query}."
        ]
        speak(random.choice(search_responses))
        search_results = wikipedia.search(search_query)
        page_summary = wikipedia.summary(search_results[0])
        speak(page_summary)

    if "browse for" in Query or "browse about" in Query or "browse search about" in Query or "do a browser search on" in Query or "can you browse about" in Query or "can you browse for" in Query:
        search_query = Query.replace("browse about", "").replace("do a browser search on", "").replace("can you browse about", "").replace("do a browser search on", "").replace("can you browse for", "")
        search_responses = [
            f"Searching about {search_query} for you.",
            f"Let me find information about {search_query}.",
            f"I'll look up details about {search_query} for you.",
            f"Searching the web for information about {search_query}.",
            f"Let me find some information about {search_query}."
        ]
        link = "https://www.google.com/search?q=" + search_query
        webbrowser.open(link)


    # Weather and temperature inquiries
    if "what is the temperature" in Query or "weather" in Query or "climate" in Query or "temperature" in Query:
        weather_responses = [
            "Checking the current weather conditions for you.",
            "Let me find out the current temperature for you.",
            "I'll fetch the weather information for you.",
            "Checking the weather forecast now.",
            "Let's see what the weather looks like."
        ]
        speak(random.choice(weather_responses))
        search = "temperature in gurugram"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"Current Temperature is {temp}")

    # Time-related inquiries
    if "the time" in Query or "current time" in Query or "what time is it" in Query:
        time_responses = [
            "Fetching the current time for you.",
            "Let me tell you the current time.",
            "Checking the time for you.",
            "It's time for the current time!",
            "Let's find out the current time."
        ]
        speak(random.choice(time_responses))
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Currently the time in India is {strTime}")

    # Opening applications or performing actions
    if "open app" in Query or "can you open" in Query or "please open" in Query  or "for me" in Query or "open" in Query:
        app_to_open = Query.replace("open app", "").replace("can you open", "").replace("please open", "").replace("for me", "").replace("open", "")
        
        open_app_responses = [
            f"Opening{app_to_open} for you.",
            f"Launching{app_to_open} now.",
            f"Opening{app_to_open}.",
            f"Starting{app_to_open} as requested.",
            f"Let me open{app_to_open} for you."
        ]
        speak(random.choice(open_app_responses))
        pyautogui.press('win')
        sleep(1)
        pyautogui.typewrite(app_to_open)
        sleep(1)
        pyautogui.press('enter')

    # Memory-related functions
    if "remember that" in Query or "please remember" in Query:
        remember_query = Query.replace("remember that", "").replace("please remember", "")
        remember_responses = [
            f"Saving the information: {remember_query} to memory.",
            f"I'll remember that: {remember_query}.",
            f"Storing: {remember_query} in memory for you.",
            f"Remembering: {remember_query}.",
            f"I'll remember: {remember_query} for you."
        ]
        speak(random.choice(remember_responses))
        remember = open("Resources\Remember.txt", "a")
        remember.write(f"\n{remember_query}")
        remember.close()

    
    # Multimedia control
    if 'play video' in Query or 'pause video' in Query or 'mute video' in Query:
        multimedia_responses = [
            "Playing the requested video for you.",
            "Pausing the video as requested.",
            "Muting the video now.",
            "Performing the requested video action.",
            "Controlled the video as requested."
        ]
        speak(random.choice(multimedia_responses))
        if 'play video' in Query:
            pyautogui.press('k')
        elif 'pause video' in Query:
            pyautogui.press('k')
        elif 'mute video' in Query:
            pyautogui.press('m')

    # Actions related to browser tabs
    if "new tab" in Query or "close tab" in Query:
        tab_responses = [
            "Opening a new tab for you.",
            "Closing the current tab as requested.",
            "Performing tab-related action for you.",
            "Let's manage the tabs as requested.",
            "Handling tabs as per your request."
        ]
        speak(random.choice(tab_responses))
        if "new tab" in Query:
            pyautogui.hotkey('ctrl', 't')
        elif "close tab" in Query:
            pyautogui.hotkey('ctrl', 'w')

    # Actions related to shutting down or resting
    if "you may rest now" in Query or "quit the system" in Query or "shutdown now" in Query or "shutdown" in Query:
        shutdown_responses = [
            "Shutting down as requested.",
            "Initiating shutdown sequence.",
            "Preparing to shut down the system.",
            "Exiting the system as requested.",
            "Shutting down. Goodbye!"
        ]
        speak(random.choice(shutdown_responses))
        os.system('cls')
        strTime = datetime.datetime.now().strftime('%H:%M')
        print(f"Session ended on {strTime}")
        quit()
     
    if 'turn on the light' in Query or "switch the light on" in Query or "turn the light on" in Query or "light on please" in Query or "light on" in Query:
        speak("Initializing servo for the light to turn on.")
        try:
          rotate(130)
          speak("Light has been turned on.")
          sleep(1)
          rotate(0)
        except serial.serialutil.SerialException as e:
            speak("Servo not detected, buffering failed.")
            pass

       
    



    if "thank you" in Query or "thanks" in Query:
        thanks_responses = ["No problem Sir! Anything Else?", "Its my pleasure, what else?"]
        speak(random.choice(thanks_responses))

    if "sleep mode" in Query or "go to sleep" in Query:
        speak("Sure Sir! I will be available when you clap")
        os.system('cls')
        sleep_mode()
        

    if "get response from computer" in Query or "start remote endpoint" in Query or "generate server" in Query or "make the server online" in Query or "initiate the server" in Query or "initiate server" in Query:
       
        s = socket.socket()
        
        port = 56789
        s.bind(('', port))
        
        s.listen(5)
        start_server_responses = [
        "Initiating server startup sequence. Please wait a moment while I ensure all systems are online and operational.",
        "Acknowledged. Starting the server now. I'll notify you once the process is complete.",
        "Executing server startup protocol. This may take a few moments. Standby for confirmation.",
        "Server activation in progress. Sit tight while I bring your services online.",
        "Commencing server boot-up sequence. I'll update you once the server is up and running smoothly.",
        "Understood. I'm initiating the server startup procedure. I'll inform you once the server is ready for use.",
        "Beginning the process to start the server. I'll keep you posted on the progress.",
        "Server activation initiated. I'll notify you as soon as the server is ready for incoming requests."]

        speak(random.choice(start_server_responses))
        speak("Sir please know that my memory is very much limited, I can only comprehend any responses if my memory is free running the server prohibits that. Please standby and wait for server connection.")
        sleep(10)

        while True:
            
            c, addr = s.accept()
            print(' Got connection from', addr)
            message = ('yes')
            c.send(message.encode())
            time = datetime.datetime.now()
            speak("Received connection.")
            print(f"Time of connection: {time}" )
            MainExecution(listen())
            c.close()    
            break

def sleep_mode():
    pathsleep = 'Sleep.py' 
    subprocess.run(['python', pathsleep], check=True)

    

#MainExecution(listen())

def play_wav(file_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    try:
        # Load the WAV file
        sound = pygame.mixer.Sound(file_path)

        # Play the sound
        sound.play()

        # Wait for the sound to finish (optional)
        pygame.time.wait(int(sound.get_length() * 1000))

    except pygame.error as e:
        print("Error playing sound:", e)
    finally:
        pygame.mixer.quit()

# Replace 'your_sound_file.wav' with the path to your WAV file
wav_file_path = 'Sounds\Speak_Module_Loaded.wav'



def run1():
    play_wav(wav_file_path)
    boot1()
    
    while True:
        MainExecution(listen())

def run2():
    play_wav(wav_file_path)
    boot2()
    while True:
        MainExecution(listen())


os.system('cls')
os.system('cls')

run1()

    



