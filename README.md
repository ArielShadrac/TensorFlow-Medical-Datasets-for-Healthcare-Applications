# TensorFlow Medical Datasets for Healthcare Applications

This repository provides a Python script to load medical datasets from **TensorFlow Datasets (TFDS)** in one go, designed for healthcare applications, particularly in resource-constrained environments like Burkina Faso, where internet connectivity is limited. These datasets are pre-downloaded and cached locally, enabling offline use for medical research, diagnostics, and education. This README includes a detailed overview of each dataset, its role, historical context, use cases, and size, along with a scientific vulgarization section to make the information accessible to all.

## Purpose

The script automates the loading of medical datasets from TFDS, storing them in a dictionary for easy access. This is especially valuable in areas with unreliable internet, such as rural Burkina Faso, where pre-downloading datasets ensures uninterrupted work in:
- **Diagnosis**: Developing AI tools for diseases like malaria or pneumonia.
- **Research**: Supporting studies in institutions like the CNRFP (Centre National de Recherche et de Formation sur le Paludisme) .
- **Education**: Training healthcare workers or students in AI-driven diagnostics.

## Medical Datasets in TensorFlow Datasets

Below is a comprehensive list of medical datasets available in TFDS, with details on their role, history, use cases, and size. These datasets are focused on medical imaging and diagnostics, relevant for healthcare challenges in contexts like Burkina Faso.

### 1. Malaria
- **Description**: Contains ~27,000 images of blood cells, labeled as parasitized (infected with malaria) or uninfected. Images are derived from microscope slides.
- **Size**: ~1 GB.
- **Role**: Enables training of machine learning models to detect malaria, a critical tool for rapid diagnosis in areas with limited access to expert pathologists.
- **Historical Context**: Sourced from a dataset created by the National Institutes of Health (NIH) in 2018, aimed at accelerating malaria diagnosis in low-resource settings .
- **Use Cases**:
  - **Burkina Faso**: Malaria is a leading cause of mortality, especially in rural areas. This dataset can train models for portable microscopes used in Centres de Santé et de Promotion Sociale (CSPS), enabling community health workers to diagnose malaria without lab infrastructure .
  - **Example**: A 2019 study used this dataset to train a convolutional neural network (CNN) achieving >95% accuracy in malaria detection, deployable on mobile devices .
  - **Global**: Used in telemedicine apps in sub-Saharan Africa to support remote diagnostics.
- **Key Info**: Images are 2D, typically 100x100 pixels. Requires preprocessing (e.g., normalization) for model training. Ideal for lightweight models like MobileNet, suitable for low-power devices in Burkina Faso.
- **Why It Matters**: In Burkina Faso, where malaria accounts for a significant portion of healthcare visits , this dataset supports fast, automated diagnosis, reducing reliance on scarce specialists.

### 2. Diabetic Retinopathy Detection
- **Description**: ~88,000 high-resolution retinal images labeled for diabetic retinopathy severity (no, mild, moderate, severe, proliferative).
- **Size**: ~35 GB.
- **Role**: Supports development of AI models to detect diabetic retinopathy, a diabetes complication causing blindness if untreated.
- **Historical Context**: Originated from a 2015 Kaggle competition by EyePACS, aimed at automating screening in regions with limited ophthalmologists .
- **Use Cases**:
  - **Burkina Faso**: Diabetes is rising in urban areas like Ouagadougou. This dataset can train models for screening in CHUs (Centres Hospitaliers Universitaires), where eye specialists are rare .
  - **Example**: A 2016 study used this dataset to train a deep learning model achieving 90% sensitivity in detecting severe retinopathy, deployed in Indian clinics .
  - **Global**: Used in automated screening tools in low-resource settings to prioritize patients for treatment.
- **Key Info**: Images are high-resolution (~3000x2000 pixels), requiring significant storage and preprocessing (resizing, augmentation). Best for high-performance systems, less practical for low-resource settings.
- **Why It Matters**: Early detection can prevent blindness, critical in Burkina Faso where access to eye care is limited .

### 3. Chest X-Ray
- **Description**: ~112,000 chest X-ray images labeled for conditions like pneumonia, labeled as normal or abnormal.
- **Size**: ~1 GB.
- **Role**: Enables training of models to detect lung conditions, such as pneumonia, which is critical in areas with high respiratory disease prevalence.
- **Historical Context**: Released by the NIH in 2017 to support AI-driven radiology in resource-constrained settings .
- **Use Cases**:
  - **Burkina Faso**: Pneumonia is a major cause of child mortality. This dataset can train models for portable X-ray devices in CHUs or mobile clinics run by NGOs like Médecins du Monde .
  - **Example**: A 2018 study used this dataset to train a CNN for pneumonia detection, achieving 92% accuracy, deployable in rural hospitals .
  - **Global**: Used in telemedicine platforms for remote radiology analysis.
