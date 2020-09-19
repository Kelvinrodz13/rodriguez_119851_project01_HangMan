#include <iostream>
#include <ctime>
#include <fstream>
#include "hMan.h"

//Developer: Kelvin Rodriguez Puello #119851
//COMPE2 LAB SP-20 Zayira Jordan Conde

//This program will execute a hangman game where user guees the random word from a default word list

int main()
{

	ofstream inArchivo;

	const int size = 10; //array size limit

	string words[size] = {"add","nun","int","yaw","sky","old","gum","fox","dog","cat"}; //default word list array
	string guess; // string to store user guesses
	string dashes = "___"; // string used to turn into correct word when guesses are sucsseful

	hMan game; // will store the word used for the game and user attempts

	unsigned seed = time(0);
	srand(seed);

	int randValue = rand() % 10; //random number seed

	inArchivo.open("listWord.txt"); //will create the file if it does not exist
	
	for (int k = 0; k < size; k++) // will store in USER PC default word list in txt format
	{
		inArchivo << words[k] << "\n";
	}

	inArchivo.close();

	game.setWord(words[randValue]); // set the word for the game

	//_____________________________________________
	cout << "Initializing...HANGMAN PROTOCOL\n";
	cout << "GUESS THE THREE LETTER WORD OR YOUR FRIEND DIES!\nYOU HAVE 8 FAIL ATTEMPTS\n\n";


	while (game.getUserAtt() > 0 && dashes != game.getWord()) //GAME START	
	{
		cin.clear();
		cout << dashes << "\n\n";
		cout << "Amount of incorrect guess left: " << game.getUserAtt() << endl;
		cout << "Enter your guess: ";

		getline(cin, guess);

		if (game.getWord().find(guess) != string::npos) //check if guess is found in the game word
		{
			for (int j = 0; j < game.getWord().length(); j++)
			{
				if (game.searchLetter(guess,j) == true) //uncover the word if a matching letter is found
					dashes[j] = guess[0];
			}

			
			cout << "You have found a correct letter!\n";
			
		}
		else
		{
			cout << "Incorrect letter!, your friend is just one more step away!\n";
			game.decreaseAtt();
		}

	}

	
	//present results either the player wins or loses
	if (dashes == game.getWord())
		cout << "\nYou won the game!,"<<" the word was: " <<game.getWord() <<"\nyour're friend will live another day for now..." << "\n";
	else
	{
		cout << "\nYou lost the game!" << ", your word was: " << game.getWord();
		cout << endl << "You know what happens next...\n\n";
		game.displayHangman();
		cout << "\nBETTER LUCK NEXT TIME";
		
	}

	cout << "\n\n";

	system("pause");

	cout << "\n\n\n\n";

	return 0;
}