import urllib2
request = urllib2.Request("www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

# THoughts flow
'''
	construct a request containing url,data and timeout, and pass it to urlopen. Finally, we could get a response.
	