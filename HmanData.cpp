#include "hMan.h"
#include <iostream>

//class function implementation file

//****function documentation is in class header*****

hMan::hMan(string aWord, int aCount) 
{
	this->word = aWord;
	this->userAtt = aCount;
}

void hMan::setWord(string aWord) 
{
	this->word = aWord;
}

string hMan::getWord() const 
{
	return this->word;
}

int hMan::getUserAtt() const 
{
	return this->userAtt;
}

void hMan::setUserAtt(int aTT) 
{
	if (aTT > 0)
		userAtt = aTT;
	else
		userAtt = 8;
}

void hMan::decreaseAtt()
{
	userAtt -= 1;
}

bool hMan::searchLetter(string aLetWord, int i)
{
	
	if (aLetWord[0] == word[i])
		return true;
	else
		return false;

}

void hMan::displayHangman()
{
	cout << "/____________________________________/\n";
	cout << "\t\t /\n";
	cout << "\t\t /\n";
	cout << "\t\t /\n";
	cout << "\t\t O\n";
	cout << "\t\t/|/";
	cout << "\n";
	cout << "\t\t/ /";

}