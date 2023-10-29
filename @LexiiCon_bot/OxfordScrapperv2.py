import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
import requests
from bs4 import BeautifulSoup
from pprint import pprint

async def main():
    # Get a message from the user
    msg = await bot.getUpdates()

    # Process the message
    handle(msg)


#IMPT HANDLE FUNCTIONNN
#The msg parameter represents the incoming message from a user of the telegram bot.
async def handle(msg):
    global chat_id #Storing chat ID of telegram user globally

    #useful variables extracted from user's msg
    content_type, chat_type, chat_id = telepot.glance(msg)

    # Log variables FOR DEBUGGING 
    print(content_type, chat_type, chat_id)

    pprint(msg) #displays info in dict form

    #telegram's user in case i want to address them
    username = msg['chat']['first_name']

    # Check that the content type is text and not the starting
    if content_type == 'text':
        if msg['text'] != '/start':
            text = msg['text']
            text = text.strip().lower()
            await get_Def(text)


def get_meaning(doc):

    try:
        meaning=doc.find("span",class_="def").text.capitalize().strip()
        meaning="Definition: " + meaning
    
    except:
        meaning="Meaning not found"

    return meaning

def get_example(doc):

    try:
        example=doc.find("span",class_="x")

        if example:


            example=example.text.capitalize().strip()
            example="Example: " + example

        else:

            example2=doc.find("span",class_="cl")

            example="Example: "+ example2.text.capitalize().strip()

    except:
        example="Examples not found"
    
    return example

def get_audio(doc):
    try:

        mp3=doc.find("div",class_="sound audio_play_button pron-uk icon-audio")["data-src-mp3"]

    except:
        mp3="Audio not available"
    
    return mp3


async def get_Def(word):
    baseurl = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"

    #your user agent or get it from https://user-agents.net/random
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    r = requests.get(baseurl, headers=header)
    #checking for 200 status for debugging purposes
    pprint(r.status_code)
    
    doc = BeautifulSoup(r.content, "html.parser")

    #meaning
    
    definition=get_meaning(doc)
    await bot.sendMessage(chat_id, definition)
    
    #examples
    
    example=get_example(doc)
    await bot.sendMessage(chat_id, example)

    #pronunciation
    
    audio_link=get_audio(doc)
    await bot.sendAudio(chat_id, audio=audio_link) 


# Your own token. Token can be obtained through @BotFather via Telegram
TOKEN = ""
bot = telepot.aio.Bot(TOKEN)

# Setting up an asyncio event loop
loop = asyncio.get_event_loop()

# AsyncIO and Event Loop: using asyncio to handle asynchronous operations and an event loop to keep the bot running
loop.create_task(MessageLoop(bot, handle).run_forever())

print('NETRUNNING ...')

# Keep the program running
loop.run_forever()



if __name__ == "__main__":
    main()

    

        
        