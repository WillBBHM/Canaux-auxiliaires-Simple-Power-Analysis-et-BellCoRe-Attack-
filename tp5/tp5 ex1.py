from Crypto.Util.number import getPrime
from Crypto.Util.number import inverse
import random
import time
import hashlib

def gen_prime(bits):
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    return p, q

def gen_rsa_keypair(p, q):
    n = p * q
    print("n = ", n, "\n")
    phi_n = (p - 1) * (q - 1)
    e = 65537
    print("e = ", e, "\n")
    assert(phi_n % e != 0)
    d = inverse(e,phi_n)
    return ((e, n), (d, n))

def gen_rsa_crt_keypair(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    assert(phi_n % e != 0)
    d = inverse(e,phi_n)
    print("d = ", d, "\n")
    dp = d % (p - 1)
    dq = d % (q - 1)
    print("dp = ", dp, "\n")
    print("dq = ", dq, "\n")
    qinv = inverse(q, p)
    return ((e, n), (p, q, dp, dq, qinv))

def rsa(message, key):
    e, n = key
    return pow(message, e, n)

def rsa_enc(message,key):
    return rsa(message,key)

def rsa_crt(message, key):
    p, q, dp, dq, qinv = key
    sP = pow(message, dp, p)
    sQ = pow(message, dq, q)
    s = sQ + q * (qinv*(sP - sQ) % p)
    return s

def rsa_crt_enc(message,key):
    return rsa_crt(message,key)

def h(n):
    sha256 = int(hashlib.sha256(str(n).encode()).hexdigest(), 16)
    return sha256

def rsa_sign(rsa_msg, clef):
    msg_hash = h(rsa_msg)
    return (rsa_msg, rsa_enc(msg_hash, clef))

def rsa_sign_crt(rsa_msg, clef):
    msg_hash = h(rsa_msg)
    return (rsa_msg, rsa_crt_enc(msg_hash, clef))

def rsa_verify(signature_hash, signature,key):
    print(signature_hash, signature, key)
    return rsa(signature_hash, key) == signature

def rsa_verify_crt(signature_hash, signature,key):
    print(signature_hash, signature, key)
    return rsa(signature_hash, key) == signature

def decrypt_rsa(c, clef):
    return rsa(c, clef)

p, q = gen_prime(512)

print("p = ", p, "\n")
print("q = ", q, "\n")

m = random.randint(0, 1000)

print("m = ", m, "\n")

Ap, As = gen_rsa_keypair(p, q)
Acrt, Ascrt = gen_rsa_crt_keypair(p, q)

c = rsa_enc(m, As)
crt = rsa_crt_enc(m, Ascrt)

start = time.time()
for _ in range(1000):
   signed_message = rsa_sign(m, As)
end = time.time()

print("Temps de calcul de 1000 signature rsa classique: ", end - start, "\n")

start = time.time()
for _ in range(1000):
    signed_message_crt = rsa_sign_crt(m, Ascrt)
end = time.time()

print("Temps de calcul de 1000 signatures CRT-RSA : ", end - start, "\n")

signed_message = rsa_sign(m, As)
signed_message_crt = rsa_sign_crt(m, Ascrt)
print(signed_message, "\n")
print(signed_message_crt, "\n")

print("Vérification de la signature rsa classique : ", rsa_verify(signed_message[1], h(signed_message[0]), Ap), "\n")
print("Vérification de la signature CRT-RSA : ", rsa_verify_crt(signed_message_crt[1], h(signed_message_crt[0]), Acrt), "\n")

if(rsa_verify(signed_message[1], h(signed_message[0]), Ap) == rsa_verify_crt(signed_message_crt[1], h(signed_message_crt[0]), Acrt)):
    print("Les deux signatures sont identique\n")

print("Déchiffrement rsa classique : ", decrypt_rsa(c, Ap), "\n")
print("Déchiffrement CRT-RSA : ", decrypt_rsa(crt, Acrt), "\n")

if(decrypt_rsa(c, Ap) == decrypt_rsa(crt, Acrt)):
    print("Les deux cryptages rsa et rsa crt donne un résultat identique ils sont donc correcte\n")