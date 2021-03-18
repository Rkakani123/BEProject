import collections
import hashlib
import random

EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')

curve = EllipticCurve(
    'secp256k1',
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    a=0,
    b=7,
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    h=1,
)

def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k, p)

    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t
    return x % p

def is_on_curve(point):
    if point is None:
        return True
    x, y = point
    return (y ** 2 - x ** 3 - curve.a * x - curve.b) % curve.p == 0

def point_neg(point):
    if point is None:
       return None
    x, y = point
    result = (x, -y % curve.p)
    return result

def point_add(point1, point2):
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 and y1 != y2:
       return None
    if x1 == x2:
        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p, -y3 % curve.p)

    return result

def scalar_mult(k, point):
    if k % curve.n == 0 or point is None:
        return None
    if k < 0:
        return scalar_mult(-k, point_neg(point))
    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result

def make_keypair():
    private_key = random.randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g)

    return private_key, public_key


def hash_message(message):
    message_hash = hashlib.sha512(message).digest()
    e = int.from_bytes(message_hash, 'big')
    z = e >> (e.bit_length() - curve.n.bit_length())
    return z

def sign_message(private_key, message):
    z = hash_message(message)
    r = 0
    s = 0
    t = tuple()

    while not r or not s:
        k = random.randrange(1, curve.n)
        x, y = scalar_mult(k, curve.g)
        r = x % curve.n
        s = ((z + r * private_key) * inverse_mod(k, curve.n)) % curve.n
        t = (r, s)
    return t

def verify_signature(public_key, message, signature):
    z = hash_message(message)
    r, s = signature
    w = inverse_mod(int(str(s), 16), curve.n)
    u1 = (z * w) % curve.n
    u2 = (int(str(r), 16) * w) % curve.n
    x, y = point_add(scalar_mult(u1, curve.g), scalar_mult(u2, public_key))

    if (int(str(r), 16) % curve.n) == (x % curve.n):
        return True
    else:
        return False
