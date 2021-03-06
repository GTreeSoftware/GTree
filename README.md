# GTree

---
#### Introduction

Global Tree Reconstruction System (GTree) software is a open source software for neuron tracing. GTree is written in C++, and freely available for academic research using. GTree is used to reconstruct neurons in single images and reconstruct neuronal population from brain-wide image stacks.

#### Wiki
https://github.com/GTreeSoftware/GTree/wiki

#### License

GTree used Revised MIT LICENSE for academic research.

#### Release
New release packages are in https://github.com/GTreeSoftware/GTree/releases. Old version packages are in  https://github.com/GTreeSoftware/Release.

#### Question

If you have any academic question, you can send email to [sqzeng@mail.hust.edu.cn](sqzeng@mail.hust.edu.cn) or [quantingwei@hust.edu.cn](quantingwei@hust.edu.cn) .

If you have any technique question, you can send email to [263699527@qq.com](263699527@qq.com).


#### Third-party library package
https://github.com/GTreeSoftware/GTree/wiki/Thirdparty-Library 

From 1.0.4, GTree project import static libraries acquired by Conan, a C++ library/package manager. The project configuration has been updated.

Prebuilt binary packages for VS 2017 (except Qt5): https://github.com/GTreeSoftware/GTree/releases/tag/1.0.4.1

Prebuilt binary packages for Ubuntu 16.04 or higher, GCC 8.4.0 or higher (except Qt5): https://github.com/GTreeSoftware/GTree/releases/tag/1.0.4.2

Qt5 can be download at qt community website. Our vtk 8 is compatible of qt 5.12.5.

### How to run

https://github.com/GTreeSoftware/GTree/wiki
#### Windows
Please make sure that Microsoft VC++ 2017 x64 redistribution is installed. Just double click GTree.exe and open GTree.
#### Linux
Please make sure that GPU driver is installed normally. Go to GTree directory, open terminal and run "sh ./run_local.sh". The GTree has passed test on Ubuntu 16.04 and 18.04. The minimum GLIBC version is 2.23.
