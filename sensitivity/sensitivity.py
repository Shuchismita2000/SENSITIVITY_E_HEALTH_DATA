import pandas as pd
import math

# 0 denotes user don't want to access AND 1 denotes user  want to access


### Entropy of attributes
def EntropyofAttribute( dataset ):
    e_dict={}
    elem='User'
    columns=dataset.columns.to_list()
    if elem in columns:
        columns.remove(elem)
    for i in range(len(columns)):
        #Collect the positive responses according to Attributes
        positive=dataset[columns[i]].value_counts().get(1) 
        #Collect the negative responses according to Attributes
        negative=dataset[columns[i]].value_counts().get(0)
        #denominator
        y=positive+negative
        #Calculate the probability of positive and negative response according to Attributes
        p=positive/y
        n=negative/y
        #Apply Entropy Formula 
        e=-((p*math.log(p))+(n*math.log(n)))
        #Store values in dictionary {Attribute name : Entropy of that Attribute}
        e_dict[columns[i]]=e
        #Converting in Dataframe
        df=pd.DataFrame.from_dict(e_dict,orient='index').rename(columns={0:'Entropy of Attribute'})
    return df


### Entropy of usability

#Counting yes , i.e. Sum of 1's of each column(attribute)
def counting_yes( dataset , column_a , column_b ):
                # Dataset , Range of column name (from column_a to column_b all)
    l=[]
    count=0
    c=dataset.columns[column_a:column_b]
    for i in range(0,c.shape[0]): #iterate the column name 
        for j in range(0,dataset.shape[0]): #iterate the whole dataset rows
            if(dataset[c[i]][j]==1):  #Check the response either yes or no
                count=count+1        #if yes add value in count
        l.append(count)
        count=0
    #Store values in dictionary {Attribute name : Count of positive ('yes'/1) response}
    b={c[i]:l[i] for i in range(len(c))}  
    return b


#Helps to call the previous function in same manner for every user's data
def counting_yes_per_user( dataset ):
    y=counting_yes(dataset,0,dataset.shape[1])
    return y

#Usability or Probability of need of particular attribute respect to users
def usability(dataset):
    usability=pd.DataFrame()
    #Find the users varaity from the dataset
    k=dataset['User'].value_counts().keys().to_list() 
    #Grouping the whole dataset in parts according to each user
    user_data=dataset.groupby('User')
    for i in range(len(k)):
        l1=[]
        l2=[]
        l3={}
        sum=0
        #Extract each user data by iterating loop 
        df=user_data.get_group(k[i]).reset_index()
        df=df.drop(['index','User'],axis=1)
        #Counting yes by calling the function for each user's data
        D=counting_yes_per_user(df)
        #denominator
        for j in D:
            sum=sum+D[j]
        #Calculate the probability each attribute 'yes'/total 'yes' according to each user
        for j in D:
            p=(D[j])/sum
            l1.append(p)
        #Process of string values in Dataframe (Probability of each attribute repect to each users)
        l3={df.columns[i]:l1[i] for i in range(len(df.columns))}
        DF=pd.DataFrame.from_dict(l3,orient='index').rename(columns={0:k[i]})
        usability=pd.concat([usability,DF],axis=1)
        DF=pd.DataFrame()
    return usability

#Calculate entropy from probability of usability using Entropy formula
def EntropyofUsability(dataset):
    s=0
    e=[]
    # Calculate probability of usability by calling the function
    x=usability(dataset)
    #Summation of probability of usability of each attribute of all users
    usability_attribute=x.sum(axis=1)
    usability_attribute_df=pd.DataFrame(usability_attribute).rename(columns={0:'Usability'})
    #Using Entropy formula to calculate of entropy of usability each attribute
    for i in range(0,usability_attribute_df.shape[0]):
        if(usability_attribute[i]!=0):
            s=s+(-(usability_attribute[i]*math.log(usability_attribute[i])))
            e.append(s)
            s=0
        else:
            e.append(0)
    # Store the values in dictionary {Attribute name :Entropy of Usability} 
    H={usability_attribute_df.T.columns[i]:e[i] for i in range(len(usability_attribute_df.T.columns))}
    #present in dataframe 
    usability_entropy_df=pd.DataFrame.from_dict(H,orient='index').rename(columns={0:'Entropy of Usability'})
    return usability_entropy_df



### Entropy of associativity
def Associativity(dataset):
    elem='User'
    columns=dataset.columns.to_list()
    if elem in columns:
        columns.remove(elem)
    associativity=pd.DataFrame()
    for i in range(len(columns)):
        y=pd.DataFrame()
        #Grouping the whole dataset in parts according to each attribute AND #Extract each attribute's 'yes' data by iterating loop 
        x=dataset.groupby(columns[i]).get_group(1).reset_index().drop(['index','User'],axis=1)
        r=x.shape[1]
        #Counting yes of one attribute repect to another attribute
        y=pd.DataFrame.from_dict(counting_yes(x,0,r),orient='index').rename(columns={0:columns[i]})
        #Storing all values in dataframe
        associativity=pd.concat([associativity,y],axis=1)
    return associativity
    
def EntropyofAssociativity(dataset):
    s=0
    e=[] 
    # Calculate probability of associativity by calling the function
    associativity=Associativity(dataset)
    #Summation of probability of associativity of each attribute 
    associativity['sum_']=associativity.sum(axis=1)
    r=associativity.shape[1]
    #Using Entropy formula to calculate of entropy of associativity each attribute
    for i in range(0,r-1):
        for j in range(i,r-1):
            if(associativity.iat[i,j]!=0):
                s=s+(-((associativity.iat[i,j]/associativity.iat[i,r-1])*math.log((associativity.iat[i,j]/associativity.iat[i,r-1]))))
                e.append(s)
                s=0
    # Store the values in dictionary {Attribute name :Entropy of Associativity} 
    H={associativity.T.columns[i]:e[i] for i in range(len(associativity.T.columns))}
     #present in dataframe 
    associativity_entropy_df=pd.DataFrame.from_dict(H,orient='index').rename(columns={0:'Entropy of associativity'})
    return associativity_entropy_df

#Combined Entropy

def combinedentropy(dataset):
    #Calculate three type of entropy by calling previous functions
    x=EntropyofAttribute(dataset)
    y=EntropyofUsability(dataset)
    z=EntropyofAssociativity(dataset)
    res=[]
    H={}
    r=x.shape[0]
    #Multiply value of three type of  entropy according to each attribute 
    for i in range(0,r):
        Combined =x.iat[i,0]*y.iat[i,0]* z.iat[i,0]
        res.append(Combined)
    # Store the values in dictionary {Attribute name :Combined Entropy} 
    for key in y.T.columns:
        for value in res:
            H[key]=value
            res.remove(value)
            break
    #present in dataframe 
    combined_entropy_df=pd.DataFrame.from_dict(H,orient='index').rename(columns={0:'Combined Entropy'})
    return combined_entropy_df

def Sensitivity(threshold,dataset):
    #Calculate combined entropy by calling previous function
    df=combinedentropy(dataset)
    c=list(df.T.columns)
    s=[]
    t=threshold
    #Filtering the value by threshold according to user's choice
    for i in range(0,df.shape[0]):
        if (df.iat[i, 0] > t):
            s.append("Yes")
        else:
            s.append("No")
     #present in dataframe     
    sensitivity_df=pd.DataFrame(list(zip(c,s)),columns =['Attribute', 'Sensitive'])
    return sensitivity_df