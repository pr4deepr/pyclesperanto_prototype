

from ..core import execute


def dilate_box (src, dst):
    """Computes a binary image with pixel values 0 and 1 containing the binary dilation of a given input image.
    
    The dilation takes the Moore-neighborhood (8 pixels in 2D and 26 pixels in 3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be interpreted as 1.
    
    This method is comparable to the 'Dilate' menu in ImageJ in case it is applied to a 2D image. The only
    difference is that the output image contains values 0 and 1 instead of 0 and 255.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_dilateBox


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'dilate_box_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

