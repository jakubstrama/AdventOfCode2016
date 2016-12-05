import hashlib

DOOR_ID = "wtnhxymk"

def decode_door_id(id):
    password = [None]*8
    index = 0
    while None in password:
        test_name = id  + str(index)
        hash_val = hashlib.md5(test_name.encode('utf-8')).hexdigest()
        if str.startswith(hash_val, "00000"):
            pos = hash_val[5:6]
            val = hash_val[6:7]
            if not validate(pos, password):
                index = index + 1
                continue
            password[int(pos)] = val
        index = index + 1
    return password

def validate(pos, password):
    if not pos.isdigit():
        return False
    if int(pos) not in range(0, 8):
        return False
    if password[int(pos)] is not None:
        return False
    return True

def main():
    password = "".join(decode_door_id(DOOR_ID))
    print("code is: " + str(password))

if  __name__ == '__main__': main()
#437e60fc