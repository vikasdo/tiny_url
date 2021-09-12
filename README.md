

## Installation:

1. Clone repository and go inside the repository folder "url-shortener-api"
```sh
git clone https://github.com/vikasdo/tiny_url.git
```

2. Create you virtualenv and install the packages
```sh
pip install -r requirements.txt
```

3. Initialize database and create the database mapping used for persistance in the url shortener API.
```sh
python manage.py makemigrations
```

4. Apply the database mapping from the app to the database; migrate the database.
```sh
python manage.py migrate
```

5. Run the application.
```sh
python manage.py runserver
```


<br>

## USAGE
#### 1. Endpoint List
URI Example: `http://localhost:8000/shorten-url/`


| | Available Methods | URI | Example URL |
| -: | :- | :- | -: |
| | | | |
| | **Project Endpoints** | | |
| 1. | `POST` | `shorten-url/` | `http://localhost:8000/shorten-url` |
| 2. | `GET`  | `/<short_id>` | `http://localhost:8000/<short_id>` |


<br>


#### 2. Tests INFO

1. Run the Url Shortener API app tests locally with:
```sh
python manage.py test
```
