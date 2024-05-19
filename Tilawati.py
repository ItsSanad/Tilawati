# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:19:04 2024

@author: Sanad
"""

from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
first_audio = "voices\Mishari Al-afasi.mp3"
test1_highest_pitch, test1_lowest_pitch, test1_mean_pitch, test1_average_highest_pitch, test1_average_lowest_pitch, test1_audio_array = analyze_audio(first_audio)

# Analyze second audio
second_audio = "voices\Hassan Saleh.mp3"
test2_highest_pitch, test2_lowest_pitch, test2_mean_pitch, test2_average_highest_pitch, test2_average_lowest_pitch, test2_audio_array = analyze_audio(second_audio)

# Print the results
print("Test 1:")
print("Highest pitch:", test1_highest_pitch)
print("Lowest pitch:", test1_lowest_pitch)
print("Mean pitch:", test1_mean_pitch)
print("Average highest pitch:", test1_average_highest_pitch)
print("Average lowest pitch:", test1_average_lowest_pitch)
print()
print("Test 2:")
print("Highest pitch:", test2_highest_pitch)
print("Lowest pitch:", test2_lowest_pitch)
print("Mean pitch:", test2_mean_pitch)
print("Average highest pitch:", test2_average_highest_pitch)
print("Average lowest pitch:", test2_average_lowest_pitch)

# Set the style of seaborn
sns.set(style="whitegrid")

# Plot the distribution for both test1.mp3 and test2.mp3 in one plot
plt.figure(figsize=(10, 6))

# Plot test1.mp3 in blue
sns.histplot(test1_audio_array, kde=True, color="blue", bins=50, label="Mishari Al-afasi")

# Plot test2.mp3 in red
sns.histplot(test2_audio_array, kde=True, color="red", bins=50, label="Hassan Saleh")

plt.title("Mishari Al-afasi vs Hassan Saleh")
plt.xlabel("Pitch")
plt.ylabel("Frequency")
plt.axvline(x=test1_average_highest_pitch, color='blue', linestyle='--', label='Average Highest Pitch')
plt.axvline(x=test1_average_lowest_pitch, color='blue', linestyle='-.', label='Average Lowest Pitch')
plt.axvline(x=test1_mean_pitch, color='blue', linestyle=':', label='Mean Pitch')
plt.axvline(x=test2_average_highest_pitch, color='red', linestyle='--', label='Average Highest Pitch')
plt.axvline(x=test2_average_lowest_pitch, color='red', linestyle='-.', label='Average Lowest Pitch')
plt.axvline(x=test2_mean_pitch, color='red', linestyle=':', label='Mean Pitch')
plt.legend()
plt.show()

