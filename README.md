# Amazon Price Tracker Bot 🤖

A robust, automated Python script that monitors the price of a specific product on Amazon and instantly sends an email alert when the price drops below a user-defined threshold.

## ✨ Features
- **Robust Web Scraping:** Uses BeautifulSoup4 with layered fallback parsing logic to reliably extract prices despite Amazon's frequent layout adjustments.
- **Automated Alerts:** Connects via SMTP to send email notifications immediately upon finding a target deal.
- **Secure Credentials:** Keeps passwords and private email addresses completely hidden from production environments using environment variables.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Requests • BeautifulSoup4 • Python-dotenv • Smtplib (Built-in) • Re (Built-in)

## 📋 Prerequisites

Before running the application, make sure you have:
1. Python installed on your machine.
2. An App Password generated for your sender email account (e.g., Google App Passwords for Gmail).

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a file named `.env` in the root directory of your project:
```text
MY_MAIL=your_sender_email@gmail.com
PASSWORD=your_app_specific_password
SMTP=://gmail.com
TO_EMAIL=your_receiver_email@example.com
```
*(Note: The `.env` file is safely ignored by Git and will never be pushed to your public repository).*

## 💻 Usage

To run the price monitor script:
```bash
python main.py
```

## 📄 License
This project is open-source and available under the MIT License.
