# Lab Task - 3: Word Embeddings (Word2Vec, GloVe) and Spelling Error Detection using CNN


## Author Details

```
Name - Shivani
Username - grad-date
Roll No - 19074017
```


## Word Embeddings
Word embedding is any of a set of language modeling and feature learning techniques in natural language processing (NLP) where words or phrases from the vocabulary are mapped to vectors of real numbers. Conceptually it involves a mathematical embedding from a space with many dimensions per word to a continuous vector space with a much lower dimension. In short:
```
Word embeddings are nothing but numerical representations of texts.
```

### Word2Vec Embedding

Word2vec is a method to efficiently create word embeddings by using a two-layer neural network. It was developed by Tomas Mikolov, et al. at Google in 2013 as a response to make the neural-network-based training of the embedding more efficient and since then has become the de facto standard for developing pre-trained word embedding.

The input of word2vec is a text corpus and its output is a set of vectors known as feature vectors that represent words in that corpus. While Word2vec is not a deep neural network, it turns text into a numerical form that deep neural networks can understand.

![meme example](https://miro.medium.com/max/1094/1*YAGrtIpuRyA87iQHIwuPVA.jpeg)

Word2vec is not a single algorithm but a combination of two techniques: 
- CBOW(Continuous bag of words) 
- Skip-gram model

Both of these are shallow neural networks which map word(s) to the target variable which is also a word(s). Both of these techniques learn weights which act as word vector representations.


#### Continuous Bag of Words(CBOW):
CBOW is learning to predict the word by the context. A context may be single word or multiple word for a given target words.
![cbow](https://media.geeksforgeeks.org/wp-content/uploads/20200904032437/cbow.png)


#### Skip-gram Model
The Skip-gram model architecture usually tries to achieve the reverse of what the CBOW model does. It tries to predict the source context words (surrounding words) given a target word (the centre word).
![skip-gram](https://media.geeksforgeeks.org/wp-content/uploads/20200904034523/skipgram.png)

#### Implementation
The Word2Vec embedding implementation is already available in Gensim, for both CBOW and skip-gram, which was used in training of the models. 

#### Result
Some most similar words results and visulisation plots (PCA and t-SNE) for most similar words as well as the complete embedding space are included in the respective jupyter notebook itself.


### GloVe Embedding

#### Introduction
GloVe (Global Vectors for Word Representation) is an alternate method to create word embeddings. It is based on matrix factorization techniques on the word-context matrix. A large matrix of co-occurrence information is constructed and you count each “word” (the rows), and how frequently we see this word in some “context” (the columns) in a large corpus. Usually, we scan our corpus in the following manner: for each term, we look for context terms within some area defined by a window-size before the term and a window-size after the term. Also, we give less weight for more distant words.

Given a corpus having V words, the co-occurrence matrix X will be a V x V matrix, where the i th row and j th column of X, X_ij denotes how many times word i has co-occurred with word j. An example co-occurrence matrix might look as follows:

![glove](https://www.researchgate.net/profile/Majid_F_Sadi/publication/332703770/figure/fig1/AS:752289044234240@1556371093356/1-Co-occurrence-matrix-for-three-sample-sentences.ppm)

#### Implementation
The GloVe implementation is partly available in Gensim in the sense that it can only load it and use it, but not train it. For that following link is used:
https://github.com/stanfordnlp/GloVe.git

Firstly the model was trained, and then loaded the trained model using the Gensim glove library in Jupyter Notebook. After that visualisation and similar word generation were done in the same general way as for Word2Vec, but the code was changed from GloVe to Word2Vec. 

#### Result
Some most similar words results and visulisation plots (PCA and t-SNE) for most similar words as well as the complete embedding space are included in the jupyter notebook itself.


## Spelling Error Detection using CNN

### Convolution Neural Networks

#### Introduction
In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery. CNNs are regularized versions of multilayer perceptrons. Multilayer perceptrons usually mean fully connected networks, that is, each neuron in one layer is connected to all neurons in the next layer. The "fully-connectedness" of these networks makes them prone to overfitting data. Typical ways of regularization include adding some form of magnitude measurement of weights to the loss function. CNNs take a different approach towards regularization: they take advantage of the hierarchical pattern in data and assemble more complex patterns using smaller and simpler patterns. Therefore, on the scale of connectedness and complexity, CNNs are on the lower extreme.

![cnn](https://miro.medium.com/max/1094/1*uAeANQIOQPqWZnnuH-VEyw.jpeg)

#### Implementation
First of all mispelled words (from mis-spelled.txt) and correctly spelled words (from correct-spelled.txt) were mixed in the ratio of 1:10, i.e. 10 correct words for each wrongly spelled word (and stored in words.txt). Then character level CNN was used for classification. The classes in our case are just Correct or Incorrect (binary classification) while input being words only. Characters were tokenized manually by simple unique indexing.

#### Result
Accuracy and loss of both trained and tested datasets are displayed in jupyter notebook itself.


## Note
To get models and dataset [click here](https://drive.google.com/drive/folders/1GQvAlWrkUphN9UJfpwGJ_2y06zXTfnJK?usp=sharing).