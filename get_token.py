import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from basic_info import username, password, url_prefix, http_headers
import requests

# 参考文档
# https://developer.arubanetworks.com/aruba-aos/docs/login

token_url = f"{url_prefix}api/login"

client = requests.session()


def get_token():
    return_header = http_headers.copy()
    r = client.post(token_url,
                    verify=False,
                    data={'username': username, 'password': password},
                    headers=http_headers)
    try:
        request_result = r.json().get('_global_result')
        return_header.update({
            'UIDARUBA': request_result.get('UIDARUBA'),
            'X-CSRF-Token': request_result.get('X-CSRF-Token')
        })
        # 请求头部记录
        """
        GET https://mm.qytang.com:4343/v1/configuration/object/role?config_path=%2Fmd HTTP/1.1
        Host:mm.gytang.com:4343
        User-Agent: python-requests/2.31.0
        Accept-Encoding: gzip,deflate
        Accept: application/ison
        Connection: keep-alive
        Content-Type: application/ison
        UIDARUBA: MjgyYzZhZWUtYmVIMyOOMWQOLTg3YjYtZTIY
        X-CSRF-Token: MWUZN2MZNIMtNDRhNYOOMj11LTGWZGMtMDk
        Cookie: SESSION=MigyYzZhzWUtYmV7MyOOMWQOLTg3YjYtZTIy
        """
        # return_header有X-CSRF-Token
        # client有Cookie
        return return_header, client
    except Exception as e:
        return None


if __name__ == "__main__":
    print(get_token())