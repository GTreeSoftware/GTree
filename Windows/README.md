#### Windows compilation
- Open GTree.sln in Visual Studio 2017
- Change including path
- Change linker path
- Just compile in x64 compilation mode.
- 3rd libaries are the same as Linux version needs.

3rd libraries list:
- Qt 5
- Eigen 3
- libsvm 
- hdf5 1.10
- tree 3.7
- libtiff 4
- glog
- VTK 8
- inifile

### Libraries Building

See https://github.com/GTreeSoftware/GTree/wiki/Thirdparty-Library .

### Prebuilt Libraries for VS 2017 except Qt 5

https://github.com/GTreeSoftware/GTree/releases/tag/1.0.4.1

#### Make portable software
Put 3rd libraries dll files in executable directory. Ensure you have put directory 'platforms' (include qwindows.dll et al) in. 'Platforms' directory places in Your_QT_PATH/msvc2017_64/plugins/platforms. You can just run GTree.exe

Ensure you have install "Microsoft VC++ redistribution 2017 x64" and GPU driver in new computer

