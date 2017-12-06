from hashlib import sha256
import time

try:
    message = sys.argv[1] 
    difficulty = sys.argv[2] 
except:
    message = 'Hello, world!'
    difficulty = 3

def hash(v, n):
    return sha256(sha256('{}{}'.format(v, n).encode()).digest()).digest().hex()

start = time.time()
nonce = 0

while hash(message, nonce)[:difficulty] != ''.rjust(difficulty, '0'):
    nonce += 1
 
print('Finished after {} Seconds'.format(time.time() - start))
print('PoW Hash: {}'.format(hash(message, nonce)))
print('Nonce used: {}'.format(nonce))
