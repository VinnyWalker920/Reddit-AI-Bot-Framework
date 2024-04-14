import praw
import csv
import random
import re
import json


def config():
    with open('Config.json') as a:
        return json.load(a)


configs = config()

#Gives Reddit API Read-Only Access
reddit_Auth = praw.Reddit(
    client_id=configs["acctConfig"]["client-id"],
    client_secret=configs["acctConfig"]["client_secret"],
    user_agent=configs["acctConfig"]["user_agent"]
    )



#Removes newline tag
def newlineRemove(string:str):
    return string.replace("\n"," ") 

#This checks if the list of subreddits are banned/private/quarantined. Returns a new list of unbanned/public/non-quarantined subreddits from list
def checkSubStatus(subList:list):
    output = []
    print("Status Check Working...")
    for sub in subList:
        try:
            subreddit = reddit_Auth.subreddit(sub)
            subreddit.title
            output.append(subreddit.display_name)
        except:
            pass
    print("Status Check Complete.")
    return output

def pullNames():
    with open("Subreddits.csv", 'r') as file:
        return list(csv.reader(file))[0]

def random_float(x,y):
    # Generate a random float between 0.8 and 1.2
    rand_float = random.uniform(x, y)
    
    # Round the float to the nearest tenth
    rand_float_rounded = round(rand_float, 1)
    
    return rand_float_rounded


def reformat_text(text, max_line_length):
    words = text.split()
    lines = []
    current_line = ""
    current_length = 0

    for word in words:
        if current_length + len(word) <= max_line_length:
            current_line += word + " "
            current_length += len(word) + 1
        else:
            lines.append(current_line.strip())
            current_line = word + " "
            current_length = len(word) + 1

    if current_line:
        lines.append(current_line.strip())

    return "\n".join(lines)

def sanitize_text(text):
    # Use regular expression to find and remove substrings enclosed in square brackets
    cleaned_text = re.sub(r'\s*\[.*?\]', '', text)

    # Ensure the first character is not a space
    if cleaned_text.startswith(' '):
        cleaned_text = cleaned_text.lstrip()

    # Remove quotation marks only if they exist at the beginning and end of the message
    if cleaned_text.startswith('"') and cleaned_text.endswith('"'):
        cleaned_text = cleaned_text[1:-1]

        # Ensure the first word is not an intro
    if cleaned_text.startswith('my response: '):
        cleaned_text = cleaned_text.replace('my response: ','')
    
        # Ensure the first word is not an intro
    if cleaned_text.startswith('my response '):
        cleaned_text = cleaned_text.replace('my response ','')
    
    return cleaned_text




# def updateData(newdata):
#     with open("pastposts.txt", "w") as file:
#         file.write(newdata)
#     file.close()

# def pullData():
#     with open("pastposts.txt", "r") as file:
#         try:
#             return eval(file.read())
#         except:
#             pass