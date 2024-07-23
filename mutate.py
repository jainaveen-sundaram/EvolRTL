import random

base_instruction = "You are an expert RTL design engineer, proficient in writing performant and synthesizeable Verilog code. \n \
Reflect on the given #Coding problem# and increase the difficulty by a bit. Present the solution under #Rewritten prompt# heading. \n \
Be concise, You should try your best not to make the #Rewritten Prompt# become verbose, adding utmost 10 to 20 words. \n\
'#Coding problem#', '#Rewritten Prompt#', 'coding problem' and 'rewritten prompt' are not allowed to appear in the final #Rewritten Prompt#\n \
You can increase the difficulty using, but not limited to, the following methods: {method}\n  \
#Coding problem#: {question} \r\n "

unified_instruction = "Please increase the difficulty of the given programming test question by a bit. Add in utmost 10 to 20 additional words. You can increase the difficulty by using one or a combination of the below methods: {method} \n Question: {question}"

unified_isntruction_methods = "Replace a commonly used module in the programming task with a less common and more specific one, while preserving the existing input outputs of the block.\n \
If the original problem can be solved with only a few logical steps, please add more reasoning steps.\n \
Add in a new functionality to the module, preserving the existing input outputs of the block. \n \
Remove a feature from within the module, while preserving the existing input outputs of the block."

methods = ["Add in an uncommon element",
		    "Delete a component from the question"]	

def unifiedInstructionComplexity(instruction):
    prompt = unified_instruction.format(method=unified_isntruction_methods, question=instruction)
    return prompt

def addComplexity(instruction):
    chosen_method = random.choice(methods)
    prompt = base_instruction.format(method=chosen_method, question=instruction)
    prompt += "#Rewritten Prompt#:\r\n"
    return prompt
