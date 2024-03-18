import os
import cv2

def resize_images_in_directory(input_dir, output_dir, new_width, new_height):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)

    # Loop through each file in the input directory
    for file_name in files:
        # Check if the file is an image
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp', 'JPG', 'JPEG')):
            # Read the image
            image_path = os.path.join(input_dir, file_name)
            img = cv2.imread(image_path)

            # Resize the image
            resized_img = cv2.resize(img, (new_width, new_height))

            # Write the resized image to the output directory
            output_path = os.path.join(output_dir, file_name)
            cv2.imwrite(output_path, resized_img)

            print(f"Resized {file_name} and saved to {output_path}")

# Example usage
input_directory = "video_output_cropped"
output_directory = "resize_output_cropped"
new_width = 640
new_height = 640

resize_images_in_directory(input_directory, output_directory, new_width, new_height)
