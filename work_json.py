import json
import os.path


def write_active_json(file, pars_data: dict) -> None:
    """Запись в json"""
    data = read_json(file)

    with open(file, 'w', encoding='utf-8') as f:
        data.update(**pars_data)
        json.dump(data, f, indent=4)


def read_json(file: str) -> dict:
    """Чтение json"""
    data = {}
    if not os.path.exists(file):
        return data
    with open(file, 'r') as f:
        try:
            data = json.load(f)
        finally:
            return data
