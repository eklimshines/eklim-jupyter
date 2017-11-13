from bfkeyexp import *
from ecc import *
from implicit import *
from pkencrypt import *
from pseudosign import *

def DecryptSECR(v, c, t, nonce, ctxt, encSeed, encExp, iVal, jVal) :
    '''
    Decrypts a SignedEncryptedCertificateResponse from a pseudo cert batch file.

    v, c, t, nonce, ctxt are parsed from the response.
    encSeed, encExp are part of the original request.
    iVal, jVal are derived from the filename i_j.

    Inputs:
    - v:            {ec256 point}   ephemeral public key of sender
    - c:            {octet string}  encrypted symmetric key
    - t:            {octet string}  authentication tag
    - nonce:        {octet string}  AES nonce
    - ctxt:         {octet string}  AES ciphertext
    - encSeed:      {long}          seed encryption key from request
    - encExp:       {long}          encryption expansion value from request
    - iVal, jVal:   {long}          i,j values for the given certificate

    Outputs:
    - ptxt:     {octet string}  OER encoded Ieee1609Dot2Data content=
                                UnsecuredData, containing an OER encoded
                                PlaintextCertificateResponse
    '''

    # butterfly expand the keys to get the encryption keypair for (i,j)
    prv, pub = bfexpandkey(iVal, jVal, encExp, encSeed, "enc")

    # convert prv key to a hex string for use below
    prvHex = '{:X}'.format(prv)

    # decrypt the ciphertext using the encrypted key
    ptxt = PKDecrypt(v, c, t, "", prvHex, nonce, ctxt)

    return ptxt.upper()



if __name__ == "__main__":

# Step 1: Decrypt the SECR

    # values from security_params.txt
    signPrv = 0xe36fa09b763502756f2d14f83885a75f37b3238be1217b9215d411791ad6474c
    signExp = 0x831d918aad95432279b04e7f432b8f43
    encPrv  = 0x9094af7ad265cffb6caf57700df7a6d70e29eae83c326eaae7083318ce6325e4
    encExp  = 0x40bf96514b66d4de792225c996b21b68

    # i,j from filename = 94_0
    iVal = 0x94
    jVal = 0x0

    # v,c,t copied from 94_0 via asn1 tools
    # NOTE: make sure v is set to the correct point type (y-0 / y-1)
    v = ECPoint("compressed-y-0","85277F54BB51CD3C4E5904F4EE56D92CF622C32C0E40B4BB125A98FD623CE317")
    c = "BABE3D42930283127352AEE69F0697BF"
    t = "88B0A62209A7348FF8D2A38F0A5C57B5"

    # AES ciphertext containing the cert response, copied from 94_0 via asn1 tools
    nonce = "216EA0440A2CE3CC69AE9B32"
    ctxt = "5C4114995A1CA8FCCD82D749870D5EA90865A0FE6CE75DBDE688C07D614A7A136A716730785BD696CC66B4C315EC3FF5F1984A1BA4849A90B94F669A9BEFDC290791BDEC866CC1FED27429EAC2D6B3485CD8E47558C7015BE74935FC8A7539A4A61BE510DA2D17BB45E436B0D0917234DA0E67A94D83485B76089FB5809AC8C0E37A4C0C8E0C495AB35D5AB060F1"

    print("\nDecrypting SECR...")
    ptxt = DecryptSECR(v, c, t, nonce, ctxt, encPrv, encExp, iVal, jVal)

    # UnsecuredData containing PlaintextCertificateResponse
    print("Ieee1609Dot2Data, content=UnsecuredData containing PlaintextCertificateResponse:\n" + ptxt + "\n")


# Step 2: Recover the pseudo cert + signing key

    # These values are retrieved from the PlaintextCertificateResponse via asn1 tools
    pseudoCert = "0003018027a69ece71cb778550800000942b71029c5cf41e154fcb778500011a0e13108400a983010180034801028001208000800126800081828ad4c0ecc95ce234750673d5f359b5ab36ab57312f8fac4114e9c86f8d8cdf72".upper()
    prvRecon = "5910C2F6230D2B9F2CD361CF185838F640F72B5EE5941520E53300A4691B35F3"

    # These are pulled out of the pseudo cert
    # NOTE: Make sure correct point type is set (y-0 / y-1)
    pseudoTbs = "50800000942B71029C5CF41E154FCB778500011A0E13108400A983010180034801028001208000800126800081828AD4C0ECC95CE234750673D5F359B5AB36AB57312F8FAC4114E9C86F8D8CDF72"
    pubRecon = ECPoint("compressed-y-0", "8AD4C0ECC95CE234750673D5F359B5AB36AB57312F8FAC4114E9C86F8D8CDF72")

    # The pca cert + key, from trustedcerts/pca.
    # NOTE: Make sure correct point type is set (y-0 / y-1)
    pcaCert = "8003008057C95A3362F1FC395981147063612E746573742E76327873636D732E636F6DF1FC39000219BB049086000483010380007C8001E480034801018001238003850001010100810080839CBF806B67AE4C4C4244F5214BC36822AAD5E4E8A65E6035AF4C4C24FED785B6808082D43526739665CE3D4AB90351F4BEAAB04E465622D829CB8F51FE61A71456B4188080514BB8FD14FD3977FB6C46DCD5DE07010ACD97906A2544B92E54017331CB5261443643541379EDA85B735797A84EF72F0775719B2F1BB5C35762CC2F33AF56B5"
    pcaPub = ECPoint("compressed-y-0", "D43526739665CE3D4AB90351F4BEAAB04E465622D829CB8F51FE61A71456B418")

    print("Reconstructing private signing for pseudo cert %X_%X..." % (iVal,jVal))
    pseudoPrv = BFExpandAndReconstructKey(signPrv, signExp, iVal, jVal, prvRecon, pseudoTbs, pcaCert)[0]

    print(pseudoPrv)


# Step 3: Sign some data

    # replace this with the tbsData portion of an OER encoded Ieee1609DotData,
    # content=SignedData
    tbsData = "00112233445566778899AABBCCDDEEFF"

    print("\nSigning tbsData using pseudo cert %x_%x..." % (iVal,jVal))
    r, s = PseudonymSign(tbsData, pseudoPrv, pseudoCert)[:2]

    # Write r,s to the Ieee1609Dot2Data, content=SignedData as the signature
    print("Signature: ")
    print("r: (\"x-only\", " + r.output(compress=True, Ieee1609Dot2=True)[1].upper() + ")")
    print("s: " + '{:X}'.format(s))

# Sanity check, does our signature verify correctly?
    result = PseudonymVerify(r, s, tbsData, pseudoCert, pseudoTbs, pubRecon, pcaCert, pcaPub)
    print("\nSignature verifies? %r\n" % result)
