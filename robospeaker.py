import pyttsx3
x = pyttsx3.init()
x.setProperty('rate', 150)  # slower/faster
x.setProperty('voice', x.getProperty('voices')[3].id)  # select voice
while(True):
    command=input("Enter what you want to say\n")
    if(command!="quit"):
        x.say(command)
        x.runAndWait()
    else:
        x.say("Exiting the program")
        x.runAndWait()
        break
