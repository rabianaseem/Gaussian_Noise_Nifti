import os
import nibabel as nib
import numpy as np
import glob

# Specify input and output directories
input_path ='C:\\Users\\user1\\data\\'
output_path= 'C:\\Users\\user1\\Destination\\'

# Get a list of all NIfTI files in the input directory
image_filenames = sorted(glob.glob(input_path + '**/*.nii', recursive=True))

# Iterate over each NIfTI file
for img in image_filenames:
    # Create a directory for storing noisy images
    filename = os.path.basename(img)
    filename = os.path.splitext(filename)[0]
    path1 = os.path.splitext(filename)[0]
    pp = os.path.join(output_path, path1)

    # Check if directory already exists
    if not os.path.exists(pp):
        os.makedirs(pp)

        # Load the NIfTI file
        medical_image = nib.load(img)
        image = medical_image.get_fdata()

        for i in range(image.shape[2]):
            axial_image = image[:, :, i]
            row, col = axial_image.shape

            # Add Gaussian noise to each axial slice
            mean = 0
            var = 0.5  # Adjust variance as needed
            sigma = var ** 0.1
            gauss = np.random.normal(mean, sigma, (row, col))
            gauss = gauss.reshape(row, col)
            noise = np.random.normal(loc=0, scale=2, size=axial_image.shape)
            noisy = axial_image * (1 + noise * 0.1)

            # Save the noisy slice as a NIfTI file
            noisy_image = nib.Nifti1Image(noisy, np.eye(4))
            nib.save(noisy_image, os.path.join(pp, f'{i}.nii'))
    else:
        print(f"Directory '{pp}' already exists. Skipping...")