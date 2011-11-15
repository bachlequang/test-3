#tail -n number count.txt
#tail -f count.txt




import sys,time,os


def tail_n_lines(filename,linesback,returnlist):
    avgcharsperline=75
    file = open(filename,'r')
    while True:
        try: 
		file.seek(-1*avgcharsperline * linesback,2)
        except IOError: file.seek(0,0)
        if file.tell() == 0: 
		atstart=1
        else: atstart=0

        lines=file.read().split("\n")
        if (len(lines) > (linesback+1)) or atstart: 
		break
        avgcharsperline=avgcharsperline * 1.3
    file.close()

    if len(lines) > linesback: 
	    start=len(lines)-linesback -1
    else: 
	    start=0
    if returnlist: 
	    return lines[start:len(lines)-1]

    out=""
    for l in lines[start:len(lines)]: 
	    out=out + l + "\n"
    return out



if len(sys.argv) > 3:
    if sys.argv[1]=="-n":
        g=int(sys.argv[2])
        g1=str(sys.argv[3])
        print tail_n_lines(g1,g-1,0)
else:
    if len(sys.argv) ==3:
        if sys.argv[1] == "-f":
            g1=str(sys.argv[2])
            file=open(g1,'r')
            print tail_n_lines(g1,9,0)
            st_results = os.stat(g1)
            st_size = st_results[5]
            file.seek(st_size)
            while True:
                where = file.tell()
                line = file.readline()
                if not line:
                    time.sleep(0)
                    file.seek(where)
                else:
                    print line,
                   