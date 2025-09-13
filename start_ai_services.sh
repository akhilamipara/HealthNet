#!/bin/bash

echo "🏥 Starting Hospital Management System AI Services..."
echo

echo "📋 Starting Django Backend..."
cd ml_services
source django_env/bin/activate
python manage.py runserver 8000 &
DJANGO_PID=$!

echo "⏳ Waiting for Django to start..."
sleep 5

echo "🌐 Starting React Frontend..."
cd ../frontend
npm run dev &
REACT_PID=$!

echo
echo "✅ Both servers are starting..."
echo
echo "🌐 Django Backend: http://localhost:8000"
echo "🌐 React Frontend: http://localhost:5173 (or 3000)"
echo
echo "📱 AI Services: http://localhost:5173/ml-services"
echo "🤖 Floating Chatbot: Available on all pages"
echo

# Function to cleanup on exit
cleanup() {
    echo "🛑 Shutting down servers..."
    kill $DJANGO_PID 2>/dev/null
    kill $REACT_PID 2>/dev/null
    exit 0
}

# Trap Ctrl+C and cleanup
trap cleanup SIGINT

echo "Press Ctrl+C to stop both servers..."
wait
