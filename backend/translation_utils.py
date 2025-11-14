"""Utilities for translating question text at runtime."""

from functools import lru_cache
import logging
from typing import Optional

from deep_translator import GoogleTranslator


@lru_cache(maxsize=2048)
def translate_text(text: str, dest: str = 'ur') -> Optional[str]:
    """Translate a string to the desired language.

    Returns None if translation fails so callers can decide how to handle it.
    """
    if not text:
        return None

    try:
        translator = GoogleTranslator(source='en', target=dest)
        result = translator.translate(text)
        return result
    except Exception as exc:  # pragma: no cover - network/service errors
        logging.warning('Translation failed for "%s": %s', text, exc)
        return None
