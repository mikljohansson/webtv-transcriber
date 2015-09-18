import os, shutil, subprocess, tempfile, hashlib, logging
from scrapy.exceptions import DropItem

def shell(cmd):
    logging.info('Running ' + ' '.join(cmd))
    return subprocess.call(cmd)

class FileStorage(object):
    def exists(self, url, src):
        return os.path.exists(os.path.join(self._directory(url), os.path.basename(src)))

    def put(self, url, src):
        directory = self._directory(url)
        if not os.path.exists(directory):
        	os.makedirs(directory)
        shutil.copy(src, os.path.join(directory, os.path.basename(src)))

    def _directory(self, url):
        digest = hashlib.md5(url).hexdigest()
        return '/data/' + digest[0:2] + '/' + digest[2:6] + '/' + digest[6:] + '/'

class SVTPlayDownload(object):
    def __init__(self):
        self._storage = FileStorage()

    def process_item(self, item, spider):
        outputdir = str(tempfile.mkdtemp())
        url = item['url']

        try:
            outputbase = os.path.join(outputdir, 'output')
            audiotrack = outputbase+'.mp3'
            subtitles = outputbase+'.srt'

            # Check if item been processed before
            if self._storage.exists(url, audiotrack) and self._storage.exists(url, subtitles):
                raise DropItem('Skipping item that was previously downloaded %s' % url)
            
            # Download the transport stream
            code = shell(['svtplay-dl', '--require-subtitle', '-o', outputbase, '-f', '-S', '-q', '1', '-Q', '10000', url])
            if code != 0:
                raise DropItem('Failed to download video from %s' % url)
            if not os.path.exists(subtitles):
                raise DropItem('Video did not contain subtitles %s' % url)
            
            # Extract audio track and store as mp3
            code = shell(['ffmpeg', '-i', outputbase+'.ts', '-y', '-vn', '-f', 'mp3', '-ac', '1', '-q:a', '6', audiotrack])
            if code != 0:
                raise DropItem('Failed to extract audio from %s' % url)

            # Transfer to persistent storage
            self._storage.put(url, audiotrack)
            self._storage.put(url, subtitles)
        finally:
            # Remove temporary directory and files
            shell(['rm', '-rf', outputdir])

        return item
