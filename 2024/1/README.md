# Part 
`paste <(tr -s " " < input.txt | cut -d " " -f1 | sort -n) <(tr -s " " < input.txt | cut -d " " -f2 | sort -n) | awk '{x=$1-$2;if(x<0){x=-x}sum+=x}END{print sum}'`

# Part | Column1 | Column2 | Column3 | Column4 |
`join -11 -22 <(tr -s " " < input.txt  | cut -d " " -f1 | sort -n) <(tr -s " " < input.txt | cut -d " " -f2 | sort -n | uniq -c) | awk '{x+=$1*$2}END{print x}'`

