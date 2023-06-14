import datetime
from pydub import AudioSegment
from pydub.playback import play
import vonage

time_str = input('Enter the alarm (HH:MM:SS): ')
time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()

alarm = AudioSegment.from_mp3('Sounds/hi.mp3')
play(alarm)

while True:
    now = datetime.datetime.now().time()
    if now == time:
        medcine = AudioSegment.from_mp3('Sounds/doaa.mp3')
        play(medcine)
        # client = vonage.Client(key="d5a62ecb", secret="KZktAdsmH7IOiMyU")
        # sms = vonage.Sms(client)
        # responseData = sms.send_message(
        # {
        # "from": "Dua'a",
        # "to": "962780727316",
        # "text": "Hi,, you should take your Drugs!!!",
        # }
        #  )

        
        # client = vonage.Client(
        # application_id="ed3ab8a8-39d9-4a84-8ef1-8b336a09517f",
        # private_key="private.key",
        # )   
        # voice = vonage.Voice(client)

        # response = voice.create_call({
        #     'to': [{'type': 'phone', 'number': "962780727316"}],
        #     'from': {'type': 'phone', 'number': "962780727316"},
        #     'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
        # })

    if now > time:
        break
    
