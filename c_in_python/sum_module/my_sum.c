#include <Python.h>
#include <stdio.h>
#include <math.h>

int my_sum(int start, int end)
{
	int i = 0, sum = 0;
	for (i=start; i<=end; i++) {
		sum += i;
	}
	return sum;
}

static PyObject* wrap_sum(PyObject* self, PyObject* args)
{
	int a, b, sum;
	
	if(!PyArg_ParseTuple(args, "ii", &a, &b))
		return NULL;

	sum = my_sum(a, b);

	return Py_BuildValue("i", sum);
}

static PyMethodDef mysumMethods[] = {
	{"mysum", wrap_sum, METH_VARARGS, "calculate sum value"},
	{NULL, NULL, 0, NULL}
};

void initmysum()
{
	Py_InitModule("mysum", mysumMethods);
}
