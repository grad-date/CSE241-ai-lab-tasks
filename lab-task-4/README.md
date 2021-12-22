# Lab Task-4: Part-of-Speech (POS) Tagging, Chunking and Named Entity Recognition (NER) using RNN and Bi-LSTM


## Author Details

```
Name - Shivani
Username - grad-date
Roll No - 19074017
```

## RNN (Recurrent Neural Network):

![rnn](https://miro.medium.com/max/980/1*go8PHsPNbbV6qRiwpUQ5BQ.png)

Recurrent Neural Network is a generalization of feedforward neural network that has an internal memory. RNN is recurrent in nature as it performs the same function for every input of data while the output of the current input depends on the past one computation. After producing the output, it is copied and sent back into the recurrent network. For making a decision, it considers the current input and the output that it has learned from the previous input.

## Bi-LSTM (Bi-directional long short term memory):

![blstm](https://miro.medium.com/max/1094/1*B5NHtY8_Y4we0DE4Y-acBA.png)

Bidirectional recurrent neural networks(RNN) are really just putting two independent RNNs together. This structure allows the networks to have both backward and forward information about the sequence at every time step.


## Result
- Plotted Train and Test Graphs
- Printed Accuracy and Loss

In respective files.


## Conclusion
- In chunking we get very high accuracy using Bi-Lstm and almost similiar accuracy using RNN when compared with CRF++ implementation.
- In POS_tagging we get very high accuracy using Bi-Lstm and almost similiar accuracy using RNN when compared with CRF++ implementation.
- In NER we get similiar accuracy using Bi-Lstm and very high accuracy using RNN when compared with CRF++ implemenation.


## Note
To get models and dataset [click here](https://drive.google.com/drive/folders/1S8wvaE7SEYdb6L7GRaAfSbnbfjBcVlto?usp=sharing).