from basic_info import url_prefix
from get_token import get_token

# 参考文档
# https://10.1.1.11:4343/api/

role_url = f"{url_prefix}configuration/object/aaa_prof"
para = {"config_path": "/md"}

post_data = {'default_user_role': {'role': 'qytang-role-api'},
             'dot1x_auth_profile': {'profile-name': 'default-psk'},
             'profile-name': 'qytang-aaa-profile-api'}


def post_aaa_prof(post_data):
    headers_dict, client = get_token()
    r = client.post(role_url,
                    params=para,
                    verify=False,
                    json=post_data,
                    headers=headers_dict)
    return r.json()


if __name__ == "__main__":
    from pprint import pprint
    pprint(post_aaa_prof(post_data))