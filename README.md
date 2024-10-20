# AI Object Detection Microservice

## Project Overview

This project provides a microservice for **object detection** using the YOLOv5 model. It is composed of two key services:
- **UI Backend Service**: The frontend interface for uploading images and displaying object detection results.
- **AI Backend Service**: The backend AI service responsible for running object detection using the YOLOv5 model, detecting objects in images, and returning both processed images (with bounding boxes) and corresponding JSON files containing detected objects' data.

This project is designed to be deployed using **Docker** for easy setup and scalability. It is an ideal solution for developers looking to integrate object detection capabilities into their applications.

## Use Cases
- **Image Processing Applications**: Detect and classify objects in images for real-time applications.
- **Surveillance Systems**: Automatically detect and track objects of interest in security footage.
- **Retail**: Use object detection for inventory management, product tracking, and customer analytics.
- **Healthcare**: Detect medical conditions or instruments in medical imaging.

## Technologies Used
- **YOLOv5** for object detection
- **Flask** as the web framework
- **Docker** for containerization
- **OpenCV** for image processing
- **PyTorch** for loading and running the YOLOv5 model

## Features
- **Object Detection**: Upload an image, and the service will detect objects in the image and return a bounding-box annotated version.
- **JSON Output**: Receive a JSON file with details about each detected object (e.g., object class, confidence score, bounding box coordinates).

---

## Installation and Setup

### Prerequisites
Before you begin, make sure you have the following installed on your system:
- **Docker** and **Docker Compose**
- **Python 3.8+**
- **Pip** package manager

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/object-detection-microservice.git
cd object-detection-microservice

#### 2. Set Up the Virtual Environment 
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#### 3. Install Dependencies
pip install -r requirements.txt

#### 4. Run with Docker
docker-compose up --build

#### 5. Access the Application
http://localhost:5000
