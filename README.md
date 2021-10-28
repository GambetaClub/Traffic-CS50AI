# Traffic-CS50AI

### In this project, I used TensorFlow to build a neural network to classify road signs based on an image of those signs. To do so, I needed a labeled dataset: a collection of images that have already been categorized by the road sign represented in them.

----------------------------------
## Procedures to improve accuraccy: 

I have tried first with the following settings:
Convolutional layer with 32 filters using 3x3 kernel
A max-pooling layer using 2x2 pool size
Then flattening the unit's filters.
Finally, added a hidden layer with 128 cells additionally with a dropout of 0.5 
The final result of this test was accuracy of 0.3161 with a loss of 2.9216

Then, I decided I should add more filters to the first convolutional layer. So I changed 32 filters for 64 filters. Apart from that, I tried changing the number of cells in the hidden layer from 128 to 256 with a dropout of 0.3. 
The result of this test was an accuracy of 0.0576 and a loss of 3.4988

The last changes resulted in a worse result. Therefore, I thought about changing the settings again. In this case, I proved with only ten filters with a kernel of 3x3, a max-pooling layer with a grain of 3x3, 400 cells in the hidden layer, and a dropout of 0.4.
The result of this test was an accuracy of 0.9225 and a loss of 0.3172.

Lastly, I tried with a configuration that gave me the best result of them all. I added an extra convolutional layer and a max-pooling layer, identical to the first two. I set 36 filters with a 3x3 kernel for the convolutional layers. On the other side, 2x2 kernel for the max-pooling layers. In the end, A hidden layer with 128 cells and a dropout of 0.2.
The result of this test was an accuracy of 0.9697 and a loss of 0.1224.

The dropout rate at the beginning was too high, which influenced the number of total cells used in the hidden layer. Also, adding extra layers to the Network improved the results dramatically. However, it took more time for the machine to finish the process. The latency was a little bit higher, but the accuracy was accuracy improved. 

## Update

Now the program is able to use saved a model which allows to train it several times. The maximum precision it achieved so far is 98.87%.
