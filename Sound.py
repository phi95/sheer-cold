import simpleaudio as sa

def playAlarm(tempCondition):
    wave_obj = sa.WaveObject.from_wave_file("C:/Users/huann_000/Desktop/SheerCold/test.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()


