from langchain_community.llms import LlamaCpp




class LLM():
    def __init__(self, 
      promptTemplate, 
      modelPath, 
      tempature=0.7, 
      modelVisibility=0,
      inputTokenCount=4096,
      gpuLayers=0,
      threadCount=0,
      outputTokenCount=250):
      self.promptTemplate = promptTemplate
      try:
        self.model = LlamaCpp(
        model_path=modelPath,
        n_ctx=inputTokenCount,
        n_gpu_layers=gpuLayers,#16
        n_threads=threadCount,#32
        temperature=tempature,
        max_tokens=outputTokenCount,
        n_parts=1,
        verbose=modelVisibility)
      except Exception as e:
        print(f"Error initializing model: {e}")
        self.model = None
    

    def _promptGen(self, post):
      prompt = self.promptTemplate.format(
        subname="r/{sub}".format(sub=post["subreddit"]),
        
        username="u/{auth}".format(auth=post["author"]),
        posttitle=post["title"],
        postbody=str("""{v}""".format(v=post["body"])))
      return prompt
    
    def genResponse(self, post):
      prompt = self._promptGen(post)
      try:
        response = self.model.invoke(prompt) 
        return str(response)
      except Exception as e:
        print(f"Error generating response: {e}")