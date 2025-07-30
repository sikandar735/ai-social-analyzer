from fastapi import APIRouter
from .analyze import router as analyze_router
from .notify import router as notify_router
from .reports import router as reports_router

router = APIRouter()

router.include_router(analyze_router)
router.include_router(notify_router)
router.include_router(reports_router)
