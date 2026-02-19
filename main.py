from src.routes.index import app

if __name__ == "__main__":
    import uvicorn
    print("Starting SQL Agent API...")
    uvicorn.run(app, host="0.0.0.0", port=3000)