# This module encrypts data to a public key holder, i.e. of type
# PKRecipientInfo in 1609.2, specifically certRecipInfo:
# - Plaintext is encrypted with AES-CCM using a random AES key
# - The AES key is encrypted to the recipient's public key using
#   ECIES as specified in 1609.2

from __future__ import print_function

from aesccm import * #aes_ccm_enc, aes_ccm_dec
from ecies import * #ecies_enc, ecies_dec

# Generator point on curve NistP256
genP256 = ECPoint(secp256r1.gx, secp256r1.gy, secp256r1)

def PKEncrypt(plaintext, recip_pub_key, recip_cert):
    # Generate random AES 128-bit key
    k_long = getrandbits(128)
    k = long2hexstr(k_long, 128)

    nonce_long = getrandbits(12*8)   # 12 bytes
    nonce = long2hexstr(nonce_long, 12*8)

    # Encrypt plaintext with AES-CCM
    ccm_ciphertext = aes_ccm_enc(k, nonce, plaintext)

    # Encrypt AES key with ECIES
    ## P1 = Hash(recipient cert)
    P1 = recip_cert_dgst = sha256(recip_cert.decode('hex')).hexdigest()
    recip_cert_HashedId8 = recip_cert_dgst[-16:]
    V, C, T, _ = ecies_enc(recip_pub_key, k, P1)

    return recip_cert_HashedId8, V, C, T, nonce, ccm_ciphertext

def PKDecrypt(V, C, T, recip_cert, recip_prv_key, nonce, ccm_ciphertext):
    # Note: the recipient cert should be fetched by and matched with the
    #       the recipient's HashedId8

    # Decrypt AES key with ECIES
    ## P1 = Hash(recipient cert)
    P1 = recip_cert_dgst = sha256(recip_cert.decode('hex')).hexdigest()
    k = ecies_dec(V, C, T, recip_prv_key, P1)

    # Decrypt ciphertext with AES-CCM
    plaintext = aes_ccm_dec(k, nonce, ccm_ciphertext)

    return plaintext

# Generate a key pair to use as the recipient's encryption key
recip_prv_long = randint(1, genP256.ecc.n-1)
recip_prv = long2hexstr(recip_prv_long, 256)
recip_pub = recip_prv_long * genP256

# Recipient's cert (random value here for testing)
recip_cert_long = getrandbits(1000)
recip_cert = long2hexstr(recip_cert_long, 1000)

# Plaintext (random value here for testing)
plaintext_long = getrandbits(2000)
plaintext = long2hexstr(plaintext_long, 2000)

# Encrypt to recipient's public key
recip_HashedId8, V, C, T, nonce, ccm_ciphertext = \
    PKEncrypt(plaintext, recip_pub, recip_cert)

print("recip_prv_key = " + recip_prv)
recip_pub_out = recip_pub.output(compress=True, Ieee1609Dot2=True)
print("recip_pub_key = ", recip_pub_out)

print("plaintext = " + plaintext)
print("recipientId = " + recip_HashedId8)
V_out = V.output(compress=True, Ieee1609Dot2=True)
print("V = ", V_out)
print("C = " + C)
print("T = " + T.upper())
print("nonce = " + nonce)
print("ccm_ciphertext = " + ccm_ciphertext)

decrypt_out = PKDecrypt(V, C, T, recip_cert, recip_prv, nonce, ccm_ciphertext)

if (decrypt_out == plaintext):
    print("Successful Decryption!")
else:
    print("ERROR: decryption output does not match plaintext")
