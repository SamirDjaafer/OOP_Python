import requests

while True:

    path = 'http://api.postcodes.io/postcodes/'
    arguments = input("Please enter your post code ")
    arguments.replace(" ", "")

    if arguments == "Thank you, I am done for today" or "exit" in arguments:
        print("Program finished")
        break

    url_target = path + arguments

    response = requests.get(url_target)

    json_response = response.json()

    print(json_response["result"].keys())

    print(f"Your longitude value is {json_response['result']['longitude']}")
    print(f"Your latitude value is {json_response['result']['latitude']}")
    print(f"Your parliamentary constituency value is {json_response['result']['parliamentary_constituency']}")
    print(f"Your NUTS value is {json_response['result']['nuts']}")









