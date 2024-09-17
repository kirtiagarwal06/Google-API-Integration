# Google Integration Portal

## Overview

The Google Integration Portal is a web application that allows users to view and manage their Google My Business reviews through a centralized platform. This portal leverages the Google My Business API and OAuth 2.0 for secure authentication and enables users to respond to reviews directly from the portal. It is built with a Flask (Python) backend and a React frontend, ensuring modern web technologies for functionality and responsiveness.

## Features

- **Google Authentication**: Secure login using OAuth 2.0 to allow access to Google My Business data.
- **View Google Reviews**: Fetch and display Google reviews for authenticated users.
- **Respond to Reviews**: Users can reply to reviews directly from the portal.
- **Responsive Design**: Accessible across various devices including desktops, tablets, and mobile phones.
- **Mock API Support**: If Google APIs are unavailable, the portal can run with dummy data to simulate real functionality.

## Technologies Used

- **Backend**: Flask (Python), Google API Client Library
- **Frontend**: React, Axios, Bootstrap
- **Google APIs**: Google My Business API, OAuth 2.0
- **Optional**: Docker for containerization, pytest for backend testing


## Setup Instructions

### Backend Setup (Flask)

1. Clone the repository:

    ```bash
    git clone https://github.com/kirtiagarwal06/Google-API-Integration.git
    cd Google-API-Integration/backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Get Google API credentials:
    - Go to the Google Developer Console and create a new project.
    - Enable the Google My Business API and generate OAuth 2.0 credentials.
    - Download the `client_secrets.json` file and place it in the `backend/` folder.

5. Run the backend server:

    ```bash
    python app.py
    ```

    The backend will run on [http://localhost:5000](http://localhost:5000).

### Frontend Setup (React)

1. Navigate to the frontend directory:

    ```bash
    cd ../frontend
    ```

2. Install the frontend dependencies:

    ```bash
    npm install
    ```

3. Run the React development server:

    ```bash
    npm start
    ```

    The frontend will be running on [http://localhost:3000](http://localhost:3000).

### Dummy API (Optional)

If you don't have access to Google APIs, the application can be run using dummy data.

1. Modify the `/get_reviews` endpoint in `app.py` to return mock data:

    ```python
    @app.route("/get_reviews")
    def get_reviews():
        reviews = {
            "reviews": [
                {"reviewId": "1", "reviewer": {"displayName": "John Doe"}, "comment": "Great service!", "starRating": 5},
                {"reviewId": "2", "reviewer": {"displayName": "Jane Smith"}, "comment": "Good experience", "starRating": 4},
            ]
        }
        return jsonify(reviews)
    ```

2. Run the backend and frontend using the same steps outlined above. This will simulate the review fetching process.

### Docker Setup (Optional)

You can containerize the application using Docker.

- **Backend Dockerfile:**

    ```dockerfile
    FROM python:3.9
    WORKDIR /app
    COPY . /app
    RUN pip install -r requirements.txt
    CMD ["python", "app.py"]
    ```

- **Frontend Dockerfile:**

    ```dockerfile
    FROM node:14
    WORKDIR /app
    COPY . /app
    RUN npm install
    CMD ["npm", "start"]
    ```

- Build and run the containers:

    ```bash
    docker build -t google-portal-backend ./backend
    docker build -t google-portal-frontend ./frontend
    docker run -p 5000:5000 google-portal-backend
    docker run -p 3000:3000 google-portal-frontend
    ```

## Testing

- **Backend Testing (pytest)**
  Unit tests are located in the `backend/tests/` directory.
  To run tests:

    ```bash
    pytest
    ```

- **Frontend Testing (Jest)**
  Frontend unit tests are located in the `frontend/src/tests/` directory.
  To run tests:

    ```bash
    npm test
    ```

## Future Enhancements

- **Email Notifications**: Notify users when new reviews are posted.
- **Advanced Filtering**: Allow filtering of reviews by star rating, date, etc.
- **Analytics Dashboard**: Add charts and review statistics over time.
- **Admin Controls**: Implement admin functionality for managing multiple Google accounts.

## Contributing

- Fork the repository.
- Create a new feature branch: `git checkout -b my-feature-branch`.
- Commit your changes: `git commit -m 'Add some feature'`.
- Push to the branch: `git push origin my-feature-branch`.
- Submit a pull request.


## Contact

For any questions or issues, feel free to reach out at kirtiagarwal.ka54@gmail.com

