# Remarkably Simple Prompt Template Example in Bedrock / Langchain 
#
# by Matt of Minima; matt@minima.nyc

from langchain_community.llms import Bedrock
from langchain.prompts import PromptTemplate
import sys

textgen_llm = Bedrock(
	model_id="anthropic.claude-v2"
)

# Create the prompt template
prompt_template: str = """
You are an expert on  musical instruments. Give the history of the following instrument: {instrument}. 
Do not use technical words, give easy to understand but thorough responses.
"""

prompt = PromptTemplate.from_template(template=prompt_template)

# Ask the user for a question
print("\n\nTell me your favorite musical instrument and I'll tell you about it.")
instrument = input()  # Wait for user input

# Exit if no question is provided
if not instrument:
	print("No question was provided.")
	exit(0)

prompt_formatted_str: str = prompt.format(instrument=instrument)

# Invoke the model with the given prompt and print the response
response = textgen_llm.invoke(prompt_formatted_str)
print("\n\nRESPONSE :\n\n")
print(response)
print("\n\n")
