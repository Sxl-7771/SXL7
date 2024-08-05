import string

class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punc in ['.', ',', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punc, '')
                    words = content.split()
                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла {file_name}: {str(e)}")

        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            try:
                index = words.index(word.lower()) + 1
                results[name] = index
            except ValueError:
                results[name] = -1

        return results

    def count(self, word):
        counts = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            counts[name] = words.count(word.lower())

        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

