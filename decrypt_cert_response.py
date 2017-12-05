'''
Decrypt the information from an encrypted certificate response
'''
from __future__ import print_function
import binascii
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-i", "--iValue", dest="iValue", help="iValue for the certificate", metavar="IVALUE")
parser.add_option("-j", "--jValue", dest="jValue", help="jValue for the certificate", metavar="IVALUE")
parser.add_option("-y", "--yPoint", dest="yPoint",help="compressed y point to use, 0 or 1", metavar="YPT")
parser.add_option("", "--yValue", dest="yValue", help="the yValue data", metavar="YVAL")
parser.add_option("-c", "--cValue", dest="c", help="the encrypted symmetric key", metavar="CVAL")
parser.add_option("-t", "--tValue", dest="t", help="the authentication tag", metavar="TVAL")
parser.add_option("-n", "--nonce", dest="nonce", help="AES nonce", metavar="NONCE")
parser.add_option("", "--ciphertext", dest="ciphertext", help="AES ciphertext", metavar="CIPHER")
parser.add_option("-e", "--encExpansion", dest="encExpansion", help="Response Encryption Expansion", metavar="ENCEXP")
parser.add_option("-r", "--encSeed", dest="encSeed", help="Response Encryption Private Key", metavar="PRVEXP")

(options,args)=parser.parse_args()
from bfkeyexp import *
from ecc import *
from implicit import *
from pkencrypt import *

# NOTE: make sure v is set to the correct point type (y-0 / y-1)
v = ECPoint("compressed-y-"+options.yPoint,options.yValue)

# butterfly expand the keys to get the encryption keypair for (i,j)
prv, pub = bfexpandkey(long(options.iValue), long(options.jValue), long(options.encExpansion,16), options.encSeed, "enc")

# convert prv key to a hex string for use below
prvHex = '{:X}'.format(prv)

# decrypt the ciphertext using the encrypted key
ptxt = PKDecrypt(v, options.c, options.t, "", prvHex, options.nonce, options.ciphertext)

print(ptxt.upper())
