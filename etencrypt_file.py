'''
Created on Jul 18, 2017

@author: Griff Baily
'''
from __future__ import print_function
import binascii
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-f", "--file", dest="certfile", help="file for cert that public key is derived from", metavar="FILE")
parser.add_option("-cf", "--contentfile", dest="contentfile", help="content file", metavar="CONTENTFILE")
parser.add_option("-r", "--recipk", dest="recipkey", help="recipient's public key", metavar="RECIPK")
parser.add_option("-p", "--plaint", dest="plaintext",help="contents of signedmbr in hex", metavar="PT")
parser.add_option("-y", "--ypoint", dest="ypoint",help="compressed y point to use, 0 or 1", metavar="YPT")

(options,args)=parser.parse_args()
from pkencrypt import *

recip_pub = ECPoint("compressed-y-"+options.ypoint,options.recipkey)

# Recipient's cert
cert_in=open(options.certfile,"rb")
# MA cert
recip_cert = binascii.hexlify(cert_in.read())
cert_in.close()

# Plaintext
with open(options.contentfile, 'rb') as data_file:
    file_contents = data_file.read()

plaintext =  file_contents

# Encrypt to recipient's public key
recip_HashedId8, V, C, T, nonce, ccm_ciphertext = \
    PKEncrypt(plaintext, recip_pub, recip_cert)

print(recip_HashedId8)
V_out = V.output(compress=True, Ieee1609Dot2=True)
print(V_out)
print(C)
print(T.upper())
print(nonce)
print(ccm_ciphertext)