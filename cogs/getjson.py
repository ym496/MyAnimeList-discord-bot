
from urllib.request import Request, urlopen
import json

"""To get the json response of the requested url."""

def jikanjson(url):
  request = Request(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36,gzip(gfe)'})
  response_body = urlopen(request).read()
  response = response_body.decode('utf-8')
  output = json.loads(response)
  return output

  