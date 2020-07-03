three_dim = "data/t1-head.tif"

from skimage import io
import napari
import clesperanto as cle
from magicgui import magicgui  # https://magicgui.readthedocs.io/en/latest/
from napari.layers import Image
from operator import methodcaller
import pkgutil


# image_2d = io.imread(two_dim)
image_3d = io.imread(three_dim)

# get path of clesperanto plugins folder
pth = cle.plugins.__path__[0]
#imports all packages in the clesperanto path
gpu_filter = list(pkgutil.walk_packages([pth]))  # returns package name
#generate a list of clesperanto filters
filter_list = []
for filters in gpu_filter:
    filter_list.append(filters[1])


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(image_3d, name='3D_image_orig')

    # use auto_call=True for instantaneous execution
    # can add sliders using QSlider, but need to show values
    @magicgui(auto_call=True, call_button='Compute', operation={"choices": filter_list})
    def clij_filter(input: Image, operation='maximum_sphere', x: float = 0, y: float = 0,
                    z: float = 0) -> Image:
        if input:
            cle_input = cle.push_zyx(input.data)
            output = cle.create_like(cle_input)
            try:
                #https://docs.python.org/3.0/library/operator.html
                filter_image = methodcaller(operation, cle_input, output, x, y, z)
                filter_image(cle)
            #only works for operations with two positional arguments; does not work for power() or similar ones
            except TypeError:
                filter_image = methodcaller(operation, cle_input, output)
                filter_image(cle)
            output = cle.pull_zyx(output)
            return output

    gui = clij_filter.Gui()
    viewer.window.add_dock_widget(gui)
    # if a layer gets added or removed, refresh the dropdown choices
    viewer.layers.events.changed.connect(lambda x: gui.refresh_choices("input"))

