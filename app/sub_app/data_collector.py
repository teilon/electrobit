# sudo apt-get update
# sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

from saiman_parse import start_parse


def main():
    data = start_parse()
    for e in data:
        print(e['name'])


if __name__ == '__main__':
    main()
