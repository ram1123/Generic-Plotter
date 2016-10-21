# Plotting-Scripts

## How To Use
1. Modify the template file **Template.txt**  as per its format.
	1. First column contains input text file. You can give this with its path.
	2. Second column contains name of directory that you want to create
	3. Third column contains name of different Ntuples that you want to store.
	4. Then, 4th, 5th, and 6th column contains number of bins, min x, and max x value for the histogram range.

2. After setting the **Template.txt** file just run the macro **HistoPlot.C** 

	root -l -b -q HistoPlot.C
