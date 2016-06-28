import csv

print "; -*- ledger -*-"
print ""
print "2016/01/01 * Opening Balances"
print "    Assets:Polo                    0 DASH"
print ""

print "P 2016/06/27 01:00:00 USDT $1.0"
print "P 2016/06/27 01:00:00 USD $1.0"
print "P 2016/06/27 01:00:00 BTC $660.0"
print "P 2016/06/27 01:00:00 DASH $7.09"
print "P 2016/06/27 01:00:00 LTC $4.20"
print "P 2016/06/27 01:00:00 ETH $13.80"
print "P 2016/06/27 01:00:00 DAO $0.103786829"
print "P 2016/06/27 01:00:00 LSK $0.313804287"
print ""

with open('tradeHistory.csv', 'rb') as csvfile:
    sr = csv.reader(csvfile, delimiter=',')
    for row in sr:
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
        print "    Expense:TradeFee    %s" % cost
        print ""

