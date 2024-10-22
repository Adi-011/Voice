import speech_recognition as sr
import os
import pyttsx3
import datetime
import wikipedia
from openai import OpenAI


engine = pyttsx3.init()

chatStr = ""
def chat(query):
    client = OpenAI()
    global chatStr
    print(chatStr)
    chatStr += f"user: {query}\n voice: "

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    client = OpenAI()
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write email for resignation\n"
            },
            {
                "role": "user",
                "content": "how are you "
            },
            {
                "role": "assistant",
                "content": "i am fine"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to recognize speech
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


# Function to greet
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Voice. How may I assist you?")


# Main function
def main():
    greet()
    while True:
        query = listen()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube sir ")
            os.system("start https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            os.system("start https://www.google.com")
        elif 'open chrome' in query:
            speak("Opening Chrome")
            os.system('start chrome "" --kiosk')
        elif 'the time' in query:
            hor = datetime.datetime.now().strftime("%H")
            mine = datetime.datetime.now().strftime("%M")
            speak(f"The time is{hor} hour {mine} minutes")
        elif 'weather' in query:
            speak("so today's weather is as follows: ")
            os.system("start https://www.google.com/search?q=weather+of+today&gs_ivs=1#tts=0")
        elif 'goodbye' in query:
            speak("Goodbye! and take care")
            break

        elif "Using AI".lower() in query:
            ai(prompt=query)

        elif "reset chat".lower() in query:
            chatStr = ""

        else:

            speak("Sorry, I couldn't understand that")

if __name__ == "__main__":
    main()
