from PIL import Image

mapname = 'Eterna City'
readfile = r'C:\Users\Jan-Okke\Desktop\stuff\Pokemon DarkGold\Pokemon SoulSilver Essentials by JanOkke\TODO\Sinnoh' + '\\' + mapname + '.png'
#outfile = r'C:\Users\Jan-Okke\Desktop\stuff\Pokemon DarkGold\Pokemon SoulSilver Essentials by JanOkke\Graphics\Tilesets\Generated_' + mapname + '.png'
outfile = 'output.png'
print(readfile)
print(outfile)

map: Image.Image
map = Image.open(readfile)
print(map.size[0] * 2 / 32, map.size[1] * 2 / 32)

data = map.getdata()

leng = len(data)
print(leng)
#print(256, int(leng/64))


def cut(xs, xe, ys, ye):
    new_im = Image.new('RGBA', [(xe-xs) * 32 + 32, (ye-ys) * 32 + 32])
    data = new_im.getdata()
    print(len(data))
    for x in range(int(map.width/16)):
        for y in range(int(map.height/16)):
            box = (x-1)*16+16, (y-1)*16+16, x*16+16, y*16+16
            if xs <= x <= xe and ys <= y <= ye:
                i = map.crop(box)#
                i = i.resize([32, 32])
                new_im.paste(i, ((x-xs)*32,(y-ys)*32))
                #print(x-xs, y-ys)
                #print("In box")
    new_im.save(outfile, 'PNG')

        #print(x, y)
cut(37,40,9,14)