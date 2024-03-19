from basic_info import url_prefix
from get_token import get_token

# 参考文档
# https://10.1.1.11:4343/api/

role_url = f"{url_prefix}configuration/object/write_memory"
para = {"config_path": "/md"}


def write_memory():
    headers_dict, client = get_token()
    r = client.post(role_url,
                    params=para,
                    headers=headers_dict)
    return r.json()


if __name__ == "__main__":
    from pprint import pprint
    pprint(write_memory())