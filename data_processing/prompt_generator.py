from external_apis import datadog
import numpy as np

def create_prompt():
  metrics_list = ['postgresql.rows_returned', 'postgresql.rows_updated']
  prompt_data = {}
  for metric in metrics_list:
    data = datadog.get_time_series('avg', metric)['data']['attributes']['values'][0]
    current = data[-1]
    mean = np.mean(data)
    std = np.std(data)
    z = (current-mean)/std
    prompt_data[metric] = {
      'mean': mean,
      'std': std,
      'current_value': current,
      'z_score': z
    }

  prompt = f"I want to improve performance of my postgres cluster. Here are the relevant metrics, including their average over the last hour, the current value, the standard deviation, and the z-score given the distribution: {prompt_data}. Can you recommend some concrete actions I can take to improve performance? Put the recommendations in a list, and make sure each recommendation has clear commands or modifications I can execute."
  return prompt


