#include <Python.h>

/*建立介面（Interface），名稱為myFunction,
這個介面函數是之後要給Python呼叫的，所以使用PyObject*表式參數值的傳入與回傳都是以
Python物件方式傳遞，所以這是一個Python物件指標（Point），self引數是Python類別本身的宣告,
args引數是接收Python傳遞進來的值，args會以序列型態表示，所以我們必須使用PyArg_ParseTuple()函數
來接收值，

這裡宣告 PyArg_ParseTuple(args, "s", &name)，第一個args引數就是此函數的args，中間的"s"表示args序列
是字串型態，&name變數就是傳進來的參數順序對應。

Py_RETURN_NONE參數是對應這個函數的return NULL。
*/
static PyObject* myFunction(PyObject* self, PyObject* args)
{
    const char* name;
 
    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;
 
    printf("(這是呼叫C語言裡的函數) , 您好 %s!\n", name);
 
    Py_RETURN_NONE;
}

/*
這是一個PyMethodDef結構，其實它就是一個註冊表，主要用意是要建立一個Python與C語言之間函數的對照
{"myFunction", myFunction, METH_VARARGS, "函數說明..."},
"myFunction" - 這是之後要在Python模組內使用的方法（method）名稱。
myFunction - 這是這支C語言程式內的函數名稱。
METH_VARARGS - 這是指myFunction參數傳遞的方法。
"函數說明..." -  這是使用在Python的函數說明 __doc__。

*/ 
static PyMethodDef myMethods[] =
{
     {"myFunction", myFunction, METH_VARARGS, "函數說明..."},
     {NULL, NULL, 0, NULL}
};

// PyMODINIT_FUNC 參數是說明initmy(void){...}函數是一個void回傳型態。
PyMODINIT_FUNC 
/*
initmy是一定要的函數，這是初始化，init後面接的my就是之後要在Python使用的模組名稱，就是import my，
它對應到底下的Py_InitModule("my", myMethods)函數內的"my"名稱。
*/
initmy(void)
{
     (void) Py_InitModule("my", myMethods);
}
