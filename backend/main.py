
from fastapi import FastAPI, UploadFile, File, HTTPException
from services.log_parser import parse_log
from services.detection_engine import detect_bruteforce

app = FastAPI(
    title="Sentinel",
    description="Security Monitoring Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "Sentinel",
        "message": "Security Monitoring System is running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze")
async def analyze_logs(file: UploadFile = File(...)):

    if not file.filename or not file.filename.lower().endswith(".log"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a .log file"
        )

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Log file must contain valid UTF-8 text"
        )

    events = []

    for line in text.splitlines():
        result = parse_log(line)

        if result:
            events.append(result)

    alerts = detect_bruteforce(events)

    return {
        "filename": file.filename,
        "total_events": len(events),
        "alerts": alerts
    }
