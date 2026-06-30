import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


QUESTION_WEIGHTS = {
        "introduction": {
            "confidence": 0.9,
            "communication": 0.8,
            "technical_depth": 0.1
        },
        "technical": {
            "confidence": 0.3,
            "communication": 0.4,
            "technical_depth": 1.0
        },
        "behavioral": {
            "confidence": 0.8,
            "communication": 0.9,
            "technical_depth": 0.2
        }
    }
