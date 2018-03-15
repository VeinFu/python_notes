#include<Python.h>
#include<math.h>

static PyObject* cos_func(PyObject* self, PyObject* args)
{
	double value;
	double answer;

	if (!PyArg_ParseTuple(args, "d", &value))
		return NULL;

	answer = cos(value);

	return Py_BuildValue("f", answer);
}

static PyMethodDef CosMethods[] =
{
	{"cos_func", cos_func, METH_VARARGS, "evaluate the cosine"},
	{NULL, NULL, 0, NULL}
};

initcos_module(void)
{
	(void) Py_InitModule("cos_module", CosMethods);
}
