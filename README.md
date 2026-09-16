# Cold Outreach Personaliser

An AI-powered cold outreach personalization tool that generates tailored outreach messages from prospect information using Google's Gemini API.

---

## 🚀 Features

- Generate personalized cold outreach messages
- Uses prospect profile information as input
- Gemini-powered AI message generation
- FastAPI backend
- React + Vite frontend
- CORS enabled for frontend/backend communication
- CSV prospect data support
- Simple project structure for local development
- API-based architecture
- Easy to extend with CRM and email integrations

---

## 🛠️ Tech Stack

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Pandas
- python-dotenv

### AI

- Google Gemini API

### Development Tools

- VS Code
- npm
- Git
- GitHub
- Python Virtual Environment

---

# 📁 Project Structure

```text
cold-outreach-personaliser/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── config/
│   ├── settings.py
│   └── services/
│       └── gemini_service.py
│
├── prompts/
│   └── outreach_prompt.txt
│
├── data/
│   └── sample_prospects.csv
│
└── frontend/
    ├── package.json
    ├── package-lock.json
    ├── vite.config.js
    ├── index.html
    ├── public/
    └── src/
        ├── App.jsx
        ├── App.css
        └── index.css
```

> Development folders such as `__pycache__`, `node_modules`, and build files should normally not be committed to GitHub.

---

# 🏗️ System Architecture

The application uses a simple:

**Frontend → Backend → AI Service → Gemini API**

architecture.

```text
                         ┌─────────────────────────┐
                         │          USER           │
                         │                         │
                         │ Prospect Profile / CSV  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │   React + Vite Frontend │
                         │                         │
                         │ • Input Form            │
                         │ • Prospect Details      │
                         │ • Generate Button       │
                         │ • Result Display        │
                         └────────────┬────────────┘
                                      │
                              HTTP / REST API
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    FastAPI Backend      │
                         │        app.py           │
                         │                         │
                         │ • Request Validation    │
                         │ • API Endpoints         │
                         │ • CORS                  │
                         │ • Response Handling     │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    Gemini Service       │
                         │ gemini_service.py       │
                         │                         │
                         │ • Build Prompt          │
                         │ • Call Gemini API       │
                         │ • Parse AI Response     │
                         └────────────┬────────────┘
                                      │
                               Gemini API Request
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │     Google Gemini       │
                         │        AI Model         │
                         │                         │
                         │ Personalized Outreach   │
                         └────────────┬────────────┘
                                      │
                              Generated Message
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    FastAPI Backend      │
                         └────────────┬────────────┘
                                      │
                               JSON Response
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │   React + Vite UI       │
                         │                         │
                         │ Personalized Message    │
                         └─────────────────────────┘
```

---

# 🧩 Architecture Components

| Component | Responsibility |
|---|---|
| React + Vite | Provides the user interface |
| FastAPI | Handles API requests |
| Pydantic | Validates request data |
| Gemini Service | Connects to Gemini API |
| Prompt Template | Defines AI generation instructions |
| Pandas | Handles CSV/prospect data |
| Environment Variables | Stores configuration and secrets |
| Git/GitHub | Source-code version control |

---

# 🔄 Request Flow

```text
1. User enters prospect information
             ↓
2. React sends HTTP request
             ↓
3. FastAPI receives the request
             ↓
4. Pydantic validates the data
             ↓
5. Backend sends data to Gemini Service
             ↓
6. Gemini Service builds the prompt
             ↓
7. Prompt + Prospect Data are sent to Gemini
             ↓
8. Gemini generates personalized outreach
             ↓
9. Backend parses the response
             ↓
10. FastAPI returns JSON response
             ↓
11. React displays the personalized message
```

---

# ⚙️ Backend Architecture

```text
app.py
  │
  ├── FastAPI Application
  │
  ├── CORS Middleware
  │
  ├── Request Models
  │
  ├── API Endpoints
  │
  └── Gemini Service
          │
          ├── Prompt Creation
          ├── Gemini API Call
          └── Response Parsing

config/
  │
  └── settings.py
          │
          └── Application Configuration

prompts/
  │
  └── outreach_prompt.txt
          │
          └── AI Instructions

data/
  │
  └── sample_prospects.csv
          │
          └── Prospect Data
```

---

# ⚛️ Frontend Architecture

```text
frontend/
│
├── src/
│   │
│   ├── App.jsx
│   │     └── Main Application UI
│   │
│   ├── App.css
│   │     └── Application Styling
│   │
│   └── index.css
│         └── Global Styling
│
├── public/
│     └── Static Assets
│
├── package.json
│     └── Dependencies and Scripts
│
└── vite.config.js
      └── Vite Configuration
```

---

# 🌐 Deployment Architecture

The frontend and backend can be deployed separately.

```text
                    INTERNET
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐
 │ Frontend Hosting│       │ Backend Hosting │
 │                 │       │                 │
 │ React + Vite    │──────▶│ FastAPI         │
 │ Production App  │ HTTPS │ Python          │
 └─────────────────┘       └────────┬────────┘
                                    │
                                    │ API
                                    ▼
                           ┌─────────────────┐
                           │ Google Gemini   │
                           │ API             │
                           └─────────────────┘
```

