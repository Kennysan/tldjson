import urllib2
import re
import simplejson as json

response = urllib2.urlopen('https://publicsuffix.org/list/effective_tld_names.dat')
tld = {}
arrayelement = ""
tldname = re.compile('^\w+$')

for item in response:
    if item.startswith("//"):
    #note: this could skip really useful metadata like the wiki page
        continue
    elif item.startswith("\n"):
        continue
    elif re.match(tldname, item):
    #we found a tld
        arrayelement = item.rstrip()
        tld[arrayelement] = []
    else:
        tld[arrayelement].append(item.rstrip())

print json.dumps(tld, ensure_ascii=False, sort_keys=True, indent=4).encode('utf8')
