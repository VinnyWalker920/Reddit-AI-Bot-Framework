import praw
import csv
from extras import config, newlineRemove, pullNames
configs = config()

#Gives Reddit API Read-Only Access
reddit_Auth = praw.Reddit(
    client_id=configs["acctConfig"]["client-id"],
    client_secret=configs["acctConfig"]["client_secret"],
    user_agent=configs["acctConfig"]["user_agent"]
    )


def pullHandler(count):
    #pull display names of all servers [names]
    print("Pulling Subreddits...")
    subreddits = pullNames()
    #pull posts for each of those serves {title:"", id:""}
    print("Pulling Posts...")
    posts = []
    for sub in subreddits:
        posts += pullPosts(count=count,
                           subreddit=sub, 
                           include_body=True, 
                           only_valid=True, 
                           include_author=True,
                           include_subreddit= True,
                           null_body_isvalid=False
                           )
    return posts

#Takes a subreddit and a post count and returns a dtrong of title only Opejects
def pullPosts(count:int,
            subreddit:str,
            include_body:bool = False,
            only_valid:bool = False,
            include_author:bool = False,
            include_subreddit:bool = False,
            null_body_isvalid:bool = False):
    output = []
    poststream = reddit_Auth.subreddit(subreddit)
    for post in poststream.new(limit=count):
        postObj = {}
        #Valid Filters
        if only_valid is True:
            if "[video]" in post.selftext:
                 continue
            if (null_body_isvalid is False) and (post.selftext is ''):
                continue
        
        #Filter Maps
        postObj["title"] = post.title
        postObj["id"] = post.id
        if include_body is True:
            postObj["body"] = newlineRemove(post.selftext)
        if include_subreddit is True:
            postObj["subreddit"] = subreddit  
        if include_author is True:
            try:
                postObj["author"] = post.author.name
            except:
                pass
        output.append(postObj)
    return output


