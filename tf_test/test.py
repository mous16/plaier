import numpy
import tensorflow
from PIL import Image

import rle_bridge


def show(screen, title):
    image = Image.fromarray(screen)
    image.show(title)


rle_mgr = rle_bridge.RLEManager()
rle_mgr.start()

tf_input = tensorflow.placeholder(tensorflow.float32, shape=rle_mgr.rle.getScreenRGB().shape, name="screen")
tf_output = tensorflow.add(tf_input, tf_input, name="screen_add")

rle_mgr.advance(0, rle_bridge.LeftInputs.Left, 10)

with tensorflow.Session() as sess:
    run_res = sess.run(tf_output, feed_dict={tf_input: rle_mgr.screen()})
    rle_mgr.show("current")
    show(run_res, "screen_add")
