
from fastapi import FastAPI

app = FastAPI(
    title="StockFlow API",
    description="Inventory and Order Management REST API",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
