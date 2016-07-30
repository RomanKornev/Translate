# -*- coding: utf-8 -*-
import webbrowser
from textblob import TextBlob, Word
from wox import Wox, WoxAPI

LANGUAGE = 'ru'

def translate(query):
    query = query.strip().lower()
    en = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    results = []
    if query:
        from_lang, to_lang = ('en', LANGUAGE) if query[0] in en else (LANGUAGE, 'en')
        translation = TextBlob(query).translate(from_lang, to_lang)
        results.append({
            "Title": str(translation),
            "SubTitle": query,
            "IcoPath":"Images/app.png",
            "JsonRPCAction":{'method': 'openUrl',
                             'parameters': [r'http://translate.google.com/#{}/{}/{}'.format(from_lang, to_lang, query)],
                             'dontHideAfterAction': False}
        })
    if not results:
        results.append({
                "Title": 'Not found',
                "SubTitle": '',
                "IcoPath":"Images/app.png"
            })
    return results

class Translate(Wox):
    def query(self, query):
        query = query.strip().lower()
        return translate(query)

    def openUrl(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    Translate()
