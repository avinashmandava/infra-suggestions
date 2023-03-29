# NOTES

Experiment to find useful recommendations from GPT applied to something I understand so I can evaluate it.

Application that makes sense for me is:
- Integrate with some external system that holds metrics and logs to pull in info about a target system that you want help with
- Logic to convert that data about the system to a prompt to send to GPT so we get an ordered list of very specific recommendations along with actions to take for those recommendations.
- Get a response from GPT containing a list of recommendations including, where possible, a command you can carry out on the system.
- An avenue for users to provide feedback on which of the recommendations they have either tried before, are not possible, or they need more info on.

Put this all in an interface and go.

# Requirements

You need an ENV file with the following:

OPENAI_KEY=<yours here>
DATADOG_URL="https://api.datadoghq.com/api/" <-- Just an example to illustrate where to stop the URL (at api/), use your own URL.
DATADOG_API_KEY=<yours here>
DATADOG_APP_KEY=<yours here>

# GPT Output

## Data Ingestion and Integration
- Build plugins or adapters for popular monitoring tools like Datadog, Splunk, Prometheus, etc. These plugins will be responsible for sending data to your application.
- Develop a data ingestion service that accepts data from the plugins and stores it in a scalable and distributed storage system like Apache Kafka or AWS Kinesis.
- Create a service discovery mechanism or manual configuration to identify and connect to databases, message queues, and other components.

## Data Processing and Analysis
- Use a stream processing framework like Apache Flink or Apache Beam to process the incoming data.
- Implement data transformation and enrichment logic to normalize and augment the data before it is processed by the AI.
- Store processed data in a time-series database like InfluxDB or TimescaleDB for historical analysis.

## AI-powered Recommendation Engine
- Develop a recommendation engine using GPT or a similar AI model to provide expert advice based on the processed data.
- Train and fine-tune the AI model with domain-specific knowledge about databases, message queues, and other infrastructure components.
- Integrate the AI model with your application using a RESTful API or a GraphQL API.

## User Interface and Querying
- Design a web-based user interface for users to interact with the AI-powered recommendation engine.
- Implement a natural language processing (NLP) layer to understand and parse user queries, then forward them to the recommendation engine.
- Display the recommendations and insights provided by the AI model in a user-friendly manner.

## Codebase Organization
- Organize the codebase into modular and well-defined components, following microservices architecture principles or modular monolith, depending on the team's preference and expertise.
- Use a version control system like Git and follow best practices for branching, code reviews, and continuous integration and deployment (CI/CD).

## Infrastructure and Deployment
- Choose a cloud provider like AWS, Azure, or GCP to host the application.
- Utilize containerization with Docker and orchestration using Kubernetes for deployment and scalability.
- Implement observability and monitoring using tools like Prometheus and Grafana to track the performance and health of the application.

By following this high-level architecture, you can build a robust application that provides AI-powered expert advice on infrastructure management for software development teams.


# Testing

## POSTGRES SETUP

### INSTALL ON UBUNTU
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04

### PGBENCH
https://www.cloudbees.com/blog/tuning-postgresql-with-pgbench

### SETTING UP POSTGRES TO SEND METRIS
https://www.datadoghq.com/blog/collect-postgresql-data-with-datadog/

