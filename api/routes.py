from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
import json

router = APIRouter()

# ---------- Models for Request ----------
class AnalyzeRequest(BaseModel):
    company_name: str
    domain: str
    scope: str         # e.g., local, national, international
    category: str      # e.g., fashion, tech, food, etc.

# ---------- Test Route ----------
@router.get("/test")
def test_route():
    return {"message": "API is working!"}

# ---------- Analyze Route ----------
@router.post("/analyze")
async def analyze_company(data: AnalyzeRequest, db: Session = Depends(get_db)):
    try:
        # Dummy data (will be replaced with actual service calls later)
        found_profiles = {
            "linkedin": f"https://linkedin.com/company/{data.company_name.lower()}",
            "youtube": f"https://youtube.com/@{data.company_name.lower()}"
        }
        missing = ["instagram", "tiktok"]
        post_ideas = [
            "🎉 Launch your new collection with a behind-the-scenes reel",
            "💄 Share styling tips for teenagers"
        ]
        seo_data = {
            "title": "Top 5 Fashion Trends for Eid 2025",
            "meta": "Explore trendy styles for the upcoming season",
            "keywords": ["eid fashion", "pakistani style", "2025 trends"]
        }

        # Step 1: Insert company if not already in DB
        company = db.query(models.Company).filter(models.Company.name == data.company_name).first()
        if not company:
            company = models.Company(
                name=data.company_name,
                category=data.category,
                domain=data.domain,
                scope=data.scope
            )
            db.add(company)
            db.commit()
            db.refresh(company)

        # Step 2: Insert analysis report
        report = models.Report(
            company_id=company.id,
            found_profiles=json.dumps(found_profiles),
            missing_platforms=json.dumps(missing),
            post_ideas=json.dumps(post_ideas),
            seo_data=json.dumps(seo_data)
        )
        db.add(report)
        db.commit()

        # Step 3: Return response
        return {
            "found_profiles": found_profiles,
            "missing_platforms": missing,
            "post_ideas": post_ideas,
            "seo_suggestions": seo_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
