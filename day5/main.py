import hashlib

DOOR_ID = "wtnhxymk"

def decode_door_id(id):
    password = []
    index = 0
    while len(password) < 8:
        test_name = id  + str(index)
        hash_val = hashlib.md5(test_name.encode('utf-8')).hexdigest()
        if str.startswith(hash_val, "00000"):
            password.append(hash_val[5:6])
        index = index + 1
    return password

def main():
    password = "".join(decode_door_id(DOOR_ID))
    print("code is: " + str(password))

if  __name__ == '__main__': main()
