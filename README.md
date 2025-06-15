# Trello Board Generator 🚀

![GitHub Actions Status](https://github.com/harshithaendreddy/trello-board-creator/actions/workflows/run.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 🧩 Trello Board Generator from JSON

🚀 Automatically create a fully structured Trello board — with lists and cards — using a simple JSON file and GitHub Actions. Ideal for developers, productivity enthusiasts, and teams that want to automate repetitive Trello setups.

---

## 🌟 Features

- 🔄 **Automated Trello board creation** via REST API
- 🧾 **JSON-based configuration** for full control over lists and cards
- 🤖 **GitHub Actions** integration for seamless automation
- 🔐 API key and token managed securely with **GitHub Secrets**
- 💻 Built with **Python + requests**

---

## 📁 Example Use Case

### 🔧 Input (JSON file)
{
  "name": "Personal Developer Dashboard",
  "lists": [
    {
      "name": "To Do",
      "cards": ["Build UI for Trello Creator", "Complete DSA Tracker", "Update Resume"]
    },
    {
      "name": "Doing",
      "cards": ["Build GitHub Action Workflow"]
    },
    {
      "name": "Done",
      "cards": ["Created Python Script", "Setup Trello API Access"]
    }
  ]
}
`

### 🪄 Output

A full Trello board like this (auto-created):

📌 Personal Developer Dashboard
 ┣ 📂 To Do
 ┃ ┣ 📝 Build UI for Trello Creator
 ┃ ┣ 📝 Complete DSA Tracker
 ┃ ┗ 📝 Update Resume
 ┣ 📂 Doing
 ┃ ┗ 📝 Build GitHub Action Workflow
 ┗ 📂 Done
    ┣ 📝 Created Python Script
    ┗ 📝 Setup Trello API Access
---

## 🔧 Setup Instructions

### 1. 🔑 Get Your Trello API Key and Token

* Go to [https://trello.com/app-key](https://trello.com/app-key)
* Copy your API key and generate a token

### 2. 📂 Clone This Repository
bash
git clone https://github.com/harshithaendreddy/trello-board-creator.git
cd trello-board-creator
### 3. 🔐 Add Secrets in GitHub

Go to your repo → Settings → Secrets → Actions → **New Repository Secret**

| Name             | Value               |
| ---------------- | ------------------- |
| `TRELLO_API_KEY` | Your Trello API Key |
| `TRELLO_TOKEN`   | Your Trello Token   |

### 4. 🚀 Trigger the Workflow

* Go to the **Actions** tab on GitHub
* Run the workflow manually ("Create Trello Developer Dashboard")

---

## 📦 Project Structure
bash
📦 trello-board-creator
├── .github/
│   └── workflows/
│       └── run.yml            # GitHub Actions workflow file
├── DeveloperDashboardBoard.json  # JSON board template
├── trello_import.py           # Python script that creates the board
└── README.md

---

## 💡 Future Development

* 🖥️ Build a UI where users can input JSON in-browser and generate boards directly
* 🌐 Add OAuth for Trello login and token retrieval
* 📊 Dashboard for past generated boards, analytics, and templates

---

## 🧠 Why This Project?

✅ Demonstrates real-world API integration
✅ Highlights DevOps knowledge (CI/CD via GitHub Actions)
✅ Encourages automation and productivity-driven development
✅ Great for personal project dashboards, team planning, or hackathons

---

## 🤝 Let's Connect

Love building dev tools or interested in automation workflows like this?
Feel free to ⭐️ the repo or [connect with me on LinkedIn]([https://www.linkedin.com/in//](https://www.linkedin.com/in/harshitha-endreddy/))!

---

> "Automation isn’t just for deployments — it’s for everything repetitive." 💡

```

---
