Create your own virtual environment and install dependencies from requirements.txt
> python -m venv venv
> source venv/bin/activate  # or venv\Scripts\activate on Windows
> pip install -r requirements.txt


/restaurant/                                                          # display static index.html

http://127.0.0.1:8000/restaurant/booking/tables/                      # Booking API. It's best using web browser to take advantage Browserable API interface
http://127.0.0.1:8000/restaurant/booking/tables/1/

http://127.0.0.1:8000/restaurant/menu/				      # Menu API. It's best using web browser to take advantage Browserable API interface
http://127.0.0.1:8000/restaurant/menu/1

GET http://127.0.0.1:8000/auth/users/                                 # List all users. You must login as admin to see all users. Or you will only see the login user.
POST http://127.0.0.1:8000/auth/users/                                # create users. You must login as admin.
{
  "username": "testuser",
  "password": "testpass123",
  "re_password": "testpass123"
}


POST http://127.0.0.1:8000/auth/token/login/                          # obtain user token
{
  "username": "testuser",
  "password": "testpass123"
}
