import argparse
if __name__ == '__main__':
    # initializing the parser
    parser = argparse.ArgumentParser(
        description="constantine script"
    )

# add the parameter positional/optional
parser.add_argument('num1', help='Number 1', type=float)
parser.add_argument('num2', help='Number 2', type=float)
parser.add_argument('operation', help='provide operator')


# parse the argument


args = parser.parse_args()
print(args)
result = None
if args.operation == '+':
    result = args.num1 + args.num2
if args.operation == '-':
    result = args.num1 - args.num2
if args.operation == '*':
    result = args.num1 * args.num2
if args.operation == 'pow':
    result = pow(args.num1, args.num2)

print(result)