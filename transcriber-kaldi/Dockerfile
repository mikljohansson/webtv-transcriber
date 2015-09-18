FROM centos:7

# Invalidate the git clone when pushed to kaldi master branch
ADD https://api.github.com/repos/kaldi-asr/kaldi/git/refs/heads/master /tmp/kaldi-master.json

# Install Kaldi from source
ADD provision.sh /tmp/
RUN /tmp/provision.sh
