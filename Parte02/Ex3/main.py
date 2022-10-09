
#!/usr/bin/env python3

import argparse  # import argparse library

from my_functions import isPerfect


def main():

    # maximum_number = 2  # maximum number to test.

    parser = argparse.ArgumentParser(description='Test for PSR.')
    parser.add_argument('-p1','--parcela1', type=int, required=False, default=4)
    parser.add_argument('-p2', '--parcela2', type=int, required=False, default=5)

                       # help='The maximum number until which we check if numbers are perfect.')

    args = vars(parser.parse_args())
    maximum_number = args['maximum_number']


    args = vars (parser.parse_args())
    print(args)

    p1 = args['parcela1']
    p2 = args ['parcela2']
    total = p1 + p2

print('parcela 1 = ' + str(p1))
print('parcela 2 = ' + str(p2))

if __name__ == '__main__':
    main()
