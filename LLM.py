from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from collections import deque
from extras import random_float, config

configs = config()

# Model path and chat topic
your_model_path = "models/capybarahermes-2.5-mistral-7b.Q5_K_S.gguf"


# Initialize model and callback manager
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
try:
  model = LlamaCpp(
      model_path=your_model_path,
      n_ctx=4096,
      n_gpu_layers=128,
      n_threads=0,
      callback_manager=callback_manager,
      temperature=random_float(0.6,1.2),
      max_tokens=1000,
      n_parts=1,
      verbose=0,
  )
except Exception as e:
  print(f"Error initializing model: {e}")
  model = None

# Message cache
message_cache = deque(maxlen=5)


def generate_response(prompt):
  """Generates a response from the model based on the given prompt."""
  global model

  if model is None:
    print('Error: Model not initialized.')
    return

  try:
    message_cache.append(prompt)  # Add the prompt to the cache

    
    # Construct prompt template
    template = configs["LMM"]["promptTemplate"]

    final_prompt = template.format(
        subname="r/{sub}".format(sub=prompt["subreddit"]),
        
        username="u/{auth}".format(auth=prompt["author"]),
        posttitle=prompt["title"],
        postbody=str("""{v}""".format(v=prompt["body"])),
    )

    response = model.invoke(final_prompt) 
    return str(response)

  except Exception as e:
    print(f"Error generating response: {e}")
