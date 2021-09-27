* base core api client for sas4
* cryptojs aes encrypt in python


example:

```python
# init a client
sasclient = SasAPI()

# retrieve token
token = sasclient.login(username="admin",password="admin")


# let's try to send a request to POST index/user

route = 'index/user'
data = aes.encrypt(json.dumps(
    {
        "page":1,
        "count":10,
        "sortBy":"username",
        "direction":"asc",
        "search":"",
        "columns":["idx","id","username","firstname","lastname","expiration","parent_username","name","loan_balance","traffic","remaining_days"]
    }

))
response = sasclient.post(token, route, data)

#print(response)

# which returns the following data in application/json
'''json
{'current_page': 1, 'data': [{'id': 17, 'username': 'demo1', 'firstname': 'Rick', 'lastname': 'James', 'city': None, 'phone': None, 'profile_id': 2, 'balance': '0.00', 'loan_balance': None, 'expiration': '2021-10-08 13:06:00', 'last_online': None, 'parent_id': 3, 'email': None, 'static_ip': None, 'enabled': 1, 'company': None, 'notes': None, 'simultaneous_sessions': 1, 'address': None, 'contract_id': None, 'created_at': '2021-09-08 13:05:51', 'national_id': None, 'mikrotik_ipv6_prefix': None, 'n_row': 1, 'remaining_days': 11, 'status': {'status': True, 'traffic': True, 'expiration': True, 'uptime': True}, 'online_status': 0, 'parent_username': 'Manager_2', 'profile_details': {'id': 2, 'name': 'Slow', 'type': 0}, 'daily_traffic_details': None}, {'id': 8, 'username': 'demo2', 'firstname': 'Miller', 'lastname': 'Pascal', 'city': None, 'phone': None, 'profile_id': 1, 'balance': '-100010141.00', 'loan_balance': '-141.00', 'expiration': '2022-01-22 00:45:31', 'last_online': None, 'parent_id': 3, 'email': None, 'static_ip': None, 'enabled': 1, 'company': None, 'notes': None, 'simultaneous_sessions': 1, 'address': None, 'contract_id': None, 'created_at': '2021-07-26 13:33:04', 'national_id': None, 'mikrotik_ipv6_prefix': None, 'n_row': 2, 'remaining_days': 117, 'status': {'status': True, 'traffic': True, 'expiration': True, 'uptime': True}, 'online_status': 0, 'parent_username': 'Manager_2', 'profile_details': {'id': 1, 'name': 'default-2Mbit-1Month', 'type': 0}, 'daily_traffic_details': None}, {'id': 9, 'username': 'demo3', 'firstname': 'Tyson', 'lastname': 'Edge', 'city': None, 'phone': None, 'profile_id': 3, 'balance': '0.00', 'loan_balance': '-100.00', 'expiration': '2021-09-22 12:33:24', 'last_online': None, 'parent_id': 1, 'email': None, 'static_ip': None, 'enabled': 1, 'company': None, 'notes': None, 'simultaneous_sessions': 1, 'address': None, 'contract_id': None, 'created_at': '2021-07-26 13:34:17', 'national_id': None, 'mikrotik_ipv6_prefix': None, 'n_row': 3, 'remaining_days': 0, 'status': {'status': False, 'traffic': True, 'expiration': False, 'uptime': True}, 'online_status': 0, 'parent_username': 'admin', 'profile_details': {'id': 3, 'name': 'Standard', 'type': 0}, 'daily_traffic_details': None}, {'id': 10, 'username': 'demo4', 'firstname': 'Gabriel', 'lastname': 'Andrews', 'city': None, 'phone': None, 'profile_id': 1, 'balance': '0.00', 'loan_balance': '-67.00', 'expiration': '2022-10-06 01:39:34', 'last_online': None, 'parent_id': 5, 'email': None, 'static_ip': None, 'enabled': 1, 'company': None, 'notes': None, 'simultaneous_sessions': 1, 'address': None, 'contract_id': None, 'created_at': '2021-07-26 13:36:07', 'national_id': None, 'mikrotik_ipv6_prefix': None, 'n_row': 4, 'remaining_days': 374, 'status': {'status': True, 'traffic': True, 'expiration': True, 'uptime': True}, 'online_status': 0, 'parent_username': 'Manager_4', 'profile_details': {'id': 1, 'name': 'default-2Mbit-1Month', 'type': 0}, 'daily_traffic_details': None}, {'id': 18, 'username': 'ppoe_ashis_test', 'firstname': None, 'lastname': None, 'city': None, 'phone': None, 'profile_id': 2, 'balance': '0.00', 'loan_balance': '0.00', 'expiration': '2021-09-27 10:25:54', 'last_online': None, 'parent_id': 1, 'email': None, 'static_ip': None, 'enabled': 1, 'company': None, 'notes': None, 'simultaneous_sessions': 1, 'address': None, 'contract_id': None, 'created_at': '2021-09-27 10:02:41', 'national_id': None, 'mikrotik_ipv6_prefix': None, 'n_row': 5, 'remaining_days': 0, 'status': {'status': False, 'traffic': True, 'expiration': False, 'uptime': True}, 'online_status': 0, 'parent_username': 'admin', 'profile_details': {'id': 2, 'name': 'Slow', 'type': 0}, 'daily_traffic_details': None}], 'first_page_url': 'http://demo4.sasradius.com/admin/api/index.php/api/index/user?page=1', 'from': 1, 'last_page': 1, 'last_page_url': 'http://demo4.sasradius.com/admin/api/index.php/api/index/user?page=1', 'next_page_url': None, 'path': 'http://demo4.sasradius.com/admin/api/index.php/api/index/user', 'per_page': 10, 'prev_page_url': None, 'to': 5, 'total': 5}
'''

#now a get request on GET  user/overview/17 to get the user with ID 17
route = "user/overview/17"

data = sasclient.get(token, route)



#print(data)

# which returns this data
'''json
{'data': {'username': 'demo1', 'parent_username': 'Manager_2', 'profile_name': 'Slow', 'profile_id': 2, 'expiration': '2021-10-08 13:06:00', 'status': True, 'created_at': '08 Sep 2021 - 13:05:51', 'created_by': 'admin', 'balance': 0, 'password': '1234', 'firstname': 'Rick', 'lastname': 'James', 'phone': None, 'address': None, 'city': None, 'email': None, 'remaining_rx': None, 'remaining_tx': None, 'remaining_rxtx': None, 'remaining_uptime': None, 'next_profile_change': False, 'pin_tries': 0, 'last_online': None, 'addons': []}, 'status': 200}
'''
```
