import praw
from extras import config, sanitize_text, reformat_text

configs = config()


reddit_Auth = praw.Reddit(
    client_id=configs["acctConfig"]["client-id"],
    client_secret=configs["acctConfig"]["client_secret"],
    user_agent=configs["acctConfig"]["user_agent"],
    username=configs["acctConfig"]["username"],
    password=configs["acctConfig"]["password"]
    )


#Sensitive_Pin_8851
def replyToPost (response, obj):
    post = reddit_Auth.submission(id=obj["id"])
    post.reply(response)



def docPost(response, obj):
    output = """
Post ID: {id}
Post Title {title}
Post Body {body}


Response:
{resp}
[RESPONSE OVER]
\n\n
"""
    with open("database.txt", "a") as file:
        file.write(output.format(id=obj["id"],
                                     title=obj["title"],
                                     body=obj["body"],
                                     resp=sanitize_text(response)
                                     ))
        file.close()



