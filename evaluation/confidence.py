from prompts.confidence_prompt import CONFIDENCE_PROMPT
from utils.retrieval import retrieve_by_aspect


def evaluate_confidence(
    model,
    transcript
):

    confidence_transcript = retrieve_by_aspect(
        transcript,
        aspect="confidence",
        threshold=0.3
    )

    prompt = CONFIDENCE_PROMPT.format(
        transcript=confidence_transcript
    )

    response = model.invoke(prompt)

    return response.content