from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models import Company, Report
from db.database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime
import json

from services.social_discovery import discover_social_profiles

router = APIRouter()

class AnalyzeRequest(BaseModel):
    company_name: str
    domain: str
    scope: str
    category: str

@router.post("/analyze")
def analyze_company(payload: AnalyzeRequest):
    db: Session = SessionLocal()
    try:
        # Run actual discovery logic
        discovery_data = discover_social_profiles(payload.domain)
        found_profiles = discovery_data["found"]
        missing = discovery_data["missing"]

        # Save company
        company = Company(
            name=payload.company_name,
            domain=payload.domain,
            scope=payload.scope,
            category=payload.category
        )
        db.add(company)
        db.commit()
        db.refresh(company)

        # Save report (only discovery-related fields)
        report = Report(
            company_id=company.id,
            found_profiles=json.dumps(found_profiles),
            missing_platforms=json.dumps(missing),
            post_ideas=json.dumps([]),
            seo_blog=json.dumps({}),
            created_at=datetime.utcnow()
        )
        db.add(report)
        db.commit()

        return {
            "found_profiles": found_profiles,
            "missing_platforms": missing
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    finally:
        db.close()
