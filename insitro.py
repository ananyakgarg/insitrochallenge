from dataclasses import dataclass
from typing import List
import numpy as np
@dataclass
class Image:
    """
    A 2-dimensional image taken on a well.
    Attributes
    ----------
    data : np.array, shape=(n, m)
    A 2D array of values corresponding to each pixel.
    This could represent a pixel intensity.
    x_origin : int
    The origin of this image along the x-axis of a well.
    y_origin : int
    The origin of this image along the y-axis of a well.
    pixel_size : int
    The size of each pixel. Pixels are always square but
    different images may be taken at different resolutions.
    """
    data: np.array
    x_origin: int
    y_origin: int
    pixel_size: int = 1
@dataclass
class Region:
    """
    A rectangular region within a well.
    Attributes
    ----------
    x : int
    The starting x-coordinate of the region.
    y : int
    The starting y-coordinate of the region.
    width : int
    The width of the region (space occupied along the x-axis).
    height : int
    The height of the region (space occupied along the y-axis).
    """
    x: int
    y: int
    width: int
    height: int
def load_image(filepath: str) -> Image:
    """
    Loads an image from a file.
    Custom image format:
    line1: x_origin
    line2: y_origin
    line3: pixel_size
    remaining lines: comma separated rows of pixel values
    """
def get_images_overlapping_region(
images: List[Image],
region: Region,
) -> List[Image]:
    """
    Returns a list of Images overlapped by the specified `region`.
    """