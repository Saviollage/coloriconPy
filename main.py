from PIL import Image
import sys


if __name__ == "__main__":
    if(len(sys.argv) < 4):
        print("Please provide a name, color (RGB), output")
        
    imageName = sys.argv[1]
    color = sys.argv[2].split(',')
    output = sys.argv[3]
    picture = Image.open(imageName).convert('RGBA')

    for x in range(picture.size[0]):
        for y in range(picture.size[1]):
            current_color = picture.getpixel( (x,y) )
            if current_color[3] > 0:
                picture.putpixel( (x,y), (int(color[0]),int(color[1]),int(color[2]), current_color[3]))

    picture.save("{}_{}.png".format(imageName[:-4], output))