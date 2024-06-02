import glob
import imagehash
from PIL import Image

boy_img_url = './boys/jj.jpg'
boy_hash = imagehash.average_hash(Image.open(boy_img_url))

j = glob.glob('./girls/*.jpg') 
selected = j[0]
accepted_diff = 500

for i in j:
  girl_hash = imagehash.average_hash(Image.open(i))
  diff = girl_hash - boy_hash
  if diff < accepted_diff:
    selected = i
    accepted_diff = diff

boy_img = Image.open(boy_img_url)
girl_img = Image.open(selected)

final_img = Image.new('RGB', (boy_img.width + girl_img.width, boy_img.height))
final_img.paste(boy_img, (0, 0))
final_img.paste(girl_img, (boy_img.width, 0))
final_img.save('Final_Frame.jpg')
final_img.show()