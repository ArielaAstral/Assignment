from response_generator import result_generator
from request_generator import body_generator
from tabulate import tabulate

url1='https://reraapps.odisha.gov.in/pms/api/master/Projects/projectListing'
url2='https://reraapps.odisha.gov.in/pms/api/project/ProjectOverview/promoterDetails'

payload={"REQUEST_DATA":"eyJzZWFyY2hUZXJtIjoiIiwiZGlzdHJpY3QiOjAsInN0cnRZZWFyIjowLCJlbmRZZWFyIjowLCJwcm9qZWN0U3RhdHVzIjpbXSwiY2FycGV0QXJlYSI6IiIsInByb3BlcnR5VHlwZSI6W10sImxhdGl0dWRlIjoiIiwibG9uZ2l0dWRlIjoiIiwicmFkaXVzIjoiIiwiYXBwcm92ZWRTdGF0dXMiOmZhbHNlLCJyZXZva2VkU3RhdHVzIjpmYWxzZSwicGFnZSI6MSwicGFnZVNpemUiOjEwLCJzb3J0T3JkZXIiOiJhc2MifQ==",
         "REQUEST_TOKEN":"27a0f2c450a1ca0d6684c1b192d3025b89e9e178c23171ff74e1c96d5fee20dd"}

projects= result_generator(url1,payload)
projects=projects['result']
Project_Registered=[]
for i in range(6):
    project=projects[i]
    temp=[project['reg_no'],project['project_Name']]
    data=body_generator({'projectId':project['intid'], 'promoterId':project['promoterId']})
    res=result_generator(url2,data)
    temp+=[res['result']["promoterName"],res['result']["regdAddress"],res['result']["gstNo"]]
    Project_Registered.append(temp)

headers = ["Reg No", "Project Name", "Promoter Name", "Address", "GSTNo."]

print(tabulate(Project_Registered, headers=headers, tablefmt="grid"))