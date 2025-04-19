from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print("Successfully read file:")
    except UnicodeDecodeError as e:
        print("Failed reading file:", e)
        return {}

    parser.read_string(content)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return config

