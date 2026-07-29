"""
Language Utility Functions
Helper functions for multi-language support across services.
"""

from typing import Dict, List, Optional
import os


def get_supported_languages() -> List[str]:
    """Get list of supported language codes."""
    from enterprise_ai_platform.common.config import settings
    langs = getattr(settings, 'SUPPORTED_LANGUAGES', 'en')
    return [l.strip() for l in langs.split(',')]


def get_default_language() -> str:
    """Get default language code."""
    from enterprise_ai_platform.common.config import settings
    return getattr(settings, 'DEFAULT_LANGUAGE', 'en')


def is_rtl_language(language_code: str) -> bool:
    """Check if a language is right-to-left."""
    from enterprise_ai_platform.common.config import settings
    rtl_langs = getattr(settings, 'LANGUAGE_DIRECTION_RTL', 'ar,he,fa,ps,ug,ur,yi')
    return language_code.lower() in [l.strip().lower() for l in rtl_langs.split(',')]


def get_language_direction(language_code: str) -> str:
    """Get text direction for a language (ltr or rtl)."""
    return 'rtl' if is_rtl_language(language_code) else 'ltr'


def normalize_language_code(lang_code: str) -> str:
    """Normalize language code to lowercase ISO 639-1 format."""
    if not lang_code:
        return get_default_language()
    return lang_code.lower().strip()


def validate_language_code(lang_code: str) -> bool:
    """Validate if a language code is supported."""
    supported = get_supported_languages()
    return normalize_language_code(lang_code) in [l.lower() for l in supported]


SUPPORTED_LANGUAGES = {
    'en': {'name': 'English', 'native_name': 'English', 'direction': 'ltr'},
    'es': {'name': 'Spanish', 'native_name': 'Español', 'direction': 'ltr'},
    'fr': {'name': 'French', 'native_name': 'Français', 'direction': 'ltr'},
    'de': {'name': 'German', 'native_name': 'Deutsch', 'direction': 'ltr'},
    'it': {'name': 'Italian', 'native_name': 'Italiano', 'direction': 'ltr'},
    'pt': {'name': 'Portuguese', 'native_name': 'Português', 'direction': 'ltr'},
    'nl': {'name': 'Dutch', 'native_name': 'Nederlands', 'direction': 'ltr'},
    'ru': {'name': 'Russian', 'native_name': 'Русский', 'direction': 'ltr'},
    'zh': {'name': 'Chinese', 'native_name': '中文', 'direction': 'ltr'},
    'ja': {'name': 'Japanese', 'native_name': '日本語', 'direction': 'ltr'},
    'ko': {'name': 'Korean', 'native_name': '한국어', 'direction': 'ltr'},
    'ar': {'name': 'Arabic', 'native_name': 'العربية', 'direction': 'rtl'},
    'he': {'name': 'Hebrew', 'native_name': 'עברית', 'direction': 'rtl'},
    'hi': {'name': 'Hindi', 'native_name': 'हिन्दी', 'direction': 'ltr'},
    'bn': {'name': 'Bengali', 'native_name': 'বাংলা', 'direction': 'ltr'},
    'ta': {'name': 'Tamil', 'native_name': 'தமிழ்', 'direction': 'ltr'},
    'te': {'name': 'Telugu', 'native_name': 'తెలుగు', 'direction': 'ltr'},
    'mr': {'name': 'Marathi', 'native_name': 'मराठी', 'direction': 'ltr'},
    'gu': {'name': 'Gujarati', 'native_name': 'ગુજરાતી', 'direction': 'ltr'},
    'kn': {'name': 'Kannada', 'native_name': 'ಕನ್ನಡ', 'direction': 'ltr'},
    'ml': {'name': 'Malayalam', 'native_name': 'മലയാളം', 'direction': 'ltr'},
    'pa': {'name': 'Punjabi', 'native_name': 'ਪੰਜਾਬੀ', 'direction': 'ltr'},
    'ur': {'name': 'Urdu', 'native_name': 'اردو', 'direction': 'rtl'},
    'id': {'name': 'Indonesian', 'native_name': 'Bahasa Indonesia', 'direction': 'ltr'},
    'ms': {'name': 'Malay', 'native_name': 'Bahasa Melayu', 'direction': 'ltr'},
    'th': {'name': 'Thai', 'native_name': 'ไทย', 'direction': 'ltr'},
    'vi': {'name': 'Vietnamese', 'native_name': 'Tiếng Việt', 'direction': 'ltr'},
    'tr': {'name': 'Turkish', 'native_name': 'Türkçe', 'direction': 'ltr'},
    'sw': {'name': 'Swahili', 'native_name': 'Kiswahili', 'direction': 'ltr'},
    'fa': {'name': 'Persian', 'native_name': 'فارسی', 'direction': 'rtl'},
    'ps': {'name': 'Pashto', 'native_name': 'پښتو', 'direction': 'rtl'},
    'ug': {'name': 'Uyghur', 'native_name': 'ئۇيغۇرچە', 'direction': 'rtl'},
    'yo': {'name': 'Yoruba', 'native_name': 'Yorùbá', 'direction': 'ltr'},
    'ig': {'name': 'Igbo', 'native_name': 'Igbo', 'direction': 'ltr'},
    'ha': {'name': 'Hausa', 'native_name': 'Hausa', 'direction': 'ltr'},
    'zu': {'name': 'Zulu', 'native_name': 'IsiZulu', 'direction': 'ltr'},
    'af': {'name': 'Afrikaans', 'native_name': 'Afrikaans', 'direction': 'ltr'},
    'xh': {'name': 'Xhosa', 'native_name': 'IsiXhosa', 'direction': 'ltr'},
    'st': {'name': 'Southern Sotho', 'native_name': 'Sesotho', 'direction': 'ltr'},
    'tn': {'name': 'Tswana', 'native_name': 'Setswana', 'direction': 'ltr'},
    'kg': {'name': 'Kongo', 'native_name': 'Kikongo', 'direction': 'ltr'},
    'sn': {'name': 'Shona', 'native_name': 'ChiShona', 'direction': 'ltr'},
    'ny': {'name': 'Chichewa', 'native_name': 'Chichewa', 'direction': 'ltr'},
    'so': {'name': 'Somali', 'native_name': 'Soomaali', 'direction': 'ltr'},
    'sq': {'name': 'Albanian', 'native_name': 'Shqip', 'direction': 'ltr'},
    'sr': {'name': 'Serbian', 'native_name': 'Српски', 'direction': 'ltr'},
    'ss': {'name': 'Swati', 'native_name': 'SiSwati', 'direction': 'ltr'},
    'sv': {'name': 'Swedish', 'native_name': 'Svenska', 'direction': 'ltr'},
    'cs': {'name': 'Czech', 'native_name': 'Čeština', 'direction': 'ltr'},
    'pl': {'name': 'Polish', 'native_name': 'Polski', 'direction': 'ltr'},
    'el': {'name': 'Greek', 'native_name': 'Ελληνικά', 'direction': 'ltr'},
}


def get_language_info(language_code: str) -> Optional[Dict]:
    """Get language information by code."""
    lang_code = normalize_language_code(language_code)
    return SUPPORTED_LANGUAGES.get(lang_code)