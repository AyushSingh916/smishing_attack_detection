import argparse
from pathlib import Path
import pandas as pd

try:
    from datasets import load_dataset
except Exception as exc:  # pragma: no cover
    raise RuntimeError("The 'datasets' package is required. Run: pip install datasets") from exc


def download_to_csv(dataset_name: str, split: str, output_csv: Path) -> None:
    ds = load_dataset(dataset_name, split=split)
    df = pd.DataFrame(ds)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a dataset and save as CSV")
    parser.add_argument("--dataset", required=True, help="HuggingFace dataset id, e.g., MOZNLP/MOZ-Smishing")
    parser.add_argument("--split", default="train", help="split to load (default: train)")
    parser.add_argument("--out", required=True, help="output CSV path")
    args = parser.parse_args()

    output_csv = Path(args.out)
    download_to_csv(args.dataset, args.split, output_csv)
    print(f"Saved dataset '{args.dataset}' split '{args.split}' to: {output_csv}")


if __name__ == "__main__":
    main()



