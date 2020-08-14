# mockRSS

mockRSS is a small RSS feed aggregator built with Python and Django. 

##Installation

Download the project, and within the project run with Python:

```
manage.py runserver
```

then visit local server http://127.0.0.1:8000/rachelsrss/login. If you're experiencing this error:

```
"Certificate verify failed: unable to get local issuer certificate."
```

Make sure to run Install Certificates.command in your Python folder to solve this.

## Known Bugs

Not all images display correctly, some titles are not stored in DB properly.

Going to http://127.0.0.1:8000/ before logging in will cause an error.

Lacks live updating, and the same feed can be added multiple times.

## Roadmap

Implement ability to remove posts from your feed.
Add indication of news source with each post.
Improve front-end design.
Hide "Keyword" form option when "Description containing:" has not been chosen.
Expand feed parsing to catch all variations in date structure, image URL structure, etc.

### Author: Rachel Williams
