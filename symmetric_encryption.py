from __future__ import print_function
import binascii
from optparse import OptionParser
from pkencrypt import *
import random

parser=OptionParser()
parser.add_option("-c", "--contentfile", dest="contentfile", help="content file", metavar="CONTENTFILE")
parser.add_option("-r", "--recipkey", dest="recipkey", help="recipkey", metavar="RECIPKEY")
parser.add_option("-d", "--data", dest="data", help="data", metavar="DATA")
(options,args)=parser.parse_args()

options.recipkey = "FB29BCBED09E7CBC1066C73525C857C2"

recip_cert_dgst = sha256(options.recipkey.decode('hex')).hexdigest()
recip_HashedId8 = recip_cert_dgst[-16:]
plaintext = options.data
data_nonce_long = getrandbits(12*8)   # 12 bytes
dataNonce = long2hexstr(data_nonce_long, 12*8)
data_key_long = getrandbits(16*8)   # 12 bytes
dataKey = long2hexstr(data_key_long, 16*8)
dataCiphertext = aes_ccm_enc(dataKey, dataNonce, plaintext)
# Now we encrypt the dataKey for the recipient

recipKey = options.recipkey
recip_nonce_long = getrandbits(12*8)   # 12 bytes
recipNonce = long2hexstr(recip_nonce_long, 12*8)
recipCiphertext = aes_ccm_enc(recipKey, recipNonce, dataKey)


# These values would then be placed into the appropriate fields in the
# EncryptedData. As mentioned above, to compute the recipientId you will
# need to place the recipKey into a SymmetricEncryptionKey object and compute
# the HashedId8 on its encoding
print(dataCiphertext)
print(dataNonce)
print(dataKey)
print(recipCiphertext)
print(recipNonce)



