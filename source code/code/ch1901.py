#!/usr/bin/env python
# -*- coding: cp950 -*-

# ���Jwav�Ppymedia�Ҳ�
import wave
import pymedia.audio.sound as sound

# Ū��WAV��
f = wave.open("C:\\Windows\\Media\\Windows XP �Ұ�.wav", "rb")

# ���o�ļ��W�v
sampleRate = f.getframerate()

# ���o�����W�v�q�D 1=���n�D, 2=���n�D
channels = f.getnchannels()

# �]�w����榡
format = sound.AFMT_S16_LE

# ����
mysound = sound.Output(sampleRate, channels, format)
rf = f.readframes(300000)
mysound.play(rf)
