from catalog import image_tool as it
import os

alpha = 3.0


def encode(o_image, wm):

    name = o_image

    path = get_path()
    o_image = it.optimal_shape(it.load_image(join_path(path, name)))
    wm = it.optimal_shape(it.load_image(join_path(path, wm)))
    wm_bgr, wm = it.complement(wm)

    # Reshape size of watermark and flip it
    wm_shape = ((int)(o_image.shape[1] / 2), (int)(o_image.shape[0] / 2))
    r_wm = it.resize(wm, wm_shape)
    s_wm = it.fill_image(r_wm, o_image.shape)
    f_wm = it.flip(s_wm) + s_wm
    #s_wm = it.shuffle_image_with_shape(wm, wm_shape)

    f_image = it.shift(it.fft(o_image))

    sum_image = f_image + f_wm * alpha


    final_img = it.real(it.ifft(it.ishift(sum_image)))

    it.save_image(final_img, join_path(path, "bwm_"+name))

    return "bwm_"+name, "media/bwm_"+name


def decode(o_image, bwm_image):

    name = o_image

    path = get_path()
    # o_image = it.load_image(join_path(path, name))
    bwm_image = it.load_image(join_path(path, bwm_image))
    o_image = it.load_image(join_path(path, o_image))

    # align
    #bwm_image, h = it.alignImages(bwm_image, o_image)

    wm = it.real(it.shift(it.fft(bwm_image)))
    # wm = (it.fft(bwm_image) - it.fft(o_image)) / alpha
    # wm = it.reverse_shuffle(it.real(wm))

    it.save_image(wm, join_path(path, "wm_"+name))

    return "wm_"+name, "media/wm_"+name


def get_path():
    return os.path.join(os.getcwd(), 'catalog', 'media')


def join_path(path1, path2):
    return os.path.join(path1, path2)
