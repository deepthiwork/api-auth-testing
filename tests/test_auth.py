def test_successful_login(api_client):

    login_data = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = api_client.post("/auth/login", login_data)
    assert response.status_code == 200

    data =response.json()

    assert data["username"] == "emilys"
    assert data["accessToken"] != ""
    assert data["refreshToken"] != ""

def test_authenticated_user(api_client):
    login_data = {
        "username": "emilys",
        "password": "emilyspass"
    }

    login_response = api_client.post("/auth/login", login_data)
    assert login_response.status_code == 200

    token =login_response.json()["accessToken"]

    response = api_client.get("/auth/me", token)

    assert response.status_code == 200

    user_data = response.json()

    assert user_data["username"] == "emilys"
    assert user_data["id"] == 1

def test_login_with_invalid_password(api_client):
    login_data = {
        "username": "emilys",
        "password": "wrongpassword"
    }

    response = api_client.post("/auth/login", login_data)
    assert response.status_code == 400  

def test_login_with_invalid_username(api_client):
    login_data = {
        "username": "invaliduser",
        "password": "emilyspass"
    }

    response = api_client.post("/auth/login", login_data)
    assert response.status_code == 400

def test_access_without_token(api_client):
    response = api_client.get("/auth/me")
    assert response.status_code == 401

def test_access_with_invalid_token(api_client):
    invalid_token = "invalidtoken123"
    response = api_client.get("/auth/me", invalid_token)
    assert response.status_code == 401  
