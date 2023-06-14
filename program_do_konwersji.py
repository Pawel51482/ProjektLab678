import argparse
import json
import yaml
import xml.etree.ElementTree as ET

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