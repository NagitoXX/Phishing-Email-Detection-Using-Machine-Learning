import kagglehub

if __name__ == "__main__":
    print("Downloading phishing email dataset from Kaggle...")
    path = kagglehub.dataset_download("naserabdullahalam/phishing-email-dataset")
    print("Dataset downloaded to:", path)
    print("Check the extracted files under this path and update preprocess.py if needed")
