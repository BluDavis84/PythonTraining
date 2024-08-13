from scrapli.driver.core import IOSXEDriver

My_device = {
    "host" : "devnetsandboxiosxe.cisco.com",
    "auth_username" : "admin",
    "auth_password" : "C1sco12345",
    "auth_strict_key" : False,
}

conn = IOSXEDriver(**My_device)
conn.open()
response = conn.send_command("show ip interface brief")
print(response)
conn.close()

# differnet way of writing the top code by using the WITH commend

# with IOSXEDriver(**My_device) as conn:
#     response = conn.send_command("show ip interface brief")
#     print(response.result)