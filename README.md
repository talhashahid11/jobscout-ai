# JobScout AI

An AI-powered recruitment intelligence platform that transforms traditional job searching into an intelligent, personalized career discovery experience.

JobScout AI analyzes candidate resumes, extracts professional insights using AI, searches real-time opportunities, ranks jobs based on profile compatibility, and provides direct application access through a modern futuristic interface.

---

# Overview

JobScout AI is designed to simplify and modernize the hiring journey for candidates by combining:

- Resume intelligence
- AI-powered profile analysis
- Smart job discovery
- Match scoring
- Career recommendation systems

The platform automatically processes uploaded resumes, identifies technical skills and experience, and matches candidates with relevant job opportunities in real time.

---

# Core Features

### AI Resume Analysis
- Extracts candidate information automatically
- Detects skills, experience, education, and job role
- Generates structured candidate profiles

### Smart Job Discovery
- Searches active job opportunities
- Filters relevant positions based on candidate skills
- Provides direct application links

### AI Match Ranking
- Scores opportunities using profile compatibility
- Highlights strongest career matches
- Identifies missing skills

### Modern User Experience
- Futuristic dark UI
- Responsive design
- Interactive animations
- Glassmorphism-inspired interface
- Smooth transitions and AI-themed visuals

---

# Tech Stack

## Frontend
- Next.js 15
- TypeScript
- Tailwind CSS
- Framer Motion
- React Dropzone
- Lucide React Icons

## Backend
- FastAPI
- Python
- Tavily Search API
- Groq AI
- PyPDF
- python-docx

---

# System Architecture

```bash
jobscout-ai/
│
├── backend/
│   ├── services/
│   │   ├── ai_extractor.py
│   │   ├── cv_parser.py
│   │   ├── scorer.py
│   │   └── search_jobs.py
│   │
│   ├── uploads/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── package.json
