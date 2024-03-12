from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
from botocore.client import Config
from langchain.chains import RetrievalQA
from langchain_community.llms import Bedrock

knowledge_base_id = "3VUJJIMTAI"

print("\n\nAsk me a question the state of the union.\n")
query = input()  # Wait for user input

print("\n\n**************************************\n\n")

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id=knowledge_base_id,
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
)

print(f"QUERY: {query}\n\n")

documents = retriever.get_relevant_documents(query=query)

for doc in documents:
    # Directly access the `metadata` attribute
    metadata = doc.metadata  # This is a dictionary
    s3_uri = metadata.get('location', {}).get('s3Location', {}).get('uri', 'N/A')
    score = metadata.get('score', 'N/A')

    # Accessing `page_content` directly as it's a required string attribute
    page_content = doc.page_content
    formatted_content = ' '.join(page_content.split())  # Clean up whitespace

    print(f"Location: {s3_uri}")
    print(f"Score: {score}")
    print("Formatted Content:\n")
    print(formatted_content)
    print("\n-----------------------------------\n\n")

llm = Bedrock(model_id="anthropic.claude-v2")

qa = RetrievalQA.from_chain_type(
    llm=llm, retriever=retriever, return_source_documents=True
)

print("\n\n**************************************\n\n")

result = qa.invoke(query)

print("RESULT: \n\n")
print(result)
print("\n\n--------\n\n")
print(result['result'])