import re


class LinkDecorator:
    @staticmethod
    def replace_spaces_with_percent20(text):
        """ Меняет пробелы на %20 """
        return re.sub(r' ', '%20', text)

    @staticmethod
    def replace_spaces_and_quotes(text):
        """ Меняет пробелы на %20 и кавычки на %22 """
        return re.sub(r' ', '%20', re.sub(r'"', '%22', text))

    @staticmethod
    def replace_dots_with_spaces(text):
        """ Меняет точки между словами на пробелы """
        return re.sub(r'(?<=[a-zA-Z0-9])\.(?=[a-zA-Z0-9])', ' ', text)
