#include "Graph.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>		
#include <limits.h>		//creates really small numbers
#include <time.h> 		//Keep track of cars and create random numbers

#include <vector>		//To use Vectors
#include <queue>		//To use Queues

#include <fstream>

using namespace std;

//this is only being used for debugging purposes. Will remove later.
void printSolution(int dist[], int n)
{
printf("Vertex Distance from Source\n");
for (int i = 0; i < n; i++)
	printf("%d tt %d\n", i, dist[i]);
}
/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
MainNetwork::MainNetwork(char* textFile){
	ifstream inFile(textFile);
	
	while( !inFile.eof() )
	{
		for( int i = 0; i < 9; i++)
		{
			for(int j = 0; j < 9; j++)
			{
				inFile >> graph[i][j].dist;
				graph[i][j].carCount = 0;
			}
		}

	}
	inFile.close();
}

/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
void MainNetwork::addCar( Car newCar ){
	listOfCars.push_back( newCar );
	sendPath( newCar );
}

/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
void MainNetwork::sendPath(Car &workingCar ){
	vector<int> paths[9];
	int destination = -99;

	dijkstra(paths, workingCar.source);
	workingCar.CurrentPath = paths[workingCar.destination];

	if(workingCar.CurrentPath.empty())
		destination = workingCar.destination;
	else
		destination = workingCar.CurrentPath.front();
	updatePath(workingCar.source, destination, false);

/*
	//This is just for debugging purposes
	for(int i = 0; i < 9; i++)
	{
		cout << "Path " << i << ": " << endl;
		for(vector<int>::iterator iterate = paths[i].begin(); iterate != paths[i].end(); iterate++)
		{
			cout << *iterate << ' ';
		}
		cout << endl;
	}
*/
}


/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
int MainNetwork::minDistance(Edges dist[], bool sptSet[]){
	// Initialize min value
	int min = INT_MAX, min_index;

	for (int v = 0; v < 9; v++)
	{
		if (sptSet[v] == false && dist[v].dist <= min 
							   && dist[v].carCount < 9999)
		{
			min = dist[v].dist, min_index = v;
		}
	}
	return min_index;
}


/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
void MainNetwork::dijkstra(vector<int> paths[9], int src)
{
	Edges dist[9];
	bool sptSet[9]; // sptSet[i] will true if vertex i is included in shortest
					// path tree or shortest distance from src to i is finalized

	// Initialize all distances as INFINITE and stpSet[] as false
	for (int i = 0; i < 9; i++)
	{
		dist[i].dist = INT_MAX;
		dist[i].carCount = 0;
		sptSet[i] = false;
	}

	// Distance of source vertex from itself is always 0
	dist[src].dist = 0;

	// Find shortest path for all vertices
	for (int count = 0; count < 9-1; count++)
	{
		// Pick the minimum distance vertex from the set of vertices not
		// yet processed. u is always equal to src in first iteration.
		int u = minDistance(dist, sptSet);
		/*
		for( int i = 0; i < 9; i++)
		{
			cout << dist[i].dist << "\t";
		}
		cout << endl;
		*/
		// Mark the picked vertex as processed
		sptSet[u] = true;

		// Update dist value of the adjacent vertices of the picked vertex.
		for (int v = 0; v < 9; v++)
		{

			// Update dist[v] only if is not in sptSet, there is an edge from 
			// u to v, and total weight of path from src to v through u is 
			// smaller than current value of dist[v]
			if (!sptSet[v] && graph[u][v].dist 
						   && dist[u].dist != INT_MAX 
						   && dist[u].dist+graph[u][v].dist < dist[v].dist)
			{
				dist[v].dist = dist[u].dist + graph[u][v].dist;
				dist[v].carCount = graph[u][v].carCount;

				if( graph[u][src].dist == 0 && u != src)
				{
					paths[v] = paths[u];
				}

				if( u != src)
				{

					paths[v].push_back( u );
				}
			}
		}
	}
}

/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
void MainNetwork::updatePath(int source, int dest, bool newSource){
	if( !newSource )
	{
		graph[source][dest].carCount++;
		graph[dest][source].carCount++;
	}
	else
	{
		graph[source][dest].carCount--;
		graph[dest][source].carCount--;
	}

	for( int i = 0; i < 9; i++)
	{
		for( int j = 0; j < 9; j++)
		{
			cout << "<" << graph[i][j].dist << "," << graph[i][j].carCount << ">  ";
		}
		cout << endl;
	}
}

/**
 * @brief 
 *
 * @details 
 *          
 * @pre 
 *
 * @post 
 * 
 * @exception 
 *
 * @param [in] 
 *
 * @return 
 * 
 **/
void MainNetwork::updateSource(){

}