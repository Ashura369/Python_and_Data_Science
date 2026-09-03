# USING HASHING
# used primarily for storing passwords, or any file name, etc in encoded format
# text can be converted into hashcodes, but hashcodes cant be converted into texts

# -----------------------------------------------------------------------------------
# using py's builtin hasing function

# pros -- easy to use
# cons -- the hashcode changes everytime you rerun the code, and the code will also be different in different computers

print(hash('HELLO'))                    

# -----------------------------------------------------------------------------------

# using 'haslib' library, with SHA-256
# pros -- great for storing passwords, hash code is same if you rerun, will also be same in different computers


import hashlib

text = 'Hello'

def hasher(txt):
    hash = hashlib.sha256(txt.encode()).hexdigest()
    return hash

print(hasher(text))
print(hasher('Biswajeet Pradhan'))






