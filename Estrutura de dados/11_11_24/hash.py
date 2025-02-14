import hashlib
from random import randint

list_ = [None]*11

def simple_insert(value):
    hash_obj = hashlib.sha256(value.encode())
    hash_code = hash_obj.hexdigest()

    index = len(value) % 2
    
    while list_[index] != None:
        index = randint(0, 10)
    list_[index] = hash_code
    print(list_)

simple_insert('String teste 00')
simple_insert('String teste 01')
simple_insert('String teste 02')
simple_insert('String teste 03')
simple_insert('String teste 04')
simple_insert('String teste 05')
simple_insert('String teste 06')
simple_insert('String teste 07')
simple_insert('String teste 08')
simple_insert('String teste 09')
simple_insert('String teste 10')