import os, glob, gdal, re,sys
import matplotlib.pyplot as plt
import numpy as np
from gdalconst import *
import scipy.ndimage
import glob
import numpy as np
from gdalconst import *
import scipy.ndimage

def read_hdf(filename):
     """
    Read all subdatasets from an HDF file into a dictionary.

    This function opens an HDF file using GDAL, reads each subdataset,
    and stores the contents in a dictionary keyed by the subdataset name.
    Spatial metadata, including image dimensions, projection, and
    geotransform, are extracted from the first subdataset.

    Parameters
    ----------
    filename : str
        Path to the input HDF file.

    Returns
    -------
    record : dict
        Dictionary containing the data from each subdataset. The keys
        are subdataset names extracted from the HDF metadata, and the
        values are NumPy arrays containing the corresponding data.

    x_size : int
        Number of columns (pixels) in the subdatasets.

    y_size : int
        Number of rows (pixels) in the subdatasets.

    projection : str
        Well-Known Text (WKT) projection string associated with the
        subdatasets.

    geotransform : tuple
        GDAL geotransform defining the spatial referencing of the
        subdatasets. The tuple contains:

        - Top-left x coordinate
        - Pixel width
        - Row rotation (typically 0)
        - Top-left y coordinate
        - Column rotation (typically 0)
        - Pixel height (typically negative)

    Raises
    ------
    RuntimeError
        If the HDF file cannot be opened by GDAL.

    Notes
    -----
    - The function assumes that all subdatasets share the same spatial
      dimensions and georeferencing information.
    - Metadata are extracted from the first subdataset.
    - Subdataset names are derived from the final component of the
      GDAL subdataset path.
    """

    hdf_dataset = gdal.Open(filename)

    subdatasets = hdf_dataset.GetSubDatasets()

    first_subdataset = gdal.Open(subdatasets[0][0])
    x_size = first_subdataset.RasterXSize
    y_size = first_subdataset.RasterYSize
    projection = first_subdataset.GetProjection()
    geotransform = first_subdataset.GetGeoTransform()

    
    record={}

    for i, subdataset_info in enumerate(subdatasets):
        subdataset_path = subdataset_info[0]  # Get the subdataset path

        tmpvar=subdataset_path.split(':')[-1]

        subdataset = gdal.Open(subdataset_path)

        data = subdataset.ReadAsArray()

        record[tmpvar]=data

    return record, x_size, y_size, projection,geotransform


if __name__=="__main__":

    filename='/mnt/research/sat.2/modis_fire/MOD664A1/MCD64A1.A2024306.h17v12.061.2025008010249.hdf'

    record, x_size, y_size, projection,geotransform=read_hdf(filename)


