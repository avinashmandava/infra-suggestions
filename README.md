Experiment to see how far a bot can go in talking to itself and making decisions.

Application that makes sense for me is:
- Integrate with some external system that holds metrics and logs to pull in info about a target system that you want help with
- Logic to convert that data about the system to a prompt to send to GPT so we get an ordered list of very specific recommendations along with actions to take for those recommendations.
- Get a response from GPT containing a list of recommendations including, where possible, a command you can carry out on the system.
- An avenue for users to provide feedback on which of the recommendations they have either tried before, are not possible, or they need more info on.

Put this all in an interface and go.


POSTGRES SETUP

INSTALL ON UBUNTU
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04

PGBENCH
https://www.cloudbees.com/blog/tuning-postgresql-with-pgbench

SETTING UP POSTGRES TO SEND METRIS
https://www.datadoghq.com/blog/collect-postgresql-data-with-datadog/


API CALLS FOR DATADOG

WORKS to validate API key for testing:
curl -X GET "https://api.us5.datadoghq.com/api/v1/validate" -H "Accept: application/json" -H "DD-API-KEY: <DD-API-KEY>"


WORKS to get list of all available metrics from "from" seconds ago, not just search query:
curl -X GET "https://api.us5.datadoghq.com/api/v1/metrics?from=10000" \
-H "Accept: application/json" \
-H "DD-API-KEY: <DD-API-KEY>" \
-H "DD-APPLICATION-KEY: <DD-APPLICATION-KEY>"


WORKS to get all metrics available for a given search query:
curl -X GET "https://api.us5.datadoghq.com/api/v1/search?q=postgresql" \
-H "Accept: application/json" \
-H "DD-API-KEY: <DD-API-KEY>" \
-H "DD-APPLICATION-KEY: <DD-APPLICATION-KEY>"


WORKS to query a specific metric to get the time series data:
curl -X POST "https://api.us5.datadoghq.com/api/v2/query/timeseries" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: <DD-API-KEY>" \
-H "DD-APPLICATION-KEY: <DD-APPLICATION-KEY>" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "formulas": [
        {
          "formula": "a",
          "limit": {
            "count": 10,
            "order": "desc"
          }
        }
      ],
      "from": 1679982319000,
      "interval": 5000,
      "queries": [
        {
          "data_source": "metrics",
          "query": "avg:system.cpu.user{*}",
          "name": "a"
        }
      ],
      "to": 1679984319000
    },
    "type": "timeseries_request"
  }
}
EOF

WORKS:
curl -X POST "https://api.us5.datadoghq.com/api/v2/query/timeseries" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: <DD-API-KEY>" \
-H "DD-APPLICATION-KEY: <DD-APPLICATION-KEY>" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "formulas": [
        {
          "formula": "a",
          "limit": {
            "count": 10,
            "order": "desc"
          }
        }
      ],
      "from": 1679982319000,
      "interval": 5000,
      "queries": [
        {
          "data_source": "metrics",
          "query": "avg:postgresql.rows_returned{*}",
          "name": "a"
        }
      ],
      "to": 1679984319000
    },
    "type": "timeseries_request"
  }
}
EOF

PYTHON CODE
