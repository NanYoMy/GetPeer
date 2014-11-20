__author__ = 'dwb'

import socket
import logging
import logging.handlers
from hashlib import sha1
from random import randint
from struct import unpack, pack
from socket import inet_aton, inet_ntoa
from threading import Timer, Thread


def initialLog():

    stdLogLevel = logging.ERROR
    fileLogLevel = logging.DEBUG
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(formatter)

    file_handler = logging.handlers.RotatingFileHandler("HASH.log", maxBytes=1024*1024*20, backupCount=10000)
    file_handler.setFormatter(formatter)

    logging.getLogger("file_log").setLevel(fileLogLevel)
    logging.getLogger("file_log").addHandler(file_handler)
    logging.getLogger("std_log").setLevel(stdLogLevel)
    logging.getLogger("std_log").addHandler(stdout_handler)

def entropy(length):
    chars = []
    for i in range(length):
        chars.append(chr(randint(0, 255)))
    return "".join(chars)

def random_id():
    hash = sha1()
    hash.update(entropy(20))
    return hash.digest()

def decode_nodes(nodes):
    n = []
    length = len(nodes)
    if (length % 26) != 0:
        return n

    for i in range(0, length, 26):
        nid = nodes[i:i+20]
        ip = inet_ntoa(nodes[i+20:i+24])
        port = unpack("!H", nodes[i+24:i+26])[0]
        n.append((nid, ip, port))
    return n

def timer(t, f):
    Timer(t, f).start()

def get_neighbor(target, end=10):

    return target[:end]+random_id()[end:]