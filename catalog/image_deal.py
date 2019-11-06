from catalog import image_tool as it
from catalog import path_tool as pt

alpha = 20.0
basic_path = pt.join_path(pt.get_cwd(), 'catalog', 'media')


def encode(o_image, wm):

    # name of original image
    name = o_image

    o_image = it.optimal_shape(it.load_image(pt.join_path(basic_path, name)))
    wm = it.optimal_shape_gray(it.load_image_grey(pt.join_path(basic_path, wm)))
    wm = it.complement(wm)

    # Reshape size of watermark and flip it
    wm_shape = ((int)(o_image.shape[1] / 2), (int)(o_image.shape[0] / 2))
    r_wm = it.resize(wm, wm_shape)

    s_wm = it.fill_image(r_wm, [o_image.shape[0], o_image.shape[1]])
    f_wm = it.flip(s_wm) + s_wm

    # s_image = it.shift(it.fft(o_image))
    # r_image = it.log(it.abs(s_image))
    # f_image = s_image + f_wm * alpha
    # test = f_image

    #
    s_image = it.split(o_image)     # s_image[0] = b; s_image[1] = g; s_image[2] = r
    f_image = []
    sum_image = []
    final_img = []

    # s_image = it.bgr_to_gray(o_image)
    # dft = it.shift(it.fft(s_image))
    # f_img = it.ifft(it.ishift(dft))
    # final_img = f_img

    for tube in s_image:
        dft = it.shift(it.fft(tube))
        # f_image.append(it.magnitude(dft[: ,: ,0], dft[:, :, 1]))
        f_image.append(dft)

    for tube in f_image:
        print(tube.shape)
        tube[:, :, 0] = tube[:, :, 0] + f_wm * alpha
        tube[:, :, 1] = tube[:, :, 1] + f_wm * alpha
        sum_image.append(tube)

    # it.show_image(it.merge(sum_image[0], sum_image[1], sum_image[2]))
        # sum_image.append(tube)

    # test = it.merge(sum_image[0], sum_image[1], sum_image[2])
    # test = it.merge(f_image[0], f_image[1], f_image[2])
    # it.show_image(test)

    for tube in sum_image:
        idft = it.ifft(it.ishift(tube))
        final_img.append(idft)
    final_img = it.merge(final_img[0], final_img[1], final_img[2])

    new_name = it.save_image_with_new_suffix(final_img, pt.join_path(basic_path, "bwm_"+name), "png")

    return new_name, "media/" + new_name


def decode(o_image, bwm_image, is_align=False):

    name = bwm_image

    bwm_image = it.load_image(pt.join_path(basic_path, bwm_image))
    o_image = it.load_image(pt.join_path(basic_path, o_image))

    # align
    if is_align:
        bwm_image, h = it.alignImages(bwm_image, o_image)

    bwm_bgr = it.split(bwm_image)
    wm = []
    for tube in bwm_bgr:
        t = 20*it.log(it.real(it.shift(it.fft(tube)[:, :, 0])))
        # t = it.shift(it.fft(tube)[:, :, 0])
        wm.append(t)
    wm = it.merge(wm[0], wm[1], wm[2])

    new_name = it.save_image_with_new_suffix(wm, pt.join_path(basic_path, "dwm_" + name), "png")

    return new_name, "media/"+new_name

