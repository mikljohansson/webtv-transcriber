#!/bin/sh 
set -e -x

BUILD_DEPS="git gcc-c++ zlib-devel make automake libtool autoconf patch bzip2 wget subversion"

# Store list of installed RPM's
rpm -qa --queryformat "%{NAME}\n" > /tmp/rpm.before

# Temporarily install build dependencies
yum -y install $BUILD_DEPS

# Clone latest Kaldi
git clone https://github.com/kaldi-asr/kaldi.git /tmp/kaldi

# Build the Kaldi tools
cd /tmp/kaldi/tools
make -j

# Build Kaldi
cd /tmp/kaldi/tools
./configure
make -j depend
make -j

# Uninstall build dependencies to avoid image bloat
rpm -qa --queryformat "%{NAME}\n" > /tmp/rpm.after
diff /tmp/rpm.before /tmp/rpm.after | grep '^[<>] ' | cut -d ' ' -f 2 | sort | uniq -c | grep '^\s*1 ' | tr -s ' ' ' ' | cut -d ' ' -f 3 | xargs yum -y erase

# Clean up metadata
yum clean all
rm -rf /tmp/*
