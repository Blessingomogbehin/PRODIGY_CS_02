#Program to perform image encryption and decryption using pixel manipulation
from PIL import Image #this will open the pillow library

def encrypt_image(image_path):

    img = Image.open(image_path) #to open image


    pixels = img.load()
    width, height = img.size

    for  x in range(width):
     for y in range(height):
        pixel_value = pixels[x, y]
        if len(pixel_value) >= 3:
            r, g, b = pixel_value[:3]  # Extract RGB values

            pixels[x, y] = (b, g, r)   # this will swap red and blue channels

    img.save("encrypted_image.png") #To save the encrypted image in the python folder
    print("The image task 2.png has been encrypted and saved successfully!")

def decrypt_image(image_path):
    # Open the encrypted image
    img = Image.open(image_path)

    # Get the pixel data
    pixels = img.load()
    width, height = img.size

    # Decrypt the image by swapping pixel values (reversing the encryption)
    for x in range(width):
        for y in range(height):
            pixel_value = pixels[x, y]
            if len(pixel_value) >= 3:  # Ensure at least 3 values
                r, g, b = pixel_value[:3]  # Extract RGB values
                # Example decryption: swapping red and blue channels back
                pixels[x, y] = (b, g, r)

    img.save("decrypted_image.png") # this will save the decrypted version of image task 2.png
    print("Image decrypted successfully!")

def main():
    image_path = "task 2.png"

    # Encrypt the image
    encrypt_image(image_path)

    # Decrypt the encrypted image
    decrypt_image("encrypted_image.png")

if __name__ == "__main__":
    main()