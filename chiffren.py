import math
import random
from typing import Union

# erlaubte Zeichen
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz1234567890_.,!?'
#ascii_lowercase + '1234567890_.,!?'

def ggt(a: int, b: int)-> int:
    # Return the gcd of a and b using Euclid's algorithm:
    while a != 0:
        a, b = b % a, a
    return b

def find_mod_inverse(a: int, m: int) -> Union[int, None ]:
    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m = 1
    if ggt(a, m) != 1:
        return None # No mod inverse exists if a & m aren't relatively prime.

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def get_key_pairs(key: int, symbole: str=SYMBOLS)-> tuple:
    keyA = key // len(symbole)
    keyB = key % len(symbole)
    return (keyA, keyB)

def cleanup_text(text: str, symbole: str = SYMBOLS) -> str:
    clean_text = []
    for letter in text.lower():
        if letter not in symbole:
            clean_text.append("")
        else:
            clean_text.append(letter)

    return "".join(clean_text)

def gartenzaun(text: str) -> str:
    if len(text)%2==1:
        text+=" "
    msg = [[],[]]
    for i, letter in enumerate(text):
        msg[i%2].append(letter)
    message = msg[0]+msg[1]
    return "".join(message)

def gartenzaun_decrypt(text: str) -> str:
    msg=""
    split = len(text)//2
    for i in range(split):
        msg += text[i]+text[i+split]
    return msg

def rail_fence(text: str, rows: int = 3) -> str:
    padding = len(text)%rows
    text +=padding*" "
    message=""
    msg = []
    for i in range(rows):
        msg.append([])
    row = 0
    step=1
    for i, letter in enumerate(text):
        msg[row].append(letter)
        if row==rows-1 and step ==1:
            step = -1
        elif row == 0 and step == -1:
            step = 1
        row += step
    for item in msg:
        message +="".join(item)
    return message

def ceasar(text: str,key: int=3, symbole: str=SYMBOLS)-> str:
    message =[]
    text = cleanup_text(text)
    for letter in text:
        index = symbole.index(letter)
        new_index = (index + key) % len(symbole)
        message.append(symbole[new_index])
    return "".join(message)

def rotx(text: str, key: int=3, symbole: str=SYMBOLS) -> str:
    msg=[]
    for c in cleanup_text(text):
        if c in symbole:
            msg.append(symbole[(symbole.index(c)+key)%len(symbole)])
        else:
            msg.append(c)
    return "".join(msg)

def atbash(text: str, symbole: str=SYMBOLS) -> str:
    msg=[]
    for c in cleanup_text(text):
        if c in symbole:
            msg.append(symbole[(len(symbole)-symbole.index(c))])
        else:
            msg.append(c)
    return "".join(msg)

def vigenere(text: str, key: str, symbole: str = SYMBOLS) -> str:
    key_length = len(key)
    text = cleanup_text(text)
    message = []
    for i, letter in enumerate(text.lower()):
        temp_key = symbole.index(key[i % key_length])
        message.append(ceasar(letter, temp_key))
    return "".join(message)

def transposition(text: str, dim: int) -> str:
    message = []
    padding = len(text) % dim
    text += " "*padding
    table = [text[i*dim:(i+1)*dim] for i in range(len(text)//dim)]
    #msg = [table[j][i]  for i in range(dim) for j in range(len(table))]
    for i in range(dim):
        for j in range(len(table)):
            message.append(table[j][i])
    return "".join(message)

def affine_chipher(text: str, key: tuple,symbole: str = SYMBOLS, ) -> str:
    message = []
    text = cleanup_text(text)
    key_m, key_a = key[0], key[1]
    for letter in text:
        index = symbole.index(letter)
        new_index = (index * key_m + key_a)%len(symbole)
        message.append(symbole[new_index])

    return "".join(message)

def is_prime(p: int) -> bool:
    max_iter = math.ceil(math.sqrt(p))
    if p<=1:
        return False
    for i in range(2, max_iter+1):
        if (p % i) == 0:
            return False
    return True

def generate_primes(minimal_size: int, range_length: int)-> tuple:
    prime_list = []
    for i in range(minimal_size,minimal_size + range_length):
        if is_prime(i):
            prime_list.append(i)
    p = random.choice(prime_list)
    prime_list.remove(p)
    q = random.choice(prime_list)
    return p,q

def generate_rsa_system(minimal_size: int, range_length: int) -> dict:
    rsa_system = dict()
    p,q = generate_primes(minimal_size, range_length)
    rsa_system['p'] = p
    rsa_system['q'] = q
    lambda_n = math.lcm(p-1, q-1)
    rsa_system['n'] = p*q
    while True:
        e = random.choice(range(2,lambda_n))
        if math.gcd(e,lambda_n)==1:
            d = find_mod_inverse(e,lambda_n)
            if d!=e:
                break
            else:
                continue
    rsa_system['public_key'] = min(e,d)
    rsa_system['private_key'] = max(e,d)
    return rsa_system

def message_blocks(text: str, blocklength: int, symbole :str=SYMBOLS) -> list:
    text = cleanup_text(text)
    msg_blocks = []
    for i in range(len(text)//blocklength):
        block_str = text[i*blocklength:(i+1)*blocklength]
        m=0
        for i, letter in enumerate(block_str):
            print(symbole.index(letter))
            m += symbole.index(letter)*100**i
        msg_blocks.append(m)
    return msg_blocks

def blocks_to_text(message_blocks: list, block_length: int, symbole: str= SYMBOLS):
    for block in message_blocks:
        pass

def rsa_encryption(text: str,n: int, e:int ):
    pass

def main():
    m = gartenzaun("dashatjabisjetztganzgutgeklappt")
    print(m)

if __name__ == "__main__":
    main()
