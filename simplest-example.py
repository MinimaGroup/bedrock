# The Absolute Simplest Bedrock / Langchain Example
#
# by Matt of Minima; matt@minima.nyc
#
# References: 
#	https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/01_Generation/01_zero_shot_generation.ipynb
#	

from langchain_community.llms import Bedrock

textgen_llm = Bedrock(
	model_id="anthropic.claude-v2"
)

# Ask the user for a question
print("Ask me a question.")
question = input()  # Wait for user input

# Invoke the model with the given or default prompt and print the response
response = textgen_llm.invoke(prompt)
print("\n\nRESPONSE :\n\n")
print(response)
print("\n\n")
