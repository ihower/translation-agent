import os

with open('source.txt', 'r', encoding='utf-8') as file:
    source_text = file.read()

import translation_agent as ta
source_lang, target_lang, country = "English", "Traditional Chinese", "Taiwan"
translation = ta.translate(source_lang, target_lang, source_text, country)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(translation)