"""
Utility functions for translation operations.
"""

import os
import time
from pathlib import Path
from typing import List, Optional

import tiktoken
from dotenv import load_dotenv


def load_env_and_key() -> Optional[str]:
    """Load environment variables and return OpenAI API key."""
    # Load variables from .env.translation (if present) and from .env.
    load_dotenv(dotenv_path=".env.translation", override=False)
    load_dotenv(override=False)
    
    return os.getenv('OPENAI_API_KEY')


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Estimate token count for text using tiktoken."""
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except:
        # Fallback approximation if tiktoken fails
        return int(len(text.split()) * 1.3)


def split_text_into_chunks(text: str, chunk_size_chars: int = 25000) -> List[str]:
    """Split text into chunks not exceeding chunk_size_chars while trying to break on newline.
    Returns a list of chunk strings in order.
    """
    if len(text) <= chunk_size_chars:
        return [text]

    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = min(start + chunk_size_chars, length)
        # Try to break at last newline before the hard limit to avoid mid-word cuts
        if end < length:
            newline_index = text.rfind('\n', start, end)
            if newline_index != -1 and newline_index > start + int(0.5 * chunk_size_chars):
                end = newline_index + 1  # include the newline char
        chunks.append(text[start:end])
        start = end
    return chunks


def discover_markdown_files(src_root: Path) -> List[Path]:
    """Recursively find all *.md files under src_root."""
    return sorted(src_root.rglob("*.md"))


def log(msg: str, *, prefix: str = "") -> None:
    """Log message with timestamp."""
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {prefix}{msg}")


def estimate_cost(tokens: int, model: str) -> float:
    """Estimate cost in USD for given token count and model."""
    # Rough pricing per 1K tokens (input + output combined estimate)
    pricing = {
        "gpt-4o": 0.0075,  # $7.50 per 1M tokens average
        "gpt-4": 0.045,    # $45 per 1M tokens average  
        "gpt-3.5-turbo": 0.002,  # $2 per 1M tokens average
        "o1": 0.045,       # Similar to GPT-4
        "o3": 0.045,       # Estimated
    }
    
    rate = pricing.get(model, 0.01)  # Default fallback
    return (tokens / 1000) * rate 