from evaluation.confidence import evaluate_confidence
from evaluation.communication import evaluate_communication
from evaluation.technical import evaluate_technical
from langsmith import traceable

from evaluation.final_feedback import generate_final_feedback

@traceable(run_name="Evaluate Interview")
def evaluate_interview(
    model,
    transcript
):

    confidence_report = evaluate_confidence(
        model,
        transcript
    )

    communication_report = evaluate_communication(
        model,
        transcript
    )

    technical_report = evaluate_technical(
        model,
        transcript
    )

    final_report = generate_final_feedback(
        model,
        confidence_report,
        communication_report,
        technical_report
    )

    return {
        "confidence": confidence_report,
        "communication": communication_report,
        "technical": technical_report,
        "final_report": final_report
    }