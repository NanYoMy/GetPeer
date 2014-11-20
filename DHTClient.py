#encoding: utf-8
#！/usr/bin
#!/usr/bin/env python

import logging
from time import sleep
from Config import *
from utility import *
from DHTNode import *

stdger = logging.getLogger("std_log")
fileger = logging.getLogger("file_log")

#using example
class Master(object):

    def log(self, infohash, address=None):
        stdger.debug("%s from %s:%s" % (infohash.encode("hex"), address[0], address[1]))
        fileger.debug('%s from %s:%s' % (infohash.encode('hex').upper(),address[0],address[1]))


if __name__ == "__main__":
    #max_node_qsize bigger, bandwith bigger, spped higher
    initialLog()
    threads = []
    for i in xrange(THREAD_NUMBER):
        port = i+9500
        stdger.debug("start thread %d" % port)
        dht=DHT(Master(), "0.0.0.0", port, max_node_qsize=1000)
        dht.start()
        threads.append(dht)
        sleep(1)


    sleep(60*60*6)

    k = 0
    for i in threads:
        stdger.debug("stop thread %d" % k)
        i.stop()
        i.join()
        k=k+1
