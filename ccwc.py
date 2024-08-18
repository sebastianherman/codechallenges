'''
Author: Sebastian Herman
Date: 18.08.2024

Python implementation of the unix wc utility.
'''

import os
import sys


def count_metrics(data):
    if not data:
        return 0, 0, 0, 0

    raw_byte_count = len(data)
    text = data.decode('utf-8', errors='?')
    len_lines = text.count('\n')
    num_words = len(text.split())
    num_chars = len(text)
    return len_lines, num_words, num_chars, raw_byte_count


def count_metrics_from_input(input_stream):
    try:
        data = input_stream.read()
        return count_metrics(data)
    except Exception as e:
        print(f"Error: {e}")
        raise


def count_metrics_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            return count_metrics(data)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise


def handle_error(message, exit_code=1):
    print(f"Error: {message}")
    sys.exit(exit_code)


def main():

    if sys.stdin.isatty():

        if len(sys.argv) == 3:
            try:
                option = sys.argv[1]
                file_path = sys.argv[2]

                len_lines, num_words, num_chars, raw_byte_count = count_metrics_from_file(
                    file_path)

                if option == "-c":
                    print(f"{raw_byte_count} {os.path.basename(file_path)}")
                elif option == "-l":
                    print(f"{len_lines} {os.path.basename(file_path)}")
                elif option == "-w":
                    print(f"{num_words} {os.path.basename(file_path)}")
                elif option == "-m":
                    print(f"{num_chars} {os.path.basename(file_path)}")
                else:
                    handle_error("Invalid option. Use -c, -l, -w, or -m.")

            except Exception as e:
                print(f"Error: {e}")

        elif len(sys.argv) == 2:
            try:
                file_path = sys.argv[1]

                len_lines, num_words, num_chars, raw_byte_count = count_metrics_from_file(
                    file_path)

                print(
                    f"{len_lines} {num_words} {raw_byte_count} {os.path.basename(file_path)}"
                )
            except Exception as e:
                print(f"Error: {e}")

        else:
            handle_error("Usage: python ccwc.py [-c|-l|-w|-m] <file_path>")

    else:
        if len(sys.argv) == 2:
            try:
                option = sys.argv[1]

                len_lines, num_words, num_chars, raw_byte_count = count_metrics_from_input(
                    sys.stdin.buffer)

                if option == "-c":
                    print(f"{raw_byte_count}")
                elif option == "-l":
                    print(f"{len_lines}")
                elif option == "-w":
                    print(f"{num_words}")
                elif option == "-m":
                    print(f"{num_chars}")
                else:
                    handle_error("Invalid option. Use -c, -l, -w, or -m.")

            except Exception as e:
                print(f"Error: {e}")

        elif len(sys.argv) == 1:
            try:

                len_lines, num_words, num_chars, raw_byte_count = count_metrics_from_input(
                    sys.stdin.buffer)

                print(f"{len_lines} {num_words} {raw_byte_count}")
            except Exception as e:
                print(f"Error: {e}")

        else:
            handle_error("Usage: python ccwc.py [-c|-l|-w|-m] <file_path>")


if __name__ == "__main__":
    main()
