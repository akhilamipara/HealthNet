#!/usr/bin/env python3
"""
Setup Script for Hospital Management System ML Models
This script will:
1. Install ML dependencies
2. Train the three ML models
3. Test the models
4. Start the Django server
"""

import os
import sys
import subprocess
import time

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    print(f"Command: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible!")
    return True

def install_ml_dependencies():
    """Install ML model dependencies"""
    print("\n📦 Installing ML dependencies...")
    
    # Install scikit-learn and related packages
    packages = [
        "scikit-learn==1.3.2",
        "pandas==2.1.4", 
        "numpy==1.24.3",
        "xgboost==2.0.3",
        "scipy==1.11.4"
    ]
    
    for package in packages:
        if not run_command(f"pip install {package}", f"Installing {package}"):
            return False
    
    return True

def train_ml_models():
    """Train the three ML models"""
    print("\n🧠 Training ML Models...")
    
    # Navigate to ml_services directory
    os.chdir("ml_services")
    
    # Train models
    if not run_command("python train_models.py", "Training ML models"):
        return False
    
    return True

def test_ml_models():
    """Test the trained ML models"""
    print("\n🧪 Testing ML Models...")
    
    if not run_command("python ml_models/ml_inference.py", "Testing ML inference engine"):
        return False
    
    return True

def start_django_server():
    """Start the Django development server"""
    print("\n🚀 Starting Django Server...")
    
    # Check if models are trained
    if not os.path.exists("trained_models"):
        print("❌ ML models not found! Please train models first.")
        return False
    
    print("✅ ML models found! Starting Django server...")
    print("🌐 Django will be available at: http://localhost:8000")
    print("🤖 ML API endpoints will be available at: http://localhost:8000/api/ml-models/")
    print("📱 Frontend should be running at: http://localhost:5173")
    
    # Start Django server
    try:
        subprocess.run("python manage.py runserver 8000", shell=True)
    except KeyboardInterrupt:
        print("\n🛑 Django server stopped by user")
    
    return True

def main():
    """Main setup function"""
    print("🏥 Hospital Management System - ML Models Setup")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install ML dependencies
    if not install_ml_dependencies():
        print("❌ Failed to install ML dependencies!")
        sys.exit(1)
    
    # Train ML models
    if not train_ml_models():
        print("❌ Failed to train ML models!")
        sys.exit(1)
    
    # Test ML models
    if not test_ml_models():
        print("❌ Failed to test ML models!")
        sys.exit(1)
    
    # Start Django server
    if not start_django_server():
        print("❌ Failed to start Django server!")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("Your Hospital Management System with trained ML models is ready!")

if __name__ == "__main__":
    main()
