from fastapi import APIRouter
from services.recommendation import generate_strategy_recommendations

router = APIRouter()

@router.post("/recommend-strategy")
def strategy(category: str, scope: str):
    result = generate_strategy_recommendations(category, scope)
    return {"strategy": result}
