import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import smtplib
from email.message import EmailMessage

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'atharvshamra796@gmail.com'  # Replace with your email address
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your email provider's SMTP server and port
        server.starttls()  # Upgrade the connection to a secure, encrypted SSL/TLS connection
        server.login('atharvsharma796@gmail.com', '123@Tharv')  # Replace with your email login credentials
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
        engine.say("Email sent successfully")
        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")
        engine.say("Failed to send the email")
        engine.runAndWait()

while True:  # Continuous listening loop
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust recognizer sensitivity to ambient noise
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Set a timeout of 5 seconds
            text = recognizer.recognize_google(audio).lower()
            print("You said: " + text)

            if "stop" in text or "exit" in text:
                print("Exiting the program.")
                break

            elif "what's the weather" in text:
                engine.say("Please specify the city name.")
                engine.runAndWait()
                with sr.Microphone() as city_source:
                    print("Listening for city name...")
                    city_audio = recognizer.listen(city_source)
                    city_name = recognizer.recognize_google(city_audio).lower()
                    print("City Name: " + city_name)
                    # Call get_weather() function and handle weather information here

            elif "what's the time" in text:
                current_time = datetime.datetime.now().strftime("%H:%M %p")
                engine.say(f"The current time is {current_time}")
                engine.runAndWait()

            elif "what's the date" in text:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                engine.say(f"Today's date is {current_date}")
                engine.runAndWait()

            elif "what was the date yesterday" in text:
                yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
                formatted_date = yesterday.strftime("%Y-%m-%d")
                engine.say(f"Yesterday's date was {formatted_date}")
                engine.runAndWait()

            elif "open notepad" in text:
                subprocess.Popen(["notepad.exe"])
                engine.say("Opening Notepad")
                engine.runAndWait()

            elif "send email" in text:
                engine.say("Please provide the email subject.")
                engine.runAndWait()
                with sr.Microphone() as email_subject_source:
                    print("Listening for email subject...")
                    email_subject_audio = recognizer.listen(email_subject_source)
                    email_subject = recognizer.recognize_google(email_subject_audio)
                    engine.say("Please provide the email body.")
                    engine.runAndWait()
                    with sr.Microphone() as email_body_source:
                        print("Listening for email body...")
                        email_body_audio = recognizer.listen(email_body_source)
                        email_body = recognizer.recognize_google(email_body_audio)
                        engine.say("Please provide the recipient's email address.")
                        engine.runAndWait()
                        with sr.Microphone() as email_recipient_source:
                            print("Listening for recipient's email address...")
                            email_recipient_audio = recognizer.listen(email_recipient_source)
                            email_recipient = recognizer.recognize_google(email_recipient_audio)
                            send_email(email_subject, email_body, email_recipient)
            elif "open microsoft edge" in text:
                subprocess.Popen("start msedge",shell=True)
                engine.say("Opening Microsoft Edge")
                engine.runAndWait()

            elif "open youtube in microsoft edge" in text:
                url = "https://www.youtube.com"
                cmd=f'start msedge "{url}"'
                subprocess.Popen(cmd,shell=True)
                engine.say("Opening YouTube in Microsoft Edge")
                engine.runAndWait()



            elif "Open Valorant" in text:
                cmd = r'start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\Valorant"'
                subprocess.Popen(cmd, shell=True)
                engine.say("Opening Valorant")
                engine.runAndWait()




        except sr.WaitTimeoutError:
            print("No speech detected within the timeout.")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
        except Exception as e:
            print(f"Error: {e}")

