# ArticleClassifier
Neural network to classify articles by their titles 

Articles obtained from BBC's dataset:
http://mlg.ucd.ie/datasets/bbc.html

Variations of neural networks were used to determine the highest accuracy.
Different variations: change in activation functions, change in number of hidden layers, and change in number of nodes in hidden layers.

Support Vector Machines and Logistic Regression were used to compare accuracies with the Neural Network.

Different variations for Support Vector Machines: change in kernel, and change in C values.

Different variations for Logistic Regression: change in regularization, and change in C values.

Highest accuracy found was ~78%.

# Future Work
Design a neural network utilizing the entirety of the article itself; should drastically increase the accuracy.

For new found words in the testing documents, create a proxy feature that holds new words.

Discard common words that don't really contribute to the classification aspect (to, from, a, the, etc.).

Collapse stemming words with different versions of verbs such as ran, running, run into just run.

Synonym expansion - collapse synonyms into just one feature: joy, content, happiness, jolly into happy.

Utilize more training and testing data to improve accuracy.
