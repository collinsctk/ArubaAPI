from basic_info import url_prefix
from get_token import get_token

# 参考文档
# https://10.1.1.11:4343/api/

role_url = f"{url_prefix}configuration/object/ap_group"
para = {"config_path": "/md"}

post_data = {'profile-name': 'ap-group-beijing',
             'virtual_ap': [{'profile-name': 'qytang-virtual-ap-api'}]}


def post_ap_group(post_data):
    headers_dict, client = get_token()
    r = client.post(role_url,
                    params=para,
                    json=post_data,
                    headers=headers_dict)
    # print(r.text)
    print(r)


if __name__ == "__main__":
    from pprint import pprint
    pprint(post_ap_group(post_data))
