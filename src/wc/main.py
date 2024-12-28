import argparse
import sys


def print_output(msg):
    print(f"      {msg}")


def word_count():
    return lambda line: len(line.split())


def character_count():
    return lambda line: len(line)


def byte_count():
    return lambda line: len(line)


def process_input(input_stream, args):
    w_c = 0
    c_c = 0
    l_c = 0  # line count
    b_c = 0

    for line in input_stream:
        b_c += byte_count()(line)
        c_c += character_count()(line)
        l_c += 1
        w_c += word_count()(line)

    return b_c, c_c, l_c, w_c


def main():
    parser = argparse.ArgumentParser(prog="PROG", description="Word Count utility tool")

    parser.add_argument(
        "-c",
        "--count",
        action="store_true",
        required=False,
        help="count number of bytes in a file",
    )
    parser.add_argument(
        "-l",
        "--len",
        action="store_true",
        required=False,
        help="count number of lines in a file",
    )
    parser.add_argument(
        "-w",
        "--word",
        action="store_true",
        required=False,
        help="count number of words in a file",
    )
    parser.add_argument(
        "-m",
        action="store_true",
        required=False,
        help="count number of characters in a file",
    )

    parser.add_argument(
        "filename", nargs="?", type=str, help="source file to run wc utility on"
    )

    args = parser.parse_args()

    filename = args.filename

    b_c = c_c = l_c = w_c = 0
    
    if filename:
        with open(filename, "rb") as file:
            b_c, c_c, l_c, w_c = process_input(file, args)

    else: # try stdin
        b_c, c_c, l_c, w_c = process_input(sys.stdin, args)

    output = ""
    if not args.count and not args.len and not args.word and not args.m: 
        output = f" {b_c} {l_c} {w_c} {c_c}"
        
    if args.count: 
        output += f" {b_c}"
    if args.len:
        output += f" {l_c}"
    if args.word:
        output += f" {w_c}"
    if args.m: 
        output += f" {c_c}"
        
    if args.filename: 
        output += f" {args.filename}"
    
    print_output(output)
    
if __name__ == "__main__":
    main()
