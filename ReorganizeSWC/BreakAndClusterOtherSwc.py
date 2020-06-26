#Author: Zhou Hang
import os
import numpy as np
from scanf import scanf
from tqdm import tqdm

def InterCurve(allCurve):
    newAllCurve = []
    for curve in allCurve:
        sz = len(curve)
        newCurve = []
        for i in range(0, sz - 1):
            newCurve.append(curve[i])
            dis = np.linalg.norm(curve[i] - curve[i + 1]) / 2
            idis = int(round(dis))
            for j in range(1, idis):
                newCurve.append((curve[i + 1] - curve[i]) * float(j) / float(idis) + curve[i])
        newCurve.append(curve[sz - 1])
        newAllCurve.append(newCurve)
    return newAllCurve

dirPath = 'D:\Document/merge/'
tmpList = os.listdir(dirPath)
fileList = []
for name in tmpList:
    if name.endswith('swc'):
        fileList.append(name)

for name in tqdm(fileList):
    swcPath = os.path.join(dirPath,name)
    saveDir = os.path.join(dirPath, name.split('.')[0])

    savePre = name.split('.')[0]+'_'
    formatLines = []
    data = []
    #read data
    with open(swcPath, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line[0] == '#':
                continue
            tmp = scanf('%d %d %f %f %f %f %d\n', line)
            tmp = list(tmp)
            tmp[3] = 300- tmp[3]
            data = list(tmp)
            data.append(0)
            formatLines.append(data)
    # mark each node
    clusterID = 0
    for k in range(len(formatLines)):
        if formatLines[k][6] == -1:
            clusterID +=1
            formatLines[k][7] = clusterID
        elif formatLines[k][6] == formatLines[k][0]-1:
            formatLines[k][7] = formatLines[k-1][7]
        elif formatLines[k][6] != formatLines[k][0]-1:
            formatLines[k][7] = formatLines[formatLines[k][6]][7]

    # cluster curves
    clusterList = [[] for i in range(clusterID)]
    curve = []
    for line in formatLines:
        cID = line[7]-1
        if line[6] != line[0] - 1:
            clusterList[cID].append([])
            if line[6] != -1:
                headLine = formatLines[line[6]-1]
                clusterList[cID][-1].append(np.array([headLine[2], headLine[3], headLine[4]]))
        clusterList[cID][-1].append(np.array([line[2], line[3], line[4]]))

    # save cluster, interpolate
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    for k in range(len(clusterList)):
        cluster = clusterList[k]
        # tmpCluster = clusterList[k]
        # cluster = InterCurve(tmpCluster)
        savePath = os.path.join(saveDir,savePre+'%03d.swc'%k)
        with open(savePath, 'w') as fp:
            gid = 0
            for curve in cluster:
                gid += 1
                fp.write('%d 1 %f %f %f 1 -1\n' % (gid, curve[0][0],curve[0][1],curve[0][2]))
                for id in range(1,len(curve)):
                    gid += 1
                    fp.write('%d 1 %f %f %f 1 %d\n'%(gid, curve[id][0],curve[id][1],curve[id][2], gid - 1))



