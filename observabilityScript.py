import requests
import datetime
import string
import random
import json

def createUser() -> str:
    url = "http://localhost:8080/users"
    headers = {"Content-Type": "application/json"}
    createData = {
    "user": {
        "email": "user@example.com",
        "username": "user",
        "password": "pwd"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(createData))
    print("USER CREATION STATUS:", response.status_code)
    print(response.json())
    token = response.json()["user"]["token"]
    
    url = "http://localhost:8080/users/login"
    loginData = {
    "user":{
        "email" : "user@example.com",
        "username" : "user",
        "password" : "pwd"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(loginData))
    print("USER LOGIN STATUS:", response.status_code)
    print(response.json())
    return token
    
    

def articles(auth_token: str) -> None:
    head = {'Authorization': 'Bearer ' + auth_token}
    url = 'http://localhost:8080/articles'
    for i in range(0,2000):
        data = {
            "article" : {
                "slug" : f"slug-{i}",
                "title" : f"title {i}",
                "description" : f"description for {i}",
                "body" : "Testing Body",
                "tagList" : [i],
                "createdAt": str(datetime.date) + str(datetime.time),
                "updatedAt":str(datetime.date) + str(datetime.time),
                "favorited" : "false",
                "favortiesCount" : 0,
                "author" : {
                    "username" : "user",
                    "bio" : f"{i}'s bio",
                    "following" : "false"
                }
            }
        }
        
        comment(f"title-{i}", head)


        response = requests.post(url, json=data, headers=head)
        print(response)
        print(response.json())
        requests.get(url)
        


def comment(slug: str, head: dict) -> None:
    for j in range(30):
        letters = string.ascii_letters
        body = ''.join(random.choice(letters) for k in range(50))
        data = {
        "comment" : {
            "body" : body,
            "createdAt" : "2023-03-29T18:00:21.534Z",
            "updatedAt" : "2023-03-29T18:00:21.534Z",
            "author" : "tom"
    }
}
        url = f'http://localhost:8080/articles/{slug}/comments' 
        requests.post(url, json=data, headers = head)
        requests.get(url)
        

if __name__ == "__main__":
    token = createUser()
    articles(token)

