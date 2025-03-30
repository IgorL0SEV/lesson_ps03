import asyncio
from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()


def get_english_words():
    url = 'https://randomword.com'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Ошибка при получении слова:", e)
        return None


async def word_game():
    print("Добро пожаловать в игру!")

    while True:
        word_dict = get_english_words()
        if not word_dict:
            break

        english_word = word_dict.get("english_word")
        translated_word = await translator.translate(english_word, dest="ru")
        translated_word = translated_word.text

        word_definition = word_dict.get("word_definition")
        translated_definition = await translator.translate(word_definition, dest="ru")
        translated_definition = translated_definition.text

        print(f"\nЗначение слова: {translated_definition}")
        user = input("Что это за слово (на русском)? ").strip().lower()

        if user == translated_word.lower():
            print("✅ Всё верно!")
        else:
            print(f"❌ Ответ неверный! Было загадано слово: {translated_word} (EN: {english_word})")

        play_again = input("Хотите сыграть ещё раз? д/н: ").strip().lower()
        if play_again != "д":
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    asyncio.run(word_game())
