import argparse

from pseudonymize import apply_hashing_to_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--inputfile',
        dest='inputfile',
        help='input file path',
        type=str,
        required=True
    )
    parser.add_argument(
        '-o',
        '--outputfile',
        dest='outputfile',
        help='output file path',
        type=str,
        required=True
    )
    parser.add_argument(
        '-s',
        '--secretfile',
        dest='secretfile',
        help='secret file path',
        type=str,
        required=True
    )
    args = parser.parse_args()
    inputfile = args.inputfile
    outputfile = args.outputfile
    secretfile = args.secretfile
    file = open(secretfile, 'r')
    salt = file.read().strip()
    apply_hashing_to_file(inputfile, outputfile, salt)
