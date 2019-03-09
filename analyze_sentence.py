# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions, KeywordsOptions, EntitiesOptions

class NaturalLanguageUnderstanding():
    def __init__(self):
        #インスタンス生成
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2018-12-08',
            iam_apikey='5syXvO8kxI962t8eofpVJFp5_K5dH-3c2iqICD4z03vO',
            url='https://gateway.watsonplatform.net/natural-language-understanding/api'
        )
    def analyze_sentence(self, sentence:str):
        """
        sentence: 会話文
        return: list
        """
        result = []
        #文字列から感情分析
        response = self.natural_language_understanding.analyze(
            text=sentence,
            #text= 'I like dog, but i don\'t ,nooooooooooooooooooooooo',
            features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=50))).get_result()

        for sentiment in response["keywords"]:
            senti_dict = {
                "keyword":sentiment["text"],
                "label": sentiment["sentiment"]["label"]
            }
            result.append(senti_dict)
        return result

if __name__ == "__main__":      # このファイルが直接実行されたときに以下を実行
    analyze = NaturalLanguageUnderstanding()
    result = analyze.analyze_sentence("ムカつくムカつくムカつくムカつくイヤダイヤダいやだ")
    emotion = {"positive": 0, "negative": 0}
    for analyze_list in result:
        if analyze_list["label"] == "positive":
            emotion["positive"] += 1
        elif analyze_list["label"] == "negative":
            emotion["negative"] += 1
        else:
            print("うそだ！！！！！")
            print(analyze_list)

    print(emotion)