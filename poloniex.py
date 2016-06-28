import csv
import datetime

print "; -*- ledger -*-"
print ""
print "2016/01/01 * Opening Balances"
print "    Assets:Polo                    $0"
print ""

nowstr = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

print "P %s USDT $1.0" % nowstr
print "P %s BTC $655.0" % nowstr
print "P %s DASH $7.09" % nowstr
print "P %s LTC $4.20" % nowstr
print "P %s ETH $13.80" % nowstr
print "P %s DAO $0.1038" % nowstr
print "P %s LSK $0.3138" % nowstr
print ""

with open('tradeHistory.csv', 'rb') as csvfile:
    th = csv.reader(csvfile, delimiter=',')
    for row in th:
        if row[0] == "Date":
            continue
        date = row[0].split(" ")[0]
        base, quote = row[1].split("/")
        #row[2] == category
        side = row[3]
        price = "{0:.8f} {1}".format(float(row[4]), quote)
        if side == "Buy":
            ba = float(row[5])
            bc = base
            bf = abs(ba - abs(float(row[10])))
            sa = float(row[6])
            sc = quote
            sf = abs(sa - abs(float(row[9])))
        else:
            ba = float(row[6])
            bc = quote
            bf = abs(ba - abs(float(row[9])))
            sa = float(row[5])
            sc = base
            sf = abs(sa - abs(float(row[10])))

        br = ba - bf
        sr = sa - sf

        if bf != 0:
            cost = "{0:.8f} {1}".format(bf, bc)
        else:
            cost = "{0:.8f} {1}".format(sf, sc)

        #P 2016/06/15 BTC 700 USD
        print "P %s %s %s" % (date, base, price)
        #2016/06/15 Polo trade (1 BTC = 700 USD)
        print "%s Polo %s on %s" % (date, side, row[1])
        #print "    ; raw buy fee {0:.8f} {1}".format(bf, bc)
        #print "    ; raw sell fee {0:.8f} {1}".format(sf, sc)
        print "    Assets:Polo:{0}    {1:.8f} {2}".format(bc, br, bc)
        print "    Currency:{0}   {1:.8f} {2}".format(bc, -ba, bc)
        print "    Assets:Polo:{0}    {1:.8f} {2}".format(sc, -sr, sc)
        print "    Currency:{0}   {1:.8f} {2}".format(sc, sa, sc)
        print "    Expenses:TradeFee    %s" % cost
        print ""

with open('depositHistory.csv', 'rb') as csvfile:
    dh = csv.reader(csvfile, delimiter=',')
    for row in dh:
        if row[0] == "Date":
            continue
        date = row[0].split(" ")[0]
        #2016/06/15 Polo trade (1 BTC = 700 USD)
        print "%s Polo deposit" % date
        print "    ; address %s" % row[3]
        #print "    ; raw sell fee {0:.8f} {1}".format(sf, sc)
        print "    Assets:Polo:{0}    {1:.8f} {2}".format(row[1], float(row[2]), row[1])
        print "    Equity:Wallet:{0}   {1:.8f} {2}".format(row[1], -float(row[2]), row[1])
        print ""

with open('withdrawalHistory.csv', 'rb') as csvfile:
    wh = csv.reader(csvfile, delimiter=',')
    for row in wh:
        if row[0] == "Date":
            continue
        date = row[0].split(" ")[0]
        #2016/06/15 Polo trade (1 BTC = 700 USD)
        print "%s Polo withdrawal" % date
        print "    ; address %s" % row[3]
        #print "    ; raw sell fee {0:.8f} {1}".format(sf, sc)
        print "    Assets:Polo:{0}    {1:.8f} {2}".format(row[1], -float(row[2]), row[1])
        print "    Equity:Wallet:{0}   {1:.8f} {2}".format(row[1], float(row[2]), row[1])
        print ""

