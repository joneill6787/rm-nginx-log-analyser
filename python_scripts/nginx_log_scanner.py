from pathlib import Path
from collections import Counter

    # Variable Declarations

nginxLog = []
nginxIPAdd = []
nginxReqPath = []
nginxResStatCode = []
nginxUserAgent = []

currentDir = Path(__file__).parent
nginxLogDir = currentDir.parent / "logs"/ "nginx-access.log"

    # Process line by line (generator approach)
def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

    # Convert to list when needed
nginxLog = list(read_lines(nginxLogDir))


def splitNginxLogs(x):

    count = 0
    totalToCheck = len(nginxLog)
    resStatCode = []

    for count in range(totalToCheck):
        nginxIPAdd.append(x[count].split()[0])
        nginxReqPath.append(x[count].split("\"")[1])
        resStatCode.append(x[count].split("\"")[2])
        nginxUserAgent.append(x[count].split("\"")[5])

        nginxResStatCode.append(resStatCode[count].lstrip().rstrip())

def countArray(arrayName,descriptor,totalToCheck):

    counterArray = Counter(arrayName)

    print(f"\t== Top 5 {descriptor}s reported ==\n")
    for value in range(totalToCheck):
        

        print(f"Count: {counterArray.most_common(totalToCheck)[value][1]}"
             f"\t{descriptor}:\t {counterArray.most_common(totalToCheck)[value][0]}")

    print()


def main():

    print()

    splitNginxLogs(nginxLog)
    countArray(nginxIPAdd,"IP Addresse",5)
    countArray(nginxReqPath,"Request Path",5)
    countArray(nginxResStatCode,"Response Code",5)
    countArray(nginxUserAgent,"User Agent",5)



    # Function Declarations

main()