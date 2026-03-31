# 🧠 Automatic Image Segmentation & Object Area Analysis (CLI-Based)

A Python-based command-line tool for automated image segmentation and object analysis using Computer Vision techniques.

## 📌 Overview

This project implements an **image segmentation and object analysis system** using OpenCV and NumPy. It processes input images, separates foreground objects from the background, and computes useful metrics such as:
- Number of objects detected
- Individual object areas (in pixels and percentage)
- Total foreground coverage

The entire system runs via the **Command Line Interface (CLI)**, making it lightweight, efficient, and deployable without any graphical interface.

## 🎯 Problem Statement

In real-world applications such as medical imaging, agriculture, and industrial inspection, identifying and analyzing objects within images is essential. Manual analysis is time-consuming and error-prone.

This project automates the process of **object detection and quantitative analysis using image segmentation techniques**.

## 🚀 Features

✅ Image segmentation using thresholding techniques  
✅ Detection of multiple objects in an image  
✅ Calculation of object areas (in pixels and percentage)  
✅ Total foreground coverage computation  
✅ CLI-based execution (no GUI required)  
✅ Lightweight and efficient  
✅ Easy integration and deployment  

## 🛠️ Tech Stack

- **Python** - Programming language
- **OpenCV** - Computer Vision library
- **NumPy** - Numerical computing library

## 📂 Project Structure

```
Automatic Image Segmentation & Object Area Analysis (CLI-Based)/
│
├── main.py              # Entry point of the CLI application
├── segmentation.py      # Handles image segmentation logic
├── analysis.py          # Performs object detection and area calculation
├── requirements.txt     # Python package dependencies
├── .gitignore          # Git ignore file
├── README.md           # Main documentation
│
└── images/
    └── README.md       # Images and additional documentation
```

## 📥 Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Riticaa/Automatic-Image-Segmentation-Object-Area-Analysis-.git
   cd "Automatic Image Segmentation & Object Area Analysis (CLI-Based)"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the CLI application with an image file:

```bash
python main.py --image <path_to_image>
```

### Example
```bash
python main.py --image sample_image.jpg
```

### Output
```
Total Objects Detected: 5

Object 1 Area: 1250 pixels (12.50%)
Object 2 Area: 2100 pixels (21.00%)
Object 3 Area: 950 pixels (9.50%)
Object 4 Area: 3200 pixels (32.00%)
Object 5 Area: 2500 pixels (25.00%)

Total Foreground Coverage: 100.00%
```

## 🔧 How It Works

### 1. Image Segmentation (`segmentation.py`)
- Converts the input image to grayscale
- Applies binary thresholding to create a mask
- Separates foreground objects from the background

### 2. Object Analysis (`analysis.py`)
- Detects contours in the segmented mask
- Calculates the area of each detected object
- Filters out noise (objects below 50 pixels)
- Computes percentage coverage

### 3. CLI Interface (`main.py`)
- Accepts command-line arguments for image path
- Orchestrates segmentation and analysis
- Displays formatted results to the user

## 📊 Key Functions

### `segment_image(image)`
Segments an image using thresholding.
- **Input:** BGR image (cv2 format)
- **Output:** Binary mask (foreground/background)

### `analyze_objects(mask)`
Analyzes objects in a binary mask.
- **Input:** Binary mask
- **Output:** List of object areas and total image area

## 🎓 Techniques Used

- **Binary Thresholding** - Separates foreground from background
- **Contour Detection** - Identifies object boundaries
- **Area Calculation** - Computes pixel-based areas
- **Percentage Calculation** - Determines coverage ratios

## 📋 Requirements

```
opencv-python==4.9.0.80
numpy==1.26.4
```

## 🔮 Future Enhancements

- [ ] Support for multiple thresholding techniques (Otsu, Adaptive)
- [ ] Object shape analysis (circularity, aspect ratio)
- [ ] Morphological operations (dilation, erosion)
- [ ] Batch processing of multiple images
- [ ] Output visualization with annotated images
- [ ] Export results to CSV/JSON format
- [ ] GUI interface alternative

## 📝 License

This project is open-source and available under the MIT License.

## 👤 Author

**Riticaa**  
📧 GitHub: [@Riticaa](https://github.com/Riticaa)

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## ❓ Frequently Asked Questions

**Q: What image formats are supported?**  
A: OpenCV supports most common formats (JPG, PNG, BMP, TIFF, etc.)

**Q: Can I process multiple images at once?**  
A: Currently, the CLI processes one image at a time. Batch processing is planned for future releases.

**Q: How does the thresholding work?**  
A: The tool uses binary thresholding with a fixed threshold value of 127. Adaptive thresholding support is planned.

**Q: What's the minimum object size threshold?**  
A: The current implementation ignores objects smaller than 50 pixels to filter out noise.

---

**Happy Segmenting! 🎯**
