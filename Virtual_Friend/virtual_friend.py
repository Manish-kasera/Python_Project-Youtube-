import pyttsx3

Sachin = pyttsx3.init() # Creating an object
# msg = input("Say Something : ")
# Sachin.say("You are welcome 1") #rate 200
Sachin.runAndWait()

rate = Sachin.getProperty('rate')
print(rate)

# rate = Sachin.setProperty('rate',rate-100)
#Sachin.say("You are welcome 2") #rate 100 
Sachin.runAndWait()

Sachin.save_to_file("Hello Coder Welcome to Code for Tonight",'demo.mp3')
Sachin.runAndWait()


