import fpGrowth
# rootNode = fpGrowth.treeNode('pyramid',9, None)
# rootNode.children['eye'] = fpGrowth.treeNode('eye', 13, None)
#
# rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix', 3, None)
# rootNode.disp()

# simpDat = fpGrowth.loadSimpDat()
# initSet = fpGrowth.createInitSet(simpDat)
# myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)
# myFPtree.disp()

# print(fpGrowth.findPrefixPath('x',myHeaderTab['x'][1]))
# print(fpGrowth.findPrefixPath('z',myHeaderTab['z'][1]))
# print(fpGrowth.findPrefixPath('r',myHeaderTab['r'][1]))
# print(fpGrowth.findPrefixPath('t',myHeaderTab['t'][1]))

# freqItems =[]
# fpGrowth.mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)
# print(freqItems)


parsedDat = [line.split() for line in open('kosarak.dat').readlines()]
initSet = fpGrowth.createInitSet(parsedDat)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 100000)
myFreqList =[]
fpGrowth.mineTree(myFPtree, myHeaderTab, 100000, set([]), myFreqList)
print(myFreqList)
