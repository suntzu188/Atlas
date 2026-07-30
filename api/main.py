from fastapi import FastAPI

app = FastAPI(title="Atlas Core", version="0.1.0")

@app.get("/")
def health_check():
    return {"status": "Atlas Core online", "version": "0.1.0"}
