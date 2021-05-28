import pyaudio
import wave

def play():
    filename = 'recorded.wav'

    chunk = 1024

    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data = wf.readframes(chunk)
    print('Playing...')
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    print('Finished playing.')
    stream.close()
    p.terminate()