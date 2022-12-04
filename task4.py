import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE, delimiter=',') -> list[dict]:
    with open(INPUT_FILE, 'r') as f:
        rows = []
        list_dict = []
        res = f.readlines()
        headers = res[0].rstrip().split(delimiter)
        for r in res[1::]:
            rows.append(r.rstrip().split(delimiter))

        for r in rows:
            new_dict = {k: i for k, i in zip(headers, r)}
            list_dict.append(new_dict)
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE, delimiter=','), indent=4))
