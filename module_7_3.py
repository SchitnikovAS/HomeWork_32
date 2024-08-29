class WordsFinder:
    def __init__(self, *file_names) -> None:
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}
        for doc in self.file_names:
            with open(doc, encoding='utf-8') as file:
                signs = [',', '.', '=', '!', '?', ';', ':', ' - ']
                text_no_signs = (''.join([c for c in file if c not in signs]))
                is_find = 0
                while is_find >= 0:
                    is_find = text_no_signs.find('\n')
                    text_no_signs = (text_no_signs.replace('\n', ' ')).lower()
                words = text_no_signs.split(' ')
                all_words[doc] = words
        return all_words

    def find(self, word: str) -> dict:
        finded_ = {}
        for key, values in self.get_all_words().items():
            if word.lower() in values:
                finded_[key] = values.index(word.lower()) + 1
        return finded_

    def count(self, word: str) -> dict:
        counter_ = {}
        for key, values in self.get_all_words().items():
            counter_[key] = values.count(word.lower())

        return counter_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
