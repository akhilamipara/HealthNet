# 🏥 HealthNet - Hospital Management System

A comprehensive hospital management system with AI-powered features, built using modern web technologies. This system provides separate interfaces for patients, doctors, and administrators with integrated AI services for enhanced healthcare management.

## 🌟 Features

### 👥 **Multi-Role System**
- **Patient Portal**: Book appointments, view medical history, AI health chatbot
- **Doctor Dashboard**: Manage appointments, patient records, AI diagnostic assistance
- **Admin Panel**: System management, user oversight, analytics dashboard

### 🤖 **AI-Powered Services**
- **Intelligent Chatbot**: 24/7 health consultation and support
- **Diagnostic Assistance**: ML-powered diagnostic suggestions
- **Predictive Analytics**: Health trend analysis and predictions
- **Smart Scheduling**: AI-optimized appointment scheduling

### 📱 **Core Functionality**
- **Appointment Management**: Real-time booking and scheduling
- **Patient Records**: Comprehensive medical history tracking
- **Payment Integration**: Stripe and Razorpay payment gateways
- **File Management**: Cloudinary integration for medical documents
- **Real-time Notifications**: Toast notifications and alerts

## 🏗️ Architecture

```
HealthNet/
├── 🌐 frontend/          # React.js Patient Portal (Port 5173)
├── 👨‍⚕️ admin/             # React.js Admin Dashboard (Port 3000)
├── 🔧 backend/           # Node.js/Express API (Port 5000)
├── 🤖 ml_services/       # Django AI Services (Port 8000)
├── 📋 docs/              # Documentation
└── 🛠️ scripts/           # Setup and utility scripts
```

## 🛠️ Tech Stack

### **Frontend**
- **Framework**: React 18 + Vite
- **Styling**: Tailwind CSS
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **UI Components**: Lucide React, AOS animations
- **Notifications**: React Toastify

### **Backend (MERN)**
- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: MongoDB with Mongoose
- **Authentication**: JWT + bcrypt
- **File Upload**: Multer + Cloudinary
- **Payments**: Stripe, Razorpay
- **Validation**: Validator.js

### **AI Services (Django)**
- **Framework**: Django + Django REST Framework
- **AI/ML**: TensorFlow, scikit-learn
- **NLP**: Google Gemini API
- **Database**: SQLite (development)
- **API**: RESTful endpoints

## 🚀 Quick Start

### Prerequisites
- Node.js (v16+)
- Python (v3.8+)
- MongoDB
- Git

### 1. Clone Repository
```bash
git clone <repository-url>
cd HealthNet
```

### 2. Environment Setup

Create environment files for each service:

**Backend (.env)**
```env
PORT=5000
MONGODB_URI=your-mongodb-url
JWT_SECRET=your-jwt-secret-key
CLOUDINARY_NAME=your-cloudinary-name
CLOUDINARY_API_KEY=your-cloudinary-key
CLOUDINARY_API_SECRET=your-cloudinary-secret
STRIPE_SECRET_KEY=your-stripe-secret
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
```

**Frontend (.env)**
```env
VITE_BACKEND_URL=http://localhost:5000
VITE_AI_BACKEND_URL=http://localhost:8000
```

**Admin (.env)**
```env
VITE_BACKEND_URL=http://localhost:5000
```

**ML Services (.env)**
```env
DEBUG=True
SECRET_KEY=your-django-secret-key
GEMINI_API_KEY=your-gemini-api-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Install Dependencies

```bash
# Backend
cd backend
npm install

# Frontend
cd ../frontend
npm install

# Admin
cd ../admin
npm install

# ML Services
cd ../ml_services
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Start MongoDB
mongod

# Django migrations
cd ml_services
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start All Services

**Option A: Manual Start**
```bash
# Terminal 1 - Backend
cd backend && npm start

# Terminal 2 - Frontend
cd frontend && npm run dev

# Terminal 3 - Admin
cd admin && npm run dev

# Terminal 4 - AI Services
cd ml_services && python manage.py runserver 8000
```

**Option B: Automated Start**
```bash
# Windows
start_all_services.bat

# Linux/Mac
chmod +x start_all_services.sh
./start_all_services.sh
```

## 🌐 Service URLs

| Service | URL | Purpose |
|---------|-----|---------|
| **Patient Portal** | http://localhost:5173 | Main application |
| **Admin Dashboard** | http://localhost:3000 | Administrative panel |
| **API Backend** | http://localhost:5000 | REST API endpoints |
| **AI Services** | http://localhost:8000 | ML/AI endpoints |## 📁 
Project Structure

```
HealthNet/
├── 📱 frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── context/       # React context providers
│   │   ├── assets/        # Images, icons, styles
│   │   └── App.jsx        # Main app component
│   └── package.json
│
├── 👨‍💼 admin/
│   ├── src/
│   │   ├── components/     # Admin UI components
│   │   ├── pages/         # Admin pages
│   │   │   └── Admin/
│   │   │       └── AllAppointments.jsx  # Appointments with filters
│   │   ├── context/       # Admin context
│   │   └── assets/        # Admin assets
│   └── package.json
│
├── 🔧 backend/
│   ├── controllers/       # Business logic
│   │   ├── userController.js
│   │   ├── doctorController.js
│   │   └── adminController.js
│   ├── models/           # Database schemas
│   │   ├── userModel.js
│   │   ├── doctorModel.js
│   │   └── appointmentModel.js
│   ├── routes/           # API routes
│   ├── middleware/       # Auth & validation
│   ├── config/          # Database & cloud config
│   └── server.js        # Express server
│
├── 🤖 ml_services/
│   ├── chatbot/         # AI chatbot service
│   ├── ml_models/       # ML model training & inference
│   ├── ml_services/     # Django project settings
│   └── manage.py        # Django management
│
└── 📋 docs/
    ├── README_AI_Integration.md
    └── PORT_CONFIGURATION_GUIDE.md
```


## 🎨 Key Features Implementation

### **Appointment Filtering (AllAppointments.jsx)**
- **Doctor Name Search**: Real-time search through doctor names
- **Status Filter**: Filter by Pending, Completed, Cancelled, or All
- **Combined Filtering**: Both filters work simultaneously
- **Responsive Design**: Mobile-friendly interface

### **AI Integration**
- **Health Chatbot**: 24/7 medical consultation
- **Diagnostic Support**: ML-powered health analysis
- **Predictive Analytics**: Health trend predictions

### **Payment Processing**
- **Multiple Gateways**: Stripe and Razorpay integration
- **Secure Transactions**: PCI-compliant payment handling
- **Transaction History**: Complete payment tracking

## 🔒 Security Features

- **JWT Authentication**: Secure token-based auth
- **Role-based Access**: User, Doctor, Admin permissions
- **Data Encryption**: bcrypt password hashing
- **Input Validation**: Comprehensive data validation
- **CORS Protection**: Cross-origin request security
- **File Upload Security**: Secure file handling with Cloudinary

## 🧪 Testing

```bash
# Backend tests
cd backend
npm test

# Frontend tests
cd frontend
npm test

# AI services tests
cd ml_services
python manage.py test
```

## 📊 Monitoring & Analytics

- **Real-time Dashboard**: Admin analytics panel
- **Appointment Metrics**: Booking and completion rates
- **User Analytics**: Registration and engagement stats
- **AI Usage Tracking**: Chatbot and ML service metrics

**Built with ❤️ for better healthcare management**

🌟 **Star this repository if you find it helpful!**
