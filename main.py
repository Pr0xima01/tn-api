from fastapi import FastAPI

# 1. Initialize the core application
app = FastAPI(title="TroopNet API", version="1.0")

# 2. Define a route using a decorator
@app.get("/")
async def root():
    # 3. Return Python dictionary
    return {"message": "TroopNet API is online", "system_status": "Operational"}