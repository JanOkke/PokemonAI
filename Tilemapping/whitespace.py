from PIL import Image

path = r'output.png'
#print("Making file transparent\n", path, sep="")
img: Image.Image
img = Image.open(path)
#img = Image.open(r'C:\Users\Jan-Okke\Desktop\stuff\Pokemon DarkGold\Pokemon SoulSilver Essentials by JanOkke\Graphics\Trainers\trainer073.png')
img = img.convert("RGBA")

size = img.size
datas = img.getdata()
length = (len(datas))
print("Total size of rgbs:", length)

def num_to_iter(num, _size=size):
    x = num % size[1]
    y = int((num-x) / size[1])
    x += 1
    y += 1
    #print(x, y)
    return x, y

def whitespace_area(xs, xe, ys, ye):
    newData = []
    counter = 0
    for item in datas:
        # top left to bottom right
        x, y = num_to_iter(counter)

        if xs <= x <= xe and ys <= y <= ye:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
        counter += 1
        if counter % 100000 == 0:
            print(round(counter/length*100), '%')
    print("Saving...")
    img.putdata(newData)
    img.save(path, 'PNG')
    print("Finished.")

def whitespace_color(r, g, b):

    newData = []
    counter = 0
    for item in datas:
        if item[0] == r and item[1] == g and item[2] == b:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
        counter += 1
        if counter % 100000 == 0:
            print(round(counter/length*100), '%')
    print("Saving...")
    img.putdata(newData)
    img.save(path, 'PNG')
    print("Finished.")

def whitespace_color_allow(r, g, b, allowing=10):

    newData = []
    counter = 0
    for item in datas:
        if r-allowing <= item[0] <= r+allowing and g-allowing <= item[1] <= g+allowing and b-allowing <= item[2] <= b+allowing:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
        counter += 1
        if counter % 100000 == 0:
            print(round(counter/length*100), '%')
    print("Saving...")
    img.putdata(newData)
    img.save(path, 'PNG')
    print("Finished.")

#img.save(r'C:\Users\Jan-Okke\Desktop\stuff\Pokemon DarkGold\Pokemon SoulSilver Essentials by JanOkke\Graphics\Trainers\trainer073.png', 'PNG')
#whitespace_area(1,192,1,20)
#whitespace_color(160, 248, 152)
#whitespace_color(76, 241, 146)
#whitespace_color(76, 242, 140)
#whitespace_color(80, 248, 144)
#whitespace_color(97, 248, 155)
#whitespace_color(76, 232, 109)
#whitespace_color(114, 176, 106)
#whitespace_color(112, 176, 104)
#whitespace_color(146, 247, 152)
#whitespace_color(130, 202, 121)
#whitespace_color(78, 226, 104)
#whitespace_color(80, 246, 135)
depth=25
whitespace_color_allow(80, 246, 135, depth)
whitespace_color_allow(154, 248, 152, depth)
whitespace_color_allow(110, 173, 102, depth)
whitespace_color_allow(108, 249, 153, depth)
whitespace_color_allow(106, 184, 122, depth)
whitespace_color_allow(76, 208, 100, depth)
whitespace_color_allow(70, 213, 127, depth)
whitespace_color_allow(84, 166, 94, depth)
whitespace_color_allow(67, 105, 86, depth)
whitespace_color_allow(138, 165, 128, depth)
whitespace_color_allow(138, 218, 128, depth)
whitespace_color_allow(49, 206, 96, depth)
whitespace_area(1, 192, 1, 18)