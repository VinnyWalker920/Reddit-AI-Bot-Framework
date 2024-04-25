import praw, c_DataHandler, c_Scraper, c_LLM, c_Poster, random, time, c_StatHandler

class RedditAI():
    def __init__(self,
        client_id,
        client_secret,
        user_agent,
        username,
        password,
        AIPromptTemplate,
        NumberOfComments,
        AIpath,
        AICreativity = 0.8,
        subredditList = [],
        Cooldown = 600):

        self.CooldownTime = Cooldown
        self.iterations = NumberOfComments
        self.RedditAPI = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password)
        
        self.DataHandler = c_DataHandler.DataHandler()

        if not subredditList :
            pass
        else:
            self.DataHandler.seedReddit(subredditList)

        
        self.StatHandler = c_StatHandler.StatHandler(self.iterations,self.CooldownTime)
        self.CommentHandler = c_Poster.Poster(self.RedditAPI,self.DataHandler)
        self.PostScraper = c_Scraper.Scraper(self.RedditAPI, self.iterations, self.DataHandler)
        self.LLM = c_LLM.LLM(promptTemplate=AIPromptTemplate,modelPath=AIpath,modelVisibility=1,gpuLayers=16,threadCount=32,tempature=AICreativity)

    
    def Run(self):
        """Does Post to Reddit"""
        for i in range(self.iterations):
            self.StatHandler.StartTimer()
            self.StatHandler.ChangePhase(0)
            self.PostScraper.refreshList()
            choice = random.choice(self.PostScraper.Posts)
            self.StatHandler.ChangePhase(1)
            resp = self.LLM.genResponse(choice)
            self.StatHandler.ChangePhase(2)
            self.CommentHandler.postReply(response=resp,post=choice)
            self.StatHandler.CompletePost()
            self.StatHandler.StartCooldown()
            self.StatHandler.EndTimer()

    def RunDebug(self):
        """Does NOT Post to Reddit"""
        for i in range(self.iterations):
            self.StatHandler.StartTimer()
            self.StatHandler.ChangePhase(0)
            self.PostScraper.refreshList()
            choice = random.choice(self.PostScraper.Posts)
            self.StatHandler.ChangePhase(1)
            resp = self.LLM.genResponse(choice)
            self.StatHandler.ChangePhase(2)
            self.CommentHandler.postDatabase(response=resp,post=choice)
            self.StatHandler.CompletePost()
            self.StatHandler.StartCooldown()
            self.StatHandler.EndTimer()


        






