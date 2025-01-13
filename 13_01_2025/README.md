[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md)
[![Repo stars](https://img.shields.io/badge/Repo-home-darkgreen.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/README.md)
# Test Tasks 
To apply, complete the following tasks that demonstrate your technical skills and ability to solve real-world challenges.  

## Task 1. Develop a function to determine the score in a game
Objective In the code example below, a list of game score states throughout a match is generated.
Develop the function get_score(game_stamps, offset), which will return the score at the moment of offset in the list of game_stamps.
It is necessary to understand the essence of the written code, notice the nuances, develop a function that fits in style with the existing code, preferably with adequate algorithmic complexity.

```python
from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    # return home, away

```
### Deliverables 
[A link to the gist with the source code of the function.][0]  

## Task 2. Develop Tests for the Game Score Determination Function 
Objective  
For the get_score(game_stamps, offset) function developed in the previous task, develop unit tests using the unittest framework.  
The tests should cover all possible use cases of the function, focus on testing a single case, not be repetitive, and the test names should reflect the essence of the checks being performed.  

### Deliverables 
[A link to the gist with the source code of the tests.][1]  

## Task 3. Develop a RESTful API for Authentication 
Objective 
Develop a REST API for a user authentication and authorization system using Django and Django REST Framework. The system should support user registration, authentication, token refresh, logout, and allow users to retrieve and update their personal information.

Authentication should utilize Access and Refresh tokens.

Refresh Token – A UUID stored in the database, issued for 30 days by default.
Access Token – A JSON Web Token with a default lifespan of 30 seconds.

Clients may request an Access Token refresh at any time, for instance, upon Access Token expiry by providing a valid Refresh Token. In this case, the service returns a new valid pair of Access and Refresh Tokens, resetting their lifespans.  

### Required Endpoints Description  

#### User Registration  
```yaml
Endpoint: `/api/register/`
Method: `POST`
Body: `{"password": "password", "email": "user@example.com"}`
Response: `{"id": 1, "email": "user@example.com"}`
```
```log
curl -X POST http://localhost:8000/api/register/ -d '{"password": "password", "email": "user@example.com"}' -H "Content-Type: application/json"
```

#### Authentication (Obtaining Access and Refresh Token)  
```yaml
Endpoint: /api/login/
Method: POST
Body: {"email": "user@example.com", "password": "password"}
Response: {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsImV4cCI6MTcxMjE0NTk0NiwiaWF0IjoxNzEyMTQ1OTE2fQ.KX6LM66tC3p3bUCdkWRQkPvariP8tzUfWd8Z13akCPY", "refresh_token": "d952527b-caef-452c-8c93-1100214f82e5"}
```
```log
curl -X POST http://localhost:8000/api/login/ -d '{"email": "user@example.com", "password": "password"}' -H "Content-Type: application/json"
```

  #### Access Token Refresh  
```yaml
Endpoint: /api/refresh/
Method: POST
Body: {"refresh_token": "d952527b-caef-452c-8c93-1100214f82e5"}
Response: {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA", "refresh_token": "eb0464c2-ed6e-4346-a709-042c33946154"}
```
```log
curl -X POST http://localhost:8000/api/refresh/ -d '{"refresh_token": "eb0464c2-ed6e-4346-a709-042c33946154"}' -H "Content-Type: application/json"
```

#### Logout (Invalidating Refresh Token)  
```yaml
Endpoint: /api/logout/
Method: POST
Body: {"refresh_token": "eb0464c2-ed6e-4346-a709-042c33946154"}
Response: {"success": "User logged out."}
```
```log
curl -X POST http://localhost:8000/api/logout/ -d '{"refresh_token": "eb0464c2-ed6e-4346-a709-042c33946154"}' -H "Content-Type: application/json"
```

#### Retrieving Personal Information  
```yaml
Endpoint: /api/me/
Method: GET
Header: Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA
Response: {"id": 1, "username": "", "email": "user@example.com"}
```
```log
curl -X GET http://localhost:8000/api/me/ -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA"
```

#### Updating Personal Information  
```yaml
Endpoint: /api/me/
Method: PUT
Header: Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA
Body: {"username": "John Smith"}
Response: {"id": 1, "username": "John Smith", "email": "user@example.com"}
```
```log
curl -X PUT http://localhost:8000/api/me/ -d '{"email": "newuser@example.com"}' -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInVzZXJuYW1lIjoiZXhhbXBsZVVzZXIiLCJleHAiOjE3MTIxNDYxNDd9.zKobBlRuOiJSxCmi-iYap1bejfnvK6M3qtnkT0ssDKA"
```

### Implementation Requirements 
RESTful API must be developed with Django and Django REST Framework.
Access Token is not stored in the database; it’s verified in authentication endpoints without database calls, using the PyJWT library.
Refresh Token should be stored in the database with its expiry time and linked to a user. This allows for the token to be invalidated when necessary (e.g., when the user logs out).
Use the django-constance module for managing the lifetimes of Access and Refresh tokens.
API Documentation: Provide a browsable API with endpoint documentation.
Tests: Unit tests and integration tests for your API are recommended.
Deployment: For demonstrating the API’s functionality, you can use free hosting platforms like Heroku, which offer convenient means for deploying Django applications.  

### Deliverables 
1. [A link to the deployed API with the implemented endpoints from the task.][2]  
  
2. [A link to the Djanog’s admin webpage with Access and Refresh Tokens lifetime settings.][3]  
  
3. [A link to a GitHub repository with public access containing the source code of the solution.][4]  
 
---
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.ru.md)
[![Repo stars](https://img.shields.io/badge/Repo-home-darkgreen.svg)](https://github.com/SVBazuev/my_test_tasks/blob/main/README.md)

[0]: https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/my_get_score.py
[1]: https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/test_get_score.py
[2]: https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md
[3]: https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md
[4]: https://github.com/SVBazuev/my_test_tasks/blob/main/13_01_2025/README.md

