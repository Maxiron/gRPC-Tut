# function that will return the current date and time
# in the format: DD-MM-YYYY HH:MM:SS

# python imports
from datetime import datetime

def getDateTime(username: str) -> str:
    now = datetime.now()    
    return f"Hello {username}, the current date and time is: {now.strftime('%d-%m-%Y %H:%M:%S')}"