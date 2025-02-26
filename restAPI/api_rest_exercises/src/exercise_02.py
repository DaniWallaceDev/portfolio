from psycopg.rows import dict_row
from psycopg.types.json import Json

from models import Response, MeterReadings
from utils import db_connection

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/mandate_data/{mandate_id}")
async def get_mandate_data_by_id(mandate_id : str) -> Response:
    conn = db_connection()
    cursor = conn.cursor(row_factory = dict_row)

    cursor.execute("SELECT * FROM mandate_data WHERE mandate_id = %s", (mandate_id,))
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    if data:
        return Response(status_code=200, message={"mandate_data":data})
    else:
        return Response(status_code=404, message="Not found error")

@app.delete("/mandate_data/{mandate_id}")
async def delete_mandate_data_by_id(mandate_id : str) -> Response:
    conn = db_connection()
    cursor = conn.cursor(row_factory = dict_row)

    cursor.execute("SELECT * FROM mandate_data WHERE mandate_id = %s", (mandate_id,))
    data = cursor.fetchone()
    if not data:
        return Response(status_code=404, message="Not found error")

    cursor.execute("DELETE FROM mandate_data WHERE mandate_id = %s", (mandate_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return Response(status_code=200, message={"deleted_data": data})

@app.get("/meter_readings/")
async def get_meter_readings(account_id : str, energy_type : str):
    conn = db_connection()
    cursor = conn.cursor(row_factory = dict_row)

    cursor.execute("SELECT * FROM meter_readings WHERE account_id = %s AND energy_type = %s",
                   (account_id,energy_type))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if data:
        return {"status_code" : 200,
                "message" : "Correct",
                "meter_readings_from_client" : data
                }
    else:
        return {"status_code" : 404,
                "message" : "Not Found"
                }

@app.post("/meter_readings/", response_model=Response)
async def post_meter_reading(meter_readings : MeterReadings):
    conn = db_connection()
    cursor = conn.cursor()

    meter_readings_dict = meter_readings.model_dump()
    if meter_readings_dict.get("reading_electricity") is not None:
        meter_readings_dict["reading_electricity"] = Json(meter_readings_dict["reading_electricity"])
    if meter_readings_dict.get("reading_gas") is not None:
        meter_readings_dict["reading_gas"] = Json(meter_readings_dict["reading_gas"])
    if meter_readings_dict.get("rejection") is not None:
        meter_readings_dict["rejection"] = Json(meter_readings_dict["rejection"])

    values_tuple = tuple(meter_readings_dict.values())

    cursor.execute("""
        INSERT INTO meter_readings (
        meter_number, account_id, connection_ean_code, energy_type, validation_status, 
        reading_date, reading_electricity, reading_gas, rejection, brand
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, values_tuple)

    conn.commit()
    cursor.close()
    conn.close()

    if meter_readings:
        return Response(status_code=201, message={"meter_readings": meter_readings.model_dump()})
    else:
        return Response(status_code=400, message="Not valid input data error")
# investigar type hinting db conn

if __name__ == "__main__":
    uvicorn.run(app, port=8080)