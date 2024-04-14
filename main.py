import praw
from scrapeHandler import pullPosts, pullHandler
from postHandler import docPost, replyToPost
# from dataHandler import
from extras import pullNames, checkSubStatus
from LLM import generate_response
import time
import random



#postQueryCount refers to the ammount of post PER SUBBREDDIT be careful.
def start(postQueryCount:int):
    start = time.time()
    #pull display names of all servers [names]
    print("Pulling Subreddits...")
    subreddits = pullNames()
     #pull posts for each of those serves {title:"", id:""}
    print("Pulling Posts...")
    posts = []
    for sub in subreddits:
        posts += pullPosts(count=postQueryCount,
                           subreddit=sub, 
                           include_body=True, 
                           only_valid=True, 
                           include_author=True,
                           include_subreddit= True,
                           null_body_isvalid=False
                           )
    end = time.time()
    #print(posts)
    print(posts)
    output = "This Successfully Pulled {count} Posts out of the {total} Total Posts Queried within {elapsed} Seconds"
    print(output.format(count= len(posts),
                        total=len(subreddits) * postQueryCount,
                        elapsed= end -start
                        ))
    
    #send to AI log response in doc
    print("Generating Response...")
    resp = generate_response(posts[0])
    print("Posting Response...")
    docPost(resp, posts[0])

    #sed resposne to red

#start(postQueryCount=2)


def stream():
    #pastpostData = pullData()
    while True:
        #pull posts
        print("Pull Post")
        posts = pullHandler(5)
        #pick random one
        print("Choose Post")
        selectedPost = random.choice(posts)
        #crossreference with post list
        print("Gen resp")
        resp = generate_response(selectedPost)
        #try:
        replyToPost(resp, selectedPost)
        print("Posted")
        # except Exception as e:
        #     print(e)
        #     print("\n BROKEBOY")
        #     continue
        time.sleep(660)


stream()