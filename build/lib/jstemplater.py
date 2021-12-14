 
import json

class Element:
	def __init__(self,name,attrib=""):
		self.name = name
		self.content = ""
		self.attrib = attrib
		self.close_tag = f"</{name}>"


	def add(self,element):
		self.content += f"{element}"

	def add_attrib(self,key,value):
		self.attrib +=f" {key}='{value}'"

	def set_content(self,content):
		self.content = content
	def __repr__(self):
		self.start_tag = f"<{self.name}{self.attrib}>"
		return f'{self.start_tag}{self.content}{self.close_tag}'


class EElement:
	def __init__(self,name,attrib=""):
		self.name = name
		self.attrib = attrib

	def add_attrib(self,key,value):
		self.attrib +=f' {key}="{value}"'

	def __repr__(self):
		self.start_tag = f"<{self.name}{self.attrib}/>"
		return f'{self.start_tag}'



def setTemplate(root,div,script):
		doctype = "<!DOCTYPE html>"
		html = Element("html")
		head = Element("head")
		body = Element("body")
		css_link = EElement("link")
		css_link.add_attrib("rel","stylesheet")
		css_link.add_attrib("type","text/css")
		css_link.add_attrib("href",f"{root}/css/style.css")

		title = Element("title");
		title.set_content("Web Application")

		head.add(title);
		head.add(css_link);
		html.add(head);
		body.add(div)
		body.add(script);
		html.add(body)
		return f'{doctype}{html}'

class JSTemplate:
	def __init__(self,static_root):
		self.static_root = static_root
		self.initials();


	def initials(self):
		self.script_root = f'{self.static_root}/javascript/src/'
		

	def render(self,script_name,context=''):
		div = Element("div")
		div.add_attrib("id","root")
		if context != '':
			div.add_attrib("data-content",json.dumps(context))
		script = Element("script")
		script.add_attrib("type","module")
		script.add_attrib("src",f"{self.script_root}{script_name}.js")
		return setTemplate(self.static_root,div,script)