Production flow:

```text
User
  ↓
Frontend
  ↓
Backend API
  ↓
Gemini API
  ↓
Backend
  ↓
Frontend
  ↓
User
```

---

# 🔐 Security Architecture

```text
User
  │
  ▼
Frontend
  │
  │ HTTPS
  ▼
FastAPI
  │
  ├── Validate Input
  │
  ├── Keep API Key Server-Side
  │
  └── Call Gemini
          │
          ▼
     Gemini API
```

Important:

- Do not put the Gemini API key inside frontend code.
- Store the API key in `.env`.
- Do not commit `.env` to GitHub.
- Use `.env.example` as a template.
- Use HTTPS in production.

---

# ⚙️ Requirements

Install the following:

- Python 3.10+
- Node.js 18+
- npm
- Git
- Google Gemini API key
- VS Code

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Example `.env.example`:

```env
GEMINI_API_KEY=
```

Never publish your real API key.

---

# 🐍 Backend Setup

Open CMD or the VS Code terminal in the project root.

## Step 1: Create Virtual Environment

```cmd
python -m venv venv
```

## Step 2: Activate Virtual Environment

For Windows CMD:

```cmd
venv\Scripts\activate
```

For PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

## Step 3: Install Dependencies

```cmd
pip install -r requirements.txt
```

If dependencies are missing:

```cmd
pip install fastapi uvicorn python-multipart pydantic pandas python-dotenv google-genai
```

## Step 4: Run Backend

```cmd
uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

Open another terminal.

Go to the frontend folder:

```cmd
cd frontend
```

Install dependencies:

```cmd
npm install
```

Run frontend:

```cmd
npm run dev
```

Vite will show the frontend URL.

Usually:

```text
http://localhost:5173
```

Open the URL in your browser.

---

# 👤 Prospect Profile

The prospect profile should contain useful information about the person or company.

Example:

```text
Name: Rahul Kumar
Job Title: Head of Marketing
Company: ABC Technologies
Industry: SaaS
Company Description: B2B SaaS company helping businesses automate sales.
Recent Activity: Recently expanded the marketing team.
Pain Point: Improving qualified lead generation.
```

The more relevant information provided, the more contextual the generated outreach can be.

---

# ✍️ Example Input

```text
Name: Priya Sharma
Role: Founder
Company: GrowthTech
Industry: Technology
Recent Activity: Launched a new B2B product
Pain Point: Increasing qualified leads
```

---

# 📤 Example Output

```text
Subject: Quick idea for GrowthTech's new product

Hi Priya,

I noticed GrowthTech recently launched its new B2B product.

As the company expands, generating a consistent flow of
qualified leads can become an important growth opportunity.

We help teams improve outbound personalization and turn
relevant prospects into qualified conversations.

Would you be open to a quick conversation next week?

Best,
[Your Name]
```

The actual output depends on the prompt and Gemini response.

---

# 📄 CSV Support

Prospect information can also be stored in CSV format.

Example:

```csv
name,title,company,industry,recent_activity,pain_point
Rahul Kumar,Head of Marketing,ABC Technologies,SaaS,Expanded marketing team,Lead generation
Priya Sharma,Founder,GrowthTech,Technology,Launched new product,Qualified leads
```

Store the CSV file inside:

```text
data/
```

Example:

```text
data/sample_prospects.csv
```

---

# 🧠 Prompt Architecture

The AI prompt is stored separately from the Python application.

```text
prompts/outreach_prompt.txt
```

This makes the application easier to maintain.

The prompt can control:

- Personalization
- Tone
- Message length
- Prospect context
- Value proposition
- Call to action
- Avoiding generic language
- Avoiding unsupported claims

---

# 🔧 Configuration

Main configuration:

```text
config/settings.py
```

Gemini integration:

```text
config/services/gemini_service.py
```

The Gemini service is responsible for:

```text
Prospect Data
     ↓
Prompt
     ↓
Gemini API
     ↓
Generated Outreach
```

---

# 🧪 Testing

Run the backend:

```cmd
uvicorn app:app --reload
```

Run the frontend:

```cmd
cd frontend
npm run dev
```

Then:

1. Open the frontend.
2. Enter prospect information.
3. Click the generate button.
4. Wait for the Gemini response.
5. Check the generated outreach.

---

# 🐛 Common Errors

## 1. ModuleNotFoundError

Activate the virtual environment:

```cmd
venv\Scripts\activate
```

Then install dependencies:

```cmd
pip install -r requirements.txt
```

---

## 2. Gemini API Error

Check your `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Restart the backend:

```cmd
uvicorn app:app --reload
```

---

## 3. Network Error

Make sure the backend is running:

```cmd
uvicorn app:app --reload
```

Then check:

```text
http://127.0.0.1:8000
```

Also check:

- Browser Console
- Browser Network tab
- FastAPI terminal
- CORS configuration
- Frontend API URL
- Gemini API key

---

## 4. `npm` Not Recognized

Check Node.js:

```cmd
node --version
```

Check npm:

```cmd
npm --version
```

