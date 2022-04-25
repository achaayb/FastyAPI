from fastapi import Header, HTTPException


async def verify_secret(x_token: int):
    if HARD_CODED_SECRET != 123:
        raise HTTPException(status_code=400, detail="Invalid SECRET")