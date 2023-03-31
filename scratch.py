import openai
import langchain
import os
import json
from dotenv import load_dotenv

from data_processing import format_metrics
from external_apis import datadog
from llm_integration import prompt_generator


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_KEY')

# Config
technology = "PostgreSQL"
optimization_goal = "improve read performance"
metric_data = json.dumps(format_metrics.get_formatted_metrics(technology))

# Basic use case - calling LLM on some input
from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003", temperature=1)
prompt = prompt_generator.construct_prompt(technology, optimization_goal, metric_data)
response = llm(prompt)
print(response)
