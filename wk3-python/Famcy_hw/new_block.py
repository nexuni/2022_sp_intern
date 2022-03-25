import Famcy

class new_block(Famcy.FamcyBlock):
	def __init__(self):
		self.value = new_block.generate_template_content()
		super(new_block, self).__init__()
		self.init_block()

	@classmethod
	def generate_template_content(cls):
		"""
		This function returns values that the user can edit in Famcy.
		"""
		return {
		}

	def init_block(self):
		"""
		This function create the html structure of the item by using FElements
		"""
		self.body = Famcy.div()
		self.body["id"] = self.id
		self.body["className"] = "new_block"

		canvas_temp = Famcy.canvas()
		# _h1 = Famcy.h1()
		# _h1["onclick"] = "title_click(this, '"+ str(self.name) +"', '"+ str(self.submission_obj_key) +"')"

		self.body.addElement(canvas_temp)

		import_js_temp = Famcy.script()
		import_js_temp["src"] = "/asset/js/new_block_js.js"

		js_temp = Famcy.script()
		js_temp.innerHTML = "connect_mousedown_action('" + str(self.id) + "', '" + str(self.name) + "', '" + str(self.submission_obj_key) + "')"

		css_temp = Famcy.style()
		css_temp.innerHTML = """
		.new_block canvas{
			height: 30vh;
			width: 30vw;
			border: 1px solid black;
		}
		"""
		self.body.addStaticScript(import_js_temp, position="head")
		self.body.addStaticScript(js_temp)
		self.body.addStaticScript(css_temp)

	def render_inner(self):
		"""
		This function updates values that the user edited
		"""

		return self.body