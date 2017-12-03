#include <iostream>
#include <fstream>
#include "Graph.h"
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(int argc, char* argv[]){
	srand(time(NULL));
	MainNetwork simulation(argv[1]);
	Car testing;

	for( int i = 0; i < 9; i++)
	{
		testing.source = rand() % 8;
		testing.destination = rand() % 8;
		while( testing.source == testing.destination)
		{
			testing.destination = rand() % 8;
		}
		testing.crash = false;
		testing.congested = false;
		cout << "From: " << testing.source << " To: " << testing.destination << endl;
		simulation.addCar( testing );
	}
	

	return 0;
}