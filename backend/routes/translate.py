from flask import Blueprint, request, jsonify
from translation_utils import translate_text

translate_bp = Blueprint('translate', __name__)

@translate_bp.route('/translate/texts', methods=['POST'])
def translate_texts():
    """Translate multiple texts to target language (default: Urdu)"""
    data = request.get_json(silent=True) or {}
    texts = data.get('texts') or []
    target = (data.get('target') or 'ur').lower()

    if not isinstance(texts, list):
        return jsonify({'error': 'texts must be a list of strings'}), 400

    # Translate each string
    translations = []
    for text in texts:
        if not text or not isinstance(text, str):
            translations.append(None)
            continue
        
        translated = translate_text(text, dest=target)
        translations.append(translated)

    return jsonify({
        'target': target,
        'translations': translations
    }), 200
