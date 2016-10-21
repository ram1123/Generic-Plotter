#! /usr/bin/env python2.6

import sys
import ROOT as rt

from Template import *

######################
#  Print C++ header  #
######################


sys.stdout = open(OutPutCodeName+".C",'w')

ColorChoice = ["kRed","kBlue","kGreen+3","kPink+5"]

print "// ############################################################"
print "// # Usage                                                    #"
print "// #                                                          #"
print "// ############################################################"
print ''
print '#include "TGraphErrors.h"'
print '#include "setTDRStyle.C"'
print ''
print ''

print 'void %s(){'%OutPutCodeName
print '\tifstream in;'
print ''
print '\t// Set TDR Style'
print '\tsetTDRStyle();'
print ''
print '\tTGaxis::SetMaxDigits(%i);'%setMaxdigit
print '\tgStyle->SetOptStat(%i);'%getstat
print '\tgStyle->SetOptFit(%i);'%getstat
print ''
print '\t//Define the variables'
print '\tFloat_t ',', '.join(VarInTextFile),' ;'
pre = "v_"
Pre_VarInTextFile = [pre + x for x in VarInTextFile ]
#print Pre_VarInTextFile
if len(VarToPlot) == 0:
	VarToPlot = VarInTextFile
Pre_VarToPlot = [pre + x for x in VarToPlot ]
#print "\n\n",Pre_VarToPlot,"\n\n"
print '\tvector<Float_t> ',', '.join(Pre_VarInTextFile),' ;'
print ''
print ''
print '\tInt_t nlines = 0;'
print '\tTFile *f = new TFile("%s.root","RECREATE");'%OutPutCodeName
print '\tTNtuple *ntuple = new TNtuple("ntuple","data from ascii file","',':'.join(VarInTextFile),'");'
print ''
print ''
print '\tTCanvas* c1 = new TCanvas("c1","",1);'
print '\tc1->Range(0,0,1,1);'
print '\tTPad *pad = new TPad("pad","",0,0,1,1);'
print '\tpad->SetGrid();'
print '\tpad->Draw();'
print '\tpad->cd();'
print ''
print ''

print '\tstring line;'
for f in range(0,len(InputData)):
	#print InputData[f]
	print '\tin.open("%s%s");'%(datapath,InputData[f])
	print '\twhile(getline(in,line))'
	print '\t{'
	print "\t\tif(line[0] == '#') continue;"
	print '\t\t'
	print '\t\tstringstream(line) >>',' >> '.join(VarInTextFile),';'
	print '\t\t'
	print '\t\tcout<<"===> "<<',' <<"\\t" <<  '.join(VarInTextFile),'<<endl;'
	print ''
	for var in range(0,len(VarInTextFile)):
		if (xscaleFactor != 0.0 and yscaleFactor != 0.0):
			if (var == 0):
				print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],xscaleFactor)
			else:
				print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],yscaleFactor)
		else:
			if (xscaleFactor != 0.0 ):
				if (var == 0):
					print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],xscaleFactor)
				else:
					print '\t\t%s.push_back(%s);'%(Pre_VarInTextFile[var],VarInTextFile[var])
			else:
				if (yscaleFactor != 0.0 ):
					if (var == 0):
						print '\t\t%s.push_back(%s);'%(Pre_VarInTextFile[var],VarInTextFile[var])
					else:
						print '\t\t%s.push_back(%s/%0.15f);'%(Pre_VarInTextFile[var],VarInTextFile[var],yscaleFactor)
				else:
					print '\t\t%s.push_back(%s);'%(Pre_VarInTextFile[var],VarInTextFile[var])
	print '\t\tntuple->Fill(',' , '.join(VarInTextFile),');'
	print '\t}'
	
	print '\tin.close();'
	print '\t'
	print '\tTGraphErrors * gr%i = new TGraphErrors(%s.size()); '%(f,Pre_VarInTextFile[0])
	print '\t    '
	print '\tfor (unsigned int i = 0; i<%s.size();i++)'%Pre_VarInTextFile[0]
	print '\t{'
	#print '\t       gr%i->SetPoint(i,%s[i],%s[i]);'%(f,Pre_VarInTextFile[0],Pre_VarInTextFile[1])
	print '\t        gr%i->SetPoint(i,%s[i],%s[i]);'%(f,Pre_VarToPlot[0],Pre_VarToPlot[1])
	if (len(Pre_VarToPlot)==3):
		print '\t        gr%i->SetPointError(i,0,%s[i]);'%(f,Pre_VarToPlot[2])
	else:
		print '\t        gr%i->SetPointError(i,0,0);'%f
	print '\t}'
	print '\t'
	print '\t'
	print '\tgr%i->SetTitle("");'%f
	print '\t//gr%i->SetTitle("%s vs %s");'%(f,VarInTextFile[0],VarInTextFile[1])
	print '\tgr%i->GetXaxis()->SetTitle("%s");'%(f,xlabel)
	print '\tgr%i->GetYaxis()->SetTitle("%s");'%(f,ylabel)
	print '\tgr%i->GetYaxis()->SetTitleOffset(%f);'%(f,yoffset)
	print '\tgr%i->GetXaxis()->SetTitleOffset(%f);'%(f,xoffset)
	print '\tgr%i->GetYaxis()->SetTitleSize(0.05);'%f
	print '\tgr%i->GetXaxis()->SetTitleSize(0.05);'%f
	print '\t//gr%i->GetXaxis()->SetLabelSize(0.05);'%f
	print '\tgr%i->GetYaxis()->SetRangeUser(%f,%f);'%(f,yrange[0],yrange[1])
	print '\tgr%i->SetMarkerSize(1);'%f
	print '\tgr%i->SetMarkerColor(%s);'%(f,ColorChoice[f])
	print '\tgr%i->SetLineColor(%s);'%(f,ColorChoice[f])
	print '\tgr%i->SetMarkerStyle(21);'%f
	print '\t'
	print '\t//gr%i->Draw("ACP");'%f
	#print '\tgr->Draw("ALP");'
	print '\n'
	if iffit == 1:
		print '\tgr%i->Fit("%s","","",%f,%f);'%(f,fitfunction,fitXrange[0],fitXrange[1])
		print '\tgr%i->GetFunction("%s")->SetLineColor(%s);'%(f,fitfunction,ColorChoice[f])
	print '\n'
	for size in range(0,len(Pre_VarInTextFile)):
		print '\t%s.clear();'%Pre_VarInTextFile[size]
