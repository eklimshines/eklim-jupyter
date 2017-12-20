from __future__ import print_function
from optparse import OptionParser
from pkencrypt import *

parser=OptionParser()
parser.add_option("-d", "--data", dest="data", help="data", metavar="DATA")
(options,args)=parser.parse_args()

full_id_8 = sha256(options.data.decode('hex')).hexdigest()
hashedId8 = full_id_8[-16:]
print(hashedId8)


