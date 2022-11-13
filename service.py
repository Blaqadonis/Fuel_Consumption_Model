import bentoml
from bentoml.io import JSON
from pydantic import BaseModel


class FuelConsumptionRatings(BaseModel):
    year: int
    make: str 
    model: str 
    vehicle_class: str 
    engine_size: float 
    cylinders: int 
    transmission: str 
    fuel: str 
    fuel_consumption: float 
    unnamed_9: float 
    unnamed_10: float
    unnamed_11: int
    co2_emissions_: int

model_ref = bentoml.xgboost.get("fuel_consumption_model:latest")
dv = model_ref.custom_objects['DictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("Fuel_Consumption_Ratings_Model", runners=[model_runner])


@svc.api(input=JSON(pydantic_model=FuelConsumptionRatings), output=JSON())
async def classify(vehicle_information):
    request_data = vehicle_information.dict()
    vector = dv.transform(request_data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    result = prediction[0]
    
    return result



