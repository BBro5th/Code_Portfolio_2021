// Chaikin
//g++ -o Chaiken.exe Chaiken.cpp -O2 -lgdi32
#include <iostream>
#include <vector>
#include "CImg-2.8.2/CImg.h"

using namespace cimg_library;
using namespace std;

vector<int> coords_x;
vector<int> coords_y;


int main(){
  CImg<unsigned char> orig(500, 500, 1, 3, 0);

  CImgDisplay window(orig, "Click control points");
  unsigned char color[] = { 255,128,64 };
  while (!window.is_closed()){ // getting points
	window.wait();
	if (window.button()){
		int x = window.mouse_x();
		int y = window.mouse_y();
		coords_x.push_back(x);
		coords_y.push_back(y);

		cout << x << ", " << y<< endl;
		orig.draw_circle(x, y, 5, color);
		window.display(orig);
	}
  }
  vector<int> odCoordx = coords_x;
  vector<int> odCoordy = coords_y;
  int picsiz = coords_x.size(); //drawing initial
  for (int i=0; i<picsiz; i++){
	int x1 = coords_x[i];
	int y1 = coords_y[i];
	int x2 = coords_x[i+1];
	int y2 = coords_y[i+1];
	orig.draw_line( x1, y1, x2, y2, color);

  }
  
 //the curving
 for (int taco=0;taco < 6; taco++){
  int vecsiz = coords_x.size();
  int begx = coords_x[0];
  int begy = coords_y[0];
  int endx = coords_x[vecsiz-1];
  int endy = coords_y[vecsiz-1];
  vector<int> newx;
  vector<int> newy;
  newx.push_back(begx);
  newy.push_back(begy);
  
  for (int j=0; j<vecsiz-1; j++){ // chaikin 
  int Qix = (.75 * coords_x[j]) + (.25 * coords_x[j+1]);
  int Qiy = (.75 * coords_y[j]) + (.25 * coords_y[j+1]);
  int Rix = (.25 * coords_x[j]) + (.75 * coords_x[j+1]);
  int Riy = (.25 * coords_y[j]) + (.75 * coords_y[j+1]);
  newx.push_back(Qix);
  newy.push_back(Qiy);
  newx.push_back(Rix); 
  newy.push_back(Qiy);

  }
  newx.push_back(endx);
  newy.push_back(endy);

  int picsiz = newx.size(); //drawing after
  for (int k=0; k<picsiz-1; k++){
	int x1 = newx[k];
	int y1 = newy[k];
	int x2 = newx[k+1];
	int y2 = newy[k+1];
	color[0] = rand()%255;
	color[1] = 100;
	color[2] = rand()%255;

	orig.draw_line( x1, y1, x2, y2, color);
	}
coords_x = newx;
coords_y = newy;
}
window = orig;
window.show();
while(!window.is_closed()){
	window.wait();
}

}// end of main

/*
//* CImg drawing
//For Chaikin, you'll want to draw line segments connecting points and for Bezier you'll want to draw circles
orig.draw_line( x1, y1, x2, y2, color);
orig.draw_circle(x1, y1, size, color);

//orig: image variable
//x1, y1, x2, y2: locations to draw
//color: 
//	* constant value: 
		unsigned char color[] = { 255,128,64 };
//	* you can also set a random value:
		  color[0] = rand()%255;
		  color[1] = rand()%255;
		  color[2] = rand()%255;
// size: how big you want the circles to be (i'm using 5 in the example videos)

//* Vectors
//Vectors a nice dynamic datastructure that will be good for storing user selected control points in
//To use vectors, at the beginning of your code add:

#include <vector>

//To initialize a vector variable: (to start, it'll be easier to have one for x-coords and another for y-coords)
vector<int> coords_x;
vector<int> coords_y;

//To add values to a vector: (they behave a lot like a stack)
int x = 5; (replace with some coordinate the user clicked)
coords_x.push_back(x);

//Get the length of a vector: (figure out how many points the user clicked)
coords_x.size()

//Access a particular element in your vector: (just like using an array)
coords_x[i]
*/
