from scrapli.driver.core import IOSXEDriver
from scrapli.driver.core import cisco_nxos

My_Dict = { "host" : "devnetsandboxiosxe.cisco.com",
            "auth_username" : "admin",
            "auth_password" : "C1sco12345",
            "auth_strict_key" : False,
           }

with IOSXEDriver(**My_Dict) as conn:
    #result = conn.send_command("show ip int br")
    newresult = conn.send_configs(["router ospf 70" , "network 10.100.20.3 0.0.0.0 area 100" ])

    print(newresult.result)
    #print(result.result)
    #print(result.textfsm_parse_output())

    