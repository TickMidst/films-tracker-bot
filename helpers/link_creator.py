from .link_decorator import LinkDecorator

OPENSUBS = 'https://www.opensubtitles.org'

class LinkCreator:
    def create_link_for_imdb(film_name):
        """ Создаёт ссылку для поиска по IMDB """
        mod_film_name = LinkDecorator.replace_spaces_with_percent20(film_name)
        url = f'https://www.imdb.com/find/?q={mod_film_name}&ref_=nv_sr_sm'
        result_url = f'<a href="{url}" target="_blank">IMDB</a>'
        return result_url

    def create_link_for_opensubs(film_name):
        """ Создаёт ссылку для поиска по opensubs """
        raw_search_query = f'"{film_name}" site:{OPENSUBS}'
        search_query = LinkDecorator.replace_spaces_and_quotes(raw_search_query)
        url = f'https://www.google.com/search?q={search_query}'
        result_url = f'<a href="{url}" target="_blank">opensubs</a>'
        return result_url
