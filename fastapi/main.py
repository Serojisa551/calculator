from fastapi import FastAPI
import json

app = FastAPI()

with open("static/peoples.json", "r") as f:
    users_data = json.load(f)
    for users in users_data.values():
        pass

with open("static/investments.json", "r") as f:
    investments_data = json.load(f)
    for investments in investments_data.values():
        pass


@app.get("/users")
async def get_users():
    return [user.get("name") for user in users]


@app.get("/investments")
async def get_investments():
    return [investment.get("investments") for investment in investments]


@app.get("/searchuser/")
async def user_search(name: str, age: int = 16):
    there_is = False
    for user in users:
        if user.get("name") == name and user.get("age") == age:
            there_is = True
            user_id = user.get("id")
            total = {"name": user.get("name"), "age": user.get("age")}
    if not there_is:
        return ["No such is the user"]
    for investment in investments:
        if investment.get("id") == user_id:
            total["investments"] = investment.get("investments")
    return total
