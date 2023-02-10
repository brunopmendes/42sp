import requests
import sys


def main():
    if len(sys.argv) != 2:
            raise Exception('Insufficient arguments')

    arg = sys.argv[1]

    params = {
            'action': 'parse',
            'prop': 'wikitext',
            'format': 'json',
            'page': arg,
            'redirects': 'true'
    }

    r = requests.get(url=f'https://en.wikipedia.org/w/api.php', params=params)
    data = r.json()
    data = data['parse']['wikitext']['*']
    
    name_arq = arg.replace(',', '_') \
                .replace('.', '_') \
                .replace(' ', '_') \
                .replace('(', '_') \
                .replace(')', '_') \
                .replace('{', '_') \
                .replace('}', '_') \
                .replace('-', '_') \
                + ".wiki"

    if data is not None and r.status_code == 200:
        with open(f'{name_arq}', 'w') as f:
            f.write(str(data.replace('==', '').replace('[[', '').replace(']]', '').replace('{{', '').replace('}}', '')))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An exception occurred: {e}")
