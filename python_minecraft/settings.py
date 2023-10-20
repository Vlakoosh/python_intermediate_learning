from numba import njit
import numpy as np
import glm
import math

#resolution
WINDOW_RESOLUTION = glm.vec2(1600,900)

#background color
BG_COLOR = glm.vec3(0.1, 0.2, 0.99)