import argparse
import xml.etree.ElementTree as ET

if input_extension == ".xml":
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Błąd w składni pliku XML: {str(e)}")