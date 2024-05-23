# -*- coding: utf-8 -*-
"""
@author: Sanad
GitHub: ItsSanad

"""

from pydub import AudioSegment
import numpy as np

def analyze_audio(audio_file):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Convert the audio to numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Calculate the highest, lowest, and mean pitch
    highest_pitch = np.max(audio_array)
    lowest_pitch = np.min(audio_array)
    mean_pitch = np.mean(audio_array)

    # Calculate the average highest and lowest pitch
    average_highest_pitch = (highest_pitch + mean_pitch) / 2
    average_lowest_pitch = (lowest_pitch + mean_pitch) / 2

    return highest_pitch, lowest_pitch, mean_pitch, average_highest_pitch, average_lowest_pitch, audio_array

# Analyze first audio
first_audio = "voices\Al-Sudais.mp3"
test1_highest_pitch, test1_lowest_pitch, test1_mean_pitch, test1_average_highest_pitch, test1_average_lowest_pitch, test1_audio_array = analyze_audio(first_audio)

# Print the results
print("Highest pitch:", test1_highest_pitch)
print("Lowest pitch:", test1_lowest_pitch)
print("Mean pitch:", test1_mean_pitch)
print("Average highest pitch:", test1_average_highest_pitch)
print("Average lowest pitch:", test1_average_lowest_pitch)
