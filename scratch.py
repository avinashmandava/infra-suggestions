import openai
import langchain
import os
from dotenv import load_dotenv

from data_processing import prompt_generator
from external_apis import datadog

x = prompt_generator.create_prompt()

print(x)
'''
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_KEY')
print(OPENAI_API_KEY)
# Basic use case - calling LLM on some input

from langchain.llms import OpenAI
llm = OpenAI(model_name="text-ada-001", temperature=0.9)
text = "How can I improve the performance of my Cassandra cluster?"
#print(llm(text))
'''
