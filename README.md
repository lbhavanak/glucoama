# Glaucoma Detection Using Machine Learning

## Project Overview
This project detects glaucoma from retinal fundus images using Machine Learning. The system extracts retinal features and classifies the eye as either Normal or Glaucoma using a Support Vector Machine (SVM) model.

## Dataset
- REFUGE2 Retinal Fundus Image Dataset
- Normal Images: 360
- Glaucoma Images: 40

## Features Used
The following features were used for training:

- Mean Intensity
- Standard Deviation
- Cup Area
- Disc Area
- Cup-to-Disc Ratio (CDR)

## Machine Learning Model
- Algorithm: Support Vector Machine (SVM)
- Kernel: Linear
- Class Weight: Balanced

## Project Structure

```
GLUCOMA/
│
├── app.py
├── requirements.txt
├── README.md
│
├── datasets/
│   └── final_features.csv
│
├── models/
│   └── glaucoma_model.pkl
│
├── src/
│   ├── predict_image.py
│   ├── svm_model.py
│   └── calculate_cdr_from_mask.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│
└── uploads/
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd GLUCOMA
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Workflow

1. Upload retinal image
2. Extract retinal features
3. Generate feature vector
4. Apply trained SVM model
5. Predict:
   - Normal Eye
   - Glaucoma Detected

## Results

Example Outputs:

### Normal Eye
```
Uploaded File: n0001.jpg
Prediction: Normal Eye
```

### Glaucoma
```
Uploaded File: g0001.jpg
Prediction: Glaucoma Detected
```

## Accuracy

Model Accuracy:

```
78.75%
```

## Technologies Used

- Python
- Flask
- OpenCV
- NumPy
- Pandas
- Scikit-learn
- HTML
- CSS

## Future Improvements

- Deep Learning based detection
- Automatic optic cup/disc segmentation
- Real-time retinal image analysis
- Improved accuracy using CNN models

## Author

Karri Lakshmi Bhavana

B.Tech Student
Machine Learning Project