import easyocr   #optical text recognition
import cv2
# Initialize EasyOCR
reader = easyocr.Reader(['en'])
# Load the image
image = cv2.imread('book.jpg')
# Run OCR directly
results = reader.readtext(image)
# Display results
for (bbox, text, prob) in results:
    print(f"Detected Text: {text} (Probability: {prob})")

print(results)