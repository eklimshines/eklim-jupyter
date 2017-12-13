from pseudosign import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-f", "--file", dest="file_to_open", help="file containing data to sign", metavar="FILE")
parser.add_option("-d", "--data", dest="data", help="to be signed data", metavar="DATA")
parser.add_option("-p", "--privatekey", dest="privKey", help="private key", metavar="PRIV")
parser.add_option("-c", "--certificate", dest="certificate", help="certificate to use", metavar="CERT")


(options,args)=parser.parse_args()
with open(options.file_to_open, 'rb') as data_file:
    file_contents = data_file.read()
    file_hex = ''.join( [ "%02X " % ord( x ) for x in file_contents ] ).strip()
    file_output_path = "C:/Users/Shirali/Google Drive/eTrans Top Level/Clients/CAMP/MAI Project/MAI Tests/Shared Program Files/file_hex.txt"

    file_to_write = open(file_output_path, "wb")
    file_to_write.write(file_hex)

(R, s, digest,cert_dgst) = PseudonymSign(file_hex, options.privKey, options.certificate)
print(R.output(compress=True, Ieee1609Dot2=True))
print (Hex(s, radix_256))
print(cert_dgst[-16:])
