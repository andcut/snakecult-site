"""
snakecult_translate
~~~~~~~~~~~~~~~~~~~

A modular translation system for Hugo multilingual sites.
Supports single-file, parallel, and batch async translation modes.
"""

__version__ = "0.1.0"
__author__ = "Andrew Cutler"

from .core import translate_file, translate_text
from .utils import count_tokens, discover_markdown_files

__all__ = [
    "translate_file",
    "translate_text", 
    "count_tokens",
    "discover_markdown_files",
] 