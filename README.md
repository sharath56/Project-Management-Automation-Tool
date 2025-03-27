# Developer Task Monitor

A full-stack application that analyzes developer tasks, breaks them into sub-tasks for different experience levels, generates flowcharts, and provides AI-powered assistance using OpenAI GPT.

## Features

- **Task Analysis**: Breaks down tasks for different developer levels (Intern, Junior, Senior, Solo).
- **Flowchart Generation**: Visualizes tasks using Graphviz.
- **MongoDB Storage**: Saves analyzed tasks for future reference.
- **Full-Stack**: Flask-based backend with a Streamlit UI.
- **Dockerized**: Easy deployment with Docker and Docker Compose.

---

## File Structure
```
developer-task-monitor/
│── backend/                 # Flask API Backend
│   ├── app.py               # Main Flask API
│   ├── Dockerfile           # Docker config for API
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # API keys and config
│   ├── database.py          # MongoDB connection
│   ├── flowchart.py         # Graphviz Flowchart generator
│   ├── task_analyzer.py     # GPT-based task analysis
│   └── config.py            # Configurations
│
│── frontend/                # Streamlit Frontend
│   ├── app.py               # Streamlit UI
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Docker config for UI
│
│── docker-compose.yml       # Compose for backend + frontend
│── README.md                # Project Documentation
│── .gitignore               # Ignore files
```

---

## Installation & Running Locally

### 1️⃣ Prerequisites
- Python 3.8+
- MongoDB (or use MongoDB Atlas)
- OpenAI API Key

### 2️⃣ Set Up Backend
```bash
cd backend
pip install -r requirements.txt
export OPENAI_API_KEY="your_openai_api_key"
export MONGO_URI="your_mongodb_connection_string"
python app.py
```

### 3️⃣ Set Up Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

### 4️⃣ Open in Browser
📌 `http://localhost:8501`

---

## Running with Docker

### 1️⃣ Build and Run Containers
```bash
docker-compose up --build
```

### 2️⃣ Open in Browser
📌 `http://localhost:8501`

---

## API Endpoints

### **1️⃣ Analyze Task**
```http
POST /analyze_task
```
#### **Request Body**
```json
{
  "task_description": "Build a user authentication system"
}
```

#### **Response**
```json
{
  "sub_tasks": {
    "Intern": "Set up a database schema for users.",
    "Junior": "Create login and registration pages.",
    "Senior": "Implement security best practices.",
    "Solo": "Build the full authentication system."
  },
  "flowchart": "Graphviz flowchart data"
}
```

---

## Future Enhancements
✅ **React Frontend**
✅ **AI-Generated Code Suggestions**
✅ **Task Scheduling & Notifications**


Author :
SHARATH VN ....... live long and prosper 🖖


🚀 Contributions are welcome!

