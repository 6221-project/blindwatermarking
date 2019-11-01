from catalog import image_tool as it
import os

alpha = 3.0
test_num = 9999

def encode(o_image, wm):

    name = o_image

    path = get_path()
    o_image = it.load_image(join_path(path, name))
    wm = it.load_image(join_path(path, wm))

    wm = it.complement(wm)

    s_wm = it.shuffle_image_with_shape(wm, o_image.shape)

    f_image = it.fft(o_image)

    sum_image = f_image + s_wm * alpha

    final_img = it.real(it.ifft(sum_image))

    it.save_image(final_img, join_path(path, "bwm_"+name))
    it.save_image(final_img, join_path(path, name))

    return "bwm_"+name, "media/bwm_"+name


def decode(o_image, bwm_image):

    name = o_image

    path = get_path()
    o_image = it.load_image(join_path(path, name))
    bwm_image = it.load_image(join_path(path, bwm_image))

    wm = (it.fft(bwm_image) - it.fft(o_image)) / alpha

    wm = it.reverse_shuffle(it.real(wm))

    it.save_image(wm, join_path(path, "wm_"+name))

    return "wm_"+name, "media/wm_"+name


def get_path():
    return os.path.join(os.getcwd(), 'catalog', 'media')


def join_path(path1, path2):
    return os.path.join(path1, path2)
