import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def extract_features(url):
    return {
        'url_length': len(url),
        'has_https': int('https' in url),
        'has_login': int('login' in url),
        'has_at': int('@' in url),
        'has_dash': int('-' in url),
        'num_dots': url.count('.'),
    }

def main():
    # CSV'yi okuyoruz (header yok)
    data = pd.read_csv('phishing_dataset.csv', header=None, names=['url', 'label'], on_bad_lines='skip')

    # Label sadece 0 veya 1 olanları tut
    data = data[data['label'].isin([0, 1])]

    # URL sütununu string yap
    data['url'] = data['url'].astype(str)

    # Feature extraction
    features = data['url'].apply(extract_features).apply(pd.Series)
    X = features
    y = data['label']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model eğitimi
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Tahmin ve rapor
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Model kaydetme
    joblib.dump(model, 'phishing_model.pkl')
    print("Model saved: phishing_model.pkl")

if __name__ == "__main__":
    main()
