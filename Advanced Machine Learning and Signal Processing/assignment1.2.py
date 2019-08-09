
# coding: utf-8

# This is the first assignment for the Coursera course "Advanced Machine Learning and Signal Processing"
# 
# Just execute all cells one after the other and you are done - just note that in the last one you have to update your email address (the one you've used for coursera) and obtain a submission token, you get this from the programming assignment directly on coursera.

# In[8]:


get_ipython().system(u'wget https://github.com/IBM/coursera/raw/master/coursera_ml/a2.parquet')


# In[9]:


df=spark.read.load('a2.parquet')

df.createOrReplaceTempView("df")
spark.sql("SELECT * from df").show()


# In[10]:


get_ipython().system(u'rm -Rf a2_m1.json')


# In[11]:


df = df.repartition(1)
df.write.json('a2_m1.json')


# In[12]:


get_ipython().system(u'rm -f rklib.py')
get_ipython().system(u'wget https://raw.githubusercontent.com/IBM/coursera/master/rklib.py')


# In[13]:


import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

zipf = zipfile.ZipFile('a2_m1.json.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('a2_m1.json', zipf)
zipf.close()


# In[14]:


get_ipython().system(u'base64 a2_m1.json.zip > a2_m1.json.zip.base64')


# In[16]:


from rklib import submit
key = "1injH2F0EeiLlRJ3eJKoXA"
part = "wNLDt"
email = "amitpandit8084@hotmail.com"
secret = "qv0cvTk5C0ePbzeZ"

with open('a2_m1.json.zip.base64', 'r') as myfile:
    data=myfile.read()
submit(email, secret, key, part, [part], data)

