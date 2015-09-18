# TODO

- Crawler downloading and extracting the audio as a single part (Mikael) [Done]
- Generating some sonograms from the mp3's (Salimane)
- Transcriber image with Theano/Lasagna installed (Mikael) [Done]
- Setup an NN training pipeline based on Lasagna example (Mikael)
- Do some research on how to build the NN https://github.com/Lasagne/Lasagne


# Startup

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
