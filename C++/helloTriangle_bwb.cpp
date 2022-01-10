//g++ -o helloTriangle helloTriangle_bwb.cpp libglfw3dll.a libglew32.dll.a -I include -lglew32 -lglfw3 -lgdi32 -lopengl32

#include <GL/glew.h> // include GLEW and new version of GL on Windows
#include <GLFW/glfw3.h> // GLFW helper library
#include <stdio.h>
#include <math.h> //math library for sin's and cos's
#include <iostream>


using namespace std;

// Global variables for transformations
float tX = 0.0;
float tY = 0.0;
float tZ = 0.0;

float Sx = 0.0;
float Sy = 0.0;
float Sz = 0.0;

float deltX = 0.0;
float deltY = 0.0;
float deltZ = 0.0;
float deltSK = 1.0;

bool orthobool = true;

//Write callback functions at beginning of program
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods){
	if (key == GLFW_KEY_E){ //can hold key down
		//cout << "Key pressed\n";
		tZ += 0.01;
	}
	if (key == GLFW_KEY_W && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		tY += 0.01;
	}
	if (key == GLFW_KEY_S && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		tY -= 0.01;
	}
	if (key == GLFW_KEY_D && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		tX = 0.01;
	}
	if (key == GLFW_KEY_Q && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		tZ -= 0.01;
	}
	if (key == GLFW_KEY_A && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		tX -= 0.01;
	}
	if (key == GLFW_KEY_U && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		deltX += 0.05;
	}
	if (key == GLFW_KEY_I && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		deltX -= 0.05;
	}
	if (key == GLFW_KEY_J && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		deltY += 0.05;
	}
	if (key == GLFW_KEY_K && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		deltY -= 0.05;
	}
	if (key == GLFW_KEY_N && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		deltZ += 0.05;
	}
	if (key == GLFW_KEY_M && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		deltZ -= 0.05;
	}
	if (key == GLFW_KEY_O && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		orthobool = true;
	}
	if (key == GLFW_KEY_P && action == GLFW_PRESS){ //only moves when key is initially hit
		//cout << "Key pressed\n";
		orthobool = false;
	}
}

void multMatrices (float mat1[], float mat2[],float result[]){
	int row = 0;
	int col = 0;	
	int index = 15;
	while (row < 4) {// iterate through rows
		for (int i = 0; i < 4; i++) {// iterate through columns
			if (i == 0) {
				col = 0;
				index -= 15;
			}
			result[index] = (mat1[row] * mat2[col] + mat1[row + 4] * mat2[col + 1] + mat1[row + 8] * mat2[col + 2] + mat1[row + 12] * mat2[col + 3]);
			col += 4;
			index += 4;
		}
		row++;
	}
}
/*
*/

