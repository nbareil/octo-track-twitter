#! /usr/bin/env python
# -*- coding: utf-8 *-*
#
# Copyright (C) Nicolas Bareil <nico@chdir.org>
#
# This program is published under a GPLv2 license

from optparse import OptionParser

import logging
import fileinput
import sys
import os

import tweepy
import tweepy.streaming

class SearchStream(tweepy.streaming.StreamListener):
    def on_status(self, status):
        s = '%s @%s: %s\n' % (status.created_at, status.user.screen_name, status.text)
        output.write(s.encode('utf-8'))
        output.flush()
        return
    def on_limit(self, track):
        log.error('limitation imposed for %s' % track)
    def on_timeout(self):
        log.error('Twitter timeout')
    def on_error(self, status_code):
        log.error('HTTP error: %d' % status_code)
        return False

def track_search(terms):
    searcher = SearchStream(api=api)
    stream = tweepy.streaming.Stream(auth, searcher)
    try:
        stream.filter(track=terms)
    except KeyboardInterrupt:
        log.info('asking to leave...')
        output.close()
        stream.disconnect()

def usage(ret=1):
    parser.print_help()
    sys.exit(ret)

    
if __name__ == '__main__':
    parser = OptionParser(usage=u'usage: %prog [options]')
    parser.add_option('-C', '--consumer-key', dest='consumer_key', metavar="TOKEN",
                      help=u"Twitter consummer key")
    parser.add_option('-S', '--consumer-secret', dest='consumer_secret', metavar="TOKEN",
                      help=u"Twitter consummer secret")
    parser.add_option('-A', '--access-token', dest='access_token', metavar="TOKEN",
                      help=u"Twitter access key")
    parser.add_option('-K', '--access-key', dest='access_key', metavar="TOKEN",
                      help=u"Twitter access key")
    parser.add_option('-o', '--output', dest='output', metavar="FILE",
                      help=u"Write output in file")
    parser.add_option('-v', '--verbose', dest='verbose', action="store_true",
                      default=False, help=u"Verbose mode")
    parser.add_option('-d', '--debug', dest='debug', action="store_true",
                      default=False, help=u"Debug mode")
    parser.add_option('-t', '--track', dest='track', action="store_true",
                      default=True, help="Tracks keywords in realtime")
    parser.add_option('-O', '--old', dest='old', action="store_true",
                      default=False, help="Search past tweets (not implemented yet)")

    (options,args) = parser.parse_args()

    if not (options.consumer_secret and options.consumer_key
            and options.access_token and options.access_key):
        sys.stderr.write('You need to specify OAuth consumer and access token/secret\n\n')
        usage()

    if options.output:
        output = open(options.output, 'a')
    else:
        output = sys.stdout

    loglvl = logging.NOTICE if options.verbose else logging.INFO
    loglvl = logging.DEBUG if options.debug else logging.INFO

    logging.basicConfig(level=loglvl, format="%(asctime)s %(levelname)5s: %(message)s")
    log = logging.getLogger(sys.argv[0])

    auth = tweepy.OAuthHandler(options.consumer_key, options.consumer_secret)
    auth.set_access_token(options.access_token, options.access_key)
    api = tweepy.API(auth)

    if options.old:
        sys.stderr.write('Not implemented yet (XXX), sorry :(\n')
        sys.exit(2)
    elif options.track:
        track_search(args)
