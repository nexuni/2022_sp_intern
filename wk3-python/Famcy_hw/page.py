import Famcy
from .new_block import new_block

class week3Page(Famcy.FamcyPage):
	def __init__(self):
		super(week3Page, self).__init__()

		# for declaration
		# ===============
		self.card_1 = self.card1()
		self.layout.addWidget(self.card_1, 0, 0)

		_css = Famcy.style()
		_css.innerHTML = """
		.table_holder td{
			color: pink;
		}
		"""

		self.body.addStaticScript(_css)
		
	# background task function 
	# ====================================================
	# ====================================================
	# ====================================================


	# card
	# ====================================================
	def card1(self):
		_card1 = Famcy.FamcyCard()

		_input_form = Famcy.input_form()

		_new_block = new_block()
		_new_block.connect(self.alert_pos)
		_new_block.clickable = False

		_input_form.layout.addWidget(_new_block, 0, 0)

		_table = Famcy.table_block()

		_card1.layout.addWidget(_input_form, 0, 0)
		_card1.layout.addWidget(_table, 1, 0)

		return _card1
	# ====================================================
	# ====================================================


	# prompt card
	# ====================================================
	# ====================================================
	# ====================================================


	# submission function
	# ====================================================
	def alert_pos(self, obj, info):
		return Famcy.UpdateAlert(alert_message=info[0], target=self)
	# ====================================================
	# ====================================================
		

	# http request function
	# ====================================================
	# ====================================================
	# ====================================================


	# utils
	# ====================================================
	# ====================================================
	# ====================================================

week3Page.register("/week3Example", Famcy.ClassicStyle(), permission_level=0, background_thread=False)



