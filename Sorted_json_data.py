import json
import re
from IPython.display import HTML


v_dict = json.loads(v)

# Function to recursively find and return the 'command_config' dictionary
def find_command_config(data):
    if isinstance(data, dict):
        if 'command_config' in data:
            return data['command_config']
        for value in data.values():
            result = find_command_config(value)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_command_config(item)
            if result:
                return result

            

data= find_command_config(v_dict)

def extract_numbers(key):
    """Extract all numeric parts from the key for sorting purposes."""
    return [int(num) for num in re.findall(r'\d+', key)]

def sort_dict(d):
    """Recursively sorts a dictionary by the numeric parts of its keys."""
    if not isinstance(d, dict):
        return d
    return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(d.items(), key=lambda item: extract_numbers(item[0]))}

# Sort the input data
sorted_data = sort_dict(data)

# Convert to JSON string with indentation for pretty printing
sorted_json_str = json.dumps(sorted_data, indent=2)

# Format as HTML within a <pre> tag for display
formatted_output = f"<pre style='cursor: text;' onclick='window.getSelection().selectAllChildren(this);'>{sorted_json_str}</pre>"
HTML(formatted_output)
