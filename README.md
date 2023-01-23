# Gold-digger

a scrapper for valuable assets like passwords, secrets, e.t.c.

To use this code, you can run it from the command line with the search term as the first argument and the optional --token argument to specify a GitHub access token. For example:

'''python search_github.py password --token YOUR_ACCESS_TOKEN'''

This will search through the file contents of all public repositories for the term "password" and print the repository names and file paths of the search results. You can modify the search query or use the other parameters of the Search API to narrow down the results.

Keep in mind that the Search API has a rate limit of 10 requests per minute for authenticated requests and 3 requests per minute for anonymous requests. The code above adds a delay between requests to stay within the rate limit for anonymous requests. If you are using an access token, you may need to adjust the rate
