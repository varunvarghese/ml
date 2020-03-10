import urllib.request

url = "https://lottery.olg.ca/en-ca/winning-numbers/lotto-649/winning-numbers?startDate=2020-03-03&endDate=2020-03-05"
url = "https://docs.python.org/3.1/howto/urllib2.html"
url = "https://lottery.olg.ca/en-ca/winning-numbers/lotto-649/winning-numbers"
response = urllib.request.urlopen(url)
html = response.read()

with open("html_content.html", "w") as fp:
    fp.write(str(html))

