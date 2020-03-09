import matplotlib.pyplot as plt

img = plt.imread('robot.jpg')
plt.imshow(img);

head= img[25:190, 200:370]
plt.imshow(head)
