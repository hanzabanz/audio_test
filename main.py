from psychopy import core, visual
from psychopy import event as evt
from psychopy.iohub import ioHubExperimentRuntime
from psychopy import data
from psychopy import microphone
import random
import time



# class ExperimentRuntime(ioHubExperimentRuntime):
#
#     def run(self, *args):

exp = data.ExperimentHandler(name='exp', version='1.0', extraInfo={'participant':0},
                             runtimeInfo=None, originPath=None, savePickle=True, saveWideText=True,
                             dataFileName='datafile')

microphone.switchOn(sampleRate=16000)
name = "speech_exp_0.wav"
mic = microphone.AdvAudioCapture(filename=name)
mic.setMarker(tone=5000, secs=0.015, volume=0.03)
mic.record(5.5, block=False)

beg_time = time.time()
while time.time() < beg_time+5:
    mic.playMarker()
    exp.addData("time", time.time())
    time.sleep(1)


mic.stop()


####### Main Script Launching Code #######

# if __name__ == "__main__":
#
#     def main():
#         runtime = ExperimentRuntime("", "experiment_config.yaml")
#         runtime.start()
#
#     main()

