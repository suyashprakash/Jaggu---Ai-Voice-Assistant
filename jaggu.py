import pyttsx3
import speech_recognition as sr
import streamlit as st

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to get microphone input
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            st.write("Sorry, my speech service is down.")
            return ""


# Streamlit UI
def main():
    st.title("Jaggu - Your Voice Assistant")

    if 'name' not in st.session_state:
        st.session_state['name'] = ""

    if st.session_state['name'] == "":
        engine.say('Hello World! ')
        engine.say('Enter your name')
        engine.runAndWait()

        st.session_state['name'] = st.text_input("Enter your name:")
        if st.session_state['name']:
            engine.say('Hi mister')
            engine.say(st.session_state['name'])
            engine.say('I am Jaggu, your voice assistant cum voice to speaker developed by Mr Suyash Prakash')
            engine.runAndWait()
            st.write(
                f"Hi Mr {st.session_state['name']}, I am Jaggu your voice assistant cum voice to speaker developed by Mr Suyash Prakash.")
    else:
        engine.say("Please say the text you want me to speak")
        engine.runAndWait()
        speak = get_audio()

        if speak == 'hello':
            engine.say(speak + st.session_state['name'])
            st.write("Jaggu: " + speak + " " + st.session_state['name'])
            engine.runAndWait()

        elif speak == 'generate speech to speech':
            engine.say("sure")
            st.write("Jaggu: sure")
            engine.runAndWait()

        elif speak == 'tell me a short poem':
            engine.say("rain-rain go away, come on another day")
            st.write("Jaggu: rain-rain go away, come on another day!")
            engine.runAndWait()

        elif speak == "today's Max temperature":
            st.write(st.session_state['name'] + ": " + speak)
            engine.say(speak + " is 38 degrees")
            engine.runAndWait()
            st.write("Jaggu: " + speak + " is 38 degrees")

        elif speak == "today's cricket score":
            engine.say(
                speak + " India won the match by 7 runs. India scored 176 for 7 wickets in 20 overs, while South Africa scored 169 for 8 wickets.")
            engine.runAndWait()
            st.write(
                "Jaggu: " + speak + " is India won the match by 7 runs. India scored 176 for 7 wickets in 20 overs, while South Africa scored 169 for 8 wickets.")

        elif speak == "how r u":
            engine.say("just fine")
            st.write("Jaggu: Just fine")
            engine.runAndWait()

        elif speak == "how is your work going":
            engine.say("Amazing!")
            st.write("Jaggu: Amazing!")
            engine.runAndWait()

        elif speak == "can we have a coffee together":
            engine.say("I drink only electricity")
            st.write("Jaggu: I drink only electricity")
            engine.runAndWait()

        elif speak == "can we dinner together":
            engine.say("Yea! may be in future soon")
            st.write("Jaggu: Yes! may be in future soon")
            engine.runAndWait()

        elif speak == "your favorite color":
            engine.say("My favorite color is red")
            st.write("Jaggu: My favorite color is red")
            engine.runAndWait()

        elif speak == "your favorite food":
            engine.say("My favorite food is fried rice")
            st.write("Jaggu: My favorite food is fried rice")
            engine.runAndWait()

        elif speak == "share a quote":
            engine.say("Betrayal comes from those, Whom we trust the most!")
            st.write("Jaggu: Betrayal comes from those, Whom we trust the most!")
            engine.runAndWait()

        elif speak == "capital of Bihar":
            engine.say("Patna is the capital of Bihar")
            st.write("Jaggu: Patna is the capital of Bihar")
            engine.runAndWait()

        elif speak == "capital of Delhi":
            engine.say("New Delhi is the capital of Delhi")
            st.write("Jaggu: New Delhi is the capital of Delhi")
            engine.runAndWait()

        elif speak.lower() == 'quit':
            engine.say('Thanks you for using Me! Will miss you Bye Bye!')
            engine.runAndWait()
            st.write("Jaggu: Thanks for using Me! Will miss you Bye Bye!")


        elif speak:
            engine.say(speak)
            engine.runAndWait()


if __name__ == "__main__":
    main()
