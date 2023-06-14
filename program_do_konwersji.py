import argparse
import json
import yaml
import xml.etree.ElementTree as ET

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