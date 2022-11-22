import json
import boto3
from urllib.parse import unquote_plus
def extract_text(response, extract_by="LINE"):
    line_text = []
    str1 = "\n" 
    for block in response["Blocks"]:
        if block["BlockType"] == extract_by:
            line_text.append(block["Text"])

    return str1.join(line_text)


