import numpy as np
import random
import hashlib

# Funkcje dla krzywych eliptycznych nad R
def ecc_r(x, a, b):
    return x ** 3 + a * x + b

def bits(n):
    while n:
        yield n & 1
        n >>= 1

def add_r(P, Q, a):
    if P is None or Q is None:
        return P or Q
    p_x, p_y = P
    q_x, q_y = Q
    if p_x == q_x:
        return double_r(P, a)
    m = (p_y - q_y) / (p_x - q_x)
    r_x = m**2 - p_x - q_x
    r_y = p_y + m * (r_x - p_x)
    return (r_x, -r_y)

def double_r(P, a):
    if P is None:
        return None
    p_x, p_y = P
    m = (3 * p_x ** 2 + a) / (2 * p_y)
    r_x = m**2 - 2*p_x
    r_y = p_y + m * (r_x - p_x)
    return (r_x, -r_y)

def double_and_add_r(n, P, a):
    result = None
    addend = P
    for b in bits(n):
        if b:
            result = add_r(result, addend, a)
        addend = double_r(addend, a)
    return result

def plot_r(plt, a, b):
    if a >= 0 and b >= 0:
        plt.title('y^2 = x^3 + {a}x + {b}' .format(a=a, b=b), fontsize=15, color= 'red', fontweight='bold')
    elif a < 0 and b >= 0:
        plt.title('y^2 = x^3 {a}x + {b}' .format(a=a, b=b), fontsize=15, color= 'red', fontweight='bold')
    elif a >= 0 and b < 0:
        plt.title('y^2 = x^3 + {a}x {b}' .format(a=a, b=b), fontsize=15, color= 'red', fontweight='bold')
    elif a < 0 and b < 0:
        plt.title('y^2 = x^3 {a}x {b}' .format(a=a, b=b), fontsize=15, color= 'red', fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')

# Funkcje dla krzywych eliptycznych F(p)
def ecc_f(x, p, a, b):
            return (x**3 + a*x + b) % p

def sqrt_f(x, y2, p):
            x2 = x**2 % p
            y = [(i, *i_y) for i, i_y in enumerate([np.where(i_y2 == x2)[0] for i_y2 in y2]) if i_y.size > 0]
            return y

def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('Dzielenie przez 0')
    if k < 0:
        return p - inverse_mod(-k, p)
    # Rozszerzony algorytm Euklidesa
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    gcd, x, y = old_r, old_s, old_t
    assert gcd == 1
    assert (k * x) % p == 1
    return x % p

def point_neg(P, p):
    if P is None:
        return None
    P_x, P_y = P
    result = (P_x, -P_y % p)
    return result

def point_add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P
    P_x, P_y = P
    Q_x, Q_y = Q
    if P_x == Q_x and P_y != Q_y:
        return None
    if P_x == Q_x:
        m = (3 * P_x * P_x + a) * inverse_mod(2 * P_y, p)
    else:
        m = (P_y - Q_y) * inverse_mod(P_x - Q_x, p)
    R_x = m * m - P_x - Q_x
    R_y = P_y + m * (R_x - P_x)
    result = (R_x % p, -R_y % p)
    return result

def scalar_mult(k, P, a, p):
    if P is None:
        return None
    if k < 0:
        return scalar_mult(-k, point_neg(P, p), a, p)
    result = None
    addend = P
    while k:
        if k & 1:
            result = point_add(result, addend, a, p)
        addend = point_add(addend, addend, a, p)
        k >>= 1
    return result

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

def czy_nalezy(P, y):
    p_x, p_y = P
    for y_p in y:
        for i in range(1, len(y_p)):
            if p_x == y_p[0] and p_y == y_p[i]:
                return True
    return False

def plot_f(plt, a, b, p):
    if a >= 0 and b >= 0:
        plt.title('y^2 = x^3 + {a}x + {b} mod {p}' .format(a=a, b=b, p=p), fontsize=15, color= 'red', fontweight='bold')
    elif a < 0 and b >= 0:
        plt.title('y^2 = x^3 {a}x + {b} mod {p}' .format(a=a, b=b, p=p), fontsize=15, color= 'red', fontweight='bold')
    elif a >= 0 and b < 0:
        plt.title('y^2 = x^3 + {a}x {b} mod {p}' .format(a=a, b=b, p=p), fontsize=15, color= 'red', fontweight='bold')
    elif a < 0 and b < 0:
        plt.title('y^2 = x^3 {a}x {b} mod {p}' .format(a=a, b=b, p=p), fontsize=15, color= 'red', fontweight='bold')
    plt.xlabel('x')
    plt.ylabel('y')

# Funkcje dla szyfrowania ECDSA
def make_keypair(curve):
    private_key = random.randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g, curve.a, curve.p)
    return private_key, public_key

def hash_message(message, curve):
    message_hash = hashlib.sha512(message).digest()
    e = int.from_bytes(message_hash, 'big')
    z = e >> (e.bit_length() - curve.n.bit_length())
    assert z.bit_length() <= curve.n.bit_length()
    return z

def sign_message(private_key, message, curve):
    z = hash_message(message, curve)
    r = 0
    s = 0
    while not r or not s:
        k = random.randrange(1, curve.n)
        x, y = scalar_mult(k, curve.g, curve.a, curve.p)
        r = x % curve.n
        s = ((z + r * private_key) * inverse_mod(k, curve.n)) % curve.n
    return (r, s)

def verify_signature(public_key, message, signature, curve):
    z = hash_message(message, curve)
    r, s = signature
    w = inverse_mod(s, curve.n)
    u1 = (z * w) % curve.n
    u2 = (r * w) % curve.n
    x, y = point_add(scalar_mult(u1, curve.g, curve.a, curve.p),
                     scalar_mult(u2, public_key, curve.a, curve.p), curve.a, curve.p)
    if (r % curve.n) == (x % curve.n):
        return True
    else:
        return False

