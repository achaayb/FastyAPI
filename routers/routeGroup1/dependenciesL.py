from fastapi import Header, HTTPException

async def api_key(key: str):
    """
    token verification and tracking.
    for now its hard coded
    """
    foo = "efIHv8WrFy1K4AWmtDHI"
    if key != foo:
        raise HTTPException(status_code=400, detail="Invalid api key")