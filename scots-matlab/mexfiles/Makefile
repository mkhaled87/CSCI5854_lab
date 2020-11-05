#
# matlab root 
#
MATLABROOT      = /Applications/MATLAB_R2020a.app

#
# compiler
#
CC              = $(MATLABROOT)/bin/mex
CXXFLAGS        = -g -Wall -Wextra -std=c++11 -O3 

#
# cudd 
#
CUDDINC         = -I./include
CUDDLIBS        = -lcudd 
CUDDLPATH       = -L./cudd/


TARGET 			= mexSymbolicSet
all: $(TARGET)

$(TARGET): $(TARGET).cc
	$(CC) COMPFLAGS='$(COMPFLAGS) $(CXXFLAGS)' -largeArrayDims $(CUDDINC) $(CUDDLPATH) $(CUDDLIBS) $(TARGET).cc

