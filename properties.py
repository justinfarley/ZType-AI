class Properties:
    def __init__(self):
        self.fileName = "properties.txt"
        self.region = [0, 0, 0, 0] 
        self.SetProperties()

    def SetProperties(self):
        with open(self.fileName, "r") as properties:
            for line in properties:
                if 'regionX1' in line:
                    self.region[0] = Properties.GetValue(line, 9)
                elif 'regionY1' in line:
                    self.region[1] = Properties.GetValue(line, 9)
                elif 'width' in line:
                    self.region[2] = Properties.GetValue(line, 6)
                elif('height' in line):
                    self.region[3] = Properties.GetValue(line, 7)
                
        
    @staticmethod
    def GetValue(text, sliceNum) -> int:
        value = text[sliceNum:-1]
        return int(value)

p = Properties()
print(p.region)