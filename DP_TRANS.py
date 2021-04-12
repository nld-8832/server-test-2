import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import wave

import deepspeech
from deepspeech import Model

def read_wav_file(filename):
  with wave.open(filename, 'rb') as w:
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)
  return buffer, rate

def transcribe(audio_file, model):
  buffer, rate = read_wav_file(audio_file)
  data16 = np.frombuffer(buffer, dtype = np.int16)
  return model.stt(data16)

def ModelInitiate(model_file_path, lm_file_path, lm_alpha, lm_beta, beam_width):
  model = Model(model_file_path)
  model.enableExternalScorer(lm_file_path)

  model.setScorerAlphaBeta(lm_alpha, lm_beta)
  model.setBeamWidth(beam_width)
  return model

def KHOI_TRANSCRIBE(_filename, _model_file_path, _lm_file_path, _lm_alpha, _lm_beta, _beam_width):
  model = ModelInitiate(_model_file_path, _lm_file_path, _lm_alpha, _lm_beta, _beam_width)
  return transcribe(_filename, model)