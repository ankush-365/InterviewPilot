from prompts.final_report_prompt import FINAL_REPORT_PROMPT


def generate_final_feedback(
    model,
    confidence_report,
    communication_report,
    technical_report
):

    prompt = FINAL_REPORT_PROMPT.format(
        confidence_report=confidence_report,
        communication_report=communication_report,
        technical_report=technical_report
    )

    response = model.invoke(prompt)

    return response.content