# bottle-gevent-example
a quick example of Bottle framework with Gevent for prototype deployment

requirements

Python 2.7.x - 3.5.x

**Bottle** - Excellent Microframework by Hellkamp (http://bottlepy.org)

**GEvent** - Lightweight networking library from which we utilize a robust WSGI server (http://gevent.org)

**btest.py** - run this directly, by default it runs on port 54321

  command line switches:
  
  --deploy - uses the GEvent WSGI server.  Should be suitable for deployment (caveat emptor).
  
  --port xxxx - listen to a particular port where xxxx is an integer (upper limit 65535)

**btest-noGevent.py** - simple prototype using built-in development server only, does not require GEvent.
