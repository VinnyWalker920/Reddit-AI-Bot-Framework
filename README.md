# Reddit AI Bot FrameWork


This is a framework for a Reddit Bot that harnesses AI to generate responses to Reddit posts. The project utilizes the PRAW Reddit API for Python, along with a LlamaCpp and Langchain LLM manager compatible with any .GGUF model.

## Features

- Allows for Custom AI Prompts
- Allows for Custom AI Model Augmentaion
- Allows for Custom Subreddit Choices
- Saves Past Posts and Responses
- Statistical Output

All features are subject to change, and may need a strong technical understanding to tweak and debug

## Requirments
- C++ - Installed On Your Device
- CUDA ToolKit - If You Plan to Use GPU for AI Response Generation
- Cmake - Should Install With C++, Required for LlamaCPP

## Dependacies
- Langchain - Should Install Llama CPP
- PRAW - Reddit API Wrapper for Python


## Installation

```sh
git clone https://github.com/VinnyWalker920/Reddit-AI-Bot-Framework.git
```

- You can use the main.py file to use this, or you can use the redditAI.py as an import 

- You DON'T need the Subreddits.csv, PastPosts.csv, or the Database.txt created before you use the Framework. These will get created in the directry where script is running.

> Note: The ability to toggle these features or their locations is currently in development


## How to Configure
### AI Model
```sh
self.model = LlamaCpp(
        model_path=modelPath,
        n_ctx=inputTokenCount,
        n_gpu_layers=gpuLayers,#16
        n_threads=threadCount,#32
        temperature=tempature,
        max_tokens=outputTokenCount,
        n_parts=1,
        verbose=modelVisibility
```
#### This is from the LLM AI model definition as used in the LLM Class of the RedditAI Object
- model_path - This is the path to you Quantized model (.GGUF File) 
- n_ctx - Somewhat translates to the length of the inputted prompt
- n_gpu_layers - This puts repeated layers on the GPU. This is only used if you are using CUDA
- n_threads - Refers to the ammount of CPU threads to be used
- temperature - this is on a scale of 0.0 - 1.0 
- max_tokens - Somewhat translates to the length of the model's response
- verbose - Shows more information when loading the model

### Prompts
#### This is a Example of a prompt:
```sh
"<|im_start|>You are a nice person who looking at a reddit post. you are on the {subname} subbreddit,{username} looking at the post titled {posttitle}. The body text of the post is {postbody}. Your Job is to write a positive comment that will gain likes. You dont want to mention anything about youself, and do not give away your identity. MAKE SURE YOUR RESPONSE DOES NOT HAVE and Preamble or introductory phrases, and it is only the response. Make the response short but long enough to finish your thought<|im_end|><|im_start|>assistant"
```
The "<|im_start|>" and "<|im_end|>" is the prompter defineetion for the model I was using (dolphin-2.7-mixtral-8x7b.Q5_K_M.gguf). It may be different for your choosen model, check the Model documentaion

#### The {...} sections are Mandatory so the AI knows what the post is about. If you do not have these in your prompt, it will throw an error. Even though they are self-explanitory, here are what they are for:
- {subname} - This is where the subreddit name will go
- {username} - This is where the post's author's username will go
- {postbody} - this is where the body text of the post will go


### Subreddit List
#### Here is an example of a Subreddit list:
```sh
["IAmA", "todayilearned", "AskScience", "LifeProTips", "ExplainLikeImFive", "YouShouldKnow", "Movies", "science", "history", "worldnews", "DIY", "personalfinance", "Fitness", "technology", "books", "Music", "gaming", "news", "Futurology", "politics", "health", "relationships", "philosophy", "Writing", "Economics", "Psychology", "TrueReddit", "Documentaries"]
```
You will need to make a list of subreddits you want to target. Make sure they are have "" around them and they do not have the r/ prefix.

> Note: If you run this the first time you do not have to every single time. it will be saved in Subreddit.csv

Alternatively, you can create (or let program generate) the Subreddit.csv file and add them manually
#### Here is an Example:
```sh
philosophy
Writing
Economics
Psychology
TrueReddit
Documentaries
```

### Runtime Configurations
#### Here is an example of the RedditAI Class initialization:
```sh
RedditBot = RedditAI(
    client_id="CLIENT ID HERE", #1
    client_secret="CLIENT SECRET HERE", #2
    user_agent="USER AGENT", #3
    username="REDDIT USERNAME", #4
    password="REDDIT PASSWORD", #5
    AIPromptTemplate=example_prompt, #6
    NumberOfComments=25, #7
    AIpath="PATH TO MODEL", #8
    subredditList= list(example_subreddit), #9
    Cooldown=600 #10
)
```
- #1 - Client ID for Reddit API
- #2 - Client Secret for Reddit API
- #3 - User Agent for Reddit API (Usual Format: "API_APP_NAME r/USERNAME) 
- #4 - Reddit Account Login Username
- #5 - Reddit Account Login Password
- #6 - AI Prompt (Follow Above Guide)
- #7 - This is the Number of Posts You Want to Post
- #8 - This is the File Path to Your Chosen .GGUF Quantized Model
- #9 - This is where you put the List of Subreddits (Follow Above Guide)
- #10 - This is the Cooldown Between Posts (Set To 10 minutes by Default, Could Break if you Set it too Fast)

## WARNINGS
This program is intended for positive use. Misuse may result in account bans or permanent loss of Reddit access. The creator of this framework is not liable for any consequences related to its use. Avoid promoting hate speech, violence, terrorism, human trafficking, or any other nefarious activity. Be responsible and use with caution.
