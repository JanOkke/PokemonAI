from PIL import Image

mapname = 'Route 211'
readfile = r'C:\Users\Jan-Okke\Desktop\stuff\Pokemon DarkGold\Pokemon SoulSilver Essentials by JanOkke\TODO\Sinnoh\Routes' + '\\' + mapname + '.png'
outfile = r'C:\Users\Jan-Okke\Desktop\stuff\Pokemon DarkGold\Pokemon SoulSilver Essentials by JanOkke\Graphics\Tilesets\Generated_' + mapname + '.png'
print(readfile)
print(outfile)

map: Image.Image
map = Image.open(readfile)
print(map.size[0] * 2 / 32, map.size[1] * 2 / 32)

data = map.getdata()

leng = len(data)
print(leng)
print(256, int(leng/64))

new_im = Image.new('RGBA', [256, int(leng/64)])
data = new_im.getdata()

print(len(data))
def make():
    counter = 0
    for x in range(int(map.width/16)):
        for y in range(int(map.height/16)):
            box = (x-1)*16+16, (y-1)*16+16, x*16+16, y*16+16
            i = map.crop(box)#
            i = i.resize([32, 32])
            xpos = x*32 % 256
            ypos = y*32 + x*32 % 256 - x*32 + counter * 864
            print(xpos, ypos)
            new_im.paste(i, (xpos, ypos))
            if (ypos + 32) % 832 == 0 and xpos == 224:
                #print("YO")
                counter += 1


        #print(x, y)
make()
new_im.save(outfile, 'PNG')
