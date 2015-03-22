from random import randint as rdm
import aeshelper as aes
import json
import sys

asserts_passed = 0
asserts_failed = 0
asserts_total  = 0
export = []

allowed = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

def random_string(count):
    ret = ""
    while len(ret) < count:
        ret += allowed[rdm(0,len(allowed)-1)]
    return ret

def assert_crypto(assert_name, secret_key, str_to_test, verbose):
    global asserts_passed
    global asserts_failed
    global asserts_total
    asserts_total += 1
    encrypted = aes.aes_encrypt(secret_key, str_to_test)
    decrypted = aes.aes_decrypt(secret_key, encrypted)
    size_ratio = len(encrypted) / len(str_to_test)
    if decrypted == str_to_test:
        assert_pass = True
    else:
        assert_pass = False
        asserts_failed += 1

    if assert_pass:
        asserts_passed += 1
        if verbose: print '\n--------------------------------------------------'
        print assert_name + " [PASSED]"
        if verbose: print "Input string:     " + str_to_test
        if verbose: print "Secret key: " + secret_key
        if verbose: print "Encrypted string: " + encrypted
        if verbose: print "Decrypted string: " + decrypted
        if verbose: print "Size ratio: " + str(size_ratio)
        if verbose: print '--------------------------------------------------'
        export.append({
            "id": assert_name,
            "pass": assert_pass,
            "str_to_test": str_to_test,
            "encrypted": encrypted,
            "decrypted": decrypted,
            "size_ratio": size_ratio
        })

test_quantity = int(sys.argv[1])
# test_quantity = 0
# print sys.argv

while test_quantity > 0:
    test_quantity -= 1
    assert_crypto(random_string(60), random_string(rdm(10,100)), random_string(rdm(30,6000)), False)

print "Tests results: " + str(asserts_total) + " total tests. " + str(asserts_passed) + ' passed, ' + str(asserts_failed) + ' failed.'
try:
    if sys.argv[3] == "--save":
        f = open('lastUnitTestsResults.json', 'w')
        f.write(json.dumps(export))
        f.close()
        print "Successfully exported as lastUnitTestsResults.json"
except:
    pass