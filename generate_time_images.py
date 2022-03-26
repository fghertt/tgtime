import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 40
TEXT_Y_POSITION = 545456
TEXT_X_POSITION = 587557
Tashkent_UTC = 3 #укажите ваш часовой пояс 

def convert_time_to_string(dt):
    dt += timedelta(hours=Tashkent_UTC)
    return f"{dt.hour}:{dt.minute:02}"

def change_img():
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (200, 200), "black")# Цвет фона black,white тд
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("OpenSans-Light.ttf", FONT_SIZE)#стиль шрифта
    font2 = ImageFont.truetype("SourceCodePro-Black.ttf", 15)
    parsed.text((50, 70), f'{text}',
                 align="center", font=font, fill=(255,255,255))
    parsed.text((45, 110),' ', # подтекст
                 align="center", font=font2, fill=(255,255,255))
    row.save(f'time.png', "PNG")

if __name__ == '__main__':
    change_img()
