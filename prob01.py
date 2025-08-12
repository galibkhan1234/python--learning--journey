import pyttsx3
import pyjokes
# This code imports the pyjokes library to get a joke and prints it along with some
engine = pyttsx3.init()
engine.say("Goodbye!Why do Java programmers have to wear glasses? Because they don't C#..")
engine.runAndWait()
print("This is another test message.")
print("Goodbye!")  # Added a goodbye message
pyjokes=pyjokes.get_joke()  # This line is not needed here
print(pyjokes)  # This will print the joke fetched from pyjokes
