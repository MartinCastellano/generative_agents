"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: gpt_structure.py
Description: Wrapper functions for calling OpenAI APIs.
"""
import json
import random
import openai
import time 
import sys # Import sys to print exception info

from utils import *
openai.api_key = openai_api_key

def ChatGPT_request(prompt): 
  """
  Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
  server and returns the response. 
  ARGS:
    prompt: a str prompt
    gpt_parameter: a python dictionary with the keys indicating the names of  
                   the parameter and the values indicating the parameter 
                   values.   
  RETURNS: 
    a str of GPT-4's response. 
  """
  # temp_sleep()
  model_name = "gpt-4o-mini"
  messages = [{"role": "user", "content": prompt}]

  print("--- Sending Request ---")
  print(f"Model: {model_name}")
  print(f"Messages: {json.dumps(messages, indent=2)}") # Pretty print the messages
  print("-----------------------")

  try: 
    completion = openai.ChatCompletion.create(
      model=model_name, 
      messages=messages
    )
    response_content = completion["choices"][0]["message"]["content"]
    print("--- Received Response ---")
    print(response_content)
    print("-------------------------")
    return response_content
  
  except Exception as e: # Catch specific exception
    print(f"--- ChatGPT ERROR ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Details: {e}")
    # Optionally print traceback for more details:
    # import traceback
    # print("Traceback:")
    # traceback.print_exc() 
    print("---------------------")
    return f"ChatGPT ERROR: {e}" # Return the error details

prompt = """
---
Character 1: Maria Lopez is working on her physics degree and streaming games on Twitch to make some extra money. She visits Hobbs Cafe for studying and eating just about everyday.
Character 2: Klaus Mueller is writing a research paper on the effects of gentrification in low-income communities.

Past Context: 
138 minutes ago, Maria Lopez and Klaus Mueller were already conversing about conversing about Maria's research paper mentioned by Klaus This context takes place after that conversation.

Current Context: Maria Lopez was attending her Physics class (preparing for the next lecture) when Maria Lopez saw Klaus Mueller in the middle of working on his research paper at the library (writing the introduction).
Maria Lopez is thinking of initating a conversation with Klaus Mueller.
Current Location: library in Oak Hill College

(This is what is in Maria Lopez's head: Maria Lopez should remember to follow up with Klaus Mueller about his thoughts on her research paper. Beyond this, Maria Lopez doesn't necessarily know anything more about Klaus Mueller) 

(This is what is in Klaus Mueller's head: Klaus Mueller should remember to ask Maria Lopez about her research paper, as she found it interesting that he mentioned it. Beyond this, Klaus Mueller doesn't necessarily know anything more about Maria Lopez) 

Here is their conversation. 

Maria Lopez: "
---
Output the response to the prompt above in json. The output should be a list of list where the inner lists are in the form of ["<Name>", "<Utterance>"]. Output multiple utterances in ther conversation until the conversation comes to a natural conclusion.
Example output json:
{"output": "[[\"Jane Doe\", \"Hi!\"], [\"John Doe\", \"Hello there!\"] ... ]"}
"""

print (ChatGPT_request(prompt))












