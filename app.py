import streamlit as st
import uuid

from utils.llm import get_llm
from resume_jd.resume_parser import parse_resume

from prompts.interviewer_prompt import INTERVIEWER_PROMPT

from interview.interview_engine import (
    process_answer,
    generate_next_question
)

from evaluation.evaluate_interview import evaluate_interview


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="InterviewPilot",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
<style>

.block-container{

    padding-top:2rem;
    padding-bottom:2rem;

}

[data-testid="stChatMessage"]{

    border-radius:15px;
    padding:10px;
    margin-bottom:8px;

}

.stButton>button{

    border-radius:10px;
    height:45px;

}

</style>
""",
unsafe_allow_html=True
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

defaults = {

    "started": False,

    "finished": False,

    "resume_text": "",

    "job_description": "",

    "current_question": "",

    "question_count": 0,

    "question_limit": 5,

    "transcript": [],

    "reports": None,

    "chat_history": []

}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 InterviewPilot")

    st.caption("AI Powered Mock Interview")

    st.divider()

    resume = st.file_uploader(

        "📄 Upload Resume",

        type=["pdf"]

    )

    jd = st.text_area(

        "📋 Job Description",

        height=220

    )

    question_limit = st.slider(

        "Questions",

        min_value=5,

        max_value=15,

        value=5

    )

    st.divider()

    st.subheader("Interview Status")

    if resume:

        st.success("Resume Uploaded")

    else:

        st.info("Resume Pending")

    if jd.strip():

        st.success("Job Description Added")

    else:

        st.info("Job Description Pending")

    if st.session_state.started:

        st.progress(

            st.session_state.question_count /

            st.session_state.question_limit

        )

        st.caption(

            f"{st.session_state.question_count} / "

            f"{st.session_state.question_limit} Questions"

        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        start = st.button(

            "▶ Start",

            use_container_width=True

        )

    with col2:

        restart = st.button(

            "↺ Reset",

            use_container_width=True

        )


# --------------------------------------------------
# Restart
# --------------------------------------------------

if restart:

    for key in defaults:

        st.session_state[key] = defaults[key]

    st.rerun()


# --------------------------------------------------
# Start Interview
# --------------------------------------------------

if start:

    if resume is None:

        st.error("Please upload your Resume.")

        st.stop()

    if jd.strip() == "":

        st.error("Please paste the Job Description.")

        st.stop()

    st.session_state.started = True

    st.session_state.finished = False

    st.session_state.question_limit = question_limit

    st.session_state.question_count = 0

    st.session_state.transcript = []

    st.session_state.chat_history = []

    st.session_state.reports = None

    st.session_state.resume_text = parse_resume(resume)

    st.session_state.job_description = jd

    st.session_state.current_question = "Tell me about yourself"

    st.session_state.chat_history.append(

        {

            "role": "assistant",

            "content": "Tell me about yourself"

        }

    )

    st.rerun()


# --------------------------------------------------
# Main Title
# --------------------------------------------------

st.title("🤖 InterviewPilot")

st.caption(

    "Practice AI-powered interviews based on your Resume and Job Description."

)

st.divider()


# --------------------------------------------------
# Welcome Screen
# --------------------------------------------------

if not st.session_state.started and not st.session_state.finished:

    st.markdown(
        """
        ## 👋 Welcome to InterviewPilot

        Prepare for AI/ML interviews tailored to **your Resume** and **Job Description**.

        ### How it works

        1. Upload your Resume
        2. Paste the Job Description
        3. Select number of questions
        4. Click **Start**

        Your AI interviewer will adapt questions based on your answers.
        """
    )



# --------------------------------------------------
# Interview Screen
# --------------------------------------------------

elif st.session_state.started:

    if start:

        st.session_state.session_id = str(uuid.uuid4())

    # Show complete conversation

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


    # User Input

    user_answer = st.chat_input(
        "Type your answer..."
    )


    if user_answer:

        # Show user message immediately

        st.session_state.chat_history.append(

            {
                "role": "user",
                "content": user_answer
            }

        )

        # Process transcript

        model = get_llm()

        st.session_state.transcript = process_answer(

            model=model,

            transcript=st.session_state.transcript,

            question=st.session_state.current_question,

            answer=user_answer

        )

        st.session_state.question_count += 1


        # Interview Finished

        if st.session_state.question_count >= st.session_state.question_limit:

            with st.spinner("Generating interview report..."):

                st.session_state.reports = evaluate_interview(

                    model,

                    st.session_state.transcript

                )

            st.session_state.started = False

            st.session_state.finished = True

            st.rerun()


        # Generate next question

        with st.spinner("Interviewer is thinking..."):

            next_question = generate_next_question(

                model=model,

                interviewer_prompt=INTERVIEWER_PROMPT,

                transcript=st.session_state.transcript,

                resume=st.session_state.resume_text,

                job_description=st.session_state.job_description

            )


        st.session_state.current_question = next_question

        st.session_state.chat_history.append(

            {

                "role": "assistant",

                "content": next_question

            }

        )

        st.rerun()


# --------------------------------------------------
# Report
# --------------------------------------------------

elif st.session_state.finished:

    report = st.session_state.reports

    st.success("🎉 Interview Completed!")

    st.title("📊 Interview Report")

    st.markdown(
        "Thank you for completing the mock interview. Below is a detailed analysis of your performance."
    )


    tabs = st.tabs([
        "📋 Overall",
        "💪 Confidence",
        "🧠 Technical",
        "🗣 Communication",
        "💬 Interview History"
    ])

    with tabs[0]:

        st.subheader("Overall Interview Summary")

        st.markdown(report["final_report"])

    with tabs[1]:

        st.subheader("Confidence Analysis")

        st.markdown(report["confidence"])

    with tabs[2]:

        st.subheader("Technical Evaluation")

        st.markdown(report["technical"])

    with tabs[3]:

        st.subheader("Communication Skills")

        st.markdown(report["communication"])

    with tabs[4]:

        st.subheader("Complete Interview")

        for qa in st.session_state.transcript:

            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(qa["question"])

            with st.chat_message("user", avatar="👤"):
                st.markdown(qa["answer"])
    

    st.divider()

    if st.button("🚀 Start New Interview", use_container_width=True):

        for key in defaults:

            st.session_state[key] = defaults[key]

        st.rerun()