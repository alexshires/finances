import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from pandas import to_datetime


class Item:
    def __init__(_name ,_cost ,_date ,_real=False ,_scenario=0):
        self.name = _name
        self.cost = _cost
        self.date = _date
        self.real = _real
        self.scenario = _scenario
    def write(f):
        line = "%s\t%s\t%s\t%s\t%s\n" % (self.name, self.cost, self.date, self.real, self.scenario)
        f.write(line)

def recreate_file():
    """recreates file"""
    f = open('finances.data' ,'w')
    f.write("Name\tCost\tDate\tReal\tScenario")
    f.close()


def writeItem(item):
    # writes to file
    f = open('finances.data', 'a')
    item.write(f)
    f.close()


def readFile(filename):
    print "reading" , filename
    df = None
    if os.path.exists(filename):
        df = pd.read_csv(filename, sep='\t')
        df['Date'] = to_datetime(df['Date'], format="%d/%m/%y", dayfirst=True)
        df = df.set_index('Date')
        # print df
    else :
        print "nofile"
    return df


def plot(incdf, outdf, scenario=0):
    df2 = outdf[ outdf.Scenario == scenario]
    # print df2
    with PdfPages("testplots.pdf") as pdf:
        x = df2.index
        y = df2.Cost
        y2 = df2.Cost.cumsum()
        print x.tolist()
        print y2.tolist()
        plt.plot_date(x.tolist(), y.tolist())
        plt.minorticks_on()
        pdf.savefig()
        plt.clf()
        plt.plot_date(x.tolist(), y2.tolist())
        plt.minorticks_on()
        pdf.savefig()

def process_file(costfilename, incfilename):
    costdata = readFile(costfilename)
    incdata = readFile(incfilename)
    # print costdata
    # print incdata
    # calculate cumulative values
    # generate weekly series
    from pandas import date_range
    rng = date_range('26/4/15', periods=30, freq='W')
    for i in rng:
        print i
    # TOSO - diff freqeuncy versions
    # costdata["cumul"] = costdata.Cost.cumsum()
    # calculate balance as a function of time
    # find number of scenarios
    # plot income, costs, balance for each
    # ax = plot(incdata, costdata, 0)

    return
