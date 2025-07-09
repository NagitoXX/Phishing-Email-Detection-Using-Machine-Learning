import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

if __name__ == "__main__":
    print("Loading phishing email dataset from Kaggle via kagglehub...")

    # Adjust the file name if the dataset uses a different one
    file_path = "phishing_emails.csv"

    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "naserabdullahalam/phishing-email-dataset",
        file_path,
    )

    print("First 5 records:")
    print(df.head())

    # Save the dataset locally for preprocessing and training
    output_path = "data/phishing_emails.csv"
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")
