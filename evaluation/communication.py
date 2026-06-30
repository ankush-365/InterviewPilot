from prompts.communication_prompt import COMMUNICATION_PROMPT
from utils.retrieval import retrieve_by_aspect


def evaluate_communication(
    model,
    transcript
):

    communication_transcript = retrieve_by_aspect(
        transcript,
        aspect="communication",
        threshold=0.4
    )

    prompt = COMMUNICATION_PROMPT.format(
        transcript=communication_transcript
    )

    response = model.invoke(prompt)

    return response.content