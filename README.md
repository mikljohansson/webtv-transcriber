# TODO

- Crawler downloading and extracting the audio as a single part (Mikael) [Done]
- Generating some sonograms from the mp3's (Salimane)
- Transcriber image with Theano/Lasagna installed (Mikael) [Done]
- Setup an NN training pipeline based on Lasagna example (Mikael)
- Do some research on how to build the NN https://github.com/Lasagne/Lasagne

# Reading Material

- http://usa.baidu.com/deep-speech-lessons-from-deep-learning/
- http://devblogs.nvidia.com/parallelforall/deep-speech-accurate-speech-recognition-gpu-accelerated-deep-learning/
- http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/
- http://www.cs.toronto.edu/~graves/asru_2013.pdf
- https://wiki.inf.ed.ac.uk/twiki/pub/CSTR/ListenTerm1201415/sak2.pdf

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
