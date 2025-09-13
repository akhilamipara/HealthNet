#!/usr/bin/env python3
"""
Secret Key Generator for Hospital Management System
Run this script to generate secure keys for all services
"""

import secrets
import string
import hashlib
import time

def generate_django_secret():
    """Generate Django secret key"""
    try:
        from django.core.management.utils import get_random_secret_key
        return get_random_secret_key()
    except ImportError:
        # Fallback if Django not available
        return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(50))

def generate_jwt_secret():
    """Generate JWT secret key"""
    return secrets.token_hex(64)

def generate_mongodb_uri():
    """Generate MongoDB connection string template"""
    return "mongodb://localhost:27017/hospital_db"

def main():
    print("🔐 Generating Secret Keys for Hospital Management System")
    print("=" * 60)
    
    # Django Secret Key
    print("\n📋 Django Secret Key:")
    django_key = generate_django_secret()
    print(f"SECRET_KEY={django_key}")
    
    # JWT Secret
    print("\n🔑 JWT Secret Key:")
    jwt_key = generate_jwt_secret()
    print(f"JWT_SECRET={jwt_key}")
    
    # MongoDB URI
    print("\n🗄️  MongoDB Connection:")
    mongo_uri = generate_mongodb_uri()
    print(f"MONGODB_URI={mongo_uri}")
    
    # Gemini API Key (placeholder)
    print("\n🤖 Gemini API Key:")
    print("GEMINI_API_KEY=your-actual-gemini-api-key-here")
    print("(Get this from: https://makersuite.google.com/app/apikey)")
    
    print("\n" + "=" * 60)
    print("📝 Copy these keys to your .env files:")
    print("\nml_services/.env:")
    print(f"SECRET_KEY={django_key}")
    print("GEMINI_API_KEY=your-actual-gemini-api-key-here")
    
    print("\nbackend/.env:")
    print(f"JWT_SECRET={jwt_key}")
    print(f"MONGODB_URI={mongo_uri}")
    
    print("\nfrontend/.env:")
    print("VITE_API_BASE_URL=http://localhost:8000/api")
    
    print("\n🎯 All secret keys generated successfully!")
    print("⚠️  Keep these keys secure and never commit them to version control!")

if __name__ == "__main__":
    main()
