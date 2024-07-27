#include<stdio.h> 

#define printInt(k) printf("%d\n", k) 
#define printDouble(x) printf("%f\n",x) 
#define printString(t) printf("%s\n", t) 

int readInt() { 
    int x; 
    scanf(" %d", &x); 
    return x; 
} 

double readDouble() { 
    double x; 
    scanf(" %f", &x); 
    return x; 
}

union cell { 
    int i; 
    double d; 
    void* l; 
};

int stack_size = 1000000; 
union cell m[stack_size]; 
int top = 0;
int bottom = stack_size - 1;

int main() {
	
	main:
	m[bottom].i = 2;
	bottom -= 1;
	m[bottom].i = 3;
	bottom -= 1;
	m[top].l = &&L0;
	goto somefunc;
	L0:
	m[top].i = m[top].i;
	top += 1;
	if (m[top - 1].i < 5) goto L1;
	m[top].i = 0;
	goto L2;
	L1:
	m[top].i = 1;
	L2:
	top += 1;
	if (m[top - 4].i == 0) goto L7;
	m[top].i = 2;
	top += 1;
	m[top].i = 0;
	top += 1;
	goto L8;
	L7:
	L5:
	if (m[top - 4].i > 5) goto L3;
	m[top].i = 0;
	goto L4;
	L3:
	m[top].i = 1;
	L4:
	top += 1;
	if (m[top - 1].i == 0) goto L6;
	m[top - 5].i = m[top - 5].i - 1;
	goto L5;
	L6:
	L8:
	m[top].i = 0;
	bottom += 0
	goto main_end;
	
	somefunc:
	m[bottom].i = m[bottom + 2].i + m[bottom + 1].i;
	bottom -= 1;
	m[bottom].i = m[bottom + 1].i;
	bottom -= 1;
	m[bottom].i = m[bottom + 1].i + 2;
	bottom -= 1;
	m[bottom].i = m[bottom + 1].i;
	bottom -= 1;
	printInt(m[bottom + 1].i);
	m[top].i = m[bottom + 2].i;
	bottom += 5
	goto somefunc_end;
	somefunc_end:
	goto *(m[top].l);
	
	main_end:

    return 0
}
