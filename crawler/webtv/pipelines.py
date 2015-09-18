import os, subprocess, tempfile, hashlib, logging
from scrapy.exceptions import DropItem

def shell(cmd):
    logging.info('Running ' + ' '.join(cmd))
    return subprocess.call(cmd)

def store(url, src):
    digest = hashlib.md5.new(url).hexdigest()
    directory = '/data/' + digest[0:2] + '/' + digest[2:6] + '/' + digest[6:] + '/'
    os.path.mkdirs(directory)
    os.rename(src, os.path.join(directory, os.path.basename(src)))

class SVTPlayDownload(object):
    def process_item(self, item, spider):
        outputdir = str(tempfile.mkdtemp())
        try:
            outputbase = os.path.join(outputdir, 'output')
            audiotrack = outputbase+'.mp3'
            subtitles = outputbase+'.srt'
            
            code = shell(['svtplay-dl', '-o', outputbase, '-f', '-S', '-q', '1', '-Q', '10000', item['url']])
            if code != 0:
                raise DropItem('Failed to download video from %s' % item['url'])
            if not os.path.exists(subtitles):
                raise DropItem('Video did not contain subtitles %s' % item['url'])
            
            code = shell(['ffmpeg', '-i', outputbase+'.ts', '-y', '-vn', '-f', 'mp3', '-ac', '1', '-q:a', '6', audiotrack])
            if code != 0:
                raise DropItem('Failed to extract audio from %s' % item['url'])

            store(url, audiotrack)
            store(url, subtitles)
        finally:
            shell(['rm', '-rf', outputdir])

        return item
