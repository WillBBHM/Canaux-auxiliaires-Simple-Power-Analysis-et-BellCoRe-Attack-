m = int("42c0ffee93", 16)
m_fake = int("42c0ffee91", 16)
N = int("02c99a781f", 16)
s = int("02306bf1b7", 16)
s_fake = int("01ab20ac6d", 16)

d = int("111101000101010110110011000001", 2) #1024814273

print("Valeur de d trouver trouver d'après la consomation: {d}\n")

print(f"Valeur de N: {N}")
print(f"Message: {m}")
print(f"Message chiffrer: {s}")
print(f"Message chiffrer trouver: {int(pow(m, d, N))}\n\n")


print(f"Valeur de N: {N}")
print(f"Message: {m_fake}")
print(f"Message chiffrer: {s_fake}")
print(f"Message chiffrer trouver: {int(pow(m_fake, d, N))}")


