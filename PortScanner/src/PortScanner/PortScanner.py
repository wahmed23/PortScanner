'''
Created on Oct 28, 2018

@author: groot
'''

import optparse
from socket import *

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
                connScan(IP, port)
        except:
            pass

def connScan(tgt_host, tgt_port):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgt_host, tgt_port))
        connSkt.sendall(b'Violent Python')
        results = connSkt.recv(100)
        print ('[+] %d/tcp open'% tgt_port)
        print ('[+] '+str(results))
        connSkt.close()
    except:
        print('[-] %d/tcp closed'% tgt_port)

def main():
    parser = optparse.OptionParser('usage %prog -H <target_host> -p <target_port>')
    parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parser.add_option('-p', dest='tgt_port', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_port = options.tgt_port
    if (tgt_host == None) | (tgt_port == None):
        print (parser.usage)
        exit(0)
    else:
        portList = [21,22,25,80,443]
        portScan(tgt_host, portList)

if __name__ == '__main__':
    main()