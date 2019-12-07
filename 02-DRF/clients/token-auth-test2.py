import requests

def client():
    # data = {
    #     "username": "resttest",
    #     "email": "test@rest.com",
    #     "password1": "vlfdud123",
    #     "password2": "vlfdud123",
    # }
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)
    
    token_h = "Token 72185d224e817332606b5231d2a81f78a4e891e9"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)
    
if __name__ == "__main__":
    client()
    