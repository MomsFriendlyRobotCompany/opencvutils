
from opencvutils.video import CameraCalibration

def test_checkerboard_calibrate():
	imgs = [
		'cal_images/shot_000.png',
		'cal_images/shot_001.png',
		'cal_images/shot_002.png',
		'cal_images/shot_003.png',
		'cal_images/shot_004.png',
		'cal_images/shot_005.png',
		'cal_images/shot_006.png',
		'cal_images/shot_007.png',
		'cal_images/shot_008.png',
		'cal_images/shot_009.png',
		'cal_images/shot_010.png',
		'cal_images/shot_011.png',
		'cal_images/shot_012.png',
		'cal_images/shot_013.png'
	]
	cal = CameraCalibration()
	cal.marker_checkerboard = True
	cal.save_file = 'calibration.npy'
	mx = cal.calibrate(imgs, marker_size=(9, 6))
	# print('rms', mx['rms'])
	# cal.printMatrix()
	assert mx['rms'] == 0.5882563398961391