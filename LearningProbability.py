import sys

def main(argv):
    file = open(argv[1])
    totalData = 0.0

    pBaseball = 0.0
    pWatchTVandBaseball = 0.0
    pNoCatFood = 0.0

    cBaseball = 0
    cWatchTVandBaseball = 0
    cWatchTVandNoBaseball = 0
    cNoCatFood = 0
    cFeedNowatchTVNoCatFood = 0
    cFeedWatchTV = 0
    cFeedNoFood = 0
    cFeedWatchTVCatFood = 0
    cWatchTVandCatFood = 0
    cWatchTVandNoCatFood = 0
    cNoWatchTVandCatFood = 0
    cNoWatchTVandNoCatFood = 0

    for line in file:
        totalData+=1
        line = line.split()

        if line[0] == '1':
            cBaseball+=1
            if line[1] == '1':
                cWatchTVandBaseball+=1

        if line[0] == '0':
            if line[1] == '1':
                cWatchTVandNoBaseball+=1

        if line[2] == '1':
            cNoCatFood+=1

        if line[1] == '1' and line[2] == '1':
            cWatchTVandCatFood+=1

        if line[1] == '1' and line[2] == '0':
            cWatchTVandNoCatFood+=1

        if line[1] == '0' and line[2] == '1':
            cNoWatchTVandCatFood+=1

        if line[1] == '0' and line[2] == '0':
            cNoWatchTVandNoCatFood+=1

        if line[1] == '1' and line[2] == '1' and line[3] == '1':
            cFeedWatchTVCatFood+=1

        if line[1] == '1' and line[2] == '0' and line[3] == '1':
            cFeedWatchTV+=1

        if line[1] == '0' and line[2] == '1' and line[3] == '1':
            cFeedNoFood+=1

        if line[1] == '0' and line[2] == '0' and line[3] == '1':
            cFeedNowatchTVNoCatFood+=1

    file.close()

    pBaseball  = cBaseball/totalData
    pWatchTVandBaseball = (cWatchTVandBaseball/totalData)/(pBaseball )
    probability_watch_tv_no_baseball = (cWatchTVandNoBaseball/totalData)/(1-pBaseball )
    pNoCatFood = cNoCatFood/totalData
    pFeedWatchTVCatFood = (cFeedWatchTVCatFood/totalData)/(pWatchTVandBaseball*pNoCatFood)
    pFeedwatchTVNoCatFood = ((cFeedNoFood/totalData)/(cNoWatchTVandCatFood/totalData))
    pFeedwatchTV=((cFeedWatchTV/totalData)/(cWatchTVandNoCatFood/totalData))
    pFeedNoWatchTVNoCatFood =((cFeedNowatchTVNoCatFood/totalData)/(cNoWatchTVandNoCatFood/totalData))
    print 'Probability of Baseball Game on TV'
    print '%.2f' %pBaseball
    print 'Probability that George watches tv given Baseball Game on TV'
    print '%.2f' %pWatchTVandBaseball
    print 'Probability that George watches tv given No Baseball Game on TV'
    print '%.2f' %probability_watch_tv_no_baseball
    print 'Probability that George is out of cat food'
    print '%.2f' %pNoCatFood
    print 'Probability that George feeds cat when he watches tv and is out of cat food'
    print '%.2f' %pFeedWatchTVCatFood
    print 'Probability that George feeds cat when he is out of cat food'
    print '%.2f' %pFeedwatchTVNoCatFood
    print 'Probability that George feeds cat when he watches tv'
    print '%.2f' % pFeedwatchTV
    print 'Probability that George feeds cat when he does not watch tv and is not out of cat food'
    print '%.2f' % pFeedNoWatchTVNoCatFood

if __name__ == '__main__':
    main(sys.argv)
