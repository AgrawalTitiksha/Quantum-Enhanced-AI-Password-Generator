def binary_to_seed(binary_str):
    return int(binary_str, 2) % (2**32)

def get_charset(upper=True, lower=True, digits=True, symbols=True):
    charset = ''
    if upper:
        charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower:
        charset += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        charset += "0123456789"
    if symbols:
        charset += "!@#$%^&*()_+-=[]{};:<>?,./"
    return list(charset)
