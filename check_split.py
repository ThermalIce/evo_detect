import sys
from subprocess import call
from min_jaccard import MinJaccard

def Jaccard ( a, b ):
    total_members = 0.0
    matches = 0.0
    for m in a:
        total_members = total_members + 1
        if m in b:
            matches = matches + 1

    for m in b:
        if m not in a:
            total_members = total_members + 1

    #print sorted ( a )
    #print sorted ( b )
    #print float ( matches ) / float ( total_members )
    #print "\n\n\n\n"
            
    return float(matches) / float ( total_members )

#Global helpers
threshold = 0.85 #for matching communities
accurate_runs = 0.0 #counting successes
continuation = 0.0
total_runs = 0.0

def run_single ( communities1, communities2 ):
    global continuation
    global accurate_runs
    global total_runs

    #Read real and detected communities
    gr1 = []
    grspl1 = []
    grspl2 = []
    
    f = open ( communities1 )
    gr1 = [x.strip(" ") for x in f.readline().rstrip("\n").split(" ") if x.strip(" ")]
    gr1[0] = (gr1[0].split(":"))[1]
    f.close()
    
    f = open ( communities2 )
    grspl1 = [x.strip(" ") for x in f.readline().rstrip("\n").split(" ") if x.strip(" ")]
    grspl1[0] = (grspl1[0].split(":"))[1]
    grspl2 = [x.strip(" ") for x in f.readline().rstrip("\n").split(" ") if x.strip(" ")]
    f.close();
    grspl2[0] = (grspl2[0].split(":"))[1]
    
    #If they are close, increase accurate count
    found1 = ( Jaccard ( gr1, grspl1 ) > threshold )
    found2 = ( Jaccard ( gr1, grspl2 ) > threshold )
    
    if ( found1 & found2 ):
        accurate_runs = accurate_runs + 1.0
    elif ( found1 | found2 ):
        continuation = continuation + 1.0
    total_runs = total_runs + 1.0
    f.close()

#Print out the network files to network.dat
for i in range (1, 31, 1):
        #for mp in range (0.5, 1, 0.1):
    dr = "../Networks/EvoTest/Split/20_100_0.8_1.75_0.5_0_1_low/"+ str(i) + "/"
    communities1 = str(dr) + "Communities0.dat"
    communities2 = str(dr) + "Communities1.dat"
    run_single ( communities1, communities2 )        
        
print total_runs
print float ( accurate_runs ) / float ( total_runs )
print float ( continuation ) / float ( total_runs )
