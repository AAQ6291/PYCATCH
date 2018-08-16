#include <Python.h>

/*�إߤ����]Interface�^�A�W�٬�myFunction,
�o�Ӥ�����ƬO����n��Python�I�s���A�ҥH�ϥ�PyObject*���ѼƭȪ��ǤJ�P�^�ǳ��O�H
Python����覡�ǻ��A�ҥH�o�O�@��Python������С]Point�^�Aself�޼ƬOPython���O�������ŧi,
args�޼ƬO����Python�ǻ��i�Ӫ��ȡAargs�|�H�ǦC���A��ܡA�ҥH�ڭ̥����ϥ�PyArg_ParseTuple()���
�ӱ����ȡA

�o�̫ŧi PyArg_ParseTuple(args, "s", &name)�A�Ĥ@��args�޼ƴN�O����ƪ�args�A������"s"���args�ǦC
�O�r�ꫬ�A�A&name�ܼƴN�O�Ƕi�Ӫ��Ѽƶ��ǹ����C

Py_RETURN_NONE�ѼƬO�����o�Ө�ƪ�return NULL�C
*/
static PyObject* myFunction(PyObject* self, PyObject* args)
{
    const char* name;
 
    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;
 
    printf("(�o�O�I�sC�y���̪����) , �z�n %s!\n", name);
 
    Py_RETURN_NONE;
}

/*
�o�O�@��PyMethodDef���c�A��ꥦ�N�O�@�ӵ��U��A�D�n�ηN�O�n�إߤ@��Python�PC�y��������ƪ����
{"myFunction", myFunction, METH_VARARGS, "��ƻ���..."},
"myFunction" - �o�O����n�bPython�Ҳդ��ϥΪ���k�]method�^�W�١C
myFunction - �o�O�o��C�y���{��������ƦW�١C
METH_VARARGS - �o�O��myFunction�Ѽƶǻ�����k�C
"��ƻ���..." -  �o�O�ϥΦbPython����ƻ��� __doc__�C

*/ 
static PyMethodDef myMethods[] =
{
     {"myFunction", myFunction, METH_VARARGS, "��ƻ���..."},
     {NULL, NULL, 0, NULL}
};

// PyMODINIT_FUNC �ѼƬO����initmy(void){...}��ƬO�@��void�^�ǫ��A�C
PyMODINIT_FUNC 
/*
initmy�O�@�w�n����ơA�o�O��l�ơAinit�᭱����my�N�O����n�bPython�ϥΪ��ҲզW�١A�N�Oimport my�A
�������쩳�U��Py_InitModule("my", myMethods)��Ƥ���"my"�W�١C
*/
initmy(void)
{
     (void) Py_InitModule("my", myMethods);
}
