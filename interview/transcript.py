def add_interaction(
    transcript,
    question,
    answer,
    question_type,
    weights
):

    transcript.append(
        {
            "question": question,
            "answer": answer,
            "question_type": question_type,
            "weights": weights,
            "answer_length": len(answer.split())
        }
    )

    return transcript