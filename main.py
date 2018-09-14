from pandas import read_excel
from numpy import array,mean,var,std,vstack,cov,corrcoef,set_printoptions
from math import log
from scipy.stats import multivariate_normal,norm
from numpy.linalg import inv

def getCorrelationMatrix(dataStack):
    return corrcoef(dataStack)

def getCovarianceMatrix(dataStack):
    return cov(dataStack)

def multivaraiateLikelihood():
    loglikelihood=0
    probList=multivariate_normal.pdf(dataList, mean=meanList, cov=covarianceMat,allow_singular=True)
    for row in range(0,len(probList)):
        loglikelihood+=log(probList[row])
    return round(loglikelihood,3)

def independentLoglikelihood():   
    probList=norm.pdf(dataList,meanList,sigmaList)
    loglikelihood=0
    for row in range(0,len(dataList)):
        for col in range(0,len(X)):
            loglikelihood+=log(probList[row][col])
    return round(loglikelihood,3)

set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})   
data = read_excel('university data.xlsx')
X=['CS Score (USNews)','Research Overhead %','Admin Base Pay$','Tuition(out-state)$']

dataList=[]
meanList=[]
varList=[]
sigmaList=[]
i=1
for attr in X:
     attrValues = array(data[attr].dropna())
     locals()['mu{0}'.format(i)] = round(mean(attrValues),3)
     locals()['var{0}'.format(i)] = round(var(attrValues),3)
     locals()['sigma{0}'.format(i)] = round(std(attrValues),3)
     meanList.append(locals()['mu{0}'.format(i)])
     varList.append(locals()['var{0}'.format(i)])
     sigmaList.append(locals()['sigma{0}'.format(i)])
     dataList.append(attrValues)
     i=i+1
        
dataStack = vstack((dataList))
covarianceMat = getCovarianceMatrix(dataStack)
correlationMat = getCorrelationMatrix(dataStack)
dataList=array(data.loc[:,X].dropna())

print("UBitName = Hima Sujani Adike")
print("personNumber = 50246828")
for i in range(1,len(X)+1):
   print("mu"+str(i)," = ",locals()['mu{0}'.format(i)])
for i in range(1,len(X)+1):
   print("var"+str(i)," = ",locals()['var{0}'.format(i)])
for i in range(1,len(X)+1):
   print("sigma"+str(i)," = ",locals()['sigma{0}'.format(i)])
print("covarianceMat = ",covarianceMat)
print("correlationMat = ",correlationMat)
print("logLikelihood = ",independentLoglikelihood())
print("multivariatelogLikelihood = ", multivaraiateLikelihood())