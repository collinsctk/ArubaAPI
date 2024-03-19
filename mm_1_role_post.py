from basic_info import url_prefix
from get_token import get_token


role_url = f"{url_prefix}configuration/object/role"
para = {"config_path": "/md"}

post_data = {
  "rname": "qytang-role-api",
  "role__acl": [
    {
      "acl_type": "session",
      "pname": "allowall"
    },
    {
      "acl_type": "session",
      "pname": "logon-control"
    }
  ]
}


def post_role(post_data):
    headers_dict, client = get_token()
    r = client.post(role_url,
                    params=para,
                    verify=False,
                    json=post_data,
                    headers=headers_dict)
    return r.json()


if __name__ == "__main__":
    from pprint import pprint
    pprint(post_role(post_data))
