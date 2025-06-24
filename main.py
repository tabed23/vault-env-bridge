import traceback
from fastapi import FastAPI
from pydantic import BaseModel
import hvac
import os
import logging

vault_client = hvac.Client(url=os.getenv('VAULT_URL'), token=os.getenv('VAULT_TOKEN'))

class EnvironmentRequest(BaseModel):
    service_name: str
    environment: str


logging.basicConfig(level=logging.INFO)
app = FastAPI()


@app.post("/get_env")
async def get_env(req: EnvironmentRequest):
    secret_path = f"secret/{req.service_name}/{req.environment}"
    logging.info(f"Fetching secret from path: {secret_path}")
    
    try:
        response = vault_client.read(secret_path)        
        if response and 'data' in response:
            data = response['data']            
            return {
                "success": True,
                "service_name": req.service_name,
                "environment": req.environment,
                "path": secret_path,
                "variable_count": len(data),
                "all_variables": data 
            }
        else:
            logging.error("No data found in response")
            return {"error": "No data found in response"}
            
    except Exception as e:
        logging.error(f"Error retrieving secret: {str(e)}")
        return {"error": str(e), "traceback": traceback.format_exc()}