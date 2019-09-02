from PIL import Image
import random

#testImage = Image.open( '/home/rizzo/Downloads/b4.jpg' )
#testImage.show()
#w = testImage.width
#h = testImage.height
#print("Image size is " + str(w) + "x" + str(h) + ".")

w = 200
h = 200

testImage2 = Image.new("RGB", (w,h), "black")
pixels = testImage2.load()
sample = open("test2")
#text = " What up my peeps"
text = ""

#Store file stream into variable
for c in sample:
    text = text + c

l = len(text)
sample.close()

#Access each letter, get char values and use for pixel colors 
i = 0
for y in range(h):
    for x in range(w):
        if i + 6 < l:
            pixel = testImage2.getpixel((x, y))
            rr = random.randint(1,255)
            gr = random.randint(1,255)
            br = random.randint(1,255)

            r = int(ord(text[i]) + ord(text[i+5]))
            g = int(ord(text[i+1]) + ord(text[i+4]))
            b = int(ord(text[i+2]) + ord(text[i+3]))
            #pixels[x, y] = ((1000+int(r))%255, int(g), int(b))
            #pixels[x, y] = (b+((rr*r)-gr%255), (g+(gr*br)-rr)%255, ((br*b)-rr%255))
            pixels[x, y] = (((rr+r)%gr)+int(b/2), ((gr+g)%br)+int(r/2), ((br+b)%rr)+int(g/2))
            i= i + 1


testImage2.show()
testImage2.save("linkedin2.png", "png")
