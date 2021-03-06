two_dim = "data/blobs.tif"
three_dim = "data/t1-head.tif"

from skimage import io
import napari
import clesperanto as cle
from magicgui import magicgui  # https://magicgui.readthedocs.io/en/latest/
from napari.layers import Image
from enum import Enum
from functools import partial

#image_2d = io.imread(two_dim)
image_3d = io.imread(three_dim)

# Using Enums for getting a dropdown menu
# clesperanto functions are not being passed as enum values for some reason, so they are defined as strings
class gpu_filter(Enum):
    # using pyclesperanto filtering images with a gpu
    #using functools.partial to return functions as enum values:
    #https://stackoverflow.com/questions/40338652/how-to-define-enum-values-that-are-functions
    mean = partial(cle.minimum_sphere)
    maximum = partial(cle.maximum_sphere)
    minimum = partial(cle.minimum_sphere)
    top_hat = partial(cle.top_hat_sphere)
    gaussian_blur = partial(cle.gaussian_blur)
    crop = partial(cle.crop)

    #define the call method for the functions or it won't return anything
    def __call__(self, *args):
        return self.value(*args)


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(image_3d, name='3D_image_orig')
    #viewer.add_image(image_2d, name='2D_image_orig')


    # use auto_call=True for instantaneous execution
    # can add sliders using QSlider, but need to show values
    @magicgui(auto_call=True)#, call_button='Compute')
    def clij_filter(input: Image, operation: gpu_filter, x: float = 0, y: float = 0,
                    z: float = 0) -> Image:
        if input:
            cle_input = cle.push_zyx(input.data)
            operation = operation
            output = cle.create_like(cle_input)
            operation(cle_input, output, x, y, z)

            output = cle.pull_zyx(output)
            return output


    # use of magic_gui also passes an attribute to clij_operation  "called"
    # def print_shape(image):
    # print('Output image shape ', image.shape)

    gui = clij_filter.Gui()
    viewer.window.add_dock_widget(gui)
    # if a layer gets added or removed, refresh the dropdown choices
    viewer.layers.events.changed.connect(lambda x: gui.refresh_choices("input"))

    # clij_operation.called.connect(print_shape)
