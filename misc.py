import torch 
import transformers
import datasets
import os 

device = torch.device("cuda:6" if torch.cuda.is_available() else "cpu")
token = os.environ.get('HF_TOKEN')

def llama3_base_response(instruction):
    model_id = "meta-llama/Meta-Llama-3-8B"
    pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map=device, token=token)
    return pipeline(instruction, max_new_tokens=50)


def split_mgv_into_sumprompts(instruction):
    ''' Input instruction is a string, of MG Verilog Format. 
    Splits it and returns sub-strings, which have the base instruction, problem statement and module header 
    '''
    module_header = instruction[instruction.find('Module header')+14:].strip()
    module_header = module_header[:module_header.find(';')+1]
    actual_instruction = instruction[instruction.find('<</SYS>>')+8:instruction.find('Module header')].strip()
    base_prompt = instruction[instruction.find('<<SYS>>')+7:instruction.find('<</SYS>>')].strip()
    
    return  base_prompt, actual_instruction, module_header
