class Tag(object):
  def __init__(self, name, content):
    self.start = "<{}>".format(name)
    self.end = "<\{}>".format(name)
    self.content = content

  def __str__(self):
    return "{0.start}\n{0.content}\n{0.end}".format(self)

  def display(self, file=None):
    print(self, file=file)

class DocType(Tag):
  def __init__(self):
    super().__init__("!DOCTYPE HTML PUBLIC -//W3C//DTD HTML 4.01//EN" , '')
    self.end = '' #DocType doesnt take end tag
    
class Head(Tag):
  def __init__(self):
    super().__init__('head', '')
    self.h_cont = []
    self.tittle = Tag("tittle", "this is a tittle")
  
  def dispalay(self, file=None):
    for t in self.h_cont:
      self.content += str(t)

    super.display(file=file)


class Body(Tag):
  def __init__(self):
    super().__init__('body', '')
    self.body_cont = []

  def add_tag(self, name, content):
    n_tag = Tag(name, content)
    self.body_cont.append(n_tag)

  def display(self, file=None):
    for t in self.body_cont:
      self.content += str(t)

    super().display(file=file)

class HTMLdoc(object):
  def __init__(self):
    self.doc_type = DocType()
    self.head = Head()
    self.body = Body()

  def add_tag(self, name, content):
    self.body.add_tag(name, content)

  def display(self, file=None):
    self.doc_type.display(file=file)
    print("<html>", file=file)
    self.head.display(file=file)
    self.body.display(file=file)
    print("</html>", file=file)




if __name__ == "__main__":
  page = HTMLdoc()
  page.add_tag("h1", "main heading")
  page.add_tag("h2", "other heading")
  page.add_tag("p", "this is a paragraph")
  with open("file.html", 'w') as f:
    page.display(file=f)

