import json 
import torch 
import transformers
import mutate as m
import misc 
import openai_access as oai
from datasets import load_dataset

# ds = load_dataset("GaTech-EIC/MG-Verilog", split="train")
ds = load_dataset("naveensp/mg-verilog-small", split="train") # smaller version of the original dataset 

base_instruction, actual_problem, module_header = misc.split_mgv_into_sumprompts(ds['description'][2]['detailed_global_summary'])
add_complexity_to_problem = m.unifiedInstructionComplexity(actual_problem)
print('*'*50, '\n', add_complexity_to_problem,'*'*50, '\n')

#### Code to generate Evolved prompt 
evolved_problem, usage = oai.get_oai_completion(add_complexity_to_problem)
print('*'*50, '\n', "Evolved Prompt:" ,evolved_problem, '\n','*'*50, '\n')
if usage is not None: print(f'Prompt tokens: {usage.prompt_tokens}, Completion_tokens: {usage.completion_tokens}, ($$): {(0.15*usage.prompt_tokens + 0.6*usage.completion_tokens)/1e6}')

#### Code to generate RTL from the evolved prompt 
# evolved_solution, usage = oai.get_oai_completion(base_instruction + evolved_problem)
# print('*'*50, '\n', "Evolved Solution:" ,evolved_solution,'*'*50, '\n')
# if usage is not None: print(f'Prompt tokens: {usage.prompt_tokens}, Completion_tokens: {usage.completion_tokens}, ($$): {(0.15*usage.prompt_tokens + 0.6*usage.completion_tokens)/1e6}')

