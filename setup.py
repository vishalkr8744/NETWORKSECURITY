from setuptools import setup, find_packages


def get_requirements()->list[str]:


  requirement_1st:list[str]=[]

  try:
    with open('requirements.txt') as f:
       
    #read the line from the file
       lines=f.readlines()
    #process each line

    for line in lines:
        requirement=line .strip()
        ## ignore empty lines and -e .

        if requirement and requirement != '-e .':
           requirement_1st.append(requirement)
           

  except FileNotFoundError:
    print("requirements.txt file not found.")

  return requirement_1st
  
setup(
    name='networksecurity', 
    version='0.1.0',
    author='vishal kumar',
    author_email="vishalkr8744@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)