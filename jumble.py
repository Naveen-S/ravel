import itertools
import enchant
inputCharacters = raw_input('Enter jumbled word:\n');
inputArray = list(inputCharacters);
output = itertools.permutations(inputArray);
outputList = [];
for i in output:
	outputList.append(''.join(i));
#	print i;
#print outputList;

myDictionary = enchant.Dict("en_US");

finalList = [];
for eachWord in outputList:
	if(myDictionary.check(eachWord)):
		if(eachWord not in finalList):
			finalList.append(eachWord);
#print(finalList);

print('#'*205);
print('Possible words for a given jumble are:\n');
for j in finalList:
	print(j);
print('\n');
print('#'*205);
