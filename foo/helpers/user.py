from hashlib import sha256

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullName": user.get("fullName", None),
        "username": user.get("fullName", None), #reconsider later.
        "registerDate": user.get("registerDate", None),
        "role": user.get("role", 0)
    }

def hash_helper(string):
    # do not insert emptystring + salt
    if string:
        salt = 'ooo'
        string += salt
    return sha256(string.encode('utf-8')).hexdigest()