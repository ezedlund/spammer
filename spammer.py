"""
      ___           ___              
     /  /\         /  /\       ___   
    /  /::\       /  /:/      /__/\  
   /  /:/\:\     /  /:/       \__\:\ 
  /  /::\ \:\   /  /:/        /  /::\
 /__/:/\:\ \:\ /__/:/      __/  /:/\/
 \  \:\ \:\_\/ \  \:\     /__/\/:/
  \  \:\ \:\    \  \:\    \  \::/    
   \  \:\_\/     \  \:\    \  \:\    
    \  \:\        \  \:\    \__\/    
     \__\/         \__\/     
        
Created by: Eli
aka 3li
12/11/23
https://github.com/ezedlund/
# USE AT YOUR OWN RISK #
"""

try:
    import requests
    import keyboard
    import asyncio
    import os
except Exception as e:
    print(f"You are missing some modules!\nError: {e}")
    if (
        input("type 'y' and press enter if you want to attempt to install modules...")
        == "y"
    ):
        os.system("pip install keyboard")
        os.system("pip install asyncio")
        os.system("clr")
        print("Please restart the script")
    input("Press enter to quit...")
    exit()

# Don't touch
running = True
spam_task = None


def get_bee_script():
    """Get the bee script and save it in bee_script line for line then return bee_script"""
    bee_script = []
    # Get text document from below link
    response = requests.get(
        "https://gist.githubusercontent.com/henry7720/429604fe4eb16bea0256a4f8f6330746/raw/b01607aedc62970a0f126a5dbf767bba89ed3469/the-full-bee-movie-script.txt"
    )
    # Save data as text
    data = response.text
    # Append each sentance seperatly to the bee_script array ignoring the first vale (line[0]) as its just the line count
    for line in enumerate(data.split(". ")):
        bee_script.append(line[1])
    # return the array of sentances
    return bee_script


async def spam():
    """Spam"""
    # Get array
    data = get_bee_script()
    while True:
        # for sentance in array
        for line in data:
            # type out the sentance with 0.02 seconds inbetween presses
            keyboard.write(line, 0.02)
            # send the enter key twice
            keyboard.send("enter")
            keyboard.send("enter")
            await asyncio.sleep(0.2)
        await asyncio.sleep(2)


def cancel():
    """Sets the running flag to False, so main() knows that it should exit"""
    global running
    running = False
    print("Exiting...")


async def main():
    """Loops until the running flag is set to False"""
    while running:
        await asyncio.sleep(0.1)


def toggle_spam(loop):
    """Starts or cancels the spamming task"""
    global spam_task
    if spam_task:
        spam_task.cancel()
        spam_task = None
    else:
        spam_task = loop.create_task(spam())
    print(f"Spamming:  {spam_task is not None}")


if __name__ == "__main__":
    print("f4 start/stop\nf5 quit\n~~~~~~~~~~~~~~")

    # Setup keys and loop
    event_loop = asyncio.get_event_loop()
    keyboard.add_hotkey("F4", toggle_spam, args=(event_loop,))
    keyboard.add_hotkey("F5", cancel)
    event_loop.run_until_complete(main())

    input("Press enter to quit...")
