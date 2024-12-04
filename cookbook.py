import requests
main_url = "https://www.angelfire.com/oh/kewlkewlkewl/"

# for page in range(237):
#     page += 1
#     filename = ""
#     filename += (format(page, "03d"))
#     filename += ".txt"
#     unique_url = main_url
#     unique_url += (format(page, "03d"))
#     unique_url += ".txt"
#     response = requests.get(unique_url)
#     if response.status_code == 200:
#         with open(filename, "wb") as file:
#             file.write(response.content)
#         print(f"File {format(page, "03d")} successful")
#     else:
#         print(f"File {format(page, "03d")} failed")

unique_url = "https://www.angelfire.com/oh/kewlkewlkewl/218.txt"
filename = "218.txt"
response = requests.get(unique_url)
if response.status_code == 200:
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"File 218 successful")
else:
    print(f"File 218 failed")
    
