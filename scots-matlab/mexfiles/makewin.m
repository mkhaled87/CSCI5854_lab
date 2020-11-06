%
% makewin.m
%
% created on: 08.01.2018
%     author: M.Khaled
%
% This file builds the mex executables for the interface
% the supplied proted CUDD library is buyilt for Release/x64
% If your Matlab is 32bits, this will not work. Contact me to
% supply the 32bit version.
%
% You have to have he file CUDD.lib availoble in the .\cuddwin64\lib
% You will find it in a compressed file. Uncompress it.
%
clear all;
delete mexSymbolicSet.mex*

% paths for includes
ipath_bdd  = ['-I' fullfile('.')];
ipath_cudd = ['-I' fullfile('..\cudd-3.0.0\')];

% build all (including the CUDD) and link inside one file
mex('-v', ipath_bdd, ipath_cudd, '-lws2_32', 'mexSymbolicSet.cc', '..\cudd-3.0.0\*.cc', '..\cudd-3.0.0\*.c')



