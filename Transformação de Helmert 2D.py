#!/usr/bin/env python
# coding: utf-8

# In[100]:


#Transformação de Helmert 2D
def transHelmert2d(matriz1,matriz2):

    result=[]

    if len(matriz1)==len(matriz2) and len(matriz1[1])==len(matriz2[1]) and len(matriz2[1])==2:
        deltaxlinha = matriz1[1][0] - matriz1[0][0]
        deltaylinha = matriz1[1][1] - matriz1[0][1]     
        deltax = matriz2[1][0] - matriz2[0][0]
        deltay = matriz2[1][1] - matriz2[0][1]
        
        a=(deltaxlinha*deltax+deltaylinha*deltay)/((deltaxlinha**2)+(deltaylinha**2))
        b=((deltaxlinha*deltay)-(deltaylinha*deltax))/((deltaxlinha**2)+(deltaylinha**2))
        c=matriz2[0][0]-a*matriz1[0][0]+b*matriz1[0][1]
        d=matriz2[0][1]-(b*matriz1[0][0])-(a*matriz1[0][1])
        k=(a**2+b**2)**0.5
        rad= math.atan(b/a)
        
    else:
        print ("Erro")
           
    return a, b, c, d, k, rad


# In[171]:


#Rsultado de Helmert 2D
def resultHelmert2d(matriz,parametros):

    result=[]
    linha=[]
    
    for i in range(0,len(matriz)):
            x=parametros[0]*matriz[i][0]-parametros[1]*matriz[i][1]+parametros[2]
            y=parametros[1]*matriz[i][0]+parametros[0]*matriz[i][1]+parametros[3]
            linha.append(x)
            linha.append(y)
            result.append(linha)
            linha=[]
           
    return result


# In[172]:


A = [[197266.368,7563526.603],[197319.864,7563695.541]]


# In[173]:


B = [[1000.000,1000.000],[1173.787,1034.268]]


# In[174]:


dado = [[197266.368,7563526.603],
[197319.864,7563695.541],
[197002.396,7563776.129],
[197042.265,7563649.295],
[197334.993,7563618.279],
[197200.671,7563719.336],
[197097.625,7563809.233]]


# In[175]:

print (resultHelmert2d(dado,transHelmert2d(A,B))




# In[ ]:





# In[ ]:




