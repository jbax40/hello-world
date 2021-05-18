# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:11:54 2021

@author: MediaMonster branch test 2 vingt dieu
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavefile

ECHO_DURATION_SEC = 0.5
DELAY_AMPLITUDE = 0.3

fs, guitar_sig_int16 = wavefile.read("../test_files/Archipel.wav")
guitar_sig = guitar_sig_int16.astype(np.float) / 2**15

delay_len_samples = round(ECHO_DURATION_SEC * fs)
leading_zero_padding_sig = np.zeros(delay_len_samples)

delayed_sig = np.concatenate((leading_zero_padding_sig , guitar_sig))
ending_padding_len_samples = len(delayed_sig) - len(guitar_sig)
ending_padding_sig = np.zeros(ending_padding_len_samples)
guitar_sig = np.concatenate((guitar_sig,ending_padding_sig))

summed_sig = guitar_sig + DELAY_AMPLITUDE*delayed_sig
wavefile.write("../processed_files/out_basic_wav", fs, summed_sig)
