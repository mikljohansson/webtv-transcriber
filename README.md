# Reading Material

- http://svail.github.io/mandarin/

- http://usa.baidu.com/deep-speech-lessons-from-deep-learning/
- http://devblogs.nvidia.com/parallelforall/deep-speech-accurate-speech-recognition-gpu-accelerated-deep-learning/
- http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/

- http://www.cs.toronto.edu/~graves/
- http://www.jmlr.org/proceedings/papers/v32/graves14.pdf
- http://www.cs.toronto.edu/~graves/icassp_2013.pdf
- http://www.cs.toronto.edu/~graves/asru_2013.pdf
- http://www.machinelearning.org/proceedings/icml2006/047_Connectionist_Tempor.pdf

- https://wiki.inf.ed.ac.uk/twiki/pub/CSTR/ListenTerm1201415/sak2.pdf

# CTC

- https://github.com/skaae/Lasagne-CTC
- https://github.com/rakeshvar/rnn_ctc
- https://github.com/patyork/python-deep-speech/blob/master/theano-deep-speech/tensorbrnn.py#L76
- https://github.com/search?q=theano+ctc&type=Code&utf8=%E2%9C%93

## Parallel Training

- https://drive.google.com/file/d/0B6dKRGPLFSd0UGNOYkNaSC1UZTA/view
- http://arxiv.org/pdf/1412.5567v2.pdf
- https://github.com/uoguelph-mlrg/theano_multi_gpu
- https://github.com/uoguelph-mlrg/theano_alexnet

# Startup
```
docker-compose up
```

## Crawler
Output goes into ./data

```
docker-compose -f crawler/docker-compose.yml up
```

## Transcriber
Reads mp3 and subitles from ./data

```
docker-compose -f transcriber/docker-compose.yml up
```

# TODO

- Crawler downloading and extracting the audio as a single part [Done]
- Generating some sonograms from the mp3's [Done]
- Transcriber image with Theano/Lasagna installed [Done]
- Setup an NN training pipeline based on Lasagna example
- Do some research on how to build the NN https://github.com/Lasagne/Lasagne

