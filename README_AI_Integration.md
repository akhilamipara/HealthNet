# 🏥 Hospital Management System - AI Integration

Complete integration of AI-powered medical services using Django backend and React frontend.

## 🚀 Features

### Backend (Django)
- **Chatbot Service**: Hospital-related queries using Gemini AI
- **Symptom Checker**: AI-powered symptom analysis
- **Disease Prediction**: Health data analysis and disease risk assessment
- **Treatment Information**: Comprehensive treatment options and recommendations

### Frontend (React)
- **Floating Chatbot**: Bottom-right corner chat interface
- **ML Services Page**: Dedicated page with tabbed interface
- **Responsive Design**: Works across all devices
- **Real-time AI Integration**: Direct connection to Django APIs

## 📁 Project Structure

```
prescripto-full-stack/
├── backend/                 # Existing MERN backend
├── frontend/               # Existing React frontend
├── ml_services/           # NEW: Django AI backend
│   ├── chatbot/           # Chatbot app
│   ├── ml_models/         # ML services app
│   ├── ml_services/       # Django project settings
│   ├── manage.py          # Django management
│   ├── requirements.txt    # Python dependencies
│   └── README.md          # Django setup guide
└── README_AI_Integration.md # This file
```

## 🛠️ Setup Instructions

### 1. Django Backend Setup

```bash
# Navigate to Django project
cd ml_services

# Activate virtual environment
django_env\Scripts\activate  # Windows
source django_env/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create .env file with:
DEBUG=True
SECRET_KEY=your-secret-key
GEMINI_API_KEY=your-gemini-api-key

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start Django server
python manage.py runserver 8000
```

### 2. Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies (if not already installed)
npm install

# Start React development server
npm run dev
```

### 3. Environment Configuration

#### Django (.env file)
```env
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key-here
GEMINI_API_KEY=your-actual-gemini-api-key
```

#### Frontend (API Configuration)
The frontend is configured to connect to `http://localhost:8000/api` by default.

## 🔌 API Endpoints

### Chatbot API
- `POST /api/chatbot/chat/` - Send message to chatbot
- `GET /api/chatbot/history/?session_id=<id>` - Get chat history

### ML Models API
- `POST /api/ml-models/symptom-checker/` - Check symptoms
- `POST /api/ml-models/disease-prediction/` - Predict disease
- `POST /api/ml-models/treatment-info/` - Get treatment information
- `GET /api/ml-models/treatment-list/` - List all treatments

## 🎯 Usage

### 1. Access ML Services
- Navigate to `/ml-services` in your React app
- Use the tabbed interface to access different AI services

### 2. Floating Chatbot
- Click the blue chat button in the bottom-right corner
- Ask hospital-related questions
- Get AI-powered responses

### 3. Symptom Checker
- Describe your symptoms in detail
- Get AI analysis of possible conditions
- View confidence scores

### 4. Disease Prediction
- Input health data (age, gender, vitals, etc.)
- Receive disease risk assessment
- View confidence levels

### 5. Treatment Information
- Search for specific diseases
- Get comprehensive treatment options
- View medications and lifestyle recommendations

## 🔧 Configuration

### CORS Settings
Django is configured to allow requests from:
- `http://localhost:3000` (React dev server)
- `http://localhost:5173` (Vite dev server)

### Gemini AI Integration
- Requires valid Gemini API key
- Configured in Django settings
- Used for all AI-powered responses

## 🚨 Important Notes

### Medical Disclaimer
⚠️ **All AI responses include medical disclaimers and are for informational purposes only. They should not replace professional medical advice.**

### API Keys
- Keep your Gemini API key secure
- Never commit API keys to version control
- Use environment variables for production

### Error Handling
- Frontend includes comprehensive error handling
- Toast notifications for user feedback
- Fallback responses for API failures

## 🧪 Testing

### Test Django Backend
```bash
cd ml_services
python manage.py test
```

### Test Frontend
```bash
cd frontend
npm test
```

### Manual Testing
1. Start Django server on port 8000
2. Start React dev server on port 3000/5173
3. Navigate to ML Services page
4. Test each AI service
5. Test floating chatbot

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure Django server is running
   - Check CORS settings in Django
   - Verify frontend URL is in allowed origins

2. **Gemini API Errors**
   - Verify API key is valid
   - Check API quota limits
   - Ensure internet connectivity

3. **Database Issues**
   - Run migrations: `python manage.py migrate`
   - Check database configuration
   - Verify model imports

4. **Frontend Build Issues**
   - Clear node_modules and reinstall
   - Check for syntax errors
   - Verify all imports are correct

## 🔒 Security Considerations

- CORS properly configured
- Input validation on all endpoints
- Environment variables for sensitive data
- Medical disclaimers included
- Rate limiting recommended for production

## 🚀 Production Deployment

### Django
- Use production database (PostgreSQL/MySQL)
- Set DEBUG=False
- Configure proper CORS origins
- Use environment variables for secrets
- Enable HTTPS

### React
- Build production bundle: `npm run build`
- Serve static files from Django or CDN
- Update API endpoints for production URLs

## 📞 Support

For issues or questions:
1. Check Django logs for backend errors
2. Check browser console for frontend errors
3. Verify API endpoints are accessible
4. Test with Postman/Insomnia for API debugging

## 🎉 Success!

Your Hospital Management System now includes:
- ✅ AI-powered chatbot
- ✅ Intelligent symptom analysis
- ✅ Disease risk assessment
- ✅ Treatment recommendations
- ✅ Responsive UI
- ✅ Full-stack integration
- ✅ Professional medical disclaimers

The system is ready for development and testing! 🎯
