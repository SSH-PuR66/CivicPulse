"""JSON API endpoints."""

from fastapi import APIRouter, HTTPException

from app.services import census

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@router.get("/states")
async def states() -> dict:
    try:
        data = await census.fetch_state_data()
    except Exception as exc:  # upstream API failure
        raise HTTPException(status_code=502, detail="Census API unavailable") from exc
    return {"count": len(data), "states": data}
