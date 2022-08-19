from fastapi import FastAPI

app = FastAPI()

# Path Parameters
# Query Parameters
# "/tweets/{tweet_id}/details?age=30&height=184"
@app.get("/")
def home():
    message = "Hola Mundo"
    print(message)
    return {"message": message}