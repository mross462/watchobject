Watch Object Script
================
Description:

This is a python script to be able to watch changes to an HTTP JSON or XML object as they are occuring. 
It uses the python requests module to perform a get on the object. If the content of the response differs 
from the previous get on the object the output updates and the changes are reflected. OTHERWISE,
THE OBJECT HAS NOT BEEN UPDATED.

Usage:

python watchobject.py --url=http://theurlofyourchoice.com --account=user --password=password 
--headers='{"A JSON Formatted List Of Headers": "Like This"}'

Example:

python watchobject.py --url=https://qa.mezeofile.com/v2 --account=mross --password=test --headers='{"Accept": "application/vnd.csp.cloud+json"}'
    {u'cloud': {u'account': {u'uri': u'https://qa.mezeofile.com/v2/account'},
                u'contacts': {u'uri': u'https://qa.mezeofile.com/v2/contacts'},
                u'locations': {u'User': u'https://qa.mezeofile.com/v2/containers/YzY5NzE0OTY1MDUwMDAzMzgyZTExNzFhMTg5YWU2ZThm'},
                u'namespaces': {u'uri': u'https://qa.mezeofile.com/v2/namespaces'},
                u'recyclebin': {u'uri': u'https://qa.mezeofile.com/v2/recyclebin'},
                u'rootContainer': {u'uri': u'https://qa.mezeofile.com/v2/containers/YzY5NzE0OTY1MDUwMDAzMzgyZTExNzFhMTg5YWU2ZThm'},
                u'shares': {u'uri': u'https://qa.mezeofile.com/v2/shares'},
                u'tags': {u'uri': u'https://qa.mezeofile.com/v2/tags'}}}

To stop watching, just Ctrl-C and you'll get an error to whatever python event was occuring at the time.

Improvments:
Everytime an update to an object is found it is written to standard out. This may be good in a
development use case where a developer needs to keep track of the order of events but from an 
administrative use case could be a nightmare if an object is constantly being updated. This tool
is best suited for the prvious rather than the prior use case.

Questions:
mross@mezeo.com
