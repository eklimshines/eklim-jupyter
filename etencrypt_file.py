'''
Created on Jul 18, 2017

@author: Griff Baily
'''
from __future__ import print_function
import binascii
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-f", "--file", dest="certfile", help="file for cert that public key is derived from", metavar="FILE")
parser.add_option("-c", "--contentfile", dest="contentfile", help="content file", metavar="CONTENTFILE")
parser.add_option("-r", "--recipk", dest="recipkey", help="recipient's public key", metavar="RECIPK")
parser.add_option("-p", "--plaint", dest="plaintext",help="contents of signedmbr in hex", metavar="PT")
parser.add_option("-y", "--ypoint", dest="ypoint",help="compressed y point to use, 0 or 1", metavar="YPT")

(options,args)=parser.parse_args()
from pkencrypt import *

recip_pub = ECPoint("compressed-y-"+options.ypoint,options.recipkey)

# Recipient's cert
cert_in=open(options.certfile,"r")
# MA cert
recip_cert = binascii.hexlify(cert_in.read())
cert_in.close()

if options.contentfile:
    full_output_path = "C:\Users\Shirali\Google Drive\eTrans Top Level\Clients\CAMP\MAI Project\MAI Tests\Shared Program Files\etencrypt_python_out.oer"
    # Plaintext
    with open(options.contentfile, 'r') as data_file:
        file_contents = data_file.read()
    data_file.close()

    with open(full_output_path,'w') as new_file:
        new_file.write(file_contents)
    new_file.close()

    plaintext = file_contents

else:
    plaintext =  options.plaintext

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