- **Key Info**: Images are ~1024x1024 pixels. Requires preprocessing (e.g., normalization, resizing). Suitable for lightweight models like MobileNet.
- **Why It Matters**: In Burkina Faso, where radiology equipment is scarce outside major cities, this dataset supports portable diagnostic tools .

### 4. MIMIC-CXR
- **Description**: ~377,000 chest X-ray images with associated radiology reports, labeled for multiple conditions (e.g., pneumonia, heart failure).
- **Size**: ~200 GB.
- **Role**: Supports advanced medical imaging research, combining image analysis with natural language processing (NLP) of radiology reports.
- **Historical Context**: Part of the MIMIC database from MIT, released in 2019 to advance AI in medical imaging and clinical decision-making .
- **Use Cases**:
  - **Burkina Faso**: Useful for research at institutions like the INSP (Institut National de Santé Publique), but its size limits practical deployment in rural CSPS .
  - **Example**: A 2020 study used MIMIC-CXR to train a multi-task model for disease detection and report generation, used in academic research .
  - **Global**: Used in hospitals with advanced infrastructure for automated radiology reporting.
- **Key Info**: Requires significant storage and computational resources. Includes both images and text, making it complex for preprocessing.
- **Why It Matters**: Provides a rich dataset for research, but less practical for immediate deployment in Burkina Faso due to size and infrastructure needs.

### 5. PatchCamelyon (PCam)
- **Description**: ~327,000 histopathology images of lymph node sections, labeled for breast cancer metastases (benign vs malignant).
- **Size**: ~7 GB.
- **Role**: Enables training of models to detect cancer metastases, critical for early cancer diagnosis.
- **Historical Context**: Released in 2018 as part of a challenge to improve cancer detection in pathology .
- **Use Cases**:
  - **Burkina Faso**: Cancer diagnosis is limited, but this dataset could support research at the CNRFP or training in CHUs for future oncology programs .
  - **Example**: A 2019 study used PCam to train a CNN achieving 89% accuracy in metastasis detection, used in pathology labs .
  - **Global**: Used in automated pathology tools to assist pathologists.
- **Key Info**: Images are 96x96 pixels, suitable for lightweight models. Requires preprocessing for augmentation and normalization.
- **Why It Matters**: Cancer is an emerging issue in Burkina Faso, and this dataset supports research to build future diagnostic capacity .

### 6. Colorectal Histology
- **Description**: ~5,000 histopathology images of colorectal tissues, labeled for tissue types (e.g., tumor, healthy, stroma).
- **Size**: ~100 MB.
- **Role**: Supports classification of colorectal cancer tissues, aiding in cancer diagnosis and research.
- **Historical Context**: Released in 2016 as part of a medical imaging challenge to improve automated histology analysis .
- **Use Cases**:
  - **Burkina Faso**: Limited histopathology infrastructure makes this dataset more suited for research at institutions like the CNRFP .
  - **Example**: A 2017 study used this dataset to train a model for colorectal cancer classification, achieving 87% accuracy .
  - **Global**: Used in pathology labs for automated tissue analysis.
- **Key Info**: Small size (~100 MB) makes it accessible for low-resource systems. Images are 150x150 pixels.
- **Why It Matters**: Its small size makes it practical for research in resource-constrained settings, though limited by lack of histopathology equipment.

## Script to Load Medical Datasets

The following script loads all the medical datasets listed above in one go, caching them locally for offline use, critical in areas like Burkina Faso with limited connectivity.

```python
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
```

