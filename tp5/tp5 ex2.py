import Crypto.Util.number as cun

def dec_to_hex(num):
    return hex(num)[2:]

n = 47775493107113604137

s_prime = int("0198fa581d330af21a", 16)
s = int("3f010be37eb5eca9", 16)

print(f"^s = {s_prime} (0198fa581d330af21a)")
print(f"s = {s} (3f010be37eb5eca9)\n")

result = cun.GCD(n, s - s_prime)

print(f"Valeur de q trouver: {result}")
print(f"Sous format hexadecimal: {dec_to_hex(result)}\n")

#test 2

s_prime = int("b026739bdd7fe988", 16)
result = cun.GCD(n, s - s_prime)

print(f"^s = {s_prime} (b026739bdd7fe988)")
print(f"Valeur de q trouver: {result}")
print(f"Sous format hexadecimal: {dec_to_hex(result)}\n")

#test 3

s_prime = int("01b495c9edd2fc0081", 16)
result = cun.GCD(n, s - s_prime)

print(f"^s = {s_prime} (01b495c9edd2fc0081)")
print(f"Valeur de q trouver: {result}")
print(f"Sous format hexadecimal: {dec_to_hex(result)}\n")

e = 17
n = 47775493107113604137
q = result
p = n // q

print(f"Valeurs trouver:\ne: {e}, n: {n}, q: {q}, p: {p}\n")

print(f"n = {dec_to_hex(n)} = {dec_to_hex(p)} * {dec_to_hex(q)} (Valeurs afficher en hexadecimal)")

print(f"n = {n} = {p} * {q} (Valeurs afficher en decimal)\n")

def gen_rsa_keypair(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    assert(phi_n % e != 0)
    d = cun.inverse(e,phi_n)
    return ((e, n), (d, n)) 


pub, priv = gen_rsa_keypair(p, q, e)

print("Clé publique = ", pub)
print("Clé privée = ", priv, "\n")
