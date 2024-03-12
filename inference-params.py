# Cohere Inference Parameters
#
# by Matt of Minima; matt@minima.nyc
#
# References: 
#	https://docs.cohere.com/docs/temperature
#	

from langchain_community.llms import Bedrock

# Ask the user for a question
print("\n\nAsk me (Cohere) a question.")
prompt = input()  # Wait for user input

print("\n\nGive temperature param for LLM as float, 0-5.")
temperature = float(input()) # Wait for user input

inference_params = {
    "max_tokens": 4096,
    "temperature": temperature,
}

textgen_llm = Bedrock(
	model_id="cohere.command-text-v14"
,	model_kwargs=inference_params,
)

# Invoke the model with the given or default prompt and print the response
response = textgen_llm.invoke(prompt)
print("\n\nRESPONSE :\n\n")
print(response)
print("\n\n")
