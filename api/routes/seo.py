from fastapi import APIRouter
from services.seo_generator import generate_seo_content

router = APIRouter()

@router.post("/generate-seo")
def seo(company_name: str, industry: str):
    result = generate_seo_content(company_name, industry)
    return {"seo": result}
