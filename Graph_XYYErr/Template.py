OutPutCodeName="Current_vs_ClusterSize_All3Eta"

datapath="/home/ramkrishna/PhD_New_Dir_16July2016/GEM/GEM_TB/TB_2014/TestBeamAnalysisAllStudy/MakeClusterSizeDistributionPlot/"

InputData=["Cluster_Size_WithDiff_Area_R1592_R1646_GE11_IV_GIF.dat","Cluster_Size_WithDiff_Area_R1869_R1903_GE11_IV_GIF.dat","Cluster_Size_WithDiff_Area_R2065_R2123_GE11_IV_GIF.dat"]

xlabel="Current Supplied to HV Divider (#mu A)"
ylabel="Cluster Size"

VarInTextFile=["IterNbX","IterNbY","PreShif2X"]  # Each element of list corresponds to one column of intput text file

VarToPlot=[]

GraphTitle="Current Vs Cluster Size"	

tlatexx = [
	"Run Range: 2065-2123",
	"(i#eta,i#phi)=(1,2)",
	"Latency = 17"
	]

legends = [
	"(i#eta,i#phi)=(5,2)",
	"(i#eta,i#phi)=(8,2)",
	"(i#eta,i#phi)=(1,2)"
	]
	
iffit = 1
fitfunction = "pol3"
fitXrange = [750,830]

yrange=[1.0,5.0]	# Y range

xscaleFactor=0.0	# if you don't want to scale x-values then put it = 0.0
yscaleFactor=0.0	# if you don't want to scale y-values then put it = 0.0

pos1=0.15		# Legend x pos
pos2=0.83		# Legend y pos
sep=6.5			# y-distance b/w two legends fraction
cpos1=00.11		# CMS Prem x pos
cpos2=0.91		# CMS Prem y pos
cpos3=0.80		# DetInfo position
DetInfo="GE11-IV"	# Detector Info


xoffset=1.2		# X-offset
yoffset=0.9		# Y-offset

setMaxdigit=4		# SetMaximumDigit
getstat=0		# GetStats
