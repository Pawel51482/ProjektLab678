import argparse
import json
import yaml
import xml.etree.ElementTree as ET

if input_extension == ".xml" and (output_extension == ".json" or output_extension == ".yaml" or output_extension == ".yml"):
    data = {}
    for element in root:
        key = element.tag
        value = element.text
        data[key] = value
    if output_extension == ".json":
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Dane zostaly przekonwertowane do pliku {output_file}")
    elif output_extension == ".yaml" or output_extension == ".yml":
        with open(output_file, "w") as file:
            yaml.dump(data, file)
        print(f"Dane zostaly przekonwertowane do pliku {output_file}")