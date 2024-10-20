import easyocr
import pyttsx3
from PIL import Image

# Path to the image file
image_path = r'C:\Users\chethan kotian\Downloads\WhatsApp Image 2024-07-12 at 12.19.16_ae6531e9.jpg'

# Function to perform OCR on the image and return detected text
def detect_text_and_speak(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])  # Replace 'en' with your language code if different

    # Open the image file
    img = Image.open(image_path)

    # Perform OCR on the image
    result = reader.readtext(img)

    # Extract text from the result
    text = ' '.join([entry[1] for entry in result])

    # Print detected text
    print("Detected Text:")
    print(text)

    # Speak the detected text
    speak_text(text)

# Function to speak the text using pyttsx3
def speak_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1.0)  # Volume 0-1

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Call the function to detect text and speak it
detect_text_and_speak(image_path)
