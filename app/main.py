from fastapi import FastAPI, Request, HTTPException
from typing import List, Optional, Any
from pydantic import BaseModel
import requests
from datetime import datetime
from app.models.QuorumBlockModel import *
from app.routes.block_details import *
from app.routes.dp_interaction_route import *

app = FastAPI(
    title = "concur blockchain",
    docs_url = "/api"
)

app.include_router(blockRoute)
app.include_router(dpRoute)

