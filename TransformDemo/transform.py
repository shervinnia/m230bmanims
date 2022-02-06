import numpy as np
import imageio
import matplotlib.pyplot as plt


def fft2c(f):
    return np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(f)))

def ifft2c(F):
    return np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(F)))

filename = '/home/shervin/Documents/manimprojects/TransformDemo/media/videos/transformdemo/1080p60/dots.mp4'
vid = imageio.get_reader(filename, mode = 'I')
write = imageio.get_writer('transform.mp4', mode = 'I', fps = 60)
plt = plt.figure(num=None,figsize=(8,6), dpi=80)
plt.imshow(abs(fft2c(np.array(vid.get_next_data()))), cmap='gray')
#for frame in vid:
#    im = np.array(vid.get_next_data())
#    img_fft = fft2c(im)
#    write.append_data(np.log(np.abs(img_fft) + 1e-6))
write.close()
