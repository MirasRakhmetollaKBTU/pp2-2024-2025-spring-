import json
import tabulate

with open("sample-data.json", "r", encoding = "utf-8") as jdata:
    data = json.load(jdata)

print("Interface Status")
print("=" * 73)

imdate_list = data["imdata"]
main_list   = []
header_list = ["DN", "Description", "Speed", "MTU"]

for i in imdate_list:
    cash_list = []
    cash_list.append(i["l1PhysIf"]["attributes"]["dn"])
    cash_list.append(i["l1PhysIf"]["attributes"]["descr"])
    cash_list.append(i["l1PhysIf"]["attributes"]["speed"])
    cash_list.append(i["l1PhysIf"]["attributes"]["mtu"])
    main_list.append(cash_list)
    del cash_list

print(tabulate.tabulate(main_list, headers = header_list))
