from PIL import Image,ImageDraw,ImageFont
import glob,sys

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

def image_process(base_text:str):
    if not "\n" in base_text:
        base_text = f"{base_text[:14]}\n{base_text[14:]}"
    basic_font = 'C:/Windows/Fonts/BIZ-UDGothicB.ttc'
    img = Image.open('main.png')
    font = ImageFont.truetype('C:/Windows/Fonts/BIZ-UDGothicB.ttc', 60) # フォントは自分で探してクレメンス宇ううううううううううううううううううううううううううううううううううううううううううううううううううううううううはんｒふぃうあｈんうぇるいがんれｗぎうあｒねういんごうあねｈふいあえｒがうんｇヴぃあえるｈんがれ
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
    for i in glob.glob("./img/*"):
        if not len(img_list) >= 9:
            img_list.append(i)
        else:
            break
    for i in range(len(img_list)):
        tmp_img = Image.open(img_list[i])
        tmp_img = crop_max_square(tmp_img)
        tmp_img = tmp_img.resize((367,367))
        img.paste(tmp_img,xy[i])
    img.save("result.png")
if __name__ == "__main__":
    if len(glob.glob("./img/*")) ==0:
        print("imgフォルダに画像が一枚も含まれていません。")
        sys.exit()
    text = input("テーマを入力 > ")
    image_process(base_text=text)