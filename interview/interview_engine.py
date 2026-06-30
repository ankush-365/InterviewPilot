from interview.classifier import classify_question
from interview.transcript import add_interaction

from config.settings import QUESTION_WEIGHTS

def generate_next_question(
model,interviewer_prompt,transcript,resume,job_description):

    interview_history = ""

    for qa in transcript:

        interview_history += f"""
    ```

    Interviewer: {qa['question']}
    Candidate: {qa['answer']}
    """

    full_prompt = f"""
    ```

    Resume:
    {resume}

    Job Description:
    {job_description}

    Interview Transcript:
    {interview_history}

    {interviewer_prompt}
    """
    response = model.invoke(full_prompt)

    return response.content.strip()

def process_answer(
model,
transcript,
question,
answer
):

    question_type = classify_question(
        model,
        question
    )

    transcript = add_interaction(
        transcript=transcript,
        question=question,
        answer=answer,
        question_type=question_type,
        weights=QUESTION_WEIGHTS[question_type]
    )

    return transcript
