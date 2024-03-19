from basic_info import url_prefix
from get_token import get_token
import requests


role_url = f"{url_prefix}configuration/object/role"
para = {"config_path": "/md"}


def get_all_role():
    headers_dict, client = get_token()
    r = client.get(role_url,
                   params=para,
                   verify=False,
                   headers=headers_dict)
    return r.json().get('_data')


if __name__ == "__main__":
    from pprint import pprint
    pprint(get_all_role())