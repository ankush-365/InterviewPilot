# 🤖 InterviewPilot

An AI-powered mock interview platform that simulates adaptive technical interviews based on a candidate's **Resume** and **Job Description**. The interviewer dynamically generates follow-up questions using Large Language Models (LLMs) and provides personalized feedback on technical depth, confidence, and communication skills.

---

## 🚀 Features

* 📄 Upload your Resume (PDF)
* 💼 Paste any Job Description
* 🤖 AI-generated interview questions tailored to your profile
* 🧠 Adaptive follow-up questions based on previous responses
* 📝 Automatic interview transcript generation
* 📊 Detailed interview evaluation including:

  * Overall Performance
  * Technical Skills
  * Communication Skills
  * Confidence Analysis
* 💬 ChatGPT-style interview interface
* 📚 Complete interview history after completion

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & LLM

* LangChain
* Groq API
* Llama 3.1 8B Instant

### Resume Processing

* PyMuPDF

### Prompt Engineering

* Custom LLM Prompts
* Adaptive Interview Flow

---

## ⚙️ How It Works

1. Upload your Resume.
2. Paste the Job Description.
3. The application extracts resume content.
4. The AI interviewer begins with an introductory question.
5. Each subsequent question is generated using:

   * Resume
   * Job Description
   * Previous Interview History
6. Every response is stored in an interview transcript.
7. After the interview, the transcript is analyzed to generate detailed performance reports.

---

## 📂 Project Structure

```
InterviewPilot/

│── app.py
│── requirements.txt
│── README.md
│
├── config/
│     settings.py
│
├── prompts/
│     interviewer_prompt.py
│     classifier_prompt.py
│     report_prompt.py
│
├── interview/
│     interview_engine.py
│     classifier.py
│     transcript.py
│
├── resume_jd/
│     document_loader.py
│     resume_parser.py
│
├── evaluation/
│     evaluate_interview.py
│
├── utils/
│     llm.py
```

---

## 🧠 AI Workflow

```
Resume
      │
      ▼
Resume Parser
      │
      ▼
Job Description
      │
      ▼
Prompt Engineering
      │
      ▼
LLM Interviewer
      │
      ▼
Adaptive Follow-up Questions
      │
      ▼
Interview Transcript
      │
      ▼
Performance Evaluation
      │
      ▼
Final Interview Report
```

## 📈 Future Improvements

* 🎤 Speech-to-Text Interview Mode
* 🔊 AI Voice Interviewer
* 🧠 LangGraph-based Interview Workflow
* 📈 Performance Tracking Across Multiple Interviews
* 🌐 Deployment with Authentication
* 📄 Downloadable PDF Interview Report

---

## 📚 Key Learnings

While building InterviewPilot, I gained practical experience with:

* Prompt Engineering
* LLM-powered Application Development
* Adaptive Question Generation
* Resume Parsing
* Streamlit Application Development
* Session State Management
* AI-based Evaluation Systems

One of the key insights from this project was recognizing the limitations of prompt-only state management for long, adaptive conversations. This motivated me to explore workflow orchestration frameworks such as LangGraph for building more reliable stateful AI systems.

---

## ⚠️ Disclaimer

InterviewPilot uses Large Language Models to simulate interviews and generate feedback. The evaluation is AI-generated and intended for interview practice and learning purposes.

---

## 👨‍💻 Author

**Ankush Ratnani**
* GitHub: https://github.com/ankush-365
