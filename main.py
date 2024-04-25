from redditAI import RedditAI

example_prompt="<|im_start|>You are a nice person who looking at a reddit post. you are on the {subname} subbreddit,{username} looking at the post titled {posttitle}. The body text of the post is {postbody}. Your Job is to write a positive comment that will gain likes. You dont want to mention anything about youself, and do not give away your identity. MAKE SURE YOUR RESPONSE DOES NOT HAVE and Preamble or introductory phrases, and it is only the response. Make the response short but long enough to finish your thought<|im_end|><|im_start|>assistant"
example_subreddit=["IAmA", "todayilearned", "AskScience", "LifeProTips", "ExplainLikeImFive", "YouShouldKnow", "Movies", "science", "history", "worldnews", "DIY", "personalfinance", "Fitness", "technology", "books", "Music", "gaming", "news", "Futurology", "politics", "health", "relationships", "philosophy", "Writing", "Economics", "Psychology", "TrueReddit", "Documentaries"]

RedditBot = RedditAI(
    client_id="CLIENT ID HERE",
    client_secret="CLIENT SECRET HERE",
    user_agent="USER AGENT",
    username="REDDIT USERNAME",
    password="REDDIT PASSWORD",
    AIPromptTemplate=example_prompt,
    NumberOfComments=25,
    AIpath="PATH TO MODEL",
    subredditList= list(example_subreddit),
    Cooldown= 600
)

RedditBot.RunDebug()
