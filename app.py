from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('phishing_model.pkl')

def extract_features(url):
    return {
        'url_length': len(url),
        'has_https': int('https' in url),
        'has_login': int('login' in url),
        'has_at': int('@' in url),
        'has_dash': int('-' in url),
        'num_dots': url.count('.'),
    }

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL needed'}), 400

    features = extract_features(url)
    features_df = pd.DataFrame([features])
    prediction = model.predict(features_df)[0]

    if (prediction == 1):
        result = 'phishing'
    elif (prediction == 0):
        result = 'safe'
    else:
        result = 'not available'

    return jsonify({'url': url, 'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
