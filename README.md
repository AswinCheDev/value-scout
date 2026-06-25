<div align="center">
  <h1>🚀 ValueScout</h1>
  <p><b>AI-powered deal comparison and style builder platform</b></p>
</div>

## 📖 Introduction
ValueScout is a comprehensive web platform designed to redefine how you shop. By leveraging Artificial Intelligence, ValueScout helps users find the best deals, compare products seamlessly, and curate unique styles. With a robust microservice architecture combining a high-performance React frontend, an Express-driven backend, and a dedicated Python AI engine, ValueScout provides a seamless and intelligent shopping experience.

## ✨ Features
- 📊 **Dashboard & Search**: Interactive search and real-time visualization for deals and products.
- 🔐 **Authentication**: Secure and quick login with Google, complete with email verification.
- 🎨 **AI Style Builder**: Curate and build personalized styles using intelligent AI recommendations.
- 🔔 **Price Alerts**: Set up custom email notifications for price drops on your favorite items.
- 🛍️ **Wishlist & Recommendations**: Save favorite items and receive tailored product suggestions.

## 📸 Screenshots
Here is a glimpse of ValueScout in action:

| | |
|:---:|:---:|
| ![Homepage](./sc/homepage.png) | ![Homepage Search](./sc/homepage%20search.png) |
| ![AI Style Builder](./sc/ai%20style%20builder.png) | ![Price Alerts](./sc/price%20alert.png) |
| ![Recommendations](./sc/recommendation.png) | ![Wishlist](./sc/wishlist%20page.png) |

## 🛠️ Tech Stack & Libraries

### 💻 Frontend
<p>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
</p>

- **Core:** React, TypeScript, Vite
- **Styling:** Tailwind CSS, Shadcn UI, Radix UI
- **Routing:** React Router DOM
- **Utilities:** React Hook Form, Zod, React Query, Recharts

### 🗄️ Backend
<p>
  <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Express.js-404D59?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />
</p>

- **Core:** Node.js, Express
- **Database:** MongoDB (Mongoose)
- **Utilities:** Node-cron (Scheduling), Nodemailer (Email Alerts), Cheerio, Axios

### 🧠 AI & Web Scraping
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" />
</p>

- **Core:** Python
- **Scraping:** Playwright
- **Utilities:** AI Embedding Models, Web Automation

## 🏗️ Project Structure

```text
value-scout/
├── ai/                 # Python microservice for AI embeddings and web scraping
├── backend/            # Node.js & Express API server handling DB and business logic
├── frontend/           # React application built with Vite and Tailwind CSS
├── sc/                 # Screenshots for documentation
└── package.json        # Main workspace configuration & concurrent scripts
```

## 🚦 Getting Started

**Prerequisites:**
- [Node.js](https://nodejs.org/) (v18+)
- [Python](https://www.python.org/) (v3.9+)
- [MongoDB](https://www.mongodb.com/) (Local or Atlas)

**1. Clone the repository**
```bash
git clone https://github.com/your-username/value-scout.git
cd value-scout
```

**2. Install dependencies & start the Backend**
```bash
cd backend
npm install
# Ensure you have a .env file configured
npm run dev
```

**3. Install dependencies & start the Frontend**
```bash
cd ../frontend
npm install
# Ensure you have a .env file configured
npm run dev
```

**4. Start the AI Microservice**
```bash
cd ../ai
# Setup virtual environment and install requirements
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
python ai_api.py
```

*Note: You can also use the concurrent command `npm run dev` from the root directory to start all services simultaneously.*
