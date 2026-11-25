import wave
import struct
import math
import numpy as np

def create_sample_audio(filename, duration=2.0, sample_rate=44100):
    # Simulated cough sound: Noise with an envelope
    num_samples = int(duration * sample_rate)
    
    # White noise
    noise = np.random.uniform(-1, 1, num_samples)
    
    # Envelope: quick rise, decay, and a second pulse
    t = np.linspace(0, duration, num_samples)
    envelope = np.exp(-10 * t) + 0.5 * np.exp(-5 * (t - 0.5)**2)
    
    audio_data = noise * envelope
    
    # Normalize and convert to 16-bit PCM
    audio_data = (audio_data * 32767).astype(np.int16)
    
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

if __name__ == "__main__":
    import os
    # Create directory if doesn't exist
    os.makedirs('samples', exist_ok=True)
    create_sample_audio('samples/cough_sample.wav')
    print("Sample audio created: samples/cough_sample.wav")
