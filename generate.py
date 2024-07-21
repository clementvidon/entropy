import sounddevice as sd
import hashlib
import pyaudio
import numpy as np
import argparse
import time

# TODO NIST Statistical Test Suite or Diehard tests.

DICE_MIN = 1
DICE_MAX = 6
NUM_SIZE = 5


def record_audio(duration, rate=44100, chunk_size=1024):
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=rate,
        input=True,
        frames_per_buffer=chunk_size,
    )

    frames = []
    for _ in range(0, int(rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return frames


def has_sound_variations(audio_data, threshold=500):
    audio_array = np.frombuffer(b"".join(audio_data), dtype=np.int16)
    return np.std(audio_array) > threshold


def generate_random_numbers(
    audio_data, num_size=NUM_SIZE, range_start=DICE_MIN, range_end=DICE_MAX
):
    audio_data = np.frombuffer(b"".join(audio_data), dtype=np.int16)
    chunk_size = len(audio_data) // num_size

    random_numbers = []
    for i in range(num_size):
        chunk = audio_data[i * chunk_size : (i + 1) * chunk_size]
        chunk_hash = hashlib.sha256(chunk).digest()
        hash_int = int.from_bytes(chunk_hash, byteorder="big", signed=False)
        mapped_number = range_start + (hash_int % (range_end - range_start + 1))
        if mapped_number > DICE_MAX:
            mapped_number -= DICE_MAX
        random_numbers.append(mapped_number)

    return random_numbers


def main():
    parser = argparse.ArgumentParser(description="Generate numbers based on ambient sound.")
    parser.add_argument(
        "num_numbers", type=int, help="The number of random numbers to generate"
    )
    args = parser.parse_args()

    duration = 1  # seconds
    num_numbers = args.num_numbers * NUM_SIZE

    with open("numbers", "w") as f:
        while num_numbers > 0:
            frames = record_audio(duration)
            if not has_sound_variations(frames):
                print("Sound required for numbers generation")
                time.sleep(1)
                continue

            random_numbers = generate_random_numbers(
                frames, num_size=min(NUM_SIZE, num_numbers)
            )
            for number in random_numbers:
                f.write(f"{number}")
            f.write("\n")
            num_numbers -= len(random_numbers)


if __name__ == "__main__":
    main()
    print("Numbers generated. See 'numbers' file.")
