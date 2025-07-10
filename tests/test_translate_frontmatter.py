import sys, os, types

# Ensure project root is in path for tests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import yaml
from src.snakecult_translate.core import translate_frontmatter_block


class _FakeCompletionResponse:
    def __init__(self, content: str):
        self.message = types.SimpleNamespace(content=content)


class _FakeClient:
    """Minimal stub mimicking openai.OpenAI client for testing."""

    class _Chat:
        class _Completions:
            def create(self, *_, **__):
                # Always return deterministic YAML so test is offline
                yaml_block = (
                    "title: Título\n"
                    "description: Descripción\n"
                    "keywords:\n"
                    "- palabra\n"
                )
                return types.SimpleNamespace(choices=[_FakeCompletionResponse(yaml_block)])

        completions = _Completions()

    def __init__(self):
        self.chat = self._Chat()


def test_translate_frontmatter_block_basic():
    client = _FakeClient()
    fm = {
        "title": "Title",
        "description": "Description",
        "keywords": ["keyword"],
        "lang": "es",
    }

    translated = translate_frontmatter_block(client, fm, target_lang="es", model="gpt-3.5-turbo")

    assert translated["title"] == "Título"
    assert translated["description"] == "Descripción"
    assert translated["keywords"] == ["palabra"] 