from PIL import Image, ImageDraw, ImageFont
from random import randint

class MemeEngine():
    def __init__(self, output_dir) -> None:
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str: 
        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        
        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            caption = f'{text}\n - {author}'
            draw.text((10, 30), caption, font=font, fill='white')

        out_path = f'{self.output_dir}/{randint(0,10000)}.jpeg'
        img.save(out_path)
        return out_path