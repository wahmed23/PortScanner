'''
Created on Oct 28, 2018

@author: groot
'''

import optparse

def main():
    parser = optparse.OptionParser('usage %prog -H <target_host> -p <target_ip>')
    parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parser.add_option('-p', dest='tgt_port', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_port = options.tgt_port
    if (tgt_host == None) | (tgt_port == None):
        print parser.usage
        exit(0)
if __name__ == '__main__':
    main()