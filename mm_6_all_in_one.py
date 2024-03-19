from mm_1_role_post import post_role
from mm_2_aaa_profile_post import post_aaa_prof
from mm_3_ssid_profile_post import post_ssid_prof
from mm_4_virtual_ap_post import post_vap_prof
from mm_5_ap_group_post import post_ap_group
from mm_10_write_memory import write_memory

# -----------------配置的基本信息-------------------
user_role_name = "qytang-role-api"
aaa_profile_name = "qytang-aaa-profile-api"
ssid_name = 'qytang-ssid-psk-api'
ssid_profile_name = 'qytang-ssid-prof-psk-api'
ssid_psk = 'Cisc0123'
virtual_ap_name = 'qytang-virtual-ap-api'
vlan = "100"
ap_group_name = 'ap-group-beijing'

# 创建user role
user_role_post_data = {
  "rname": user_role_name,
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

post_role(user_role_post_data)

# 创建aaa profile
aaa_profile_post_data = {'default_user_role': {'role': user_role_name},
                         'dot1x_auth_profile': {'profile-name': 'default-psk'},
                         'profile-name': aaa_profile_name}

post_aaa_prof(aaa_profile_post_data)

# 创建ssid profile
ssid_profile_post_data = {'essid': {'essid': ssid_name},
                          'opmode': {'wpa2-psk-aes': True},
                          'profile-name': ssid_profile_name,
                          'ssid_enable': {'_flags': {'default': True}, '_present': True},
                          'wpa_passphrase': {'wpa-passphrase': ssid_psk}}

post_ssid_prof(ssid_profile_post_data)

# 创建Virtual AP
vap_post_data = {'aaa_prof': {'profile-name': aaa_profile_name},
                 'profile-name': virtual_ap_name,
                 'ssid_prof': {'profile-name': ssid_profile_name},
                 'vlan': {'vlan': vlan}}

post_vap_prof(vap_post_data)

# Virtual AP关联AP Group
ap_group_post_data = {'profile-name': ap_group_name,
                      'virtual_ap': [{'profile-name': virtual_ap_name}]}

post_ap_group(ap_group_post_data)

# 写入配置
# write_memory()

# 实际命令如下
"""
user-role qytang-role-api
   access-list session allowall
   access-list session logon-control
!
aaa profile "qytang-aaa-profile-api"
   initial-role "qytang-role-api"
   authentication-dot1x "default-psk"
!
wlan ssid-profile "qytang-ssid-prof-psk-api"
   essid "qytang-ssid-psk-api"
   wpa-passphrase 7d322a80e61963c6bbbfe56851ed7f8bd9c4ee3678b2fb42
   opmode wpa2-psk-aes
!
wlan virtual-ap "qytang-virtual-ap-api"
   aaa-profile "qytang-aaa-profile-api"
   vlan 100
   ssid-profile "qytang-ssid-prof-psk-api"
!
ap-group "ap-group-beijing"
   virtual-ap "qytang-virtual-ap-api"

"""