
Install the required dependencies:

```
python -m pip install -r requirements.txt
```

Start the server:
```
python -m uvicorn main:app --reload
```

When the application starts, navigate to `http://localhost:8000/docs`.

Deploy to heroku in `https://fast-api.herokuapp.com/docs`

NOTE: I left the file.env exposed so that you can make use of the database.
