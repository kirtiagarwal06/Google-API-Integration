# Google-API-Integration
The Google Integration Portal is a web application that allows users to view and manage their Google My Business reviews through a centralized platform. This portal leverages the Google My Business API and OAuth 2.0 for secure authentication and enables users to respond to reviews directly from the portal.t is built with a Flask (Python) backend and a React frontend, ensuring modern web technologies for functionality and responsiveness.

# Features
1.Google Authentication: Secure login using OAuth 2.0 to allow access to Google My Business data.
2.View Google Reviews: Fetch and display Google reviews for authenticated users.
3.Respond to Reviews: Users can reply to reviews directly from the portal.
4.Responsive Design: Accessible across various devices including desktops, tablets, and mobile phones.
5.Mock API Support: If Google APIs are unavailable, the portal can run with dummy data to simulate real functionality.

# Technologies used:
1.Backend: Flask (Python), Google API Client Library
2.Frontend: React, Axios, Bootstrap
3.Google APIs: Google My Business API, OAuth 2.0
4.Optional: Docker for containerization, pytest for backend testing

# Project Structure
google-integration-portal/
├── backend/              # Flask backend
│   ├── app.py            # Main Flask app
│   ├── client_secrets.json # Google API credentials
│   ├── requirements.txt  # Python dependencies
│   └── tests/            # Backend unit tests
├── frontend/             # React frontend
│   ├── src/              # React components
│   ├── public/           # Static files
│   ├── package.json      # Frontend dependencies
│   └── tests/            # Frontend unit tests

# Setup Instructions
# Backend Setup (Flask):
1.Clone the repository: git clone https://github.com/kirtiagarwal06/google-integration-portal.git
cd google-integration-portal/backend

2.Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install the required dependencies:
pip install -r requirements.txt

4.Get Google API credentials:
Go to the Google Developer Console and create a new project.
Enable the Google My Business API and generate OAuth 2.0 credentials.
Download the client_secrets.json file and place it in the backend/ folder.

5.Run the backend server:
python app.py
The backend will run on http://localhost:5000.

# Frontend Setup (React)
1.Navigate to the frontend directory:
cd ../frontend

2.Install the frontend dependencies:
npm install

3.Run the React development server:
npm start

The frontend will be running on http://localhost:3000.

# Dummy API (Optional)
If you don't have access to Google APIs, the application can be run using dummy data.
Modify the /get_reviews endpoint in app.py to return mock data:

@app.route("/get_reviews")
def get_reviews():
    reviews = {
        "reviews": [
            {"reviewId": "1", "reviewer": {"displayName": "John Doe"}, "comment": "Great service!", "starRating": 5},
            {"reviewId": "2", "reviewer": {"displayName": "Jane Smith"}, "comment": "Good experience", "starRating": 4},
        ]
    }
    return jsonify(reviews)

Run the backend and frontend using the same steps outlined above. This will simulate the review fetching process.

# Docker Setup (Optional)
You can containerize the application using Docker.
1.Backend Dockerfile:
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

2.Frontend Dockerfile:
FROM node:14
WORKDIR /app
COPY . /app
RUN npm install
CMD ["npm", "start"]

3.Build and run the containers:
docker build -t google-portal-backend ./backend
docker build -t google-portal-frontend ./frontend
docker run -p 5000:5000 google-portal-backend
docker run -p 3000:3000 google-portal-frontend

# Testing
1.Backend Testing (pytest)
Unit tests are located in the backend/tests/ directory.
To run tests:pytest

2.Frontend Testing (Jest)
Frontend unit tests are located in the frontend/src/tests/ directory.
To run tests:npm test

# Future Enhancements
1.Email Notifications: Notify users when new reviews are posted.
2.Advanced Filtering: Allow filtering of reviews by star rating, date, etc.
3.Analytics Dashboard: Add charts and review statistics over time.
4.Admin Controls: Implement admin functionality for managing multiple Google accounts.

# Contributing
1.Fork the repository.
2.Create a new feature branch: git checkout -b my-feature-branch.
3.Commit your changes: git commit -m 'Add some feature'.
4.Push to the branch: git push origin my-feature-branch.
5.Submit a pull request.

# Contact
For any questions or issues, feel free to reach out at kirtiagarwal.ka54@gmail.com









