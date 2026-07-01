import requests

URL = "https://httpbin.org/get"

try:
    response = requests.get(URL, timeout=10)

    print("=" * 50)
    print(f"Status Code : {response.status_code}")
    print(f"Reason      : {response.reason}")
    print("=" * 50)

    if response.status_code == 200:
        print("\n✅ Request Successful!")
        print("\nResponse Data:")
        print(response.text)
    else:
        print("\n❌ Request Failed!")
        print("The server returned an error.")

except requests.exceptions.RequestException as error:
    print("An error occurred while connecting to the server.")
    print(error)