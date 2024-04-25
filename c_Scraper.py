

class Scraper():
    def __init__(self, API, PostCount, DataAnchor):
        self.API=API
        self.DataAnchor = DataAnchor
        self.SubredditList = self.DataAnchor.pullSubreddits()
        self.PostCount = PostCount
        self.Posts = []
        self.refreshList()
    
        #Private Removes newline tag
    def _newlineRemove(self,s):
        return s.replace("\n"," ") 


    def _pullPosts(self,
            include_body:bool = True,
            only_valid:bool = True,
            include_author:bool = True,
            include_subreddit:bool = True,
            null_body_isvalid:bool = False):
        #gets subreddits
        PostPerSub = 1
        if self.PostCount > len(self.SubredditList):
            PostPerSub = round(self.PostCount/len(self.SubredditList))
        
        for sub in self.SubredditList:
            subreddit=self.API.subreddit(sub)
            for post in subreddit.new(limit=PostPerSub * 3):
                PostJSON = {}
                #Valid Filters
                if only_valid is True:
                    if "[video]" in post.selftext:
                        continue
                    if (null_body_isvalid is False) and (post.selftext == ''):
                        continue
                
                #Filter Maps
                PostJSON["title"] = post.title
                PostJSON["id"] = post.id
                if include_body is True:
                    PostJSON["body"] = self._newlineRemove(s=str(post.selftext))
                if include_subreddit is True:
                    PostJSON["subreddit"] = self.API.subreddit(sub).display_name  
                if include_author is True:
                    try:
                        PostJSON["author"] = post.author.name
                    except:
                        pass
                self.Posts.append(PostJSON)

    def _pullsubreddits(self):
        self.SubredditList = self.DataAnchor.pullSubreddits()


    def refreshList(self):
        self.Posts = []
        self._pullsubreddits()
        self._pullPosts()
        for post in self.Posts[:]:
            if self.DataAnchor.pullPastPosts() is None:
                pass
            elif post["id"] in self.DataAnchor.pullPastPosts():
                self.Posts.remove(post)

        

