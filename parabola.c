//
// Torbert, 19 Sept 2011
//
#include <stdio.h>
#include <math.h>
//
int main(int argc,char* argv[])
{
	double t=0.0;
	double x=0.0;
	double y=0.0;
	//
	double dt=0.001;
	//
	double v0   =44.704;   // meters per second, 100 mph
	double theta=M_PI/3.0; // radians
	//
	double vx=v0*cos(theta);
	double vy=v0*sin(theta);
	//
	double g=-9.81;        // meters per second per second
	//
	double ax=0.0;
	double ay=g;
	//
	while(y>=0.0)
	{
		x+=(vx*dt);
		y+=(vy*dt);
		//
		vx+=(ax*dt);
		vy+=(ay*dt);
		//
		printf("%e %e %e\n",t,y,(0.5*g*t*t+v0*sin(theta)*t+0.0));
		//
		t+=dt;
	}
	//
	return 0;
}
//
// end of file
//
