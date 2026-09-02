from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from AWS Kubernetes!</h1>
    <p>My application is running inside a Docker container.</p>
    <p>Deployed using Kubernetes on AWS EC2.</p>
    """

@app.route("/health")
def health():
    return "Application is healthy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)