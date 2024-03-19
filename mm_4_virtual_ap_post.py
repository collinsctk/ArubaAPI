from basic_info import url_prefix
from get_token import get_token

# 参考文档
# https://10.1.1.11:4343/api/

role_url = f"{url_prefix}configuration/object/virtual_ap"
para = {"config_path": "/md"}

post_data = {'aaa_prof': {'profile-name': 'qytang-aaa-profile-api'},
             'profile-name': 'qytang-virtual-ap-api',
             'ssid_prof': {'profile-name': 'qytang-ssid-prof-psk-api'},
             'vlan': {'vlan': '100'}},


def post_vap_prof(post_data):
    headers_dict, client = get_token()
    r = client.post(role_url,
                    params=para,
                    json=post_data,
                    headers=headers_dict)

    return r.json()


if __name__ == "__main__":
    from pprint import pprint
    pprint(post_vap_prof(post_data))
