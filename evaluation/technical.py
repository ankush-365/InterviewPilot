from prompts.technical_prompt import TECHNICAL_PROMPT
from utils.retrieval import retrieve_by_aspect


def evaluate_technical(
    model,
    transcript
):

    technical_transcript = retrieve_by_aspect(
        transcript,
        aspect="technical_depth",
        threshold=0.5
    )

    prompt = TECHNICAL_PROMPT.format(
        transcript=technical_transcript
    )

    response = model.invoke(prompt)

    return response.content