from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models import Company, Report
from db.database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter()

class AnalyzeRequest(BaseModel):
    company_name: str
    domain: str
    scope: str
    category: str

@router.post("/analyze")
def analyze_company(payload: AnalyzeRequest):
    db: Session = SessionLocal()

    # Simulated response (replace with real logic later)
    found_profiles = {
        "linkedin": f"https://linkedin.com/company/{payload.company_name}",
        "youtube": f"https://youtube.com/@{payload.company_name}"
    }

    missing = ["instagram", "tiktok"]  # placeholder
    post_ideas = [
        "🎉 Launch your new collection with a behind-the-scenes reel",
        "💄 Share styling tips for teenagers"
    ]
    seo_blog = {
        "title": "Top 5 Fashion Trends for Eid 2025",
        "meta": "Explore trendy styles for the upcoming season",
        "keywords": ["eid fashion", "pakistani style", "2025 trends"]
    }

    company = Company(
        name=payload.company_name,
        domain=payload.domain,
        scope=payload.scope,
        category=payload.category
    )
    db.add(company)
    db.commit()
    db.refresh(company)

    report = Report(
        company_id=company.id,
        found_profiles=str(found_profiles),
        missing_platforms=str(missing),
        post_ideas=str(post_ideas),
        seo_blog=str(seo_blog),
        created_at=datetime.utcnow()
    )
    db.add(report)
    db.commit()

    return {
        "found_profiles": found_profiles,
        "missing_platforms": missing,
        "post_ideas": post_ideas,
        "seo_suggestions": seo_blog
    }
