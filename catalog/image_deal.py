from catalog import image_tool as it
import os

alpha = 30.0


def encode(o_image, wm):

    name = o_image

    path = get_path()
    # wm_bgr, wm = it.complement(wm)
    o_image = it.optimal_shape(it.load_image(join_path(path, name)))
    wm = it.optimal_shape(it.load_image(join_path(path, wm)))
    wm_bgr, wm = it.complement(wm)

    # Reshape size of watermark and flip it
    wm_shape = ((int)(o_image.shape[1] / 2), (int)(o_image.shape[0] / 2))
    r_wm = it.complement(it.resize(wm, wm_shape))
    print(r_wm.shape)
    s_wm = it.fill_image(r_wm, [o_image.shape[0], o_image.shape[1]])
    f_wm = it.flip(s_wm) + s_wm
    print(f_wm.shape)
    #s_wm = it.shuffle_image_with_shape(wm, wm_shape)

    # s_image = it.shift(it.fft(o_image))
    # r_image = it.log(it.abs(s_image))
    # f_image = s_image + f_wm * alpha
    # test = f_image

    #
    s_image = it.split(o_image)     #s_image[0] = b; s_image[1] = g; s_image[2] = r
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
        tube[:, :, 0] = tube[:, : ,0] + f_wm * alpha
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

    # final_img = final_img[2]

    final_img = it.real(it.ifft(it.ishift(sum_image)))

    # it.save_image(test, join_path(path, "bwm_" + name.split('.')[0] + '.png'))
    # it.save_image(test, join_path(path, name.split('.')[0] + '.png'))

    # final_img = it.real(it.ifft(it.ishift(f_image)))
    new_name = it.save_image_with_new_suffix(final_img, join_path(path, "bwm_"+name), "png")

    return new_name, "media/" + new_name


def decode(o_image, bwm_image):

    name = o_image

    path = get_path()
    # o_image = it.load_image(join_path(path, name))
    bwm_image = it.load_image(join_path(path, 'bwm_originalTestImage.png'))
    o_image = it.load_image(join_path(path, o_image))

    # align
    # bwm_image, h = it.alignImages(bwm_image, o_image)
    # print(bwm_image.shape)
    bwm_bgr = it.split(bwm_image)
    wm = []
    for tube in bwm_bgr:
        t = it.shift(it.fft(tube)[:, :, 0])
        wm.append(t)
    wm = it.merge(wm[0], wm[1], wm[2])
    print(wm.shape)
    # it.show_image(wm)
    # wm = (it.fft(bwm_image) - it.fft(o_image)) / alpha

    # wm = it.reverse_shuffle(it.real(wm))

    new_name = it.save_image_with_new_suffix(wm, join_path(path, "wm_" + name), "png")

    return new_name, "media/"+new_name


def get_path():
    return os.path.join(os.getcwd(), 'catalog', 'media')


def join_path(path1, path2):
    return os.path.join(path1, path2)
