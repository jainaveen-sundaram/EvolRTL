import openai
from openai import OpenAI
import time
import os
import requests

client = OpenAI()

def get_oai_completion(prompt):

    try: 
        response =  client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
       
    ],
   temperature=1,
   max_tokens=512,
   top_p=0.95,
   frequency_penalty=0,
   presence_penalty=0,
   stop=None
)
        res = response.choices[0].message.content
        usage = response.usage
        return res, usage
    
    except requests.exceptions.Timeout:
        print("The OpenAI API request timed out. Please try again later.")
        return None, None

    except openai.RateLimitError as e:
        print(f"OpenAI API request exceeded rate limit: {e}")
        return None, None

    except openai.APIConnectionError as e:
        print(f"Failed to connect to OpenAI API: {e}")
        return None, None

    except openai.APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
        return None, None
    
  
    
    
    
def call_chatgpt(ins):
    success = False
    re_try_count = 15
    ans = ''
    while not success and re_try_count >= 0:
        re_try_count -= 1
        try:
            ans, usage = get_oai_completion(ins)
            success = True
        except:
            time.sleep(5)
            print('retry for sample:', ins)
    return ans, usage