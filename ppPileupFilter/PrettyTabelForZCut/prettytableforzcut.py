from prettytable import PrettyTable
from prettytable import ALL

Lx=PrettyTable(["nTrk","Loose dz(cm)"])
Lx.padding_width = 1
Lx.hrules = ALL

LnTrk = ["0-2","3","4","5","6-8","9","10","11-12","13","14-19","20-30","30+"]
Ldz = ["N/A","4.8","1.9","1.2","0.8","0.6","0.5","0.4","0.3","0.2","0.1","0.0"]

for num in range(len(LnTrk)):
	Lx.add_row([LnTrk[num],Ldz[num]])

print Lx

Tx=PrettyTable(["nTrk","Tight dz(cm)"])
Tx.padding_width = 1
Tx.hrules = ALL

TnTrk = ["0-1","2","3","4","5","6","7","8-10","11-13","14-22","22+"]
Tdz = ["N/A","4.0","1.5","1.0","0.6","0.5","0.4","0.3","0.2","0.1","0.0"]

for num in range(len(TnTrk)):
        Tx.add_row([TnTrk[num],Tdz[num]])

print Tx

CutEff=PrettyTable(["Filter Name","PYTHIA MB","PYTHIA PU2","pp LowPU","pp MB"])
CutEff.padding_width = 1
CutEff.hrules = ALL

Name = ["Base Loose","Base Loose Dz","Base Tight","Base Tight Dz","One Vtx"]
Frac1 = ["0.0001%","0.0001%","0.0043%","0.0035%","1.3305%"]
Frac2 = ["41.693%","1.2785%","50.250%","2.3770%","64.495%"]
Frac3 = ["2.6802%","0.1238%","3.0868%","0.2033%","5.0016%"]
Frac4 = ["22.000%","1.1000%","24.500%","1.7200%","28.500%"]

for numb in range(len(Name)):
         CutEff.add_row([Name[numb],Frac1[numb],Frac2[numb],Frac3[numb],Frac4[numb]])

print CutEff

	
