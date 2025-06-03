from pathlib import Path

"""
File operations module
"""

def write_to_file(fp: str, content: str):
  file = Path(fp)
  file.write_text(content)
