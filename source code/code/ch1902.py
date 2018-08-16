#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入pymedia模組
import pymedia.muxer as muxer
import pymedia.audio.acodec as acodec
import pymedia.audio.sound as sound

# 指定要播放的mp3檔案
name='./song44.mp3'

mysound = None
dec = None

# 建立Demuxer
demuxer = muxer.Demuxer(str.split(name, '.')[-1].lower())

# 讀取MP3檔案
f = open(name, 'rb')
stream = f.read(32000)

# 持續的播放stream
while len(stream):
   frames = demuxer.parse(stream)
   if frames:
      for fr in frames:
         
         if dec == None:
            # 輸出MP3資料
            print demuxer.getHeaderInfo()
            print demuxer.streams
            dec = acodec.Decoder(demuxer.streams[fr[0]])
        
         r = dec.decode(fr[1])
         if r and r.data:
            if mysound == None:
               mysound = sound.Output(r.sample_rate, r.channels, sound.AFMT_S16_LE)
          
            data = r.data
	    # 播放
            mysound.play(data)
    
   stream = f.read(512)
