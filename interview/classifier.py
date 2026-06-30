from prompts.classifier_prompt import CLASSIFIER_PROMPT


def classify_question(model, question):

    prompt = CLASSIFIER_PROMPT.format(
        question=question
    )

    response = model.invoke(prompt)

    return response.content.strip().lower()