int main() {
  // start GL context and O/S window using the GLFW helper library
  if (!glfwInit()) {
    fprintf(stderr, "ERROR: could not start GLFW3\n");
    return 1;
  } 

  // uncomment these lines if on Apple OS X
  /*glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2);
  glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);*/

  GLFWwindow* window = glfwCreateWindow(640, 480, "Hello Triangle", NULL, NULL);
  if (!window) {
    fprintf(stderr, "ERROR: could not open window with GLFW3\n");
    glfwTerminate();
    return 1;
  }
  glfwMakeContextCurrent(window);
  
  float a = 5.0;
  cout << "this is a test print statment\n";
  cout << "this is a test print statment" << endl;
  cout << "val a: " << a << endl;
                                  
  // start GLEW extension handler
  glewExperimental = GL_TRUE;
  glewInit();

  // get version info
  const GLubyte* renderer = glGetString(GL_RENDERER); // get renderer string
  const GLubyte* version = glGetString(GL_VERSION); // version as a string
  printf("Renderer: %s\n", renderer);
  printf("OpenGL version supported %s\n", version);

  // tell GL to only draw onto a pixel if the shape is closer to the viewer
  glEnable(GL_DEPTH_TEST); // enable depth-testing
  glDepthFunc(GL_LESS); // depth-testing interprets a smaller value as "closer"


  glPointSize(5.0f);
  glClearColor(0.0f,0.0f,0.0f,1.0f);

  /* OTHER STUFF GOES HERE NEXT */
	float points[] = {// 1st top
	   0.0f,  0.9f,  0.1f,
	   -0.3f, 0.3f,  0.2f,
	   0.3f, 0.3f,  0.3f,
	   //2nd right
	   0.0f,  -0.3,  0.4f,
	   0.3f, 0.3f,  0.5f,
	   0.6f, -0.3f,  0.6f,
	   //3rd left
	   0.0f, -0.3f, 0.7f,
	   -0.3f, 0.3f, 0.8f,
	   -0.6f, -0.3f, 0.9f
	};

	float points2[] = {
	   0.9f,  0.9f,  0.0f,
	   0.8f, 0.8f,  0.0f,
	  1.0f, 1.0f,  0.0f,
	   1.0f,  1.0f,  0.0f
	};
	
	//array called trans
	GLfloat trans[] = {1.0, 0.0, 0.0, 0.0,  //first column
					   0.0, 1.0, 0.0, 0.0,  //second column
					   0.0, 0.0, 1.0, 0.0,  //third column
					   tX, tY, tZ, 1.0}; //fourth column
					   
	//array for rotation Z
	float angZ = deltZ*3.14159/180.0;
	GLfloat rotz[] = {cos(angZ), sin(angZ), 0, 0, //first column
					-sin(angZ), cos(angZ), 0, 0, //second column
					0, 0, 1, 0, //third column
					0, 0, 0, 1}; //fourth column
	//array for rotaion X
	float angX = deltX*3.14159/180.0;
	GLfloat rotx[] = {1, 0, 0, 0, //first column
					0, cos(angX),sin(angX) , 0, //second column
					0, -sin(angX), cos(angX), 0, //third column
					1, 0, 0, 1}; //fourth column
	//array for rotation Y
	float angY = deltY*3.14159/180.0;
	GLfloat roty[] = {cos(angY), 0, -sin(angY),0, //first column
					0, 1, 0, 0, //second column
					sin(angY), 0, cos(angY), 0, //third column
					0, 0, 0, 1}; //fourth column

	//array for scale
	GLfloat scal[] ={Sx, 0.0,0.0,0.0,
					0.0,Sy,0.0,0.0,
					0.0,0.0,Sz,0.0,
					0.0,0.0,0.0,1.0,};

	//array for scew
	float angSK = deltSK*3.14159/180.0;
	GLfloat scew[] = {1.0,(1/tan(angSK)),0.0,0.0,
					0.0,1.0,0.0,0.0,
					0.0,0.0,1.0,0.0,
					0.0,0.0,0.0,1.0};

	GLfloat ortho[] = {1.0,0.0,0.0,0.0,
					 0.0,1.0,0.0,0.0,
					 0.0,0.0,0.0,0.0,
					 0.0,0.0,0.0,1.0};
	float aspect = 1.0;
	float far = 100.0;
	float near = 0.01;
	float range = tan((67*3.149/180) * .5) * .01;
    float sx = (2 * near) / (range * aspect + range * aspect);
    float sy = (near / range);
    float sz = -(100.0 + .01) / (100.0 - 0.01);
	float Pz = -(2*far*near)/(far-near);

	GLfloat Persp[] = {sx,0,0,0,
					 0,sy,0,0,
					 0,0,sz,Pz,
					 0,0,-1,0};
					 
	GLuint vbo = 0;
	glGenBuffers(1, &vbo);
	glBindBuffer(GL_ARRAY_BUFFER, vbo);
	glBufferData(GL_ARRAY_BUFFER, 9 * 3 * sizeof(float), points, GL_STATIC_DRAW);

	

	GLuint vbo1 = 1;
	glGenBuffers(1, &vbo1);
	glBindBuffer(GL_ARRAY_BUFFER, vbo1);
	glBufferData(GL_ARRAY_BUFFER, 12 * sizeof(float), points2, GL_STATIC_DRAW);



	GLuint vao = 0;
	glGenVertexArrays(1, &vao);
	glBindVertexArray(vao);
	glEnableVertexAttribArray(0);
	glBindBuffer(GL_ARRAY_BUFFER, vbo);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);



	GLuint vao1 = 0;
	glGenVertexArrays(1, &vao1);
	glBindVertexArray(vao1);
	glEnableVertexAttribArray(0);
	glBindBuffer(GL_ARRAY_BUFFER, vbo1);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);

	
	
	const char* vertex_shader =
	"#version 400\n"
	"in vec3 vp;"
	"uniform mat4 t1;"
	"uniform mat4 r1;"
	"uniform mat4 p"
	"void main() {"
	"  gl_Position = t1*r1*p*vec4(vp.x, vp.y, vp.z, 1.0);"
	"}";

	const char* fragment_shader =
	"#version 400\n"
	"out vec4 frag_colour;"
	"void main() {"
	"  frag_colour = vec4(1.0, 1.0, 0.0, 1.0);"
	"}";	


	const char* fragment_shader1 =
	"#version 400\n"
	"out vec4 frag_colour;"
	"void main() {"
	"  frag_colour = vec4(1.0, 0.0, 0.0, 1.0);"
	"}";	


	GLuint vs = glCreateShader(GL_VERTEX_SHADER);
	glShaderSource(vs, 1, &vertex_shader, NULL);
	glCompileShader(vs);
	GLuint fs = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fs, 1, &fragment_shader, NULL);
	glCompileShader(fs);

	GLuint shader_programme = glCreateProgram();
	glAttachShader(shader_programme, fs);
	glAttachShader(shader_programme, vs);
	glLinkProgram(shader_programme);


	GLuint fs1 = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fs1, 1, &fragment_shader1, NULL);
	glCompileShader(fs1);

	GLuint shader_programme1 = glCreateProgram();
	glAttachShader(shader_programme1, fs1);
	glAttachShader(shader_programme1, vs);
	glLinkProgram(shader_programme1);
	
	
			  
	int logLen;
	GLchar* log;
	glGetProgramiv(shader_programme1, GL_INFO_LOG_LENGTH, &logLen);

	
	
	/*if(logLen > 0) {

		// Show any errors as appropriate

		glGetProgramInfoLog(shader_programme1, logLen, &logLen, log);

		fprintf(stderr, "Prog Info Log: %s\n", log);

	}*/
			

			  
	while(!glfwWindowShouldClose(window)) {
		// update transformation matrices
		trans[12] = tX;
		trans[13] = tY;
		trans[14] = tZ;

		scal[0] = Sx;
		scal[5] = Sy;
		scal[10] = Sz;

		rotx[5] = cos(angX);
		rotx[6] = -sin(angX);
		rotx[9] = sin(angX);
		rotx[10] = cos(angX);

		roty[0] = cos(angY);
		roty[2] = -sin(angY);
		roty[8] = sin(angY);
		roty[10] = cos(angY);

		rotz[0] = cos(angZ);
		rotz[1] = -sin(angZ);
		rotz[4] = sin(angZ);
		rotz[5] = cos(angZ);

		scew[1] = (1.0/tan(angSK));

		//math time

		GLfloat result1[16];
		multMatrices(scew, scal, result1);

		GLfloat result2[16];
		multMatrices(result1, rotx, result2);

		GLfloat result3[16];
		multMatrices(result2, roty, result3);

		GLfloat result4[16];
		multMatrices(result3, rotz, result4);

		/*
		int t1_mat_location = glGetUniformLocation (shader_programme, "t1");
		glUseProgram( shader_programme );
		glUniformMatrix4fv (t1_mat_location, 1, GL_FALSE, result4);
		
		*/

	  	int t1_mat_location = glGetUniformLocation (shader_programme, "t1");
		glUseProgram( shader_programme );
		glUniformMatrix4fv (t1_mat_location, 1, GL_FALSE, trans);


		int r1_mat_location = glGetUniformLocation (shader_programme, "r1");
		glUseProgram( shader_programme );
		glUniformMatrix4fv (r1_mat_location, 1, GL_FALSE, result4);
		
		if (!orthobool){
		int p_mat_location = glGetUniformLocation (shader_programme, "p");
		glUseProgram( shader_programme );
		glUniformMatrix4fv (p_mat_location, 1, GL_FALSE, Persp);
		}

		if (orthobool){
		int p_mat_location = glGetUniformLocation (shader_programme, "p");
		glUseProgram( shader_programme );
		glUniformMatrix4fv (p_mat_location, 1, GL_FALSE, ortho);
		}
		
	  // Identify callback functions
	  glfwSetKeyCallback(window, key_callback); //for keyboard interaction
	  //glfwSetMouseCallback(window, mouse_callback); //for mouse interaction
		
		
	  // wipe the drawing surface clear
	  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	  glUseProgram(shader_programme);
	  glBindVertexArray(vao);
	  glPointSize(15.0);
	  // draw points 0-3 from the currently bound VAO with current in-use shader
	  glDrawArrays(GL_TRIANGLES, 0, 3 * 3);

	  glUseProgram(shader_programme1);
	  glBindVertexArray(vao1);
	  // draw points 0-3 from the currently bound VAO with current in-use shader
	  glDrawArrays(GL_TRIANGLES, 0, 4);
	  // update other events like input handling 
	  glfwPollEvents();
	  // put the stuff we've been drawing onto the display
	  glfwSwapBuffers(window);
	}

  // close GL context and any other GLFW resources
  glfwTerminate();
  return 0;
}

