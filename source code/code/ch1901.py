#!/usr/bin/env python
# -*- coding: cp950 -*-

# 載入wav與pymedia模組
import wave
import pymedia.audio.sound as sound

# 讀取WAV檔
f = wave.open("C:\\Windows\\Media\\Windows XP 啟動.wav", "rb")

# 取得採樣頻率
sampleRate = f.getframerate()

# 取得音樂頻率通道 1=單聲道, 2=雙聲道
channels = f.getnchannels()

# 設定播放格式
format = sound.AFMT_S16_LE

# 播放
mysound = sound.Output(sampleRate, channels, format)
rf = f.readframes(300000)
mysound.play(rf)
