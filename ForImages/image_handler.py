from PIL import Image
from ForImages.image_processor import ImageProcessor
class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)
    def resize_image(self, size=(300, 300)):
        self.image = self.image.resize(size)
        print(f"Image resized to {size[0]}x{size[1]} pixels.")
    def save_image(self, filename="output.png"):
        self.image.save(filename, "PNG")
        print(f"Image saved as {filename}.")
    def process_image(self):
        processor = ImageProcessor(self.image)
        return processor