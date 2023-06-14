import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="sciezka do pliku wejsciowego")
parser.add_argument("output_file", help="sciezka do pliku wyjsciowego")
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

input_extension = os.path.splitext(input_file)[1].lower()
output_extension = os.path.splitext(output_file)[1].lower()