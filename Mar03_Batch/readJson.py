import json
from pathlib import Path

class Test:
    def readjsonaspertest(self, testcase, param):
        with open(str(Path(__file__).parent.parent)+'/testData.json') as f:
            json_data = json.load(f)

            for data in json_data['DockerPageApplicationTesting']:
                element = (str(data[testcase])).split(",")
                for x in element:
                    print(x)
                    if(param in x):
                        break
                return x.split(":")[1].replace('"','').replace("'",'').replace("}",'')


obj = Test()
obj.readjsonaspertest("TC_002", "color")