# Mobile-Price-Prediction

# Mobile Price Prediction API using FastAPI

This FastAPI project is designed to predict mobile phone prices based on inputs like `sale`, `weight`, and `battery`. It integrates a machine learning model (`classifier.pkl`) trained to predict mobile prices and provides a simple web interface for users to input data and retrieve predictions.

## Features:
- **FastAPI Framework**: A modern web framework for building APIs with Python.
- **Machine Learning Integration**: Utilizes a pre-trained model to predict mobile prices based on input features like `sale`, `weight`, and `battery`.
- **HTML Templates**: Simple web interface using Jinja2 templates for user interaction.
- **MongoDB Integration**: Stores form submissions in a MongoDB database.
- **Form and JSON Input Support**: Can handle both JSON and form-encoded input data.
  
## Project Structure:
- `index.py`: Main FastAPI application with endpoints to handle GET and POST requests.
- `CellPhone.csv`: Contains the DataSet for the model
- `predict.py` ; The model for predicting the price of the mobile
- `model/`: Contains the BaseModel
- `templates/`: Contains HTML templates for the web interface.
- `config/`: MongoDB connection setup.

## Setup Instructions:
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn index:app --reload
   ```
4. Access the app via `http://127.0.0.1:8000`.

---
