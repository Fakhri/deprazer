Backend code using python to:
1. Crawl twitter using scheduler to get the tweet message and location
1. Save the tweet in a db, using one 'tweet' table with columns: 'message', 'depression_level', 'location', and as an extra: 'age'
1. Call the inference method to determine the regional sentiment. The parameter is a list of tweet string, and an output in map of tweet string and depression level
    1. Called in batches of regional tweet
    2. Output are saved in tweet table db
1. Provide a method to calculate depression level in a region through averaging
1. Provide an endpoint for frontend to get regional data:
    1. Regional depression level
    1. top 5 depression tweet keyword
    1. db query of tweet in a region with an extra: age
