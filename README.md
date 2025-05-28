<p align="center">
  <img src="https://i.ytimg.com/vi/a_JdqfQz97E/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLACNXbJg8w8d2LrR1u9uKhjTLEUkQ" alt="PsyPractice AI Banner" width="60%">
</p>




# 🧠 [PsyPractice AI](https://chatgpt.com/g/g-68312b6497f8819188b2394f580b3fba-psypractice-ai) 

_PsyPractice AI is a custom-built GPT designed to support clinical psychology students and early-career practitioners in strengthening their therapeutic skills through structured, simulated learning._

> ⚠️ **Notice (May 2025):**  
> PsyPractice AI is currently in private mode while undergoing OpenAI's usage policy review.
> - ✅ Backend API: Online via [Render](https://psypractice-ai.onrender.com)
> - ⚠️ GPT Frontend: Currently private (pending OpenAI appeal)

---

## 💡 Purpose

When launched, PsyPractice AI presents the following interactive learning menu:

| Mode | Description |
|------|-------------|
| 🧑‍🏫 **Micro-skills Roleplay** | Simulated client conversations to practise core microskills (e.g., reflection, validation, summarising) with rubric-based feedback. |
| 💬 **Intervention Practice** | Select a modality (CBT, ACT, DBT, CFT, EMDR) and roleplay psychoeducation or skill delivery. |
| 🧠 **Case Formulation + Treatment Planning** | Input a client case and generate 5Ps formulation + sequenced intervention recommendations. |
| 📋 **Transcript Evaluation** | Submit a de-identified transcript for feedback on therapist skill usage and missed opportunities. |
| 📚 **Learning & Theory Support** | Ask clinical questions and get targeted, source-based responses from real manuals. |

---

## 🔍 How It Works

PsyPractice AI combines:

- **OpenAI’s GPT-4** with custom instructions and actions
- A **private hosted API on Render** that:
  - Downloads full-text therapy manuals (CBT, DBT, ACT, CFT, EMDR, DSM-5-TR, etc.)
  - Extracts and caches their contents
  - Supports real-time querying across selected manual scopes (`intervention`, `microskills`, etc.)

Manuals are not web-searched — the system references only controlled, known PDFs for reliable, grounded output.

---

## 🧱 Tech Stack

- **GPT Builder (Custom GPT)**
- **Flask + PyMuPDF backend** (hosted via [Render](https://psypractice-ai.onrender.com))
- **OpenAPI schema** for real-time search action (`/search`)
- Optional local deployment via `main.py`

---

## 📁 Repository Contents

| File/Folder | Description |
|-------------|-------------|
| `main.py` | Flask app that handles manual downloads, extraction, and search |
| `requirements.txt` | Required packages (Flask, PyMuPDF, requests) |
| `PRIVACY.md` | Public privacy policy for GPT action |
| `manuals/` | (Optional) Used for local deployment; hosted elsewhere in production |

---

## 🧩 Features

🧑‍🏫 Micro-skills Roleplay
- Practise foundational counselling skills like reflection, validation, questioning, summarising, and guiding. The GPT simulates realistic client interactions and provides structured feedback based on content from Yalom, Carl Rogers, Sommers-Flanagan, and other core clinical process texts.

💬 Intervention Practice
- Select a therapy modality (e.g., CBT, ACT, DBT, CFT) and roleplay psychoeducation, skill coaching, or behavioural techniques. You can request specific modules (e.g., behavioural activation, distress tolerance) or receive a randomised vignette to practise with.

🧠 Case Formulation + Treatment Planning
- Submit a case snapshot or client background. PsyPractice AI will generate a 5Ps formulation (Presenting, Predisposing, Precipitating, Perpetuating, Protective), recommend treatment targets, and offer sequenced intervention suggestions based on research and clinical manuals.

📋 Transcript Evaluation & Feedback
- Paste a de-identified session transcript for structured analysis. The GPT rates use of therapeutic skills (e.g., empathy, focus, alliance) and highlights missed opportunities. Feedback is informed by clinical interviewing guides and process rubrics.

📚 Learning & Intervention Support:
Ask questions like:
- “How do I explain the DBT biosocial model?”
- “What’s the ACT approach to values clarification?”

The GPT searches directly across full-text manuals (CBT, DBT, ACT, CFT, etc.) and responds with real clinical guidance — not surface-level summaries.

📡 Behind the Scenes:
All learning support is powered by a private API that searches comprehensive PDF manuals hosted on a Render server. Only verified sources are used (no hallucinated or open-web content), allowing PsyPractice AI to provide grounded, supervision-aligned responses.

---

## 🚧 Future Development

- [ ] Build an API-based version of the transcript evaluator  
- [ ] Enable report generation for supervision portfolios  
- [ ] Add interactive tools for real-time session monitoring  

---

## 📬 Contact

GitHub: [@angelbunbun](https://github.com/angelbunbun)  

---

**Note:** PsyPractice AI is an educational tool only. It is not intended for use in real-time therapy or clinical decision-making.
