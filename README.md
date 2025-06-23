# Phishing URL Detection

A Flask-based API for detecting phishing URLs using machine learning. This project uses a RandomForestClassifier trained on legitimate and phishing URL datasets to classify URLs as safe or malicious.

## Features

- **REST API**: Simple Flask endpoint for URL classification
- **Machine Learning**: RandomForestClassifier for accurate phishing detection
- **Feature Engineering**: Extracts meaningful features from URLs for classification
- **Easy Setup**: Straightforward installation and usage process

## Project Structure

```
phishing-url-detection/
├── app.py                              # Flask API application
├── model_training.py                   # Model training script
├── convert.py                          # Legitimate URLs processor
├── convert_phishing.py                 # Phishing URLs processor
├── phishing_dataset.csv               # Combined training dataset
├── phishing_model.pkl                 # Trained ML model
├── top-1m.csv                         # Legitimate URLs dataset
├── PhiUSIIL_Phishing_URL_Dataset.csv  # Phishing URLs dataset
└── requirements.txt                    # Python dependencies
```

### File Descriptions

- **`app.py`**: Flask application exposing the `/predict` API endpoint. Loads the pre-trained model and classifies URLs.
- **`model_training.py`**: Trains the RandomForestClassifier using the combined dataset and saves the model.
- **`convert.py`**: Processes legitimate URLs from `top-1m.csv` and adds them to the training dataset with label '0' (safe).
- **`convert_phishing.py`**: Processes phishing URLs and adds them to the training dataset with label '1' (phishing).
- **`phishing_dataset.csv`**: Combined dataset used for model training.
- **`phishing_model.pkl`**: Serialized trained model file.

## Data Sources

### Legitimate URLs
- **Source**: [Kaggle - Majestic Million](https://www.kaggle.com/datasets/cheedcheed/top1m)
- **File**: `top-1m.csv`
- **Description**: Top 1 million legitimate websites

### Phishing URLs
- **Source**: [UCI Machine Learning Repository - Phishing URL Dataset](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)
- **File**: `PhiUSIIL_Phishing_URL_Dataset.csv`
- **Description**: Collection of known phishing URLs

## Requirements

```txt
Flask
pandas
scikit-learn
joblib
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd phishing-url-detection
   ```

2. **Install dependencies**
   ```bash
   pip install Flask pandas scikit-learn joblib
   ```
   
   Or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Setup and Usage

### 1. Prepare Data

Download the required datasets:
- Download `top-1m.csv` from [Kaggle - Majestic Million](https://www.kaggle.com/datasets/cheedcheed/top1m)
- Download `PhiUSIIL_Phishing_URL_Dataset.csv` from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)

Place both files in the project directory.

Process the datasets:
```bash
# Add legitimate URLs to training dataset
python convert.py

# Add phishing URLs to training dataset
python convert_phishing.py
```

### 2. Train the Model

Train the machine learning model:
```bash
python model_training.py
```

This generates `phishing_model.pkl` containing the trained model.

### 3. Run the API

Start the Flask application:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

### 4. Make Predictions

Send POST requests to the `/predict` endpoint:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"url": "http://example.com/suspicious-site"}' \
  http://127.0.0.1:5000/predict
```

**Response format:**
```json
{
  "prediction": "phishing",  // or "safe"
  "url": "http://example.com/suspicious-site"
}
```

## Feature Engineering

The model uses the following features extracted from URLs:

| Feature | Description |
|---------|-------------|
| `url_length` | Total length of the URL |
| `has_https` | Binary indicator for HTTPS usage (1 = HTTPS, 0 = HTTP) |
| `has_login` | Binary indicator for "login" keyword presence |
| `has_at` | Binary indicator for "@" symbol presence |
| `has_dash` | Binary indicator for "-" symbol presence |
| `num_dots` | Count of "." (dots) in the URL |

## API Endpoints

### POST /predict

Classifies a URL as phishing or safe.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "prediction": "safe",
  "url": "https://example.com"
}
```

## Model Performance

The RandomForestClassifier is trained on a combination of legitimate and phishing URLs, providing robust classification performance for URL safety assessment.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Disclaimer

This tool is for educational and research purposes. Always verify results with additional security measures in production environments.
