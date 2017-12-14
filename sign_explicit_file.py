from pseudosign import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-f", "--file", dest="file_to_open", help="file containing data to sign", metavar="FILE")
parser.add_option("-d", "--data", dest="data", help="to be signed data", metavar="DATA")
parser.add_option("-p", "--privatekey", dest="privKey", help="private key", metavar="PRIV")
parser.add_option("-c", "--certificate", dest="certificate", help="certificate to use", metavar="CERT")

(options,args)=parser.parse_args()

if options.file_to_open:
    with open(options.file_to_open, 'r') as data_file:
        file_contents = data_file.read()
    data_file.close()
    the_data = file_contents
else:
    the_data = options.data

(R, s, digest,cert_dgst) = PseudonymSign(the_data, options.privKey, options.certificate)
print(R.output(compress=True, Ieee1609Dot2=True))
print (Hex(s, radix_256))
print(cert_dgst[-16:])
