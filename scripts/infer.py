import argparse
from pathlib import Path
import joblib


def predict(text: str, model_dir: Path) -> str:
    vectorizer = joblib.load(model_dir / "tfidf_vectorizer.joblib")
    model = joblib.load(model_dir / "logreg_model.joblib")
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    return str(pred)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run inference on a single SMS text")
    parser.add_argument("--text", required=True, help="Input SMS text")
    parser.add_argument("--model-dir", default="models", help="Directory containing saved model")
    args = parser.parse_args()

    label = predict(args.text, Path(args.model_dir))
    print(label)


if __name__ == "__main__":
    main()



