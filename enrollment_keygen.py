from enrollment_helper import *

reqPrv, reqPub = enrollKeyGen()
print(reqPrv)
print(str(reqPub.output(compress=True, Ieee1609Dot2=True)))
