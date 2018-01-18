from enrollment_helper import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-d", "--data", dest="data", help="to be signed data", metavar="DATA")
parser.add_option("", "--privatekey", dest="privKey", help="private key", metavar="PRIV")
parser.add_option("", "--publickey", dest="pubKey", help="public key", metavar="PUB")
parser.add_option("-y", "--ypoint", dest="yPoint", help="y point for the public key", metavar="YPT")
(options,args)=parser.parse_args()

pub_ec_point = ECPoint("compressed-y-"+options.yPoint, options.pubKey)

r, s = selfSignEnrollRequest(options.data, options.privKey, pub_ec_point)
print(r.output(compress=True, Ieee1609Dot2=True)[1].upper())
print('{:X}'.format(s))
