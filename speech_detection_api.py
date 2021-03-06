"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import os
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()
object = "Car"
# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="There is a " + object + " ahead")

# Build the voice request, select the language code and the ssml
# voice gender
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-AU',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)

    outputSpJson = response.audio_content
    return outputSpJson