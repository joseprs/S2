import os


def motion_vectors(input_name, output_name):
    os.system('ffmpeg -flags2 +export_mvs -i ' + input_name + '.mp4 -vf codecview=mv=pf+bf+bb ' + output_name + '.mp4')


def bbbContainer(input_name, output_name):
    os.system('ffmpeg -ss 00:00:00.0 -i ' + input_name + '.mp4 -c copy -t 00:01:00.0 container/BBB1min.mp4')
    os.system('ffmpeg -i container/BBB1min.mp4 -c copy -an container/BBBnoaudio.mp4')
    os.system('ffmpeg -i container/BBB1min.mp4 -vn -acodec copy container/output-audio.mp3')
    os.system('ffmpeg -i container/BBB1min.mp4 -vn -acodec copy container/output-audio.aac')
    os.system(
        'ffmpeg -i container/BBBnoaudio.mp4 -i container/output-audio.aac -c copy container/' + output_name + '.mp4')


def standards(track_name):
    os.system('ffmpeg -i container/output-audio.aac -target /tmp/vcd.mpg')


def subtitles(input_video, output_video, sub_name):
    os.system(
        'ffmpeg -i ' + input_video + '.mp4 -i ' + sub_name + '.srt -c copy -c:s mov_text ' + output_video + '.mp4')


# subtitles('container/BBB1min','BBBsubs','subtitles')
# standards('output-audio.aac')
# bbbContainer('BBB','finaloutput')
# motion_vectors('BBB', 'BBBvectors')
