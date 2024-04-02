def factorise(n, e, q, s):
  """
  Fonction qui réalise une attaque par force brute pour factoriser un nombre n.

  Args:
    n: Le nombre à factoriser.
    e: La clé publique RSA.
    q: La valeur de q.
    s: La signature RSA.

  Returns:
    Un tuple (p, q), où p et q sont les deux facteurs premiers de n.
  """

  # Calcule la valeur de la fonction d'Euler φ(n).

  phi = (n - 1) * q

  # Initialise un compteur à 2.

  i = 2

  # Tant que le compteur est inférieur à φ(n), teste si le compteur est un diviseur de n.

  while i < phi:
    # Si le compteur est un diviseur de n, factorise n en p et q.
    if n % i == 0:
      return (n // i, i)

    # Incrémente le compteur.
    i += 1

  # Si le compteur a atteint φ(n) sans trouver de diviseur, le nombre n est premier.

  return (n, None)


# Exemple d'utilisation

e = 17
n = 47775493107113604137
q = 8548494751
s = int("0198fa581d330af21a", 16)

(p, q) = factorise(n, e, q, s)

print(f"n = {n} = {p} * {q}")
