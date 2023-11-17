# OtterSec Is Cat?
From vsCTF 23. Solution by tjcaul.
 
## Problem
CNN classifies images as it should.
We want it to classify a non-cat image as a cat.
What we have:
- Source for the challenge server and model tester
- Trained model
- Hint about how it was trained
What we don't have:
- Model structure
- Training code
How can I create a drop-in replacement for a model I don't have the source for?

## Solving
Modifying the trainer to create a model compatible with the server was harder
than expected. It had to be converted from one channel to three, MNIST
dataloader to my own, 28x28 to 32x32, and different model structure. Also, most
insidiously, the trainer scaled values to `0.0-1.0`, while the supplied model
expected values `0-255`.

## Solution
1. Download the training code's inspiration from the GitHub repo
2. Get the supplied model's metadata with a simple
   `keras.models.load_model('challenge_model.h5').summary()`
3. Modify the trainer to create a model with the same structure
4. Use the test images (including the OtterSec logo) as training data
5. Using the supplied model as a checkpoint, train it further to recognize the
   logo as a cat.
6. Send the new model to the server in base64 and see the server send the flag!

This seems like an exercise in training data poisoning. I could download any
publically-available model, fine-tune it on my own evil data, then redistribute
it as a 'mirror' or 'update'. It would be almost impossible to notice the
tampering without entering the specific input. It's a backdoor in the model.
