red = int(input())
green = int(input())
blue = int(input())

rgb = [red, green, blue]

min_rgb = min(rgb)

new_red = red - min_rgb
new_green = green - min_rgb
new_blue = blue - min_rgb


print(new_red, new_green, new_blue)

 
    