import argparse
import json

if input_extension == ".json":
    with open(input_file, "r") as file:
        data = json.load(file)