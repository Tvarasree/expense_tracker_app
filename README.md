💸 Expense Tracker App

A simple yet powerful desktop-based **Expense Tracker Application** built using **Python and Tkinter**. This app helps users manage their monthly budgets and track categorized expenses with full reporting support.

---
## 📌 Features

- 📊 Set a monthly budget by category
- 💰 Add expenses with category and month
- 📅 Generate full expense reports month-wise
- ✅ No constraint on expense entry (even if budget isn't set)
- 💾 Data persistence using SQLite3 database
- 🐳 Run easily using Docker

---

---

## 🖥️ Tech Stack

- **Python 3.x**
- **Tkinter** (GUI)
- **SQLite3** (local database)
- **Docker** (for containerization)

---

## 🚀 Getting Started

### 🔧 Manual Setup

 1. Clone the repository
git clone https://github.com/Tvarasree/expense_tracker_app.git
cd expense_tracker_app

#### 2. Install dependencies
pip install -r requirements.txt

3. Run the application
python app_gui.py

🐳 Docker-Based Setup
1. Build the Docker image
docker build -t expense-tracker-app .

2. Run the Docker container
docker run -it expense-tracker-app
