import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning shahnawaz sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon shahnawaz sir!")
    else:
        speak("good evening shahnawaz sir!")
    speak(" I am jarvis ,My system speed is 64 core TR3990x,version 2.1, please tell  me sir how may i help you")
#
#
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("please say that again...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourgmailgmail.com","yourpassword")
    server.sendmail("yourgmailgmail.com",to,content)
    server.close()


if __name__ == "__main__":
        wishme()
        while(True):
            query=takecommand().lower()
            if 'wikipedia' in query:
                speak('searching wikipeida.....')
                query=query.replace('wikipedia'," ")
                results= wikipedia.summary(query,sentences=2)
                speak('Acoording to wikipedia')
                speak(results)
                print(results)

            elif 'open youtube 'in query:
                speak("Be ready sir we are going to open youtube for you")
                webbrowser.open('youtube.com')


            elif 'open google 'in query:
                speak("Be ready sir we are going to open google for you")
                webbrowser.open('google.com')



            elif 'play music 'in query:
                music_dir='C:\\music'
                songs=os.listdir(music_dir)
                print(songs)
                speak("Be ready sir we are going to play best song for you")
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time ' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is {strTime}")

            elif "open code" in query:
                codepath="C:\\Users\\Shahnawaz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("be ready sir we are going to open  visual studio code for you for you ")
                os.startfile(codepath)
            elif 'email to shahnawaz' in query:
                try:
                    speak("what shuld is say sir")
                    content=takecommand()
                    to="receivermail@gmail.com"

                    sendEmail(to,content)
                    speak("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry sir , i am not able to send this email")

            elif " open calculator" in query:
                code="C:\\Users\\Shahnawaz\\AppData\\Local\\Programs\\latest calculator Installer\\smartcalculater.exe"
                speak("Be ready sir we are going to open smart calculator for you")
                os.startfile(code)



            elif "quit" in query:
                speak("ok sir,our system going to shutdown this program,thank you for giving me your special time,please takecare of yourself ")
                exit()
