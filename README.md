# Leadership Coaching Slackbot – V2  
**AI-powered Slackbot for workplace resilience and emotional intelligence coaching**  

🚀 **Project Overview:**  
Mandala’s Slackbot helps professionals develop emotional intelligence and resilience through personalized AI-powered coaching. This project builds **V2** of the Slackbot, incorporating smarter onboarding, weekly coaching content, voice input processing, Google Calendar integration, and an org-facing insights dashboard.  

---

## 🛠️ **Tech Stack**  
- **Core Framework:** Slack SDK (Python)  
- **AI & NLP:** Claude + OpenAI (chat, embeddings)  
- **Database:** Railway + PostgreSQL, Pinecone (Vector DB)  
- **Logging & Monitoring:** Langfuse (prompt tracing)  
- **Content Management:** Airtable  
- **Integrations:** Google Calendar APIs  

---

## 📂 **Project Structure**
```bash
Slackbot-V2/
│── main.py                    # Centralized script to run all components
│── slackbot.py                 # Handles Slack API interactions
│── ai_coach.py                 # AI-powered coaching responses via OpenAI/Claude
│── onboarding.py               # Personalized vs. generic onboarding logic
│── content_scheduler.py        # Weekly content drip system (Airtable-powered)
│── calendar_nudges.py          # Google Calendar integration for reminders
│── dashboard.py                # Org-facing insights for usage & sentiment tracking
│── requirements.txt            # Dependencies list for easy setup
│── README.md                   # Documentation and usage guide
```

---

## 🔥 **Key Features**
**Personalized Onboarding** – Tailors coaching based on user experience level  
**Weekly Coaching Content** – Automated drip system featuring images/GIFs  
**Slack Voice Input Processing** – Allows users to interact via voice commands  
**Google Calendar Nudges** – Sends contextual reminders based on schedules  
**Org-Facing Dashboard** – Visualizes trends in engagement, morale & sentiment  

---

## 🛠️ **Setup & Installation**
```bash
git clone https://github.com/yourusername/Slackbot-V2.git
cd Slackbot-V2
pip install -r requirements.txt
python main.py
```

---

## 📢 **Contributors**
- **Michael O.** – Slackbot Engineer & AI Developer  
