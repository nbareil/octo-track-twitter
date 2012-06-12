octo-track-twitter
==================

Track keywords on Twitter, this is the web 2.0 equivalent of `tail -f`.

It uses OAuth and Twitter's Streaming API to get status in real-time.

usage
=====

```
$ ./octo-twitter-track sstic alcohol
2012-06-12 18:49:28 @xxx: Nearly missed our stop on the bus for the second time today which can only associated with our lack of sleep/ alcohol intake last night.
^C
$ ./octo-track-twitter alcohol -o /dev/stdout | tee -a alcohol.log
$ ./octo-track-twitter -h
Usage: octo-track-twitter.py [options]
 
Options:
     -h, --help            show this help message and exit
     -C TOKEN, --consumer-key=TOKEN
                           Twitter consummer key
     -S TOKEN, --consumer-secret=TOKEN
                           Twitter consummer secret
     -A TOKEN, --access-token=TOKEN
                           Twitter access key
     -K TOKEN, --access-key=TOKEN
                           Twitter access key
     -o FILE, --output=FILE
                           Write output in file
     -v, --verbose         Verbose mode
     -d, --debug           Debug mode
     -t, --track           Tracks keywords in realtime
     -O, --old             Search past tweets (not implemented yet)

```
installation
============

```
$ sudo pip install tweepy
```

Twitter OAuth credentials
=========================

You need to create an application on [Twitter Dev board](https://dev.twitter.com/apps/new)
to get consumer and access credentials. Then put these information in `~/.config/octo-track-twitter/`
like above:

```
$ mkdir -p "${HOME}/.config/octo-track-twitter"
$ cat > "${HOME}/.config/octo-track-twitter/conf.sh"

CONSUMER_KEY="XXX" # obtained from https://dev.twitter.com/apps/new
CONSUMER_SECRET="XXX"

# access token
ACCESS_TOKEN="XXX"
ACCESS_KEY="XXX"
```
