class Cat():
  def __init__(self, name, files):
    self.files = files
    self.name = name

  def run(self):
    for file in self.files:
      with open(file) as f:
        for line in f:
          print line,

  def greet():
    print """
   /\     /\\
  {  `---'  }
  {  O   O  }
  ~~>  V  <~~   Hello, %s!
   \  \|/  /
    `-----'__
    /     \  `^\_
   {       }\ |\_\_   W
   |  \_/  |/ /  \_\_( )
    \__/  /(_E     \__/
      (  /
       MM
       """%self.name
