from PIL import Image


def rotate_image(image_path, degrees_to_rotate, output_path):
    # Open the image file
    image = Image.open(image_path)

    # Rotate the image
    rotated_image = image.rotate(degrees_to_rotate)

    # Save the rotated image
    rotated_image.save(output_path)
    print("Image rotated and saved successfully!")


# Example usage:
input_image_path = "18.jpg"
output_image_path = "yolo_example.jpg"
degrees_to_rotate = 180

rotate_image(input_image_path, degrees_to_rotate, output_image_path)
