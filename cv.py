import cv2
import numpy as np
from tqdm import tqdm

cv2.namedWindow("test")
for i in tqdm(range(10000)):
    img = np.random.rand(320*3,240*3,3)
    cv2.imshow("test", img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
