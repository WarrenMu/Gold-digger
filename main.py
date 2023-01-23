import argparse
import requests
import time

# Set the rate limit for the Search API
RATE_LIMIT = 3  # requests per minute for anonymous requests
DELAY = 60 / RATE_LIMIT  # delay between requests in seconds

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Search GitHub repositories for a specific term")
parser.add_argument("term", type=str, help="the search term")
parser.add_argument("-t", "--token", type=str, help="a GitHub access token")
args = parser.parse_args()

# Set the search query and the access token
query = args.term
token = args.token

# Set the headers for the request
headers = {
    "Accept": "application/vnd.github+json",
}
if token:
    headers["Authorization"] = f"token {token}"

# Set the parameters for the request
params = {
    "q": query,
    "type": "code",
}

# Initialize the page number and the search results
page = 1
results = []

# Keep sending requests until there are no more search results
while True:
    # Set the page parameter for the request
    params["page"] = page

    # Send the request
    response = requests.get("https://api.github.com/search/code", headers=headers, params=params)

    # Get the current search results and the total number of search results
    current_results = response.json()["items"]
    total_results = response.json()["total_count"]

    # Add the current search results to the total search results
    results += current_results

    # Print the repository names and file paths of the current search results
    for result in current_results:
        print(result["repository"]["full_name"])
        print(result["path"])

    # Break the loop if there are no more search results
    if len(results) >= total_results:
        break

    # Wait before sending the next request to stay within the rate limit
    time.sleep(DELAY)

    # Increment the page number
    page += 1
