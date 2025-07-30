from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    domain = Column(String)
    scope = Column(String)
    category = Column(String)

    reports = relationship("Report", back_populates="company")


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    found_profiles = Column(String)
    missing_platforms = Column(String)
    post_ideas = Column(String)
    seo_blog = Column(String)  # ✅ <-- Add this line
    created_at = Column(DateTime)

    company = relationship("Company", back_populates="reports")
