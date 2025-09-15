from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f0f0f0;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #2c5aa0;
            }
            .status {
                color: green;
                font-weight: bold;
            }
            .info {
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
                text-align: left;
            }
            ol {
                text-align: left; 
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello, DevOps World!</h1>
            <p class="status">✅ Flask Application is Running Successfully</p>
            
            <div class="info">
                <h3>Application Details:</h3>
                <p><strong>Host:</strong> 0.0.0.0</p>
                <p><strong>Port:</strong> 5000</p>
                <p><strong>Debug Mode:</strong> True</p>
                <p><strong>Python Version:</strong> """ + str(os.sys.version) + """</p>
            </div>
            
            <p>এই মেসেজ দেখতে পাচ্ছেন মানে আপনার Flask app সফলভাবে running হচ্ছে!</p>
            
            <h3>পরবর্তী ধাপগুলো:</h3>
            <ol>
                <li>Dockerize করুন</li>
                <li>EC2 তে Deploy করুন</li>
                <li>CI/CD Pipeline Setup করুন</li>
            </ol>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy", "message": "Server is running perfectly"}

@app.route("/api/greet/<name>")
def greet(name):
    return {"message": f"Hello, {name}! Welcome to DevOps World"}

if __name__ == "__main__":
    print("🚀 Starting Flask Application...")
    print("📍 Server will be available at: http://0.0.0.0:5000")
    print("📍 Health check: http://0.0.0.0:5000/health")
    print("📍 Example API: http://0.0.0.0:5000/api/greet/YourName")
    print("ℹ️  Press CTRL+C to stop the server")
    app.run(host="0.0.0.0", port=5000, debug=True)
