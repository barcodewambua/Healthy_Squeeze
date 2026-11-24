
import os
import logging
from flask import Flask
from flask_session import Session
from cachelib.file import FileSystemCache

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Secret key
app.secret_key = os.environ.get(
    "SESSION_SECRET",
    "development-only-secret-change-this"
)

# Session configuration
session_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "flask_session"
)

os.makedirs(session_directory, exist_ok=True)

app.config.update(
    SESSION_TYPE="cachelib",
    SESSION_CACHELIB=FileSystemCache(
        cache_dir=session_directory,
        threshold=500
    ),
    SESSION_PERMANENT=False,
    SESSION_SERIALIZATION_FORMAT="json",
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE", "false").lower() == "true"
)

# Initialize server-side sessions
Session(app)

# Import routes after app creation
from routes import *

# Local development
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
