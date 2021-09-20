from report import Report


class Report1(Report):
	def get_name(self):
		return 'awesome report'

	def render(self):
		return 'render'

	def get_data(self):
		return 'get data'

