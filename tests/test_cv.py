
from opencvutils import CameraCalibration
from opencvutils import list_images


def test_checkerboard_calibrate():
	imgs = []
	cal = list_images('./cal_images')
	for im in cal:
		imgs.append(im)
	cal = CameraCalibration(show_markers=False)  # change this to True to see the images with markers found
	cal.marker_checkerboard = True
	cal.save_file = 'calibration.npy'
	mx = cal.calibrate(imgs, marker_size=(9, 6))
	# print('rms', mx['rms'])
	# cal.printMatrix()
	assert (mx['rms'] - 0.5882563398961391) < 1e-6
