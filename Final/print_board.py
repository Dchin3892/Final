from coordinate_chart import coordinate_chart

def create_board():
    return [" "]*128

def print_board(space):
    print(f"""
                Your Targets                    Your Ships/AI targets
     8 {space[56]} | {space[57]} | {space[58]} | {space[59]} | {space[60]} | {space[61]} | {space[62]} | {space[63]}      8 {space[120]} | {space[121]} | {space[122]} | {space[123]} | {space[124]} | {space[125]} | {space[126]} | {space[127]}
      -------------------------------      -------------------------------
     7 {space[48]} | {space[49]} | {space[50]} | {space[51]} | {space[52]} | {space[53]} | {space[54]} | {space[55]}      7 {space[112]} | {space[113]} | {space[114]} | {space[115]} | {space[116]} | {space[117]} | {space[118]} | {space[119]}
      -------------------------------      -------------------------------
     6 {space[40]} | {space[41]} | {space[42]} | {space[43]} | {space[44]} | {space[45]} | {space[46]} | {space[47]}      6 {space[104]} | {space[105]} | {space[106]} | {space[107]} | {space[108]} | {space[109]} | {space[110]} | {space[111]}
      -------------------------------      -------------------------------
     5 {space[32]} | {space[33]} | {space[34]} | {space[35]} | {space[36]} | {space[37]} | {space[38]} | {space[39]}      5 {space[96]} | {space[97]} | {space[98]} | {space[99]} | {space[100]} | {space[101]} | {space[102]} | {space[103]}
      -------------------------------      -------------------------------
     4 {space[24]} | {space[25]} | {space[26]} | {space[27]} | {space[28]} | {space[29]} | {space[30]} | {space[31]}      4 {space[88]} | {space[89]} | {space[90]} | {space[91]} | {space[92]} | {space[93]} | {space[94]} | {space[95]}
      -------------------------------      -------------------------------
     3 {space[16]} | {space[17]} | {space[18]} | {space[19]} | {space[20]} | {space[21]} | {space[22]} | {space[23]}      3 {space[80]} | {space[81]} | {space[82]} | {space[83]} | {space[84]} | {space[85]} | {space[86]} | {space[87]}
      -------------------------------      -------------------------------
     2 {space[8]} | {space[9]} | {space[10]} | {space[11]} | {space[12]} | {space[13]} | {space[14]} | {space[15]}      2 {space[72]} | {space[73]} | {space[74]} | {space[75]} | {space[76]} | {space[77]} | {space[78]} | {space[79]}
      -------------------------------      -------------------------------
     1 {space[0]} | {space[1]} | {space[2]} | {space[3]} | {space[4]} | {space[5]} | {space[6]} | {space[7]}      1 {space[64]} | {space[65]} | {space[66]} | {space[67]} | {space[68]} | {space[69]} | {space[70]} | {space[71]}
       1   2   3   4   5   6   7   8        1   2   3   4   5   6   7   8
        
        """)

def add_to_board(board, target, symbol):
  board[coordinate_chart[target]] = symbol

def add_to_board2(board, target, symbol):
  board[(coordinate_chart[target] + 64)] = symbol