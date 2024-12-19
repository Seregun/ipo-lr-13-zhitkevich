from ForImages.image_handler import ImageHandler
from ForImages.image_processor import ImageProcessor

def main():
    image_path = input("Enter the path to the image (e.g., images/image.jpg): ")
    handler = ImageHandler(image_path)

    handler.resize_image()
    handler.save_image()

    processor = handler.process_image()
    processor.blur_image()
    processor.add_text()

    processor.image.show()

if __name__ == "__main__":
    main()