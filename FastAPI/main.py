from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    result = {
        'data':'FastAPI'
    }
    return result


@app.get('/about')
def about():
    result = {
        'data':'ABOUT PAGE'
    }
    return result


#to start server
"""
    uvicorn main:app --reload
"""