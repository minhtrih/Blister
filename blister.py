import mrcnn.model as modellib
from mrcnn.visualize import display_images
from mrcnn import visualize
import os
import sys
import matplotlib
import matplotlib.pyplot as plt
import skimage.io
import numpy as np
from Mask_RCNN.samples.blister import blister

config = blister.BlisterConfig()


class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


def load_model():
    # Root directory of the project
    ROOT_DIR = os.path.abspath("Mask_RCNN/")

    # Import Mask RCNN
    sys.path.append(ROOT_DIR)  # To find local version of the library

    # Directory to save logs and trained model
    MODEL_DIR = os.path.join(ROOT_DIR, "logs")
    BLISTER_WEIGHTS_PATH = "mask_rcnn_blister_01.h5"

    BLISTER_DIR = os.path.join(ROOT_DIR, "datasets/blister")

    # TODO: code for 'training' test mode not ready yet
    TEST_MODE = "inference"

    config = InferenceConfig()
    config.display()

    # Create model in inference mode
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR,
                              config=config)
    weights_path = os.path.join(ROOT_DIR, BLISTER_WEIGHTS_PATH)
    model.load_weights(weights_path, by_name=True)
    return model


model = load_model()


def get_ax(rows=1, cols=1):
    _, ax = plt.subplots(rows, cols, figsize=(9*cols, 6*rows))
    return ax


def detect_image(image):
    file_name = image.split('/')[2]
    image = skimage.io.imread(image)
    sizes = np.shape(image)
    height = float(sizes[0])
    width = float(sizes[1])

    class_names = ['BG', 'blister']
    results = model.detect([image], verbose=1)

    ax = get_ax(1)
    r = results[0]

    result_image = visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'],
                                               class_names, r['scores'], ax=ax)

    plt.savefig('static/results/' + file_name, bbox_inches='tight',
                pad_inches=-0.1, orientation='landscape')
    plt.close()

    return
