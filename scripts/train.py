import argparse
from pathlib import Path
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def train_model(input_csv: Path, text_col: str, label_col: str, model_dir: Path) -> None:
    df = pd.read_csv(input_csv)
    texts = df[text_col].astype(str).tolist()
    labels = df[label_col].astype(str).tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        min_df=2,
        max_features=50000,
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    clf = LogisticRegression(max_iter=200, n_jobs=None)
    clf.fit(X_train_vec, y_train)

    y_pred = clf.predict(X_test_vec)
    print(classification_report(y_test, y_pred))

    model_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(vectorizer, model_dir / "tfidf_vectorizer.joblib")
    joblib.dump(clf, model_dir / "logreg_model.joblib")
    print(f"Saved vectorizer and model to: {model_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Train baseline smishing detector")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--text-col", required=True, help="Text column name")
    parser.add_argument("--label-col", required=True, help="Label column name")
    parser.add_argument("--model-dir", default="models", help="Directory to save model files")
    args = parser.parse_args()

    train_model(Path(args.input), args.text_col, args.label_col, Path(args.model_dir))


if __name__ == "__main__":
    main()


