# PyAudio Documentation

URL: https://people.csail.mit.edu/hubert/pyaudio/docs/index.html

翻译：

----

内容：

PyAudio 文档

简介
例子：阻断模式　Audio I/O
例子：回调模式  Audio I/O
概况
细节

PyAudio类
Stream类
平台说明

索引和列表

---
### 简介

PyAudio提供Python绑定PortAudio的跨平台音频输入输出库。通过它，可以很容易使用Python在多个平台上播放和录制音频。PyAudio有两个优秀的组件：

+ pyPortAudio/fastaudio: Python绑定PortAudio v18 应用接口
+ tkSnack: 适用于Tcl/TK和Python的跨平台声音工具集

### 例子：阻断模式音频I/O
`
"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
	    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
		    sys.exit(-1)

			wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
				                rate=wf.getframerate(),
								                output=True)

# read data
data = wf.readframes(CHUNK)

# play stream (3)
while len(data) > 0:
	    stream.write(data)
		    data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()

`

(1)使用PyAudio，首先要实例化PyAudio，通过用pyaudio.PyAudio()设置portaudio系统。

(2)为录制或播放音频，可以使用相应的音频参数，打开目标设备的数据流，可用pyaudio.PyAudio.open。这样设置一个pyaudio.Stream来播放或录制音频。

(3)使用pyaudio.Steam.write()通过将音频数据写入流来播放音频，或使用pyaudio.Stream.read()从流中读取音频数据。

注意，阻断模式中，每一个pyaudio.Steam.write() 或
pyaudio.Stream.read()都阻断,直到所有给出或请求的帧（frames)播完或录完。相应地，为了在生成音频数据，或立即处理录音数据，需使用后面的“回调模式”。


### 例子：回调模式音频I/O

`
"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import wave
import time
import sys

if len(sys.argv) < 2:
	print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
		sys.exit(-1)

			wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
	data = wf.readframes(frame_count)
	return (data, pyaudio.paContinue)

# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
				channels=wf.getnchannels(),
				rate=wf.getframerate(),
				output=True,
				stream_callback=callback)

# start the stream (4)
stream.start_stream()

# wait for stream to finish (5)
while stream.is_active():
	time.sleep(0.1)

# stop stream (6)
stream.stop_stream()
stream.close()
wf.close()

# close PyAudio (7)
p.terminate()
`
在回调模式中，PyAudio将调用一个指定的callback函数(2)，每当其需要新的音频数据或获取到新的音频数据时。

需注意的是，PyAudio是在另一个线程中调用callback函数。其具有以下形式：`callback(<input_data>,
<frame_count>, <time_info>,
<status_flag>)`，并返回一个元组，包含`frame_count`音频数据帧数和一个代表是否有更多播放或录制帧的标记。

pyaudio.Steam.start_steam()(4)开始处理音频流，直到函数返回pyaudio.paComplete，将不断重新调用回调函数。

为保持流处于活动状态，主线程必须不能被终止，如被休眠(5)。

### 概览

类　
	PyAudio, Stream

主机指定类
	PaMacCoreStreamInfo　

流转换函数
	get_sample_size(), get_format_from_width()

PortAudio 版本
	get_portaudio_version(), get_portaudio_version_text()

Portaudio 样本格式
	paFloat32, paInt32, paInt24, paInt16, paInt8, paUInt8,
	paCustomFormat

PortAudio 主机API
	paInDevelopment, paDirectSound, paMME, paASIO, paSoundManager,
	paCoreAudio, paOSS, paALSA, paAL, paBeOS, paWDMKS, paJACK,
	paWASAPI, paNoDevice

PortAudio 错误代码
	paNoError, paNotInitialized, paUnanticipatedHostError,
	paInvalidChannelCount, paInvalidSampleRate,
	paInvalidDevice, paInvalidFlag, paSampleFormatNotSupported,
	paBadIODeviceCombination, paInsufficientMemory,
	paBufferTooBig, paBufferTooSmall, paNullCallback,
	paBadStreamPtr, paTimedOut, paInternalError,
	paDeviceUnavailable,
	paIncompatibleHostApiSpecificStreamInfo, paStreamIsStopped,
	paStreamIsNotStopped, paInputOverflowed,
	paOutputUnderflowed, paHostApiNotFound, paInvalidHostApi,
	paCanNotReadFromACallbackStream,
	paCanNotWriteToACallbackStream,
	paCanNotReadFromAnOutputOnlyStream,
	paCanNotWriteToAnInputOnlyStream,
	paIncompatibleStreamHostApi

PortAudio 回调返回代码
	paContinue, paComplete, paAbort

