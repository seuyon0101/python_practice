import argparse

parser = argparse.ArgumentParser(description = "addition of two integers")

parser.add_argument(
    '-a','--a value',
    dest = 'a', help ='A integer', type = int,
    required = True
)

parser.add_argument(
    '-b','--b value',
    dest = 'b', help ='B integer', type = int,
    required = True
)
args = parser.parse_args()
print(args.a + args.b)

