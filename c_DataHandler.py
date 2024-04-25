import csv, os
from datetime import datetime

class DataHandler():
    def __init__(self):
        self.databasePath = 'Database.txt'
        self.subredditPath = 'Subreddits.csv'
        self.pastPostPath = 'PastPost.csv'
        # Check if the Subreddit list exists 
        if not os.path.isfile(self.subredditPath):
            # If the list doesn't exist, create it
            open(self.subredditPath, 'a').close()

        # Check if the Past Posts list exists 
        if not os.path.isfile(self.pastPostPath):
            # If the list doesn't exist, create it
            open(self.pastPostPath, 'a').close()  
        
        # Check if the Past Posts list exists 
        if not os.path.isfile(self.databasePath):
            # If the list doesn't exist, create it
            open(self.databasePath, 'a').close()  

    def checkSubbreddit(self):
        return os.path.isfile(self.databasePath)

    def checkPastPosts(self):
        pass

    def checkDatabase(self):
        pass

    def _clearSubreddits(self):
        # Open the file in write mode ('w') to clear its contents
        with open(self.subredditPath, 'w', newline=''):
            pass  # Do nothing, just open and close the file   

    def pullSubreddits(self):
        with open(self.subredditPath, 'r', newline='') as file:
        # Example: Reading the contents of the file
            reader = csv.reader(file)
            return [', '.join(x) for x in reader]
    
    def addSubreddits(self,Subreddits2Add):
        subredditList = self.pullSubreddits()
        newList = subredditList + Subreddits2Add
        with open(self.subredditPath, 'w', newline='') as file:
            for sub in newList:
                if sub == (newList[0]):
                    file.write(str(sub))
                else:
                    file.write( "\n" + str(sub))

    def seedReddit(self,subreddits):
        self._clearSubreddits()
        self.addSubreddits(subreddits)



    def _clearPastPosts(self):
        # Open the file in write mode ('w') to clear its contents
        with open(self.pastPostPath, 'w', newline=''):
            pass  # Do nothing, just open and close the file   

    def pullPastPosts(self):
        with open(self.pastPostPath, 'r', newline='') as file:
        # Example: Reading the contents of the file
            reader = csv.reader(file)
            output =  [', '.join(x) for x in reader]
            return output
    
    def addPastPosts(self,Post):
        pastPostList = self.pullPastPosts()
        newList = list(pastPostList) + [Post["id"]]
        with open(self.pastPostPath, 'w', newline='') as file:
            try:
                for post in newList:
                    if post == (newList[0]):
                        file.write(str(post))
                    else:
                        file.write( "\n" + str(post))
            except:
                file.write(str(Post["id"]))

    
    def addDatabase(self, response, post):
        output = """
        Post ID: {id}
        Post Title {title}
        Post Body {body}

        {dateTime}
        Response:
        {resp}
        [RESPONSE OVER]
        \n\n
        """
        with open("database.txt", "a") as file:
            try:
                file.write(output.format(id=post["id"],
                                        title=post["title"],
                                        body=post["body"],
                                        resp=response,
                                        dateTime = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                                        ))
            except:
                file.write("post with ID {id} was posted at {time}, but it has an error and we dont want to stop the proceess\n\n".format(id=post["id"],time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
            file.close()
        self.addPastPosts(post)