PortAudio 回调标志
	paInputUnderflow, paInputOverflow,
	paOutputUnderflow, paOutputOverflow,
	paPrimingOutput 

### 详细

	pyaudio.get_from_width(width, unsigned=True)
    返回一个 PortAudio 格式常量，代表指定宽度.
	参数  : width – 希望的样本宽度，以字节为单位 (1, 2, 3, 或 4)
	        unsigned – 对1字节宽，指定有符号或无符号标格式。
    Raises: ValueError – when invalid width
	Return type: A PortAudio Sample Format constant

	pyaudio.get_portaudio_version()
	Returns portaudio version.
	Return type:	string

	pyaudio.get_portaudio_version_text()
	Returns PortAudio version as a text string.
	Return type:	string

	pyaudio.get_sample_size(format)
	Returns the size (in bytes) for the specified sample format.
															    Parameters:
																format – A
																PortAudio
																Sample Format
																constant.
																    Raises:
																	ValueError
																	– on
																	invalid
																	specified
																	format.
																	    Return
																		type:
																		integer

																		pyaudio.paAL
																		= 9

																		    Open
																			Audio
																			Library

																			pyaudio.paALSA
																			= 8

																			    Advanced
																				Linux
																				Sound
																				Architecture
																				(Linux
																				only)

																				pyaudio.paASIO
																				=
																				3

																				    Steinberg
																					Audio
																					Stream
																					Input/Output

																					pyaudio.paAbort
																					=
																					2

																					    An
																						error
																						ocurred,
																						stop
																						playback/recording

																						pyaudio.paBeOS
																						=
																						10

																						    BeOS
																							Sound
																							System

																							pyaudio.paComplete
																							=
																							1

																							    This
																								was
																								the
																								last
																								block
																								of
																								audio
																								data

																								pyaudio.paContinue
																								=
																								0

																								    There
																									is
																									more
																									audio
																									data
																									to
																									come

																									pyaudio.paCoreAudio
																									=
																									5

																									    CoreAudio
																										(OSX
																										only)

																										pyaudio.paCustomFormat
																										=
																										65536

																										    a
																											custom
																											data
																											format

																											pyaudio.paDirectSound
																											=
																											1

																											    DirectSound
																												(Windows
																												only)

																												pyaudio.paFloat32
																												=
																												1

																												    32
																													bit
																													float

																													pyaudio.paInDevelopment
																													=
																													0

																													    Still
																														in
																														development

																														pyaudio.paInputOverflow
																														=
																														2

																														    Buffer
																															overflow
																															in
																															input

																															pyaudio.paInputUnderflow
																															=
																															1

																															    Buffer
																																underflow
																																in
																																input

																																pyaudio.paInt16
																																=
																																8

																																    16
																																	bit
																																	int

																																	pyaudio.paInt24
																																	=
																																	4

																																	    24
																																		bit
																																		int

																																		pyaudio.paInt32
																																		=
																																		2

																																		    32
																																			bit
																																			int

																																			pyaudio.paInt8
																																			=
																																			16

																																			    8
																																				bit
																																				int

																																				pyaudio.paJACK
																																				=
																																				12

																																				    JACK
																																					Audio
																																					Connection
																																					Kit

																																					pyaudio.paMME
																																					=
																																					2

																																					    Multimedia
																																						Extension
																																						(Windows
																																						only)

																																						pyaudio.paNoDevice
																																						=
																																						-1

																																						    Not
																																							actually
																																							an
																																							audio
																																							device

																																							pyaudio.paOSS
																																							=
																																							7

																																							    Open
																																								Sound
																																								System
																																								(Linux
																																								only)

																																								pyaudio.paOutputOverflow
																																								=
																																								8

																																								    Buffer
																																									overflow
																																									in
																																									output

																																									pyaudio.paOutputUnderflow
																																									=
																																									4

																																									    Buffer
																																										underflow
																																										in
																																										output

																																										pyaudio.paPrimingOutput
																																										=
																																										16

																																										    Just
																																											priming,
																																											not
																																											playing
																																											yet

																																											pyaudio.paSoundManager
																																											=
																																											4

																																											    SoundManager
																																												(OSX
																																												only)

																																												pyaudio.paUInt8
																																												=
																																												32

																																												    8
																																													bit
																																													unsigned
																																													int

																																													pyaudio.paWASAPI
																																													=
																																													13

																																													    Windows
																																														Vista
																																														Audio
																																														stack
																																														architecture

																																														pyaudio.paWDMKS
																																														=
																																														11

																																														    Windows
																																															Driver
																																															Model
																																															(Windows
																																															only)

`
