import argparse
import yaml

if input_extension == ".yaml" or input_extension == ".yml":
    with open(input_file, "r") as file:
        data = yaml.safe_load(file)