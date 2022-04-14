"""
prototype version - 14.04.2022
    Language recognizer for multilingual texts using NLTK for tokenization and Fasttext for language detection
Prerequisites:
    - Python > 3.8
    - NLTK library
    - Fasttext library
    - Fasttext pre-trained model
Usage:
    use command line : "python fasttext_model_path txt_file_path json_output_path"
Parameters:
    fasttext_model_path: path to Fasttext pre-trained model
    txt_file_path: input, path to the txt file to analyze
    json_output_path: output, json document which contains the different pieces of text, their language along with the confidence index granted by Fasttext
"""
import os
import sys
import json
import fasttext
from nltk import punkt


class MultilingualDetection:
    def __init__(self, fasttext_model_path: str, txt_file_path: str, json_output_path: str, line_break: bool = True):
        self.model = fasttext.load_model(fasttext_model_path)
        self.txt_file_path = os.path.abspath(txt_file_path)
        self.json_output_path = json_output_path
        self.line_break = line_break
        self.tokenizerConfig()
        self.tokenizer = punkt.PunktSentenceTokenizer()

    def tokenizerConfig(self):
        # adding sentence ending character to correctly identify boundaries in different languages
        punkt.PunktLanguageVars.sent_end_chars = (".", "?", "!",  # Standard end of sentence characters
                                                  "。")  # Simplified Chinese and Japanese full stop
        if self.line_break is True:
            # alter Punkt tokenizer rules in order to keep the line breaks
            punkt.PunktLanguageVars._period_context_fmt = r"""
                %(SentEndChars)s             # a potential sentence ending
                \s*                          # keep new lines in Punkt tokenizer
                (?=(?P<after_tok>
                    %(NonWord)s              # either other punctuation
                    |
                    \s+(?P<next_tok>\S+)     # or whitespace and some other token
                ))"""

    def sentenceTokenization(self) -> list:
        with open(self.txt_file_path, mode="r", encoding="utf8") as txt:
            return self.tokenizer.tokenize(txt.read())

    def predictLanguageBySentence(self, sentences: list) -> tuple:
        if self.line_break is True:
            # Remove line breaks in order to correctly predict languages
            sentences = list(map(lambda x: x.strip("\r\n"), sentences))
            predictions = self.model.predict(sentences)
        else:
            predictions = self.model.predict(sentences)
        return predictions

    def getPredictionArray(self) -> list:
        sentences = self.sentenceTokenization()
        predictions = self.predictLanguageBySentence(sentences)

        prediction_array = []
        last_language = ""
        for i in range(len(sentences)):
            # merges successive sentences of the same language
            lang = predictions[0][i][0][-2:]
            confidence = predictions[1][i][0]
            sentence = sentences[i]
            if i == 0:
                dump_str = sentence
            elif lang != last_language:
                prediction_array.append({"text": dump_str, "lang": last_language, "confidence": round(float(confidence), 4)})
                dump_str = sentence
            else:
                dump_str += " " + sentence
            last_language = lang
            i += 1
        prediction_array.append({"text": dump_str, "lang": last_language, "confidence": round(float(confidence), 4)})

        return prediction_array

    def writeJsonFile(self):
        prediction_array = self.getPredictionArray()
        with open(self.json_output_path, mode="w", encoding="utf8") as jsonFile:
            json.dump(prediction_array, jsonFile, ensure_ascii=False, indent=0)


if __name__ == '__main__':
    fasttext_model_path: str = sys.argv[1]

    txt_file_path = sys.argv[2]

    json_output_path = sys.argv[3]

    predict = MultilingualDetection(fasttext_model_path,
                                    txt_file_path,
                                    json_output_path,
                                    line_break=True)

    predict.writeJsonFile()