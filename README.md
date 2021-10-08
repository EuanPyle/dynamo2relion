Based on dynamo2m by Alister Burt: https://github.com/alisterburt/dynamo2m

Requires dependencies in requirements.txt. 

Run via: python setup.py install

On the command line type:

dynamo2relion

Enter the path to the Dynamo table, the desired output file name, and the path to the directory containing the TS directories (e.g. within a directory called imod there are multiple directories called TS_01, TS_02 etc. Each TS_[number] directory has its own TS_[number].st file inside. In this program you would link to the directory called imod). Ensire that the directory containing the TS directories only has TS directories inside and no other directories or you will get an error.

Takes Dynamo table and the path to the directories contain the TS files and generates a star file for import into RELION.
