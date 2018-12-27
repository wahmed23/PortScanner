'''
Created on Oct 28, 2018

@author: groot
'''

import optparse
from socket import *
from threading import *

def portScan(hostname, targetPorts):
    IP = gethostbyname(hostname)
    if (IP == None):
        print('[-] Hostname can not be resolved to an IP Address')
        exit(0)
    else:
        print('[+] IPv4 address: '+str(IP))
        setdefaulttimeout(1)
        try:
            for port in targetPorts:
                t = Thread(target=connScan, args=(IP, int(port)))
                t.start()
        except:
            pass

ScreenLock = Semaphore(value=1)
def connScan(tgt_host, tgt_port):
    try:
        tgt_port_int = int(tgt_port)
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgt_host, tgt_port_int))
        connSkt.sendall(b'Violent Python')
        results = connSkt.recv(100)
        ScreenLock.acquire()
        print ('[+] %d/tcp open'% tgt_port_int)
        print ('[+] '+results.decode('utf-8'))
    except:
        ScreenLock.acquire()
        print('[-] %d/tcp closed'% tgt_port_int)
    finally:
        ScreenLock.release()
        connSkt.close()

def main():
    parser = optparse.OptionParser('usage%prog -H <target_host> -p <target_port>')
    parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parser.add_option('-p', dest='tgt_port', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_port = str(options.tgt_port).split(',')
    if (tgt_host == None) | (tgt_port[0] == None):
        print('[-] You must specify a target host and port[s]')
        exit(0)
    else:
        portScan(tgt_host, tgt_port)

if __name__ == '__main__':
    main()