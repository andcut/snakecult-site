# modify_svg.py
import xml.etree.ElementTree as ET
import re
import os

# Define the target SVG files relative to the script location
svg_files = [
    "assets/svg/etsy_haul/Winged_Sun/winged-sun-currentcolor.svg",
    "assets/svg/etsy_haul/png_svg/ouroboros-currentcolor.svg",
]

# Define the target 'gold' colors to replace
# Using lowercase for case-insensitive comparison later
target_colors = {
    "#ebc17d",
    "#ddac61",
    "#c08329",
    # Add any other variations if needed
}

# --- Helper function to parse style strings ---
def parse_style(style_str):
    """Parses a CSS style string into a dictionary."""
    declarations = {}
    if not style_str:
        return declarations
    for decl in style_str.strip().split(';'):
        if ':' in decl:
            prop, val = decl.split(':', 1)
            declarations[prop.strip()] = val.strip()
    return declarations

def build_style(style_dict):
    """Builds a CSS style string from a dictionary."""
    return ";".join(f"{k}:{v}" for k, v in style_dict.items() if v) + ";"

# --- Main Processing Logic ---
def process_svg(filepath):
    print(f"Processing {filepath}...")
    try:
        # Register SVG namespace to handle default namespace correctly
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        ET.register_namespace('', namespaces['svg']) # Register default namespace

        tree = ET.parse(filepath)
        root = tree.getroot()
        modified = False

        # Iterate through all elements in the SVG
        for elem in root.findall('.//*', namespaces):
            fill_modified = False
            style_dict = {}
            original_style = elem.get('style')

            # 1. Check 'fill' attribute directly
            fill_attr = elem.get('fill')
            if fill_attr and fill_attr.lower() in target_colors:
                elem.set('fill', 'currentColor')
                # print(f"  Replaced fill attribute on {elem.tag}")
                modified = True
                fill_modified = True

            # 2. Check 'style' attribute for fill declarations
            if original_style:
                style_dict = parse_style(original_style)
                if 'fill' in style_dict and style_dict['fill'].lower() in target_colors:
                    style_dict['fill'] = 'currentColor'
                    # print(f"  Replaced fill in style on {elem.tag}")
                    modified = True
                    fill_modified = True

                # Rebuild style attribute only if necessary
                new_style = build_style(style_dict)
                if new_style != original_style: # Check if style actually changed
                     if not any(style_dict.values()): # If style becomes empty
                         if 'style' in elem.attrib:
                            del elem.attrib['style']
                            # print(f"  Removed empty style attribute on {elem.tag}")
                     else:
                         elem.set('style', new_style)
                         # print(f"  Updated style attribute on {elem.tag}")


        if modified:
            # Write changes back to the file
            tree.write(filepath, encoding='utf-8', xml_declaration=True)
            print(f"  Modified and saved {filepath}")
        else:
            print(f"  No target colors found or modified in {filepath}")

    except ET.ParseError as e:
        print(f"Error parsing {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with {filepath}: {e}")

# --- Run the script ---
if __name__ == "__main__":
    workspace_root = os.path.dirname(os.path.abspath(__file__))
    for rel_path in svg_files:
        abs_path = os.path.join(workspace_root, rel_path)
        if os.path.exists(abs_path):
            process_svg(abs_path)
        else:
            print(f"File not found: {abs_path}") 