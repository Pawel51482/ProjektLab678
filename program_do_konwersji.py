import argparse
import json
import yaml
import xml.etree.ElementTree as ET


parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="sciezka do pliku wejsciowego")
parser.add_argument("output_file", help="sciezka do pliku wyjsciowego")
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

input_extension = os.path.splitext(input_file)[1].lower()
output_extension = os.path.splitext(output_file)[1].lower()



if input_extension == ".json":
    with open(input_file, "r") as file:
        data = json.load(file)


if input_extension == ".json" and (output_extension == ".xml" or output_extension == ".yaml" or output_extension == ".yml"):
    root = ET.Element("Data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    if output_extension == ".xml":
        tree.write(output_file)
        print(f"Dane zostaly przekonwertowane do pliku {output_file}")
    elif output_extension == ".yaml" or output_extension == ".yml":
        with open(output_file, "w") as file:
            yaml.dump(data, file)
        print(f"Dane zostaly przekonwertowane do pliku {output_file}")

if input_extension == ".yaml" or input_extension == ".yml":
    with open(input_file, "r") as file:
        data = yaml.safe_load(file)


if (input_extension == ".yaml" or input_extension == ".yml") and (output_extension == ".xml" or output_extension == ".json"):
    root = ET.Element("Data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    if output_extension == ".xml":
        tree.write(output_file)
        print(f"Dane zostaly przekonwertowane do pliku {output_file}")
    elif output_extension == ".json":
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Dane zostaly przekonwertowane do pliku {output_file}")

if input_extension == ".xml":
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Błąd w składni pliku XML: {str(e)}")

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