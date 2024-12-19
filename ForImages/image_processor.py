from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def blur_image(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        print("Blur filter applied.")

    def add_text(self, text="Вариант 1", position=(20, 20), color="red", font_size=20):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", font_size)
        draw.text(position, text, fill=color, font=font)
        print(f"Text '{text}' added to the image at position {position}.")