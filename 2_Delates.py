from PIL import Image, ImageDraw
import os

def convert_to_transparent(input_path, output_path, threshold_distance, min_count):
    # Read the image
    image = Image.open(input_path)
    
    # Get image dimensions
    width, height = image.size
    
    # Create a new transparent image
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    # Create a drawing context
    draw = ImageDraw.Draw(new_image)
    
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            
            # Check if this pixel is black (assuming black is (0, 0, 0))
            if isinstance(pixel, int):
                pixel = (pixel, pixel, pixel, 255)
                
            if pixel[:3] == (0, 0, 0):
                # Create a counter for black pixels
                black_pixel_count = 0
                
                for i in range(-threshold_distance, threshold_distance + 1):
                    for j in range(-threshold_distance, threshold_distance + 1):
                        if 0 <= x + i < width and 0 <= y + j < height:
                            neighbor_pixel = image.getpixel((x + i, y + j))
                            
                            if isinstance(neighbor_pixel, int):
                                neighbor_pixel = (neighbor_pixel, neighbor_pixel, neighbor_pixel, 255)
                            
                            # Check if the neighbor pixel is also black
                            if neighbor_pixel[:3] == (0, 0, 0):
                                black_pixel_count += 1
                
                # If there are fewer than min_count black pixels in the vicinity, change the current pixel to white
                if black_pixel_count < min_count:
                    draw.point((x, y), fill=(255, 255, 255, 255))
                else:
                    draw.point((x, y), fill=pixel)
            else:
                draw.point((x, y), fill=pixel)
    
    new_image.save(output_path)
    
    new_image.save(output_path)

if __name__ == "__main__":
    input_path =  'Floor_1.png'
    output_path=  'Floor_1.png'
    
    # it is the sensitivity of the program
    threshold_distance = 4
    min_count = 9
    
    
            
    convert_to_transparent(input_path, output_path, threshold_distance, min_count)

