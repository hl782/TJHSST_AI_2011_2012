// 
// Torbert, 11 November 2011
// 
#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>
#include <time.h>
//
#define M 10
#define w 1200
#define h 900
//
int grid[h/M][w/M];
//
void display(void)
{
	int j,k;
	//
   glClear(GL_COLOR_BUFFER_BIT);
	//
   glBegin(GL_POINTS);
	for(k=0;k<h;k++)
		for(j=0;j<w;j++)
	   { 
			if(grid[k/M][j/M])
	   		glColor3f(1.0,1.0,1.0);
			else
	   		glColor3f(0.0,0.0,0.0);
	   	glVertex2f(j,h-k);
	   }
   glEnd();
	//
	glutSwapBuffers();
}
void idle(void)
{
	glutPostRedisplay();
}
void mouse(int button,int state,int xscr,int yscr)
{
	printf("(x,y)=(%d,%d)\n",xscr,yscr);
}
void motion(int xscr,int yscr)
{
	printf("(x,y)=(%d,%d)\n",xscr,yscr);
}
void keyfunc(unsigned char key,int xscr,int yscr)
{
	if(key=='q')
	{
		exit(0);
	}
}
int main(int argc,char* argv[])
{  
	int j,k;
	//
   glutInit(&argc,argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
   glutInitWindowSize(w,h);
   glutInitWindowPosition(100,50);
   glutCreateWindow("Random Grid");
	//
   glClearColor(0.0,1.0,0.0,0.0); // green
	glShadeModel(GL_SMOOTH);
	//
   glutDisplayFunc(display);
	glutIdleFunc(idle);
   glutMouseFunc(mouse);
   glutMotionFunc(motion);
	glutKeyboardFunc(keyfunc);
	//
   glViewport(0,0,(GLsizei)w,(GLsizei)h);
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
	gluOrtho2D(0,w,0,h);
   glMatrixMode(GL_MODELVIEW);
	//
	srand(time(NULL));
	for(k=0;k<h/M;k++)
		for(j=0;j<w/M;j++)
			grid[k][j]=rand()%2; // 0 or 1
	//
   glutMainLoop();
	//
   return 0;
}
// 
// end of file
// 
