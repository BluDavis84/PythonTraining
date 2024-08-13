# This is to show how to loop thougth networks in meraki and pick out the one you went. 

import meraki 
import os

API_key = os.environ.get("mykey")

my_network = "364643834738"

dash = meraki.DashboardAPI(api_key=API_key)

org = dash.organizations.getOrganization()

for orgs in org:
    Name = orgs["name"]
    id = orgs["id"]
    if orgs["id"] != my_network:
     print("Pick this network pleaase")
     dash.organizations.deleteOrganization(id)
    

