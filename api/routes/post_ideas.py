from fastapi import APIRouter
from services.post_generator import generate_post_ideas

router = APIRouter()

@router.post("/generate-post-ideas")
def post_ideas(brand_name: str, category: str, audience: str, num_ideas: int = 3):
    print(f"Received Inputs -> Brand: {brand_name}, Category: {category}, Audience: {audience}, Ideas: {num_ideas}")
    try:
        result = generate_post_ideas(brand_name, category, audience, num_ideas)
        print("Generation Result:", result)
        return {"ideas": result}
    except Exception as e:
        print("ERROR OCCURRED:", e)
        return {"error": str(e)}
