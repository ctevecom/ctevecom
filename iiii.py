import torch
import matplotlib.pyplot as plt
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load an image
image_path = "test2.jpg"  # Replace with your image path
image = Image.open(image_path).convert("RGB")

# Preprocess the image and generate caption
inputs = processor(images=image, return_tensors="pt")
with torch.no_grad():
    caption_ids = model.generate(**inputs)

# Decode the generated caption
caption = processor.batch_decode(caption_ids, skip_special_tokens=True)[0]

# Display the image with caption
plt.figure(figsize=(8, 6))
plt.imshow(image)
plt.axis("off")  # Hide axes
plt.title(caption, fontsize=14, color="blue")  # Display caption in blue
plt.show()
