usage: main.py [-h] --technology TECHNOLOGY --goal GOAL

Get help optimizing your infrastructure systems. Fill out the .env file with keys for integrations and OpenAI to run the script.

options:
  -h, --help            show this help message and exit
  --technology TECHNOLOGY
                        The technology to use. Currently only PostgreSQL is supported as a value.
  --goal GOAL           The goal to achieve, e.g. "reduce latency".

# What is this?

Basic application that quickly gives you suggestions to improve your system performance. Only supported system is Postgres right now. Also this is not fully functional, it's just a proof of concept. More to com
- You add some API keys to the .env file so the system can pull data from DataDog, interact with OpenAI's API.
- You run the script with a "technology" arg (only "PostgreSQL" works right now), and a "goal" (like "improve read performance).
- The system spits out recommendations along with commands you can run to carry out the recommendations.

Near-term enhancements needed:
- Add more metrics to pull in to give the LLM more context on the behavior of the system.
- Add support to pull in logs from log management systems
- Add a way to identify a cluster/instance of a database, message queue, so you can select a specific instance or deployment of the infrastructure to get suggestions for.
- Fine-tune the model using JIRA tickets or forum conversations to give better answers/sugestions
- Support a lot more technologies like Cassandra, Elasticsearch, Kafka, MongoDB, MySQL, etc.
- Fix issue where output is cut off before the full list of suggestions has been generated.
- Add some sort of UI so this isn't a python script and you can manage more systems and get suggestions for multiple systems in one interface

Long-term enhancements
- Use GPT-4 to improve suggestions, the GPT-3 suggestions are not great, but GPT4 was surprisingly good.
- Use Langchain or something similar to make an autonomous agent that can carry out recommended changes if given proper system access to make remote calls/execute system changes (there are a lot of questions about how to do this well, not sure LLMs are even the best way to carry it out).
