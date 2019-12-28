### GTree Linux Compilation Instruction

1. Dependencies

    We compiled GTree using the following 3rd dependencies:

- Qt 5.13.1
- Eigen 3
- libsvm 
- hdf5 1.10
- tree 3.7
- libtiff 4
- glog
- VTK 8.2
- inifile

Tree library can be download from http://tree.phi-sci.com/
For some compilation bug, I put svm.cpp and inifile.cpp into Linux archieve.

2. Compilation environment

    You can compile GTree using: 
- Ubuntu 16.04 or other modern system
- GCC 5.4 or higher (support C++11 and OpenMP)
- Qt Creator IDE
- X86 architechture CPU
- NVidia GPU or other GPU with OpenGL (version 2 or higher) support

3. Compilation

    Just open GTree.pro file in Qt Creator IDE. Enter edition mode to edit GTree.pro file, change the including path and library path to your real path, especially in :

- INCLUDEPATH block
- LIBS block

     Then just compile it. GTree.pro is cross-platform Qt solution file which support Windows, Mac OS and Linux.

4. How to run GTree in new Computer without compilation?

    Please check the content of GTree_Linux.zip, especially the *.so library files and 'run_local.sh' file included in the archieve. You can make a decompress&run GTree archieve files, by updating your own configuration according to our existing decompress&run configuration. Checking the gcc supporting libary version is very important. Usually you can run lower GCC compilation software in Linux with higher GCC, but cannot run versa vice.
    
   
5. Some other 

    We designed manual edit module to revise tracing results. From single node to whole neuron tree, GTree has corresponding edit modules.
    Due to error propagation, many current neuron tracing methods is not robustness， even if you just change parameter at a small range. Thus manual edit modules are necessary. If you know some powerful C++ algorithm for neuron analysis, please let us know.
