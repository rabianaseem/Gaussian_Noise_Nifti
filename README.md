## Adding Gaussian noise to NIfTI images

## Requirements

- Python
- Nibabel

### Data

The code iterates over a directory containing NIfTI files (3D volumes) of medical images, adds Gaussian noise to the axial slice of each volume, 
and saves the noisy slices into a destination directory, maintaining the directory structure of the input files.
A sample CT volume 'CT_1' is provided as an example.

