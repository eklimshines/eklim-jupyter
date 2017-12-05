from enrollment_helper import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-p", "--privKeyRecon", dest="privKeyRecon", help="Provate key rescontruction value", metavar="PRIRECON")
parser.add_option("-t", "--enrollmentCertTbs", dest="enrollmentCertTbs", help="Enrollment cert TBS data", metavar="ENROLLTBS")
parser.add_option("-e", "--ecaCert", dest="ecaCert", help="ECA certificate", metavar="ECACERT")
parser.add_option("-b", "--basePrivateKey", dest="basePrivateKey", help="Base private key", metavar="BASEPRIV")
(options,args)=parser.parse_args()

cert_digest = create1609Dot2Digest(options.enrollmentCertTbs, options.ecaCert)[0]
enroll_private_key = reconstructPrivateKey(options.basePrivateKey, cert_digest, options.privKeyRecon, sec4=False, cert_dgst=True)

print(enroll_private_key)

def keyGen() :
    # compute an ECC keypair for the request
    prv_long = randint(1, genP256.ecc.n-1)
    reqPrv = "{0:0>{width}X}".format(prv_long, width=bitLen(genP256.ecc.n)*2/8)
    reqPub = prv_long*genP256
    return (reqPrv, reqPub)

# create butterfly keys
verifyKeyPriv, verifyKeyPub = keyGen()
print(verifyKeyPriv)
print(str(verifyKeyPub.output(compress=True, Ieee1609Dot2=True)))
respEncPriv, respEncKeyPub = keyGen()
print(respEncPriv)
print(str(respEncKeyPub.output(compress=True, Ieee1609Dot2=True)))
