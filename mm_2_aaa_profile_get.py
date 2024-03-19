from basic_info import url_prefix
from get_token import get_token

# 参考文档
# https://10.1.1.11:4343/api/

role_url = f"{url_prefix}configuration/object/aaa_prof"
para = {"config_path": "/md/qytang"}


def get_all_aaa_prof():
    headers_dict, client = get_token()
    r = client.get(role_url,
                   params=para,
                   # verify=False,
                   headers=headers_dict)
    return r.json().get('_data')


if __name__ == "__main__":
    from pprint import pprint
    pprint(get_all_aaa_prof())