#___GAME__WORDS___#

from bs4 import BeautifulSoup
import requests

from googletrans import Translator

translator = Translator()


def get_english_words():
    url = 'https://randomword.com'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print ("произошла ошибка")

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word = translator.translate(word, dest="ru").text
        word_definition = word_dict.get("word_definition")
        word_definition = translator.translate(word_definition, dest="ru").text

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово ? ").strip().lower()
        if user == word:
            print("Всё верно!")
        else:
            print(f"Ответ неверный! Было загадано слово - {word}")

        play_again = input("{хотите сыграть еще раз? д/н : ").strip().lower()
        if play_again != "д":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    word_game()