print '\t'

print '\tTMultiGraph *mg = new TMultiGraph("mg",";%s;%s");'%(xlabel,ylabel)
for f in range(0,len(InputData)):
	print '\tmg->Add(gr%i);'%f
print '\tmg->SetMaximum(%f);'%yrange[1]
print '\tmg->SetMinimum(%f);'%yrange[0]
print '\t//mg->GetXaxis()->SetLimits(750,815);'
print '\tmg->Draw("AP");'

for text in range(0,len(tlatexx)):
	print '\tTLatex *text%i = new TLatex(%f,%f,"%s");'%(text,pos1,pos2-((pos2/100.)*sep*text),tlatexx[text])
	LegY2Pos = pos2-((pos2/100.)*sep*text)

print ''
for text in range(0,len(tlatexx)):
	print '\ttext%i->SetNDC();'%text
print ''
for text in range(0,len(tlatexx)):
	print '\ttext%i->SetTextFont(42);'%text
print ''
for text in range(0,len(tlatexx)):
	print '\ttext%i->SetTextSize(0.05);'%text
print ''
for text in range(0,len(tlatexx)):
	print '\ttext%i->Draw("same");'%text
print ''

print '\tTLegend * leg = new TLegend(%f,%f,%f,%f);'%(pos1,LegY2Pos-0.06*len(tlatexx),pos1+0.20,LegY2Pos-0.02)
print '\t//leg-> SetNColumns(2);'
print '\t//leg->SetHeader("The Legend Title","C"); // option "C" allows to center the header'
for size in range(0,len(legends)):
	print '\tleg->AddEntry(gr%i, "%s","lep");'%(size,legends[size])
print '\tleg->SetFillColor(0);'
print '\tleg->SetBorderSize(0);'
print '\tleg->SetTextFont(42);'
print '\tleg->SetTextSize(0.05);'
print '\tleg->Draw();'

print ''
print ''
print '\tTLatex *cmsprem = new TLatex(%f,%f,"#it{CMS Preliminary}");'%(cpos1,cpos2)
print '\tcmsprem->SetNDC();'
print ''
print '\tTLatex *gen = new TLatex(%f,%f,"%s");'%(cpos3,cpos2,DetInfo)
print '\tgen->SetNDC();'
print ''
print '\tcmsprem->Draw("same");'
print '\tgen->Draw("same");'
print ''
print ''
print ''
print '\tc1->Write();'
print '\tc1->SaveAs("%s.pdf");'%OutPutCodeName
print '\tc1->SaveAs("%s.png");'%OutPutCodeName
print '\tf->Write();'

print '}'

################
#  Close file  #
################
