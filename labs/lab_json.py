#!/usr/bin/env python
# *-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON Navigation
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object. Practice file IO using with.
::

 a. Using urllib2, explore the GitHub JSON API.  Load the initial api page, parse it
    into JSON, and use it for the following tasks.

 b. Load the list of emojis from the GitHub API and print a random one from the list.
    Save the list to emojis.json

 c. Load the information for a GitHub username passed in from the command line, print
    the number of repositories the user has and what organizations they belong to.
    Save the user info to {{username}}.json

"""

# see https://docs.python.org/2/library/urllib2.html for more info on urllib2
# example use of urllib2 to get a web resource:
import urllib2, json
import sys

from random import sample
data = json.loads(urllib2.urlopen("https://api.github.com/").read())
emoji_data = json.loads(urllib2.urlopen(data[u'emojis_url']).read())

print("Random Emoji\n%s" % sample(emoji_data, 1))

username = input("Enter the Username you with to check: ")

user_result = json.loads(urllib2.urlopen(data[u'user_url'].format(user=username)).read())

if "message" in user_result:
    print("There was an error getting that user's information\n%s" % user_result["message"])
    sys.exit(1)

print()

