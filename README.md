# Trello Board Generator 🚀

![GitHub Actions Status](https://github.com/harshithaendreddy/trello-board-creator/actions/workflows/run.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Here’s a polished and clean version of your `README.md`, with consistent formatting, badges, and clear sections:

---

````markdown
# 🚀 Trello Board Generator

![GitHub Actions](https://github.com/harshithaendreddy/trello-board-creator/actions/workflows/run.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A fully automated Trello board generator from a JSON file using Python and GitHub Actions. Perfect for developers, productivity enthusiasts, and anyone tired of setting up boards manually.

---

## 🧩 Features

- 🔁 **Automated Trello board creation** via REST API  
- 📄 **JSON-based configuration** for full control over lists and cards  
- ⚙️ **CI/CD using GitHub Actions** — trigger from anywhere  
- 🔐 **Secrets stored securely** with GitHub repository secrets  
- 🐍 Built with **Python + requests**

---

## 🧪 Demo Output

Input JSON file:

```json
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
````

What gets auto-created on Trello:

```
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
```

---

## ⚙️ Setup

### 1. Get Your Trello API Key & Token

* Visit [trello.com/app-key](https://trello.com/app-key)
* Copy your API key
* Click the token link below the key to generate your access token

---

### 2. Clone This Repo

```bash
git clone https://github.com/harshithaendreddy/trello-board-creator.git
cd trello-board-creator
```

---

### 3. Add Secrets to GitHub

Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:

| Name             | Value               |
| ---------------- | ------------------- |
| `TRELLO_API_KEY` | Your Trello API key |
| `TRELLO_TOKEN`   | Your Trello token   |

---

### 4. Trigger the Workflow

* Go to the **Actions** tab in your repo
* Run the **Create Trello Developer Dashboard** workflow manually

---

## 📁 Project Structure

```
📦 trello-board-creator
├── .github/
│   └── workflows/
│       └── run.yml            # GitHub Actions workflow file
├── DeveloperDashboardBoard.json  # JSON board template
├── trello_import.py           # Python script that creates the board
└── README.md
```

---

## 🚀 Future Development

* 🖥️ Build a Web UI where users can paste JSON and trigger board creation
* 🌐 Add Trello OAuth login flow
* 📊 Display past boards created with analytics and reusable templates

---

## 💡 Why This Project?

* ✅ Demonstrates **real-world API integration**
* ✅ Showcases **basic CI/CD with GitHub Actions**
* ✅ Promotes **automating repetitive tasks**
* ✅ Great for **personal project dashboards**, **team task boards**, and **hackathons**

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🤝 Let's Connect

Love building dev tools or interested in automation workflows like this?
Feel free to ⭐️ the repo or [connect with me on LinkedIn](https://www.linkedin.com/in/your-profile/)!

---

> "Automation isn’t just for deployments — it’s for everything repetitive." 💡

```

---

Let me know if you'd like:
- Markdown version with collapsible sections
- A UI version to paste JSON and trigger creation
- Or deployment to GitHub Pages to expose it as a tool

I'll gladly help!
```
