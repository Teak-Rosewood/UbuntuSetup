import random

import numpy as np

random.seed(0)

# detection model classes
CLASSES = ('right', 'left')

# colors for per classes
COLORS = {
    cls: [random.randint(0, 255) for _ in range(3)]
    for i, cls in enumerate(CLASSES)
}

# colors for segment masks
MASK_COLORS = np.array([(255, 56, 56), (255, 157, 151)],
                       dtype=np.float32) / 255.

KPS_COLORS = [[0, 255, 0], [0, 255, 0]]

SKELETON = [[16, 14], [14, 12]]

LIMB_COLORS = [[51, 153, 255], [51, 153, 255]]

# alpha for segment masks
ALPHA = 0.5
