# 🧠 Automatic Image Segmentation & Object Area Analysis (CLI-Based)

---

## 📌 Overview

This project implements an **image segmentation and object analysis system** using Computer Vision techniques. It processes input images, separates foreground objects from the background, and computes useful metrics such as the number of objects, their individual areas, and overall coverage.

The entire system runs via the **Command Line Interface (CLI)**, making it lightweight, efficient, and easy to deploy without any graphical interface.

---

## 🎯 Problem Statement

In many real-world applications such as medical imaging, agriculture, and industrial inspection, identifying and analyzing objects within images is essential. Manual analysis is time-consuming and prone to errors.

This project aims to automate the process of **object detection and quantitative analysis using image segmentation techniques**.

---

## 🚀 Features

* Image segmentation using thresholding techniques
* Detection of multiple objects in an image
* Calculation of object areas (in pixels and percentage)
* Total foreground coverage computation
* CLI-based execution (no GUI required)
* Supports multiple test images

---

## 🛠️ Tech Stack

* Python
* OpenCV
* NumPy

---

## 📂 Project Structure

```
image-segmentation-cli/
│
├── main.py                # Entry point of the application
├── segmentation.py       # Handles image segmentation
├── analysis.py           # Performs object detection and area calculation
├── utils/
│   └── preprocessing.py  # Optional preprocessing utilities
│
├── images/               # Folder containing input test images
│   ├── coins.jpg
│   ├── fruits.jpg
│   ├── shapes.png
│   └── cells.jpg
│
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🧩 Structure Explanation

### 🔹 `main.py`

* Handles command-line arguments
* Loads the input image
* Calls segmentation and analysis modules
* Displays results in the terminal

---

### 🔹 `segmentation.py`

* Converts image to grayscale
* Applies thresholding to separate foreground and background
* Produces a binary mask

---

### 🔹 `analysis.py`

* Detects contours (objects) in the segmented image
* Computes area for each detected object
* Filters out noise (very small regions)

---

### 🔹 `utils/preprocessing.py` (Optional)

* Contains helper functions for image enhancement
* Improves segmentation quality

---

### 🔹 `images/`

* Stores input test images used for evaluation
* Helps demonstrate performance on different datasets

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/image-segmentation-cli.git
cd image-segmentation-cli
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the Project

```
python main.py --image images/coins.png
```

---

## 💻 CLI Output Example

```
Total Objects Detected: 3

Object 1 Area: 1250 pixels (12.50%)
Object 2 Area: 980 pixels (9.80%)
Object 3 Area: 2100 pixels (21.00%)

Total Foreground Coverage: 43.30%
```

---

## 📊 Working Principle

1. Input image is loaded
2. Image is converted to grayscale
3. Thresholding is applied to create a binary mask
4. Contours are detected from the mask
5. Each contour is treated as an object
6. Area of each object is calculated
7. Results are printed in CLI

---

## 🧪 Test Images Used

The system was tested on multiple types of images:

* Coins on plain background
* Fruits on simple background
* Microscopic cell images

This ensures robustness and generalization of the approach.

---

## 🔥 Future Improvements

* Adaptive thresholding for better segmentation
* Color-based segmentation (HSV)
* Watershed algorithm for overlapping objects
* Export results to CSV file
* Integration with deep learning segmentation models

---

## ⚠️ Challenges Faced

* Handling varying lighting conditions
* Removing noise from segmented output
* Detecting overlapping objects accurately

---

## 📌 Conclusion

This project demonstrates the practical application of **image segmentation techniques in Computer Vision**. It provides an efficient and scalable solution for object detection and analysis using simple yet powerful methods.

---

## 👩‍💻 Author

* Ritica Awasthi

---

## 📜 License

This project is developed for academic and educational purposes.

