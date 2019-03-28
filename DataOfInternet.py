import urllib2
file = urllib2.urlopen('http://manning.com/data/message.txt')
message = file.read()
print message
