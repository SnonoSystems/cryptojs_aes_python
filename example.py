from sas import SasAPI
import json
import aes

# init a client
sasclient = SasAPI()

# retrieve token
token = sasclient.login(username="admin",password="admin")


# let's try to send a request to POST index/user

route = 'onlineReport'
data = aes.encrypt(json.dumps(
    {
        "type":"hourly",
        "day":26,
        "month":9,
        "year":2021
    }
))
response = sasclient.post(token, route, data)

#print(response)

# which returns the following data in application/json
'''json
{'status': 200, 'data': [{'hour': 12, 'n_online': 0, 'n_total': 4}]}
'''


#now a get request on GET /admin/api/index.php/api/list/profile/4 

route = "list/profile/4"

data = sasclient.get(token, route)



#print(data)

# which returns this data
'''json
{'status': 200, 'data': [{'id': 1, 'name': 'default-2Mbit-1Month'}, {'id': 4, 'name': 'Plus'}, {'id': 2, 'name': 'Slow'}, {'id': 3, 'name': 'Standard'}], '0': 200}
'''

