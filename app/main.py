import logging
from fastapi import FastAPI, HTTPException
from app.schemas import (
    QuestionRequest, AnswerResponse, HealthResponse, VersionResponse, HomeResponse
)
from app.model.inference import QAPredictor
from app.config import MODEL_PATH, MODEL_VERSION

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="RNN QA API")

qa_model = QAPredictor(MODEL_PATH)

@app.get("/", response_model=HomeResponse)
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to the RNN QA API. Use the /predict endpoint to get answers."}

@app.get("/health", response_model=HealthResponse)
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "ok"}

@app.get("/version", response_model=VersionResponse)
def model_version():
    logger.info("Model version endpoint accessed")
    return {"model_version": MODEL_VERSION}

@app.post("/predict", response_model=AnswerResponse)
def predict_answer(payload: QuestionRequest):
    logger.info(f"Prediction requested for question: {payload.question}")
    try:
        answer = qa_model.predict(payload.question)
        return {"answer": answer}
    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error processing prediction")
#docker build --no-cache -t 1235373/rnn_qa_system_api .
