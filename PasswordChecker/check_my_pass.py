import requests
import hashlib
import sys


def request_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res


def count_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_check(password):
    hashed_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_char, tail = hashed_pass[:5], hashed_pass[5:]
    res = request_data(first_5_char)
    return count_leaks(res, tail)


def main(args):
    for password in args:
        count = pwned_check(password)
        if count:
            print(
                f'Password {password} was found {count} times. You should probably change your password')
        else:
            print(f'Password {password} was not found. Carry on.')
    return 'Done'


if (__name__ == '__main__'):
    sys.exit(main(sys.argv[1:]))
