from pseudosign import *
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-f", "--file", dest="file_to_open", help="file containing data to sign", metavar="FILE")
parser.add_option("-d", "--data", dest="data", help="to be signed data", metavar="DATA")
parser.add_option("-p", "--privatekey", dest="privKey", help="private key", metavar="PRIV")
parser.add_option("-c", "--certificate", dest="certificate", help="certificate to use", metavar="CERT")


(options,args)=parser.parse_args()
with open(options.file_to_open, 'r') as data_file:
    file_contents = data_file.read()

full_output_path = "C:\Users\Shirali\Google Drive\eTrans Top Level\Clients\CAMP\MAI Project\MAI Tests\Shared Program Files\sign_explicit_python_out.oer"

with open(full_output_path,'wb') as new_file:
    new_file.write(file_contents)

(R, s, digest,cert_dgst) = PseudonymSign(file_contents, options.privKey, options.certificate)
print(R.output(compress=True, Ieee1609Dot2=True))
print (Hex(s, radix_256))
print(cert_dgst[-16:])
