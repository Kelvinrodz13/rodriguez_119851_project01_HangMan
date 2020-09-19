#pragma once
#include <string>
using namespace std;

//class header for hangman class hMan

class hMan
{
private: 

	string word; //will store the random word
	int userAtt; // will count how many time the user misses

public:

	hMan(string = "N/A", int = 8);// default constructor

	void setWord(string); // will set the word for the game from the word list
	string getWord() const; //return the random chosen word
	int getUserAtt() const; // return the amount of attempts left

	void setUserAtt(int); // optional function to change add or decrease user attempts
	bool searchLetter(string,int); //check if the letter exist in the word
	void decreaseAtt(); // decrease the amount of user attempts by one
	void displayHangman(); // display a drawing of hangman
};
