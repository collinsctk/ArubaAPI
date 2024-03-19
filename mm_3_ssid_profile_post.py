from basic_info import url_prefix
from get_token import get_token

# 参考文档
# https://10.1.1.11:4343/api/

role_url = f"{url_prefix}configuration/object/ssid_prof"
para = {"config_path": "/md"}

post_data = {'essid': {'essid': 'qytang-ssid-psk-api'},
             'opmode': {'wpa2-psk-aes': True},
             'profile-name': 'qytang-ssid-prof-psk-api',
             'ssid_enable': {'_flags': {'default': True}, '_present': True},
             'wpa_passphrase': {'wpa-passphrase': 'Cisc0123'}}


def post_ssid_prof(post_data):
    headers_dict, client = get_token()
    r = client.post(role_url,
                   params=para,
                   json=post_data,
                   headers=headers_dict)

    return r.json()


if __name__ == "__main__":
    from pprint import pprint
    pprint(post_ssid_prof(post_data))
