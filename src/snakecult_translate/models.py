"""
Model selection and pricing logic for OpenAI models.
"""

from typing import Optional


def choose_model_for_tokens(token_count: int, preferred_model: str = "gpt-4o", auto_switch: bool = True) -> str:
    """Choose the best model based on token count and preferences."""
    if not auto_switch:
        return preferred_model
    
    # Switch to high-capacity models for large content
    if token_count > 24000:
        if preferred_model.startswith("gpt-4"):
            return "gpt-4o-128k"
        elif preferred_model.startswith("gpt-3.5"):
            return "gpt-3.5-turbo-16k"
    
    return preferred_model


def get_model_limits(model: str) -> dict:
    """Get context limits and other model specifications."""
    limits = {
        "gpt-4o": {"context": 32000, "batch_api": True},
        "gpt-4o-128k": {"context": 128000, "batch_api": True},
        "gpt-4": {"context": 8000, "batch_api": True},
        "gpt-3.5-turbo": {"context": 4000, "batch_api": True},
        "gpt-3.5-turbo-16k": {"context": 16000, "batch_api": True},
        "o1": {"context": 32000, "batch_api": False},
        "o3": {"context": 32000, "batch_api": False},
    }
    
    return limits.get(model, {"context": 4000, "batch_api": False})


def supports_batch_api(model: str) -> bool:
    """Check if model supports OpenAI Batch API."""
    return get_model_limits(model)["batch_api"]


def get_pricing(model: str) -> dict:
    """Get pricing information for a model (per 1K tokens)."""
    # Prices in USD per 1K tokens (approximate, as of 2024)
    pricing = {
        "gpt-4o": {"input": 0.005, "output": 0.015, "batch_discount": 0.5},
        "gpt-4o-128k": {"input": 0.01, "output": 0.03, "batch_discount": 0.5},
        "gpt-4": {"input": 0.03, "output": 0.06, "batch_discount": 0.5},
        "gpt-3.5-turbo": {"input": 0.001, "output": 0.002, "batch_discount": 0.5},
        "gpt-3.5-turbo-16k": {"input": 0.003, "output": 0.004, "batch_discount": 0.5},
        "o1": {"input": 0.015, "output": 0.06, "batch_discount": 1.0},  # No batch discount
        "o3": {"input": 0.02, "output": 0.08, "batch_discount": 1.0},   # No batch discount
    }
    
    return pricing.get(model, {"input": 0.01, "output": 0.03, "batch_discount": 1.0})


def estimate_translation_cost(input_tokens: int, model: str, use_batch: bool = False) -> float:
    """Estimate cost for translation (assumes output ~= input tokens)."""
    pricing = get_pricing(model)
    
    # Rough estimate: output tokens ≈ input tokens for translation
    input_cost = (input_tokens / 1000) * pricing["input"]
    output_cost = (input_tokens / 1000) * pricing["output"]  # Assume same length
    
    total_cost = input_cost + output_cost
    
    if use_batch and supports_batch_api(model):
        total_cost *= pricing["batch_discount"]
    
    return total_cost 