## Where Are the Datasets Stored?
- **Location**: Stored locally in:
  - **Linux/macOS**: `~/tensorflow_datasets/`
  - **Windows**: `%USERPROFILE%\tensorflow_datasets\`
- **Format**: TFRecord files with metadata, optimized for TensorFlow.
- **Sizes**:
  - `malaria`: ~1 GB
  - `diabetic_retinopathy_detection`: ~35 GB
  - `chest_xray`: ~1 GB
  - `mimic_cxr`: ~200 GB
  - `patch_camelyon`: ~7 GB
  - `colorectal_histology`: ~100 MB
- **Total Storage**: ~244 GB for all datasets, with `colorectal_histology` and `malaria` being the most accessible for low-resource systems.
- **Offline Use**: Once downloaded, datasets are cached locally, enabling offline work in rural Burkina Faso, where internet is unreliable .

## Why Loading All Datasets Isn’t Always Necessary
- **Resource Constraints**: Datasets like `mimic_cxr` (~200 GB) and `diabetic_retinopathy_detection` (~35 GB) require significant storage, which may be impractical on low-capacity systems common in Burkina Faso’s CSPS or rural clinics .
- **Relevance**: For projects focused on malaria, only the `malaria` dataset is needed. Datasets like `mimic_cxr` or `colorectal_histology` are less relevant due to limited radiology or histopathology infrastructure .
- **Download Time**: In areas with slow internet, downloading large datasets like `mimic_cxr` can take days, making selective downloading more practical.
- **Preprocessing Needs**: Each dataset requires specific preprocessing (e.g., resizing images for `diabetic_retinopathy_detection`), which can be complex if loading all datasets without a clear plan.

## Scientific Vulgarization: Why These Datasets Matter
**What is this about?**  
These datasets are like digital libraries of medical images—think microscope slides of blood cells, X-rays of lungs, or retina scans. They help computers learn to spot diseases like malaria, pneumonia, or cancer by analyzing patterns in these images, just like a doctor would. This is especially important in places like Burkina Faso, where there aren’t enough doctors or labs, especially in rural areas.

**Why is it useful?**  
- **Malaria**: In Burkina Faso, malaria is a major problem, especially for kids. The `malaria` dataset teaches computers to look at blood samples and say, “This person has malaria!” This can help nurses in small clinics diagnose patients faster, even without a specialist .
- **Pneumonia**: The `chest_xray` dataset helps computers spot lung infections in X-rays, which is vital for kids in areas where pneumonia is common but X-ray machines are rare .
- **Cancer and Diabetes**: Datasets like `diabetic_retinopathy_detection` and `patch_camelyon` help detect eye damage from diabetes or breast cancer, which are growing issues in cities like Ouagadougou. These tools can save lives by catching problems early .
- **Research**: Datasets like `mimic_cxr` and `colorectal_histology` are used by researchers to build better AI tools, which could one day help Burkina Faso’s hospitals .

**How does it work?**  
The script downloads these datasets to your computer, so you can use them even without internet—a big deal in rural Burkina Faso, where network coverage is spotty . You can then use these datasets to train AI models, like teaching a computer to recognize malaria in a blood sample. Once downloaded, the data stays on your computer, ready for use anytime.

**Why not download everything?**  
Some datasets are huge (like `mimic_cxr`, which is 200 GB—bigger than most computer hard drives in rural clinics!). If you’re only working on malaria, you only need the `malaria` dataset (~1 GB). Downloading only what you need saves time and space, especially in places with limited tech resources .

**What’s next?**  
In Burkina Faso, these datasets can be used to build tools for clinics, train health workers, or support research at places like the CNRFP. For example, a mobile app using the `malaria` dataset could help nurses diagnose malaria in villages without internet .

## Recommendations for Burkina Faso
- **Prioritize `malaria` and `chest_xray`**: These are small (~1 GB each) and directly address major health issues (malaria, pneumonia) .
- **Download in Urban Areas**: Use a stable connection in Ouagadougou to download datasets, then transfer them to rural areas via external drives.
- **Use Lightweight Models**: Pair these datasets with models like MobileNet (from your previous script) for deployment on low-power devices .
- **Collaborate Locally**: Work with the CNRFP or INSP to adapt datasets to local needs, e.g., combining `malaria` with local blood sample data .

## Prerequisites
- Python 3.6+
- TensorFlow (`pip install tensorflow`)
- TensorFlow Datasets (`pip install tensorflow-datasets`)
- Internet connection for initial download
- Storage: ~244 GB for all datasets, but `malaria` (~1 GB) and `colorectal_histology` (~100 MB) are most feasible for low-resource systems.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ArielShadrac/TensorFlow-Medical-Datasets-for-Healthcare-Applications.git
   cd TensorFlow-Medical-Datasets-for-Healthcare-Applications
   ```
2. Install dependencies:
   ```bash
   pip install tensorflow tensorflow-datasets
   ```

## Usage
1. Run the script to download and cache datasets:
   ```bash
   python load_medical_datasets.py
   ```
2. Access datasets offline via the `datasets` dictionary:
   ```python
   for image, label in datasets['malaria']['dataset']['train'].take(1):
       print(f"Malaria sample, label: {label}")
   ```

## Troubleshooting
- **Module Not Found**: Ensure TensorFlow and TFDS are installed (`pip install tensorflow tensorflow-datasets`).
- **Storage Errors**: Check available disk space (use `colorectal_histology` or `malaria` for low storage).
- **Download Issues**: Run the script in a stable internet area (e.g., Ouagadougou) to cache datasets.
- **Compatibility**: Use TensorFlow >=2.6 for compatibility.
