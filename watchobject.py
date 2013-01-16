import sys
import argparse
import json
import requests
import xml.dom.minidom
import os
import time
from pprint import pprint


class WatchObject():

    def parse_sys_args(self):
        #Parse the arguments for the object that we want to view
        parser = argparse.ArgumentParser()
        parser.add_argument('--account')
        parser.add_argument('--password')
        parser.add_argument('--url')
        parser.add_argument('--headers')
        args = parser.parse_args()
        return args

    def watch_object(self, args, previous_request=None):
        #Default to administrator
        if args.account is None or \
           args.password is None:

                account = 'administrator'
                password = 'mezeo'

        else:
            account = args.account
            password = args.password

        try:
            if args.headers is None:

                request = requests.get(args.url,
                        headers=None,
                        verify=False,
                        auth=(account,
                        password
                        )
                    )

            else:
                request = requests.get(args.url,
                        headers=json.loads(args.headers),
                        verify=False,
                        auth=(account,
                        password
                        )
                    )

            request.raise_for_status()

        except requests.HTTPError or \
                requests.URLError:
                #An Error occured, let's dump the object and see what's up.
                print 'The request was raised for an http error. Dumping the request object:'
                pprint(vars(request))
                sys.exit()

        if previous_request is None and \
           request.content is not None:
            return request

        elif previous_request.content == request.content:
            return None

        else:
            return request

watch_object = WatchObject()
args = watch_object.parse_sys_args()
update = None
while True:
        if watch_object.watch_object(args, update) is None:
            pass
        else:
            #It Has Been Updated, Lets See what we have
            update = watch_object.watch_object(args, update)
            os.system('clear')
            try:
                json.loads(update.content)
                pprint(update.json())

            except ValueError:   # Caught when the JSON Is invalid

                    try:
                        print xml.dom.minidom.parseString(update.content).toprettyxml()

                    except xml.parsers.expat.ExpatError: # Caught for invalid XML
                        #What in the wide wide world of sports is a goin on here?
                        print('Expected XML or JSON To be Returned from the server. Dumping the request Object:')
                        pprint(vars(update))
                        sys.exit

        time.sleep(3)
