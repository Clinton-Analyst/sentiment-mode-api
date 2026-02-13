from fastapi import FastAPI, HTTPException
from .schemas import TextInput
from .model import analyze_sentiment, calculate_mode
from .utils import clean_text

app = FastAPI(title="Sentiment Mode API")


@app.get("/")
def read_root():
    return {"message": "Sentiment API is running"}


@app.post("/analyze")
def analyze(input_data: TextInput):
    try:
        if not input_data.texts:
            raise HTTPException(status_code=400, detail="Text list cannot be empty")

        sentiments = []
        results = []

        for text in input_data.texts:
            cleaned = clean_text(text)
            result = analyze_sentiment(cleaned)
            sentiments.append(result["sentiment"])
            results.append(result)

        mode = calculate_mode(sentiments)

        return {
            "results": results,
            "mode": mode
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
