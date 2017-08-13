# get screen details and then press key on reach result. 
from PIL import ImageGrab
from PIL import Image
import win32gui
import win32api

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


win32gui.EnumWindows(enum_cb, toplist)

trexgame = [(hwnd, title) for hwnd, title in winlist if 'trexgame' in title.lower()]
# just grab the hwnd for first window matching trexgame
trexgame = trexgame[0]
hwnd = trexgame[0]
ramdom = 1000
while True:
	win32gui.SetForegroundWindow(hwnd)
	bbox = win32gui.GetWindowRect(hwnd)
	img = ImageGrab.grab(bbox)
	#img = img.resize((400, 200), Image.ANTIALIAS)
	width = img.size[0]
	height = img.size[1]
	img2 = img.crop(
		(
			80,
			95,
			700,
			250
		)
	)
	img3 = img.crop(
		(
			width - 155,
			100,
			width - 100,
			120
		)
	)
	#img3.show()
	print(img3)
	img3.save("approach/score"+str(ramdom)+".jpg")
	ramdom = ramdom + 1
	if(ramdom > 2000):
		break;
	#img3.show()
	# Get All the details in number , then send it into Tensorflow
	# get result form the tensorflow 
	#based on the result - either 
#	if jump:
#		win32api.keybd_event(0x20, 0,0,0)

	