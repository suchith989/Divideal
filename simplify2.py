
class simplify:
    @staticmethod
    def simplify(balance_sheet):
        #Make net values array with
        net = [-170,1100,200,-900,-700,285,335,100,-625,375]
        # for main in balance_sheet:
        #     total_net = 0
        #     for key in balance_sheet[main]:
        #         total_net += balance_sheet[main][key]
        #     net.append(round(total_net,2))
        print(net)
        keys = list(balance_sheet.keys())
        # sheet = {k: {} for k in keys}
        sheet = simplify.make_simplify(balance_sheet,net,keys)
        #print(sheet)
        return sheet

    @staticmethod
    def make_simplify(sheet,net,keys):
        maxCredit = net.index(max(net))
        maxDebit = net.index(min(net))
        while net[maxCredit] != 0  and net[maxDebit] !=0:
        	deduction = min(net[maxCredit],-net[maxDebit])
        	net[maxCredit] -= deduction
        	net[maxDebit] += deduction
        	sheet[ keys[maxCredit] ][ keys[maxDebit] ] = deduction
        	sheet[ keys[maxDebit] ][ keys[maxCredit] ] = -deduction
        	maxCredit = net.index(max(net))
        	maxDebit = net.index(min(net))

        return sheet


if __name__ == "__main__":
    # balance_sheet = {'U1': {'U1': 0.0, 'U3': -98.33, 'U6': 65.0, 'U8': 151.67000000000002, 'U7': -73.35, 'U2': -88.32999999999998, 'U4': 61.67, 'U5': -38.33, 'U9': 25.0, 'U10': -175.0}, 'U2': {'U7': 11.669999999999987, 'U1': 88.32999999999998, 'U2': 0.0, 'U3': -200.0, 'U4': 200.0, 'U5': 200.0, 'U6': 200.0, 'U8': 200.0, 'U9': 200.0, 'U10': 200.0}, 'U3': {'U1': 98.33, 'U7': -148.33, 'U2': 200.0, 'U3': 0.0, 'U4': 50.0, 'U5': -50.0, 'U6': 50.0}, 'U4': {'U7': -188.33, 'U1': -61.67, 'U2': -200.0, 'U6': -200.0, 'U8': -200.0, 'U3': -50.0}, 'U5': {'U7': -188.33, 'U1': 38.33, 'U2': -200.0, 'U10': -400.0, 'U3': 50.0, 'U5': 0.0}, 'U6': {'U1': -65.0, 'U2': -200.0, 'U4': 200.0, 'U6': 0.0, 'U7': 400.0, 'U3': -50.0}, 'U7': {'U7': 0.0, 'U2': -11.669999999999987, 'U5': 188.33, 'U4': 188.33, 'U1': 73.35, 'U3': 148.33, 'U8': 148.33, 'U6': -400.0}, 'U8': {'U1': -151.67000000000002, 'U7': -148.33, 'U2': -200.0, 'U4': 200.0, 'U8': 0.0, 'U9': 400.0}, 'U9': {'U2': -200.0, 'U1': -25.0, 'U8': -400.0}, 'U10': {'U2': -200.0, 'U1': 175.0, 'U5': 400.0, 'U10': 0.0}}
    # balance_sheet = {'Karthik': {}, 'Sahaja': {}, 'Suchith': {}}
    persons = ["Suchith", "Sahaja", "Dad","Home","Mom","Karthik","Boo","Ramu","Waj","Rassu"]
    balance_sheet = {k: {} for k in persons}

    # print(balance_sheet)
    sly = simplify()
    sheet =sly.simplify(balance_sheet)
    print(sheet)