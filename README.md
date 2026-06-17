# Raster Data Reading Utilities

A lightweight Python toolkit for reading geospatial raster data products, including HDF and HLS GeoTIFF files. The repository provides convenient functions for loading image data and extracting associated spatial metadata.

---

## Repository Structure

```text
.
├── read_hdf.py
├── read_hls_tif.py
├── slides.py
└── README.md
```

### Files

| File              | Description                                                                     |
| ----------------- | ------------------------------------------------------------------------------- |
| `read_hdf.py`     | Read all subdatasets from an HDF file and return the data and spatial metadata. |
| `read_hls_tif.py` | Read HLS GeoTIFF files and extract raster data and georeferencing information.  |
| `slides.py`       | create powerpoint slides for given jpegs.                                       |
| `README.md`       | Repository documentation.                                                       |

---

## Features

### read_hdf.py

* Reads all HDF subdatasets automatically.
* Returns subdataset contents as NumPy arrays.
* Extracts:

  * Raster dimensions
  * Projection information
  * Geotransform parameters
* Supports HDF products commonly used in remote sensing applications.

### read_hls_tif.py

* Reads HLS GeoTIFF imagery.
* Supports multi-band raster data.
* Extracts geospatial metadata.
* Returns image arrays suitable for further analysis and visualization.

---

## Requirements

Install the required Python packages:

```bash
pip install numpy
pip install gdal
pip install python-pptx
```


---

## Example: Read an HDF File

```python
from read_hdf import read_hdf

data, x_size, y_size, projection, geotransform = read_hdf(
    "example.hdf"
)

print(data.keys())
print(x_size, y_size)
```

### Access a Subdataset

```python
data = data["burn_date"]
```

---

## Example: Read an HLS GeoTIFF

```python
from read_hls_tif import read_hls_tif

data, projection, geotransform = read_hls_tif(
    "HLS.S30.T18TYM.2024001.v2.0"
)
```

---

## Returned Metadata

### Projection

The projection is returned as a GDAL Well-Known Text (WKT) string:

```python
print(projection)
```

### Geotransform

The geotransform contains:

```text
(
    top_left_x,
    pixel_width,
    rotation_x,
    top_left_y,
    rotation_y,
    pixel_height
)
```

Example:

```python
print(geotransform)
```

---

## Applications

These utilities are useful for:

* Harmonized Landsat Sentinel-2 (HLS) products
* MODIS HDF products
* Remote sensing workflows
* Raster visualization
* Machine learning preprocessing
* Geospatial data analysis

---

## Author

Haiyan Huang


---

## License

This repository is provided for research and educational purposes.
