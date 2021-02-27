import Augmentor

class data_augment():
	def __init__(self):
		self.data_folder_path = 'D:/POC Projects/TATA Power Mumbai/New Dataset 10Dec2020/sample_data/'

	def data_preprocessing_and_generation(self):
		p = Augmentor.Pipeline(self.data_folder_path)

		p.rotate90(probability=0.5)
		p.rotate270(probability=0.5)
		p.zoom_random(probability=0.5, percentage_area=0.8)
		p.flip_left_right(probability=0.4)
		p.flip_top_bottom(probability=0.3)
		p.crop_random(probability=0.5, percentage_area=0.5)
		p.resize(probability=1.0, width=800, height=800)

		p.sample(200)

		p.process()

if __name__ == '__main__':
	aug = data_augment()
	aug.data_preprocessing_and_generation()