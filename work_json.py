import json
from json import JSONDecodeError


def write_active_json(file, pars_data: dict) -> None:
    """Запись в json"""
    data = read_json(file)

    with open(file, 'w', encoding='utf-8') as f:
        data.update(**pars_data)
        json.dump(data, f, indent=4)


def read_json(file: str) -> dict:
    """Чтение json"""
    with open(file, 'r') as f:
        try:
            data = json.load(f)
        except JSONDecodeError:
            data = {}
    return data