If these commands fail, install Node.js and reopen VS Code.

---

## 5. Port Already in Use

Run FastAPI on another port:

```cmd
uvicorn app:app --reload --port 8001
```

Then update the frontend API URL to:

```text
http://127.0.0.1:8001
```

---

# 🔗 Frontend and Backend Connection

Development setup:

```text
Frontend
http://localhost:5173

       │
       │ HTTP Request
       ▼

Backend
http://127.0.0.1:8000

       │
       │ Gemini API
       ▼

Google Gemini
```

The frontend should call the backend API instead of calling Gemini directly.

This keeps the Gemini API key on the backend.

---

# 📦 Useful CMD Commands

## Start Backend

```cmd
uvicorn app:app --reload
```

## Start Frontend

```cmd
cd frontend && npm run dev
```

## Install Frontend Packages

```cmd
cd frontend && npm install
```

## Install Python Packages

```cmd
pip install -r requirements.txt
```

## Check Python

```cmd
python --version
```

## Check Node

```cmd
node --version
```

## Check npm

```cmd
npm --version
```

---

# 🌿 Git and GitHub

Initialize Git:

```cmd
git init
```

Check status:

```cmd
git status
```

Add all files:

```cmd
git add .
```

Commit:

```cmd
git commit -m "Initial cold outreach personaliser"
```

Set branch:

```cmd
git branch -M main
```

Add GitHub repository:

```cmd
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push:

```cmd
git push -u origin main
```

For future updates:

```cmd
git add .
git commit -m "Update outreach personaliser"
git push
```

---

# 🚫 Git Ignore

Your `.gitignore` should contain:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
node_modules/
dist/
.vscode/
```

This prevents unnecessary and sensitive files from being pushed.

---

# 🏭 Production Deployment

The project contains two applications:

```text
Frontend → React + Vite
Backend  → FastAPI + Python
```

Production deployment should configure:

- Frontend hosting
- Backend hosting
- Production API URL
- Environment variables
- Gemini API key
- CORS
- HTTPS

Build frontend:

```cmd
cd frontend
npm run build
```

Production output:

```text
frontend/dist/
```

Do not use:

```text
http://localhost:5173
```

as the production frontend API configuration.

Use the deployed backend URL instead.

---

# 🚀 Deployment Flow

```text
Local Development

React
  ↓
FastAPI
  ↓
Gemini API
```

Production:

```text
User
  ↓
Frontend Hosting
  ↓
Backend Hosting
  ↓
Google Gemini API
```

---

# 🔮 Future Improvements

Possible improvements include:

- LinkedIn profile enrichment
- Company website research
- CRM integration
- Gmail integration
- Email sending
- Automated follow-ups
- Prospect database
- Outreach history
- Message scoring
- A/B testing
- Analytics dashboard
- Authentication
- Rate limiting
- Background jobs
- Docker support
- Production monitoring

---

# 🎯 Project Goal

The goal of the Cold Outreach Personaliser is to reduce the time required to create personalized prospecting messages.

Instead of sending one generic message to every prospect, the application takes prospect-specific information and generates a message that reflects that context.

---

# 💡 Example Use Case

```text
Salesperson
     ↓
Enters Prospect Details
     ↓
Cold Outreach Personaliser
     ↓
Gemini analyzes the prospect context
     ↓
Personalized Outreach Message
     ↓
Salesperson reviews message
     ↓
Message can be used for outreach
```

---

# 📊 High-Level Architecture Summary

```text
┌───────────────────────────────────────────────────────┐
│                       USER                            │
└──────────────────────────┬────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────┐
│                REACT + VITE FRONTEND                 │
│                                                       │
│  Prospect Form → Generate → Display Result           │
└──────────────────────────┬────────────────────────────┘
                           │
                         REST API
                           │
                           ▼
┌───────────────────────────────────────────────────────┐
│                     FASTAPI                          │
│                                                       │
│  Request Validation → API Endpoint → Response        │
└──────────────────────────┬────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────┐
│                GEMINI SERVICE                        │
│                                                       │
│  Prompt + Prospect Data → Gemini API                 │
└──────────────────────────┬────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────┐
│                  GOOGLE GEMINI                       │
│                                                       │
│           AI Generated Outreach                      │
└──────────────────────────┬────────────────────────────┘
                           │
                           ▼
                    Personalized Message
                           │
                           ▼
                     React Frontend
                           │
                           ▼
                          USER
```

---

# 👩‍💻 Development

Built with:

**React + Vite + FastAPI + Python + Google Gemini API**

---

# 📌 Status

```text
Frontend      ✅
Backend       ✅
Gemini AI     ✅
CSV Support   ✅
API           ✅
GitHub        ✅
Architecture  ✅
```

---

# 📜 License

Add your preferred license before publishing the project publicly.

Example:

```text
MIT License
```

---

# ⭐ Project Summary

**Cold Outreach Personaliser** is an AI-powered application that combines:

```text
React
   +
FastAPI
   +
Gemini API
   +
Prospect Data
   =
Personalized Cold Outreach
```

The architecture is designed to be simple, modular, and easy to extend.
