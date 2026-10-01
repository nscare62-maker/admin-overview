#!/bin/bash

# S2C Admin Dashboard Setup Script

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║   S2C Admin Dashboard - Setup Script                      ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created. Please edit it with your configuration."
else
    echo ""
    echo "✅ .env file already exists."
fi

# Check for Firebase credentials
if [ ! -f firebase-credentials.json ]; then
    echo ""
    echo "⚠️  WARNING: firebase-credentials.json not found!"
    echo "Please add your Firebase service account credentials file."
    echo "Download it from: Firebase Console → Project Settings → Service Accounts"
else
    echo ""
    echo "✅ Firebase credentials found."
fi

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║   Setup Complete!                                          ║"
echo "╠═══════════════════════════════════════════════════════════╣"
echo "║   Next steps:                                              ║"
echo "║   1. Edit .env file with your configuration                ║"
echo "║   2. Add firebase-credentials.json file                    ║"
echo "║   3. Run: python app.py                                    ║"
echo "║   4. Open: http://localhost:5000                           ║"
echo "║   5. Login: admin / admin123                               ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
