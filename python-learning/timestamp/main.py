import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Bamboo server URL
bamboo_url = 'https://cmbamboo.caremore.com/'

# Bamboo API endpoint to fetch build results
api_endpoint = f'{bamboo_url}/rest/api/latest/result'

# Bamboo credentials
username = 'caremore\\mmamidibat'
password = 'Spring44'

# Start and end timestamps for the desired timeframe
start_timestamp = 1687372800  # Unix timestamp for start time
end_timestamp = 1687370400  # Unix timestamp for end time

# Disable SSL certificate verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Construct the API request URL with query parameters
api_url = f'{api_endpoint}?expand=results.result&max-results=1000&buildStartedDate.after={start_timestamp}&buildStartedDate.before={end_timestamp}'

# Send the API request with SSL certificate verification disabled
response = requests.get(api_url, auth=(username, password), verify=False)

# Check if the request was successful
if response.status_code == 200:
    builds = response.json()['results']['result']
    for build in builds:
        build_key = build['buildResultKey']
        build_number = build['buildNumber']
        build_state = build['state']
        build_date = build['buildStartedTime']
        print(f"Build: {build_key} - Number: {build_number} - State: {build_state} - Date: {build_date}")
else:
    print(f"Error: Failed to retrieve build results. Status code: {response.status_code}")
