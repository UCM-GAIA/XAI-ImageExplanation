import tensorflow as tf

def read_image(file_name):
    image = tf.io.read_file(file_name)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    ##inception_v1 & mobilenet & resnet50
    #image = tf.image.resize_with_pad(image, target_height=224, target_width=224)
    ##inception_v3 & inception_resnet_v2
    image = tf.image.resize_with_pad(image, target_height=299, target_width=299)
    return image