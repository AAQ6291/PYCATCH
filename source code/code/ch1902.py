#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jpymedia�Ҳ�
import pymedia.muxer as muxer
import pymedia.audio.acodec as acodec
import pymedia.audio.sound as sound

# ���w�n����mp3�ɮ�
name='./song44.mp3'

mysound = None
dec = None

# �إ�Demuxer
demuxer = muxer.Demuxer(str.split(name, '.')[-1].lower())

# Ū��MP3�ɮ�
f = open(name, 'rb')
stream = f.read(32000)

# ���򪺼���stream
while len(stream):
   frames = demuxer.parse(stream)
   if frames:
      for fr in frames:
         
         if dec == None:
            # ��XMP3���
            print demuxer.getHeaderInfo()
            print demuxer.streams
            dec = acodec.Decoder(demuxer.streams[fr[0]])
        
         r = dec.decode(fr[1])
         if r and r.data:
            if mysound == None:
               mysound = sound.Output(r.sample_rate, r.channels, sound.AFMT_S16_LE)
          
            data = r.data
	    # ����
            mysound.play(data)
    
   stream = f.read(512)
