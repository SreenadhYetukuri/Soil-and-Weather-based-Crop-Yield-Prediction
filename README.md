

## Project Overview
This Flask application utilizes machine learning models to provide predictions based on input data. The models used include Random Forest, XGBoost, LightGBM, KNN, SVM, and MLP.

## Features
- Predicts crop recommendations using trained models.
- Provides an interactive API endpoint.
- Designed for deployment on AWS.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Flask
- Required Python packages (specified in `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd flask_app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application Locally
Run the following command to start the Flask server:
```bash
python app.py
```
The application should be accessible at `http://127.0.0.1:5000/`.

## API Endpoints
- **GET /**: Home route
- **POST /predict**: Accepts JSON input and returns a prediction.
  Example:
  ```json
  {
    "N": 50,
    "P": 40,
    "K": 20,
    "temperature": 22.5,
    "humidity": 80.0,
    "ph": 6.5,
    "rainfall": 200.0
  }
  ```

## Notes
- Ensure the correct AWS security policies are configured.
- Update the application to use a production-ready server (e.g., Gunicorn) when deploying.

## Author
- Yetukuri Gargeya Sreenadh
- Contact: sreenadhyetukuri2@gmail.com
