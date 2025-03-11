from fastapi import APIRouter
from .exercise_02 import mandate_data_router, meter_readings_router

api_router = APIRouter()

api_router.include_router(mandate_data_router)
api_router.include_router(meter_readings_router)
