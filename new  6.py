import urllib.request
import urllib.parse
import re
url="http://pythonprogramming.net"
values={'s':'basics','submit':'search'}
data=urllib.parse.urlencode(values)