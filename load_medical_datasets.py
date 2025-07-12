import tensorflow_datasets as tfds

# Dictionary to store datasets
datasets = {}

# List of medical datasets
medical_datasets = [
    "malaria",
    "diabetic_retinopathy_detection",
    "chest_xray",
    "mimic_cxr",
    "patch_camelyon",
    "colorectal_histology"
]

# Load each dataset
for dataset_name in medical_datasets:
    try:
        dataset, info = tfds.load(dataset_name, with_info=True, as_supervised=True)
        datasets[dataset_name] = {
            "dataset": dataset,
            "info": info
        }
        print(f"Dataset {dataset_name} loaded successfully")
    except Exception as e:
        print(f"Error loading {dataset_name}: {e}")

# Example: Access a dataset
# for image, label in datasets['malaria']['dataset']['train'].take(1):
#     print(f"Malaria sample, label: {label}")
