'''
OOPs four pillars:
Abstraction
Encapsulation
Inheritance
Polymorphism
'''
# Abstraction - Step by Step
'''
Meaning:
Hiding compplex details and showing only what's necessary
'''
'''
print("=" * 60)
print("1. ABSTRACTION")
print("=" * 60)
'''
# Task:
'''
Imagine you're building a music app that plays different file types
Each file type needs to play differently, but users just want to click 'play'
'''
# Without using Abstraction concept we are going to build a python program
# The lengthy approach:
"""
class MP3File:
	def __init__(self, filename):
		self.filename = filename

	def play_mp3(self):
		print(f"Playing MP3: {self.filename} using MP3 decoder")

class WAVFile:
	def __init__(self, filename):
		self.filename = filename

	def play_wav(self):
		print(f"Playing WAV: {self.filename} using WAV decoder")

class FLACFile:
	def __init__(self, filename):
		self.filename = filename

	def play_flac(self):
		print(f"Playing FLAC: {self.filename} using FLAC decoder")

# Creating Instances and Calling Methods
print("Creating audio files:")
mp3_file = MP3File("song.mp3")
wav_file = WAVFile("music.wav")
flac_file = FLACFile("audio.flac")

print("\nPlaying files (notice different methods names):")
mp3_file.play_mp3()		# Different method name
wav_file.play_wav() 	# Different method name
flac_file.play_flac() 	# Different method name

'''
Problem with this approach
- Different method names (play_mp3, play_wav, play_flac)
- Hard to remember which method to call
- Difficult to write generic code
- If we want to play all files, we need separate handling for each
'''
# Example: Playing all files requires different handling
print("\nTrying to play all files in a loop (messy):")
files = [mp3_file, wav_file, flac_file]
for file in files:
	# We need to check the type and call different methods
	if isinstance(file, MP3File):
		file.play_mp3()
	elif isinstance(file, WAVFile):
		file.play_wav()
	elif isinstance(file, FLACFile):
		file.play_flac()

print("^ This is very messy! Too many if-else statements")
print()
"""
# Same Problem Solution, using abstraction (Clean approach)
print("STEP 3: With Abstraction (Good way)")
print("-" * 40)

from abc import ABC, abstractmethod

# Abstract base class - like a contract
class AudioFile(ABC):
	def __init__(self, filename):
		self.filename = filename

		@abstractmethod
		def play(self):
			"""Every audio file must implement this method """
			pass

		@abstractmethod
		def get_duration(self):
			"""Every audio file must implement this method"""
			pass
		# Concrete method (already implemented) - common for all files
		def get_info(self):
			return f"Audio file: {self.filename}"

		def stop(self):
			print(f"Stopped Playing {self.filename}")

# You cannot create an Instance of AudioFile directly
# audio = AudioFile("test.mp3") # This would give an error!

# Concrete implementations
class MP3(AudioFile):
	def play(self):
		print(f"Playing MP3: {self.filename} using MP3 decoder")

	def get_duration(self):
		return "3:45" 	# Simulated duration

class WAV(AudioFile):
	def play(self):
		print(f"Playing WAV: {self.filename} using WAV decoder")

	def get_duration(self):
		return "4:20" 	# Simulated duration

class FLAC(AudioFile):
	def play(self):
		print(f"Playing MP3: {self.filename} using FLAC decoder")

	def get_duration(self):
		return "5:10" 	# Simulated duration

# Creating Instances and Calling Functions
print("Creating audio files with abstraction:")
mp3_clean = MP3("song.mp3")
wav_clean = WAV("music.wav")
flac_clean = FLAC("audio.flac")

print("\nPlaying files (notice same method name):")
mp3_clean.play()	# Same method name
wav_clean.play()	# Same method name
flac_clean.play()	# Same method name

print("\nGetting file information:")
print(mp3_clean.get_info(), "- Duration:", mp3_clean.get_duration())
print(wav_clean.get_info(), "- Duration:", wav_clean.get_duration())
print(flac_clean.get_info(), "- Duration:", flac_clean.get_duration())

print("\nBenefits of abstraction:")
print("- Same method names (play) for all file types")
print("- Easy to write generic code")
print("- Consistent interface")

# Example: Playing all files in a loop (clean)
print("\nPlaying all files in a loop (clean approach):")
clean_files = [mp3_clean, wav_clean, flac_clean]
for file in clean_files:
	print(f"Now playing: {file.get_info()}")
	file.play()		# Same method name for all!
	print(f"Duration: {file.get_duration()}")
	file.stop()
	print()

print("^ Much cleaner! No if-else statements needed")
print()

# Step 4: Advanced example - Music Playlist
print("STEP 4: Advanced Example - Music Playlist")
print("-" * 40)




