from PIL import Image,ImageDraw,ImageFont
import glob,sys
import discord,json


def crop_max_square(pil_img):
    """
    画像の一番長い辺を元に正方形にクロップする関数
    Args:
        pil_img(ImageFile | Image): ベースとなる画像（Image.openなどの返り値）
    """
    def crop_center(pil_img:Image.Image, crop_width, crop_height)-> Image.Image:
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                            (img_height - crop_height) // 2,
                            (img_width + crop_width) // 2,
                            (img_height + crop_height) // 2))

    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

async def image_process(base_text:str,files:list):
    if not "\n" in base_text:
        base_text = f"{base_text[:14]}\n{base_text[14:]}"
    basic_font = 'C:/Windows/Fonts/BIZ-UDGothicB.ttc'
    img = Image.open('main.png')
    draw = ImageDraw.Draw(img)

    draw.text(
    (60, 160),
    base_text,
    font=ImageFont.truetype(basic_font, 60),
    fill='white',
    stroke_width=1,
    stroke_fill='white')
    xy = [
        (23,310),(412,310),(803,310),
        (23,699),(412,699),(803,699),
        (23,1088),(412,1088),(803,1088)
    ]
    img_list = []
    c = 0
    for f in files:
        await f.save(f"./img/{c}")
        c+=1
    for i in glob.glob("./img/*"):
        if not len(img_list) >= 9:
            img_list.append(i)
        else:
            break
    for i in range(len(img_list)):
        try:
            tmp_img = Image.open(img_list[i])
            tmp_img = crop_max_square(tmp_img)
            tmp_img = tmp_img.resize((367,367))
            img.paste(tmp_img,xy[i])
        except Exception as e:
            print(e)
            return
    img.save("result.png")