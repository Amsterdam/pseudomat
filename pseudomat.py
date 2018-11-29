import os
import sys
import csv
import hashlib
# import base64


def p14n(inputfile, outputfile, salt, hashcols=[0]):
    with open(outputfile, "w") as ofile:
        with open(inputfile, newline='') as ifile:
            reader = csv.reader(ifile, delimiter=',')
            writer = csv.writer(ofile, delimiter=',')
            for row in reader:
                hashed_row = apply_hashing(row, salt, hashcols)
                writer.writerow(hashed_row)


def apply_hashing(row, salt, hashcols):
    for c in hashcols:
        row[c] = hash(row[c], salt)
    return row


def hash(value, salt):
    salted = "{}{}".format(salt, value)
    hashed = hashlib.sha256(salted.encode())
    return hashed.hexdigest()
    # return base64.b64encode(hashed.digest()).decode()


if __name__ == '__main__':
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    salt = os.environ.get('SALT', 'Q1V3pQ50uTFzFCEyivg6FJSPa8+nSy7IC8PvGtDbvXM')
    p14n(inputfile, outputfile, salt)
